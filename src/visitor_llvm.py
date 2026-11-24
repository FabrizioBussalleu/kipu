"""Generación LLVM desde el árbol de ANTLR; cada visit conecta con IRBuilder."""
from __future__ import annotations
from decimal import Decimal

from llvmlite import ir
from generated.KipuVisitor import KipuVisitor
from errores import ErrorCompilacion
from tipos_kipu import Tipo, ENTERO, DECIMAL, ESCALA_MONTO, ESCALA_PORCENTAJE, a_escala
I1, I8, I32, I64 = ir.IntType(1), ir.IntType(8), ir.IntType(32), ir.IntType(64)
F64 = ir.DoubleType()
I8P = I8.as_pointer()
VOID = ir.VoidType()
MONEDAS = {"PEN": 0, "USD": 1, "EUR": 2}


class ErrorGeneracion(Exception):
    def __init__(self, nodo, mensaje: str):
        super().__init__(mensaje)
        tok = nodo.start
        self.error = ErrorCompilacion("GEN", "GEN-01", tok.line, tok.column + 1, mensaje)


def tipo_llvm(t):
    return {"entero": I64, "decimal": F64, "porcentaje": I64, "monto": I64,
            "booleano": I1, "texto": I8P}[t.nombre]



class LLVMVisitor(KipuVisitor):
    def __init__(self, nombre_modulo="kipu"):
        self.modulo = ir.Module(name=nombre_modulo)
        self.variables = {}
        self.cadenas = {}
        self.funciones = {}
        self._declarar_runtime()

    def _declarar_runtime(self) -> None:
        m = self.modulo
        f = lambda nombre, ret, args: ir.Function(m, ir.FunctionType(ret, args), name=nombre)  # noqa: E731
        self.rt = {
            "entero": f("kipu_imprimir_entero", VOID, [I64]),
            "decimal": f("kipu_imprimir_decimal", VOID, [F64]),
            "monto": f("kipu_imprimir_monto", VOID, [I64, I32]),
            "porcentaje": f("kipu_imprimir_porcentaje", VOID, [I64]),
            "booleano": f("kipu_imprimir_booleano", VOID, [I32]),
            "texto": f("kipu_imprimir_texto", VOID, [I8P]),
            "separador": f("kipu_imprimir_separador", VOID, []),
            "fin_linea": f("kipu_imprimir_fin_linea", VOID, []),
            "texto_igual": f("kipu_texto_igual", I32, [I8P, I8P]),
            "texto_concatenar": f("kipu_texto_concatenar", I8P, [I8P, I8P]),
            "leer_entero": f("kipu_leer_entero", I64, []),
            "leer_decimal": f("kipu_leer_decimal", F64, []),
            "leer_monto": f("kipu_leer_monto", I64, []),
            "leer_porcentaje": f("kipu_leer_porcentaje", I64, []),
            "leer_booleano": f("kipu_leer_booleano", I32, []),
            "leer_texto": f("kipu_leer_texto", I8P, []),
        }
        self.div_redondeo = self._crear_div_redondeo()

    def _crear_div_redondeo(self) -> ir.Function:
        """i64 kipu.div_redondeo(i64 a, i64 b): a / b redondeado half-up (alejándose de cero)."""
        fn = ir.Function(self.modulo, ir.FunctionType(I64, [I64, I64]), name="kipu.div_redondeo")
        fn.linkage = "internal"
        a, b = fn.args
        a.name, b.name = "a", "b"
        bld = ir.IRBuilder(fn.append_basic_block("entrada"))
        cero = ir.Constant(I64, 0)
        q = bld.sdiv(a, b, name="cociente")
        r = bld.srem(a, b, name="resto")
        r2 = bld.mul(r, ir.Constant(I64, 2), name="resto_x2")
        abs_r2 = bld.select(bld.icmp_signed("<", r2, cero), bld.neg(r2), r2, name="abs_resto_x2")
        abs_b = bld.select(bld.icmp_signed("<", b, cero), bld.neg(b), b, name="abs_divisor")
        ajustar = bld.icmp_signed(">=", abs_r2, abs_b, name="ajustar")
        negativo = bld.xor(bld.icmp_signed("<", a, cero), bld.icmp_signed("<", b, cero), name="signo_negativo")
        signo = bld.select(negativo, ir.Constant(I64, -1), ir.Constant(I64, 1), name="signo")
        bld.ret(bld.add(q, bld.select(ajustar, signo, cero), name="resultado"))
        return fn

    def _alloca(self, simbolo, tipo: Tipo):
        if simbolo.ambito == "global":
            puntero = ir.GlobalVariable(self.modulo, tipo_llvm(tipo), name=simbolo.nombre)
            puntero.initializer = ir.Constant(tipo_llvm(tipo), None)
            self.variables[id(simbolo)] = puntero
            return puntero
        ptr = self.b_alloca.alloca(tipo_llvm(tipo), name=simbolo.nombre)
        self.variables[id(simbolo)] = ptr
        return ptr

    def _cadena(self, texto: str):
        if texto not in self.cadenas:
            datos = bytearray(texto.encode("utf-8")) + b"\x00"
            tipo = ir.ArrayType(I8, len(datos))
            g = ir.GlobalVariable(self.modulo, tipo, name=f".cadena.{len(self.cadenas)}")
            g.global_constant = True
            g.linkage = "private"
            g.initializer = ir.Constant(tipo, datos)
            self.cadenas[texto] = g
        return self.b.bitcast(self.cadenas[texto], I8P)

    def _a_double(self, valor, tipo: Tipo):
        return valor if tipo == DECIMAL else self.b.sitofp(valor, F64)

    def _redondear(self, valor_f64):
        """Redondeo half-up (alejándose de cero) a i64 sin depender de libm:
        x >= 0 -> trunc(x + 0.5);  x < 0 -> trunc(x - 0.5)."""
        b = self.b
        negativo = b.fcmp_ordered("<", valor_f64, ir.Constant(F64, 0.0), name="es_negativo")
        medio = b.select(negativo, ir.Constant(F64, -0.5), ir.Constant(F64, 0.5), name="medio")
        return b.fptosi(b.fadd(valor_f64, medio, name="ajustado"), I64, name="redondeado")

    def _convertir(self, valor, origen: Tipo, destino: Tipo):
        if origen == ENTERO and destino == DECIMAL:
            return self.b.sitofp(valor, F64)
        return valor

    def _comparacion(self, op, a, ta, b, tb):
        if ta.es_numerico and tb.es_numerico and DECIMAL in (ta, tb):
            return self.b.fcmp_ordered(op, self._a_double(a, ta), self._a_double(b, tb), name="cmp")
        if ta.nombre == "texto":
            igual = self.b.icmp_signed("!=", self.b.call(self.rt["texto_igual"], [a, b]), ir.Constant(I32, 0))
            return igual if op == "==" else self.b.not_(igual)
        if ta.nombre == "booleano":
            return self.b.icmp_unsigned(op, a, b, name="cmp")
        return self.b.icmp_signed(op, a, b, name="cmp")

    def _aritmetica(self, op, a, ta, b, tb, nodo):
        """Devuelve (valor, tipo_resultado) siguiendo las reglas del sistema de tipos."""
        b_ = self.b
        if ta.es_numerico and tb.es_numerico:
            if op == "mod":
                return b_.srem(a, b, name="mod"), ENTERO
            if op == "/" or DECIMAL in (ta, tb):
                x, y = self._a_double(a, ta), self._a_double(b, tb)
                f = {"+": b_.fadd, "-": b_.fsub, "*": b_.fmul, "/": b_.fdiv}[op]
                return f(x, y, name="r"), DECIMAL
            f = {"+": b_.add, "-": b_.sub, "*": b_.mul}[op]
            return f(a, b, name="r"), ENTERO
        escalados = ("monto", "porcentaje")
        if op in ("+", "-") and ta.nombre in escalados and ta == tb:
            return (b_.add if op == "+" else b_.sub)(a, b, name="r"), ta
        if op == "*":
            # normalizar: el operando escalado (monto/porcentaje) a la izquierda
            if tb.nombre == "monto" or (tb.nombre == "porcentaje" and ta.nombre != "monto"):
                a, ta, b, tb = b, tb, a, ta
            if tb == ENTERO:
                return b_.mul(a, b, name="r"), ta
            if tb == DECIMAL:
                return self._redondear(b_.fmul(b_.sitofp(a, F64), b)), ta
            if tb.nombre == "porcentaje":
                prod = b_.mul(a, b, name="prod")
                return b_.call(self.div_redondeo, [prod, ir.Constant(I64, ESCALA_PORCENTAJE)], name="r"), ta
        if op == "/" and ta.nombre in escalados:
            if tb == ENTERO:
                return b_.call(self.div_redondeo, [a, b], name="r"), ta
            if tb == DECIMAL:
                return self._redondear(b_.fdiv(b_.sitofp(a, F64), b)), ta
            if tb == ta:
                return b_.fdiv(b_.sitofp(a, F64), b_.sitofp(b, F64), name="r"), DECIMAL
        raise ErrorGeneracion(nodo, f"La operación '{op}' entre {ta} y {tb} se genera en el Hito 3.")


    def _sentencias_ctx(self, lista):
        while lista.sentencia() is not None:
            if not self.builder.block.is_terminated:
                self.visit(lista.sentencia())
            lista = lista.listaSentencias()

    def _argumentos(self, ctx):
        resultado = []
        if ctx.expresion() is not None:
            resultado.append(ctx.expresion())
            cola = ctx.argumentosCola()
            while cola.expresion() is not None:
                resultado.append(cola.expresion())
                cola = cola.argumentosCola()
        return resultado

    def _parametros(self, ctx):
        resultado = []
        if ctx.parametro() is not None:
            resultado.append(ctx.parametro())
            cola = ctx.parametrosCola()
            while cola.parametro() is not None:
                resultado.append(cola.parametro())
                cola = cola.parametrosCola()
        return resultado

    def _crear_funcion(self, regla):
        sim = regla.simbolo
        retorno = tipo_llvm(sim.tipo) if sim.tipo is not None else ir.VoidType()
        parametros = [tipo_llvm(t) for t in sim.parametros]
        funcion = ir.Function(self.modulo, ir.FunctionType(retorno, parametros), name=sim.nombre)
        self.funciones[id(sim)] = funcion

    def visitPrograma(self, ctx):
        lista = ctx.listaSentencias()
        while lista.sentencia() is not None:
            regla = lista.sentencia().regla()
            if regla is not None:
                self._crear_funcion(regla)
            lista = lista.listaSentencias()

        main = ir.Function(self.modulo, ir.FunctionType(I32, []), name="main")
        self.fn = main
        entrada = main.append_basic_block("entrada")
        cuerpo = main.append_basic_block("inicio")
        self.builder = ir.IRBuilder(cuerpo)
        self.b = self.builder
        self.b_alloca = ir.IRBuilder(entrada)
        lista = ctx.listaSentencias()
        while lista.sentencia() is not None:
            sentencia = lista.sentencia()
            if sentencia.regla() is None and not self.builder.block.is_terminated:
                self.visit(sentencia)
            lista = lista.listaSentencias()
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(I32, 0))
        self.b_alloca.branch(cuerpo)

        lista = ctx.listaSentencias()
        while lista.sentencia() is not None:
            regla = lista.sentencia().regla()
            if regla is not None:
                self.visit(regla)
            lista = lista.listaSentencias()
        return self.modulo

    def visitSentencia(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitBloque(self, ctx):
        self._sentencias_ctx(ctx.listaSentencias())

    def visitDeclaracion(self, ctx):
        sim = ctx.simbolo
        puntero = self._alloca(sim, sim.tipo)
        expresion = ctx.expresion() if ctx.CONST() else ctx.inicializacion().expresion()
        if expresion is not None:
            valor = self._convertir(self.visit(expresion), expresion.tipo_kipu, sim.tipo)
        elif sim.tipo.nombre == "texto":
            valor = self._cadena("")
        else:
            valor = ir.Constant(tipo_llvm(sim.tipo), 0)
        self.builder.store(valor, puntero)

    def visitAsignacion(self, ctx):
        sim = ctx.simbolo
        puntero = self.variables[id(sim)]
        expresion = ctx.expresion()
        valor = self.visit(expresion)
        tipo_valor = expresion.tipo_kipu
        operador = ctx.opAsignacion().getText()
        if operador in ("+=", "-="):
            actual = self.builder.load(puntero, name=sim.nombre)
            valor, tipo_valor = self._aritmetica(operador[0], actual, sim.tipo, valor, tipo_valor, ctx)
        self.builder.store(self._convertir(valor, tipo_valor, sim.tipo), puntero)

    def visitSeleccion(self, ctx):
        fin = self.fn.append_basic_block("si.fin")
        actual = ctx
        hay_salida = False
        while True:
            entonces = self.fn.append_basic_block("si.entonces")
            siguiente = self.fn.append_basic_block("si.siguiente")
            condicion = self.visit(actual.expresion())
            self.builder.cbranch(condicion, entonces, siguiente)
            self.builder.position_at_end(entonces)
            self.visit(actual.bloque())
            if not self.builder.block.is_terminated:
                self.builder.branch(fin)
                hay_salida = True
            self.builder.position_at_end(siguiente)
            parte = actual.parteSino()
            if parte.SINO() is None:
                break
            cola = parte.colaSino()
            if cola.bloque() is not None:
                self.visit(cola.bloque())
                break
            actual = cola.seleccion()
        if not self.builder.block.is_terminated:
            self.builder.branch(fin)
            hay_salida = True
        self.builder.position_at_end(fin)
        if not hay_salida:
            self.builder.unreachable()

    def visitIteracion(self, ctx):
        if ctx.MIENTRAS():
            condicion = self.fn.append_basic_block("mientras.cond")
            cuerpo = self.fn.append_basic_block("mientras.cuerpo")
            fin = self.fn.append_basic_block("mientras.fin")
            self.builder.branch(condicion)
            self.builder.position_at_end(condicion)
            self.builder.cbranch(self.visit(ctx.expresion(0)), cuerpo, fin)
            self.builder.position_at_end(cuerpo)
            self.visit(ctx.bloque())
            if not self.builder.block.is_terminated:
                self.builder.branch(condicion)
            self.builder.position_at_end(fin)
            return
        puntero = self._alloca(ctx.simbolo, ENTERO)
        self.builder.store(self.visit(ctx.expresion(0)), puntero)
        hasta = self.visit(ctx.expresion(1))
        paso_ctx = ctx.pasoOpcional().expresion()
        paso = self.visit(paso_ctx) if paso_ctx else ir.Constant(I64, 1)
        condicion = self.fn.append_basic_block("para.cond")
        cuerpo = self.fn.append_basic_block("para.cuerpo")
        fin = self.fn.append_basic_block("para.fin")
        self.builder.branch(condicion)
        self.builder.position_at_end(condicion)
        actual = self.builder.load(puntero, name=ctx.ID().getText())
        asc = self.builder.icmp_signed(">", paso, ir.Constant(I64, 0))
        continuar = self.builder.select(asc, self.builder.icmp_signed("<=", actual, hasta), self.builder.icmp_signed(">=", actual, hasta))
        self.builder.cbranch(continuar, cuerpo, fin)
        self.builder.position_at_end(cuerpo)
        self.visit(ctx.bloque())
        if not self.builder.block.is_terminated:
            self.builder.store(self.builder.add(self.builder.load(puntero), paso), puntero)
            self.builder.branch(condicion)
        self.builder.position_at_end(fin)

    def visitRegla(self, ctx):
        funcion = self.funciones[id(ctx.simbolo)]
        self.fn = funcion
        entrada = funcion.append_basic_block("entrada")
        cuerpo = funcion.append_basic_block("inicio")
        self.builder = ir.IRBuilder(cuerpo)
        self.b = self.builder
        self.b_alloca = ir.IRBuilder(entrada)
        for argumento, parametro in zip(funcion.args, self._parametros(ctx.parametros())):
            argumento.name = parametro.ID().getText()
            puntero = self._alloca(parametro.simbolo, parametro.simbolo.tipo)
            self.builder.store(argumento, puntero)
        self.visit(ctx.bloque())
        if not self.builder.block.is_terminated:
            if ctx.simbolo.tipo is None:
                self.builder.ret_void()
            else:
                raise ErrorGeneracion(ctx, "La regla no termina con retornar en este camino.")
        self.b_alloca.branch(cuerpo)

    def visitRetorno(self, ctx):
        expresion = ctx.valorRetorno().expresion()
        if expresion is None:
            self.builder.ret_void()
        else:
            tipo_destino = self.fn.function_type.return_type
            valor = self.visit(expresion)
            if valor.type != tipo_destino:
                valor = self.builder.sitofp(valor, tipo_destino)
            self.builder.ret(valor)

    def visitLlamadaSentencia(self, ctx):
        return self.visit(ctx.llamada())

    def visitEntradaSalida(self, ctx):
        if ctx.LEER():
            sim = ctx.simbolo
            valor = self.builder.call(self.rt["leer_" + sim.tipo.nombre], [])
            if sim.tipo.nombre == "booleano":
                valor = self.builder.icmp_signed("!=", valor, ir.Constant(I32, 0))
            self.builder.store(valor, self.variables[id(sim)])
            return
        argumentos = [ctx.expresion()]
        cola = ctx.argumentosCola()
        while cola.expresion() is not None:
            argumentos.append(cola.expresion())
            cola = cola.argumentosCola()
        for i, arg in enumerate(argumentos):
            if i:
                self.builder.call(self.rt["separador"], [])
            valor = self.visit(arg)
            tipo = arg.tipo_kipu
            if tipo.es_monto:
                self.builder.call(self.rt["monto"], [valor, ir.Constant(I32, MONEDAS[tipo.moneda])])
            elif tipo.nombre == "booleano":
                self.builder.call(self.rt["booleano"], [self.builder.zext(valor, I32)])
            else:
                self.builder.call(self.rt[tipo.nombre], [valor])
        self.builder.call(self.rt["fin_linea"], [])

    def visitExpresion(self, ctx):
        return self._binaria_ctx(ctx)

    def visitConjuncion(self, ctx):
        return self._binaria_ctx(ctx)

    def visitIgualdad(self, ctx):
        return self._binaria_ctx(ctx)

    def visitRelacional(self, ctx):
        return self._binaria_ctx(ctx)

    def visitAritmetica(self, ctx):
        return self._binaria_ctx(ctx)

    def visitTermino(self, ctx):
        return self._binaria_ctx(ctx)

    def _binaria_ctx(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        izquierda = ctx.getChild(0)
        derecha = ctx.getChild(2)
        operador = ctx.getChild(1).getText()
        if operador in ("y", "o"):
            primero = self.visit(izquierda)
            bloque_izquierdo = self.builder.block
            bloque_derecho = self.fn.append_basic_block(f"{operador}.derecha")
            bloque_final = self.fn.append_basic_block(f"{operador}.fin")
            if operador == "y":
                self.builder.cbranch(primero, bloque_derecho, bloque_final)
            else:
                self.builder.cbranch(primero, bloque_final, bloque_derecho)
            self.builder.position_at_end(bloque_derecho)
            segundo = self.visit(derecha)
            final_derecho = self.builder.block
            self.builder.branch(bloque_final)
            self.builder.position_at_end(bloque_final)
            resultado = self.builder.phi(I1)
            resultado.add_incoming(ir.Constant(I1, int(operador == "o")), bloque_izquierdo)
            resultado.add_incoming(segundo, final_derecho)
            return resultado
        a = self.visit(izquierda)
        b = self.visit(derecha)
        ta = izquierda.tipo_kipu
        tb = derecha.tipo_kipu
        if operador in ("==", "!=", "<", "<=", ">", ">="):
            return self._comparacion(operador, a, ta, b, tb)
        if operador == "+" and ta.nombre == tb.nombre == "texto":
            return self.builder.call(self.rt["texto_concatenar"], [a, b])
        valor, _ = self._aritmetica(operador, a, ta, b, tb, ctx)
        return valor

    def visitNegacion(self, ctx):
        if ctx.NO():
            return self.builder.not_(self.visit(ctx.negacion()))
        return self.visit(ctx.igualdad())

    def visitUnario(self, ctx):
        if ctx.RESTA():
            valor = self.visit(ctx.unario())
            if ctx.unario().tipo_kipu == DECIMAL:
                return self.builder.fsub(ir.Constant(F64, 0.0), valor)
            return self.builder.neg(valor)
        return self.visit(ctx.primario())

    def visitPrimario(self, ctx):
        if ctx.CONVERTIR():
            centimos = self.visit(ctx.expresion(0))
            tasa = self.visit(ctx.expresion(1))
            if ctx.expresion(1).tipo_kipu == ENTERO:
                return self.builder.mul(centimos, tasa)
            return self._redondear(self.builder.fmul(self.builder.sitofp(centimos, F64), tasa))
        if ctx.PAR_IZQ():
            return self.visit(ctx.expresion(0))
        if ctx.llamada():
            return self.visit(ctx.llamada())
        if ctx.literal():
            return self.visit(ctx.literal())
        return self.builder.load(self.variables[id(ctx.simbolo)], name=ctx.ID().getText())

    def visitLiteral(self, ctx):
        if ctx.numero():
            return ir.Constant(I64, a_escala(Decimal(ctx.numero().getText()), ESCALA_MONTO))
        if ctx.NUM_ENTERO():
            return ir.Constant(I64, int(ctx.NUM_ENTERO().getText()))
        if ctx.NUM_DECIMAL():
            return ir.Constant(F64, float(ctx.NUM_DECIMAL().getText()))
        if ctx.LIT_PORCENTAJE():
            return ir.Constant(I64, a_escala(Decimal(ctx.LIT_PORCENTAJE().getText()[:-1]), ESCALA_PORCENTAJE // 100))
        if ctx.CADENA():
            texto = ctx.CADENA().getText()[1:-1]
            for viejo, nuevo in (("\\n", "\n"), ("\\t", "\t"), ('\\"', '"'), ("\\\\", "\\")):
                texto = texto.replace(viejo, nuevo)
            return self._cadena(texto)
        return ir.Constant(I1, int(ctx.VERDADERO() is not None))

    def visitLlamada(self, ctx):
        funcion = self.funciones[id(ctx.simbolo)]
        valores = []
        for argumento, esperado in zip(self._argumentos(ctx.argumentos()), ctx.simbolo.parametros):
            valor = self.visit(argumento)
            valores.append(self._convertir(valor, argumento.tipo_kipu, esperado))
        return self.builder.call(funcion, valores)
