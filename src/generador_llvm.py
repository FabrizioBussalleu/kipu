"""Generador de código intermedio LLVM IR para Kipu (avance del Hito 2).

Representación de los tipos en LLVM:
  entero      -> i64
  decimal     -> double
  monto<M>    -> i64 en céntimos (100.50 PEN -> 10050), sin error de punto flotante
  porcentaje  -> i64 como fracción x 10^4 (18% -> 1800, 12.5% -> 1250)
  booleano    -> i1
  texto       -> i8* (cadena constante terminada en cero)

Las operaciones monetarias redondean a céntimos con "half-up" (alejándose de cero) mediante
la función interna kipu.div_redondeo (enteros) o _redondear (decimales), sin
depender de bibliotecas externas. La salida (mostrar) se
delega a funciones de un runtime pequeño (kipu_imprimir_*): en ejecución JIT las provee
ejecutor.py y para un ejecutable nativo, runtime/kipu_runtime.c.

Cobertura del Hito 2: declaraciones, asignaciones (=, +=, -=), todas las expresiones
(aritméticas, monetarias, relacionales, lógicas con cortocircuito, convertir), si / sino si /
sino, mientras, para y mostrar. Pendiente para el Hito 3: reglas, retornar, llamadas, leer y
concatenación de textos.
"""
from __future__ import annotations

from llvmlite import ir

import ast_kipu as A
from ast_kipu import DECIMAL, ENTERO, ESCALA_MONTO, ESCALA_PORCENTAJE, a_escala
from errores import ErrorCompilacion

I1, I8, I32, I64 = ir.IntType(1), ir.IntType(8), ir.IntType(32), ir.IntType(64)
F64 = ir.DoubleType()
I8P = I8.as_pointer()
VOID = ir.VoidType()
MONEDAS = {"PEN": 0, "USD": 1, "EUR": 2}


class ErrorGeneracion(Exception):
    def __init__(self, nodo, mensaje: str):
        super().__init__(mensaje)
        self.error = ErrorCompilacion("GEN", "GEN-01", nodo.linea, nodo.columna, mensaje)


def tipo_llvm(t: A.Tipo):
    return {"entero": I64, "decimal": F64, "porcentaje": I64, "monto": I64,
            "booleano": I1, "texto": I8P}[t.nombre]


class GeneradorLLVM:
    def __init__(self, nombre_modulo: str = "kipu"):
        self.modulo = ir.Module(name=nombre_modulo)
        self.variables = {}          # id(Simbolo) -> alloca
        self.cadenas = {}            # texto -> variable global
        self._declarar_runtime()

    # --- runtime e intrínsecos ------------------------------------------------------
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

    # --- punto de entrada --------------------------------------------------------------
    def generar(self, programa: A.Programa) -> ir.Module:
        main = ir.Function(self.modulo, ir.FunctionType(I32, []), name="main")
        self.fn = main
        self.bloque_entrada = main.append_basic_block("entrada")
        cuerpo = main.append_basic_block("inicio")
        self.b = ir.IRBuilder(cuerpo)
        self.b_alloca = ir.IRBuilder(self.bloque_entrada)
        self._sentencias(programa.sentencias)
        self.b.ret(ir.Constant(I32, 0))
        self.b_alloca.branch(cuerpo)
        return self.modulo

    # --- utilidades -----------------------------------------------------------------------
    def _alloca(self, simbolo, tipo: A.Tipo):
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

    def _a_double(self, valor, tipo: A.Tipo):
        return valor if tipo == DECIMAL else self.b.sitofp(valor, F64)

    def _redondear(self, valor_f64):
        """Redondeo half-up (alejándose de cero) a i64 sin depender de libm:
        x >= 0 -> trunc(x + 0.5);  x < 0 -> trunc(x - 0.5)."""
        b = self.b
        negativo = b.fcmp_ordered("<", valor_f64, ir.Constant(F64, 0.0), name="es_negativo")
        medio = b.select(negativo, ir.Constant(F64, -0.5), ir.Constant(F64, 0.5), name="medio")
        return b.fptosi(b.fadd(valor_f64, medio, name="ajustado"), I64, name="redondeado")

    def _convertir(self, valor, origen: A.Tipo, destino: A.Tipo):
        if origen == ENTERO and destino == DECIMAL:
            return self.b.sitofp(valor, F64)
        return valor

    # --- sentencias -------------------------------------------------------------------------
    def _sentencias(self, lista) -> None:
        for s in lista:
            getattr(self, "_s_" + type(s).__name__, self._no_soportado)(s)

    def _no_soportado(self, nodo) -> None:
        nombre = type(nodo).__name__.lower()
        raise ErrorGeneracion(nodo, f"La generación de LLVM IR para '{nombre}' se completa en el Hito 3.")

    def _s_Bloque(self, b: A.Bloque) -> None:
        self._sentencias(b.sentencias)

    def _s_Declaracion(self, d: A.Declaracion) -> None:
        ptr = self._alloca(d.simbolo, d.tipo_decl)
        if d.valor is not None:
            valor = self._convertir(self._expr(d.valor), d.valor.tipo, d.tipo_decl)
        elif d.tipo_decl.nombre == "texto":
            valor = self._cadena("")
        else:
            valor = ir.Constant(tipo_llvm(d.tipo_decl), 0)     # valor por defecto: cero
        self.b.store(valor, ptr)

    def _s_Asignacion(self, a: A.Asignacion) -> None:
        ptr = self.variables[id(a.simbolo)]
        tipo_dest = a.simbolo.tipo
        valor = self._expr(a.valor)
        tipo_valor = a.valor.tipo
        if a.op in ("+=", "-="):
            actual = self.b.load(ptr, name=a.nombre)
            valor, tipo_valor = self._aritmetica(a.op[0], actual, tipo_dest, valor, tipo_valor, a)
        self.b.store(self._convertir(valor, tipo_valor, tipo_dest), ptr)

    def _s_Si(self, s: A.Si) -> None:
        fin = self.fn.append_basic_block("si.fin")
        for i, (cond, bloque) in enumerate(s.ramas):
            entonces = self.fn.append_basic_block(f"si.entonces{i}")
            siguiente = self.fn.append_basic_block(f"si.siguiente{i}")
            self.b.cbranch(self._expr(cond), entonces, siguiente)
            self.b.position_at_end(entonces)
            self._s_Bloque(bloque)
            self.b.branch(fin)
            self.b.position_at_end(siguiente)
        if s.sino is not None:
            self._s_Bloque(s.sino)
        self.b.branch(fin)
        self.b.position_at_end(fin)

    def _s_Mientras(self, m: A.Mientras) -> None:
        cond_bb = self.fn.append_basic_block("mientras.cond")
        cuerpo_bb = self.fn.append_basic_block("mientras.cuerpo")
        fin_bb = self.fn.append_basic_block("mientras.fin")
        self.b.branch(cond_bb)
        self.b.position_at_end(cond_bb)
        self.b.cbranch(self._expr(m.condicion), cuerpo_bb, fin_bb)
        self.b.position_at_end(cuerpo_bb)
        self._s_Bloque(m.cuerpo)
        self.b.branch(cond_bb)
        self.b.position_at_end(fin_bb)

    def _s_Para(self, p: A.Para) -> None:
        ptr = self._alloca(p.simbolo, ENTERO)
        self.b.store(self._expr(p.desde), ptr)
        hasta = self._expr(p.hasta)
        paso = self._expr(p.paso) if p.paso is not None else ir.Constant(I64, 1)
        cond_bb = self.fn.append_basic_block("para.cond")
        cuerpo_bb = self.fn.append_basic_block("para.cuerpo")
        fin_bb = self.fn.append_basic_block("para.fin")
        self.b.branch(cond_bb)
        self.b.position_at_end(cond_bb)
        i = self.b.load(ptr, name=p.variable)
        ascendente = self.b.icmp_signed(">", paso, ir.Constant(I64, 0), name="ascendente")
        cond = self.b.select(ascendente, self.b.icmp_signed("<=", i, hasta), self.b.icmp_signed(">=", i, hasta), name="continuar")
        self.b.cbranch(cond, cuerpo_bb, fin_bb)
        self.b.position_at_end(cuerpo_bb)
        self._s_Bloque(p.cuerpo)
        self.b.store(self.b.add(self.b.load(ptr), paso, name="siguiente"), ptr)
        self.b.branch(cond_bb)
        self.b.position_at_end(fin_bb)

    def _s_Mostrar(self, m: A.Mostrar) -> None:
        for k, arg in enumerate(m.args):
            if k:
                self.b.call(self.rt["separador"], [])
            valor, t = self._expr(arg), arg.tipo
            if t.nombre == "monto":
                self.b.call(self.rt["monto"], [valor, ir.Constant(I32, MONEDAS[t.moneda])])
            elif t.nombre == "booleano":
                self.b.call(self.rt["booleano"], [self.b.zext(valor, I32)])
            else:
                self.b.call(self.rt[t.nombre], [valor])
        self.b.call(self.rt["fin_linea"], [])

    # --- expresiones -----------------------------------------------------------------------
    def _expr(self, e: A.Expr):
        return getattr(self, "_e_" + type(e).__name__, self._no_soportado)(e)

    def _e_Literal(self, e: A.Literal):
        if e.clase == "entero":
            return ir.Constant(I64, e.valor)
        if e.clase == "decimal":
            return ir.Constant(F64, float(e.valor))
        if e.clase == "monto":
            return ir.Constant(I64, a_escala(e.valor, ESCALA_MONTO))
        if e.clase == "porcentaje":
            return ir.Constant(I64, a_escala(e.valor, ESCALA_PORCENTAJE // 100))
        if e.clase == "booleano":
            return ir.Constant(I1, int(e.valor))
        return self._cadena(e.valor)

    def _e_Variable(self, e: A.Variable):
        return self.b.load(self.variables[id(e.simbolo)], name=e.nombre)

    def _e_Conversion(self, e: A.Conversion):
        cent = self._expr(e.expr)
        tasa = self._expr(e.tasa)
        if e.tasa.tipo == ENTERO:
            return self.b.mul(cent, tasa, name="convertido")
        return self._redondear(self.b.fmul(self.b.sitofp(cent, F64), tasa))

    def _e_Unaria(self, e: A.Unaria):
        v = self._expr(e.expr)
        if e.op == "no":
            return self.b.not_(v, name="no")
        if e.expr.tipo == DECIMAL:
            return self.b.fsub(ir.Constant(F64, 0.0), v, name="neg")
        return self.b.neg(v, name="neg")

    def _e_Binaria(self, e: A.Binaria):
        if e.op in ("y", "o"):
            return self._logica(e)
        a, b = self._expr(e.izq), self._expr(e.der)
        ta, tb = e.izq.tipo, e.der.tipo
        if e.op in ("==", "!=", "<", "<=", ">", ">="):
            return self._comparacion(e.op, a, ta, b, tb)
        valor, _ = self._aritmetica(e.op, a, ta, b, tb, e)
        return valor

    def _logica(self, e: A.Binaria):
        izq = self._expr(e.izq)
        bb_izq = self.b.block
        bb_der = self.fn.append_basic_block(f"{e.op}.derecha")
        bb_fin = self.fn.append_basic_block(f"{e.op}.fin")
        if e.op == "y":
            self.b.cbranch(izq, bb_der, bb_fin)
        else:
            self.b.cbranch(izq, bb_fin, bb_der)
        self.b.position_at_end(bb_der)
        der = self._expr(e.der)
        bb_der_fin = self.b.block
        self.b.branch(bb_fin)
        self.b.position_at_end(bb_fin)
        phi = self.b.phi(I1, name=e.op)
        phi.add_incoming(ir.Constant(I1, 0 if e.op == "y" else 1), bb_izq)
        phi.add_incoming(der, bb_der_fin)
        return phi

    def _comparacion(self, op, a, ta, b, tb):
        if ta.es_numerico and tb.es_numerico and DECIMAL in (ta, tb):
            return self.b.fcmp_ordered(op, self._a_double(a, ta), self._a_double(b, tb), name="cmp")
        if ta.nombre == "texto":
            igual = self.b.icmp_signed("!=", self.b.call(self.rt["texto_igual"], [a, b]), ir.Constant(I32, 0))
            return igual if op == "==" else self.b.not_(igual)
        if ta.nombre == "booleano":
            return self.b.icmp_unsigned(op, a, b, name="cmp")
        return self.b.icmp_signed(op, a, b, name="cmp")

    def _aritmetica(self, op, a, ta: A.Tipo, b, tb: A.Tipo, nodo):
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
