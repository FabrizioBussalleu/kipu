"""Análisis semántico directamente sobre contextos del parser ANTLR."""
from decimal import Decimal

from generated.KipuVisitor import KipuVisitor
from errores import ErrorCompilacion
from tipos_kipu import Tipo, ENTERO, DECIMAL, PORCENTAJE, BOOLEANO, TEXTO, monto
from tabla_simbolos import Simbolo, TablaSimbolos

DESCRIPCION_ERRORES = {
    "SEM-01": "Identificador no declarado",
    "SEM-02": "Identificador redeclarado en el mismo ámbito",
    "SEM-03": "Monedas incompatibles",
    "SEM-04": "Tipos incompatibles",
    "SEM-05": "Modificación de una constante",
    "SEM-06": "Condición no booleana",
    "SEM-07": "retornar fuera de una regla",
    "SEM-08": "Valor de retorno incompatible",
    "SEM-09": "Número de argumentos incorrecto",
    "SEM-10": "Tipo de argumento incompatible",
    "SEM-11": "Regla que no retorna en todos los caminos",
    "SEM-12": "Porcentaje fuera de rango",
    "SEM-13": "División entre cero",
    "SEM-14": "Regla sin valor usada en una expresión",
}


class VisitorSemantico(KipuVisitor):
    def __init__(self):
        self.tabla = TablaSimbolos()
        self.errores = []
        self.regla_actual = None

    def _error(self, codigo, ctx, mensaje):
        tok = ctx.getSymbol() if hasattr(ctx, "getSymbol") else ctx.start
        self.errores.append(ErrorCompilacion("SEM", codigo, tok.line, tok.column + 1, mensaje))

    def _declarar(self, simbolo, ctx):
        previo = self.tabla.actual.buscar_local(simbolo.nombre)
        if previo:
            self._error("SEM-02", ctx, f"'{simbolo.nombre}' ya fue declarado en este ámbito (línea {previo.linea}).")
            return None
        simbolo.ambito = self.tabla.actual.nombre
        self.tabla.actual.simbolos[simbolo.nombre] = simbolo
        return simbolo

    def _simbolo(self, nombre, categoria, tipo, ctx, parametros=None):
        tok = ctx.getSymbol() if hasattr(ctx, "getSymbol") else ctx.start
        return Simbolo(nombre, categoria, tipo, tok.line, tok.column + 1, parametros or [])

    @staticmethod
    def compatible(destino, origen):
        return destino is None or origen is None or destino == origen or destino == DECIMAL and origen == ENTERO

    def _asignable(self, destino, origen, ctx, descripcion, codigo="SEM-04"):
        if self.compatible(destino, origen):
            return
        if destino.es_monto and origen.es_monto:
            self._error("SEM-03", ctx, f"Monedas incompatibles: no se puede asignar {origen} a {descripcion} de tipo {destino}; use convertir(...).")
        else:
            self._error(codigo, ctx, f"Tipos incompatibles: no se puede asignar {origen} a {descripcion} de tipo {destino}.")

    def _sentencias(self, lista):
        while lista.sentencia() is not None:
            self.visit(lista.sentencia())
            lista = lista.listaSentencias()

    def _parametros(self, ctx):
        resultado = []
        if ctx.parametro() is not None:
            resultado.append(ctx.parametro())
            cola = ctx.parametrosCola()
            while cola.parametro() is not None:
                resultado.append(cola.parametro())
                cola = cola.parametrosCola()
        return resultado

    def _argumentos(self, ctx):
        resultado = []
        if ctx.expresion() is not None:
            resultado.append(ctx.expresion())
            cola = ctx.argumentosCola()
            while cola.expresion() is not None:
                resultado.append(cola.expresion())
                cola = cola.argumentosCola()
        return resultado

    def visitPrograma(self, ctx):
        lista = ctx.listaSentencias()
        while lista.sentencia() is not None:
            regla = lista.sentencia().regla()
            if regla is not None:
                self._registrar_regla(regla)
            lista = lista.listaSentencias()
        self._sentencias(ctx.listaSentencias())
        self.errores.sort(key=lambda e: (e.linea, e.columna))

    def visitSentencia(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitBloque(self, ctx):
        self.tabla.abrir(f"bloque (línea {ctx.start.line})")
        self._sentencias(ctx.listaSentencias())
        self.tabla.cerrar()

    def visitTipo(self, ctx):
        return monto(ctx.MONEDA().getText()) if ctx.MONTO() else Tipo(ctx.getText())

    def visitDeclaracion(self, ctx):
        tipo = self.visit(ctx.tipo())
        valor = ctx.expresion() if ctx.CONST() else ctx.inicializacion().expresion()
        if valor is not None:
            self._asignable(tipo, self.visit(valor), valor, f"'{ctx.ID().getText()}'")
        categoria = "constante" if ctx.CONST() else "variable"
        ctx.simbolo = self._declarar(self._simbolo(ctx.ID().getText(), categoria, tipo, ctx.ID()), ctx.ID())

    def visitAsignacion(self, ctx):
        tipo_valor = self.visit(ctx.expresion())
        nombre = ctx.ID().getText()
        sim = self.tabla.actual.buscar(nombre)
        if sim is None:
            self._error("SEM-01", ctx.ID(), f"'{nombre}' no ha sido declarado.")
            return
        ctx.simbolo = sim
        if sim.categoria == "constante":
            self._error("SEM-05", ctx.ID(), f"No se puede modificar la constante '{nombre}'.")
            return
        if sim.categoria == "regla":
            self._error("SEM-04", ctx.ID(), f"'{nombre}' es una regla y no puede recibir una asignación.")
            return
        op = ctx.opAsignacion().getText()
        if op in ("+=", "-="):
            tipo_valor = self._tipo_binario(op[0], sim.tipo, tipo_valor, ctx.expresion())
        self._asignable(sim.tipo, tipo_valor, ctx.expresion(), f"'{nombre}'")

    def _condicion(self, ctx, donde):
        tipo = self.visit(ctx)
        if tipo is not None and tipo != BOOLEANO:
            self._error("SEM-06", ctx, f"La condición de '{donde}' debe ser booleana; se recibió {tipo}.")

    def visitSeleccion(self, ctx):
        actual = ctx
        primera = True
        while True:
            self._condicion(actual.expresion(), "si" if primera else "sino si")
            self.visit(actual.bloque())
            parte = actual.parteSino()
            if parte.SINO() is None:
                break
            cola = parte.colaSino()
            if cola.bloque() is not None:
                self.visit(cola.bloque())
                break
            actual = cola.seleccion()
            primera = False

    def visitIteracion(self, ctx):
        if ctx.MIENTRAS():
            self._condicion(ctx.expresion(0), "mientras")
            self.visit(ctx.bloque())
            return
        paso = ctx.pasoOpcional().expresion()
        for nombre, expresion in (("desde", ctx.expresion(0)), ("hasta", ctx.expresion(1)), ("paso", paso)):
            if expresion is None:
                continue
            tipo = self.visit(expresion)
            if tipo is not None and tipo != ENTERO:
                self._error("SEM-04", expresion, f"Tipos incompatibles: el límite '{nombre}' del para debe ser entero, se recibió {tipo}.")
        nombre = ctx.ID().getText()
        self.tabla.abrir(f"para {nombre} (línea {ctx.start.line})")
        ctx.simbolo = self._declarar(self._simbolo(nombre, "contador", ENTERO, ctx.ID()), ctx.ID())
        self._sentencias(ctx.bloque().listaSentencias())
        self.tabla.cerrar()

    def _registrar_regla(self, ctx):
        parametros = [self.visit(p.tipo()) for p in self._parametros(ctx.parametros())]
        retorno = ctx.tipoRetorno().tipo()
        tipo = self.visit(retorno) if retorno else None
        nombre = ctx.ID().getText()
        ctx.simbolo = self._declarar(self._simbolo(nombre, "regla", tipo, ctx.ID(), parametros), ctx.ID())
        ctx.registrada = True

    def visitRegla(self, ctx):
        if not hasattr(ctx, "registrada"):
            self._registrar_regla(ctx)
        anterior = self.regla_actual
        self.regla_actual = ctx
        self.tabla.abrir(f"regla {ctx.ID().getText()}")
        for p in self._parametros(ctx.parametros()):
            p.simbolo = self._declarar(self._simbolo(p.ID().getText(), "parametro", self.visit(p.tipo()), p.ID()), p.ID())
        self._sentencias(ctx.bloque().listaSentencias())
        self.tabla.cerrar()
        if ctx.tipoRetorno().tipo() is not None and not self._retorna_siempre(ctx.bloque().listaSentencias()):
            self._error("SEM-11", ctx.ID(), f"La regla '{ctx.ID().getText()}' declara tipo {self.visit(ctx.tipoRetorno().tipo())} pero no retorna un valor en todos los caminos.")
        self.regla_actual = anterior

    def _retorna_siempre(self, lista):
        while lista.sentencia() is not None:
            s = lista.sentencia()
            if s.retorno():
                return True
            if s.bloque() and self._retorna_siempre(s.bloque().listaSentencias()):
                return True
            if s.seleccion() and self._seleccion_retorna(s.seleccion()):
                return True
            lista = lista.listaSentencias()
        return False

    def _seleccion_retorna(self, ctx):
        if not self._retorna_siempre(ctx.bloque().listaSentencias()):
            return False
        parte = ctx.parteSino()
        if parte.SINO() is None:
            return False
        cola = parte.colaSino()
        if cola.bloque():
            return self._retorna_siempre(cola.bloque().listaSentencias())
        return self._seleccion_retorna(cola.seleccion())

    def visitRetorno(self, ctx):
        valor = ctx.valorRetorno().expresion()
        tipo_valor = self.visit(valor) if valor else None
        regla = self.regla_actual
        if regla is None:
            self._error("SEM-07", ctx, "'retornar' solo puede usarse dentro de una regla.")
            return
        esperado_ctx = regla.tipoRetorno().tipo()
        esperado = self.visit(esperado_ctx) if esperado_ctx else None
        nombre = regla.ID().getText()
        if esperado is None and valor is not None:
            self._error("SEM-08", ctx, f"La regla '{nombre}' no declara tipo de retorno y no puede retornar un valor.")
        elif esperado is not None and valor is None:
            self._error("SEM-08", ctx, f"La regla '{nombre}' debe retornar un valor de tipo {esperado}.")
        elif esperado is not None and not self.compatible(esperado, tipo_valor):
            detalle = "moneda distinta" if esperado.es_monto and tipo_valor.es_monto else "tipo distinto"
            self._error("SEM-08", valor, f"Valor de retorno incompatible ({detalle}): la regla '{nombre}' retorna {esperado} y se intenta retornar {tipo_valor}.")

    def visitLlamadaSentencia(self, ctx):
        self._llamada(ctx.llamada(), False)

    def visitEntradaSalida(self, ctx):
        if ctx.MOSTRAR():
            self.visit(ctx.expresion())
            cola = ctx.argumentosCola()
            while cola.expresion() is not None:
                self.visit(cola.expresion())
                cola = cola.argumentosCola()
            return
        nombre = ctx.ID().getText()
        sim = self.tabla.actual.buscar(nombre)
        if sim is None:
            self._error("SEM-01", ctx.ID(), f"'{nombre}' no ha sido declarado.")
        elif sim.categoria == "constante":
            self._error("SEM-05", ctx.ID(), f"No se puede leer un valor sobre la constante '{nombre}'.")
        elif sim.categoria == "regla":
            self._error("SEM-04", ctx.ID(), f"'{nombre}' es una regla; leer requiere una variable.")
        else:
            ctx.simbolo = sim

    def visitExpresion(self, ctx):
        return self._binaria(ctx)

    def visitConjuncion(self, ctx):
        return self._binaria(ctx)

    def visitIgualdad(self, ctx):
        return self._binaria(ctx)

    def visitRelacional(self, ctx):
        return self._binaria(ctx)

    def visitAritmetica(self, ctx):
        return self._binaria(ctx)

    def visitTermino(self, ctx):
        return self._binaria(ctx)

    def _binaria(self, ctx):
        if ctx.getChildCount() == 1:
            tipo = self.visit(ctx.getChild(0))
        else:
            izquierda = self.visit(ctx.getChild(0))
            derecha = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op in ("y", "o"):
                for lado, tipo_lado in ((ctx.getChild(0), izquierda), (ctx.getChild(2), derecha)):
                    if tipo_lado is not None and tipo_lado != BOOLEANO:
                        self._error("SEM-04", lado, f"Tipos incompatibles: el operador '{op}' requiere booleanos, se recibió {tipo_lado}.")
                tipo = BOOLEANO
            elif op in ("==", "!=", "<", "<=", ">", ">="):
                tipo = self._comparar(op, izquierda, derecha, ctx)
            else:
                if op in ("/", "mod") and self._literal_cero(ctx.getChild(2)):
                    self._error("SEM-13", ctx.getChild(2), f"División entre cero: el divisor de '{op}' es el literal 0.")
                tipo = self._tipo_binario(op, izquierda, derecha, ctx)
        ctx.tipo_kipu = tipo
        return tipo

    def _literal_cero(self, ctx):
        while ctx.getChildCount() == 1:
            if hasattr(ctx, "literal") and ctx.literal() is not None:
                break
            ctx = ctx.getChild(0)
        if hasattr(ctx, "literal") and ctx.literal():
            ctx = ctx.literal()
        if not hasattr(ctx, "NUM_ENTERO"):
            return False
        if ctx.numero():
            return Decimal(ctx.numero().getText()) == 0
        if ctx.NUM_ENTERO():
            return int(ctx.NUM_ENTERO().getText()) == 0
        if ctx.NUM_DECIMAL():
            return Decimal(ctx.NUM_DECIMAL().getText()) == 0
        if ctx.LIT_PORCENTAJE():
            return Decimal(ctx.LIT_PORCENTAJE().getText()[:-1]) == 0
        return False

    def visitNegacion(self, ctx):
        if ctx.NO():
            tipo = self.visit(ctx.negacion())
            if tipo is not None and tipo != BOOLEANO:
                self._error("SEM-04", ctx, f"Tipos incompatibles: el operador 'no' requiere booleano, se recibió {tipo}.")
            ctx.tipo_kipu = BOOLEANO
        else:
            ctx.tipo_kipu = self.visit(ctx.igualdad())
        return ctx.tipo_kipu

    def visitUnario(self, ctx):
        if ctx.RESTA():
            tipo = self.visit(ctx.unario())
            if tipo is not None and not (tipo.es_numerico or tipo.es_monto or tipo == PORCENTAJE):
                self._error("SEM-04", ctx, f"Tipos incompatibles: el operador '-' no se aplica a {tipo}.")
                tipo = None
        else:
            tipo = self.visit(ctx.primario())
        ctx.tipo_kipu = tipo
        return tipo

    def visitPrimario(self, ctx):
        if ctx.CONVERTIR():
            origen = self.visit(ctx.expresion(0))
            tasa = self.visit(ctx.expresion(1))
            if origen is not None and not origen.es_monto:
                self._error("SEM-04", ctx.expresion(0), f"convertir(...) requiere un monto como primer argumento, se recibió {origen}.")
            if tasa is not None and not tasa.es_numerico:
                self._error("SEM-04", ctx.expresion(1), f"El tipo de cambio debe ser entero o decimal, se recibió {tasa}.")
            if self._literal_cero(ctx.expresion(1)):
                self._error("SEM-13", ctx.expresion(1), "El tipo de cambio no puede ser cero.")
            tipo = monto(ctx.MONEDA().getText())
        elif ctx.PAR_IZQ():
            tipo = self.visit(ctx.expresion(0))
        elif ctx.llamada():
            tipo = self._llamada(ctx.llamada(), True)
        elif ctx.literal():
            tipo = self.visit(ctx.literal())
        else:
            nombre = ctx.ID().getText()
            sim = self.tabla.actual.buscar(nombre)
            if sim is None:
                self._error("SEM-01", ctx.ID(), f"'{nombre}' no ha sido declarado.")
                tipo = None
            elif sim.categoria == "regla":
                self._error("SEM-04", ctx.ID(), f"'{nombre}' es una regla; debe invocarse con paréntesis.")
                tipo = None
            else:
                ctx.simbolo = sim
                tipo = sim.tipo
        ctx.tipo_kipu = tipo
        return tipo

    def visitLiteral(self, ctx):
        if ctx.numero():
            tipo = monto(ctx.MONEDA().getText())
        elif ctx.NUM_ENTERO():
            tipo = ENTERO
        elif ctx.NUM_DECIMAL():
            tipo = DECIMAL
        elif ctx.LIT_PORCENTAJE():
            tipo = PORCENTAJE
            valor = Decimal(ctx.LIT_PORCENTAJE().getText()[:-1])
            if not Decimal(0) <= valor <= Decimal(100):
                self._error("SEM-12", ctx, f"Porcentaje fuera de rango: {valor}% (debe estar entre 0% y 100%).")
        elif ctx.CADENA():
            tipo = TEXTO
        else:
            tipo = BOOLEANO
        ctx.tipo_kipu = tipo
        return tipo

    def _llamada(self, ctx, en_expresion):
        argumentos = self._argumentos(ctx.argumentos())
        tipos = [self.visit(arg) for arg in argumentos]
        nombre = ctx.ID().getText()
        sim = self.tabla.actual.buscar(nombre)
        if sim is None:
            self._error("SEM-01", ctx.ID(), f"La regla '{nombre}' no ha sido declarada.")
            return None
        if sim.categoria != "regla":
            self._error("SEM-04", ctx.ID(), f"'{nombre}' es de tipo {sim.tipo} y no puede invocarse como regla.")
            return None
        ctx.simbolo = sim
        if len(tipos) != len(sim.parametros):
            self._error("SEM-09", ctx.ID(), f"La regla '{nombre}' espera {len(sim.parametros)} argumento(s) y recibió {len(tipos)}.")
        else:
            for i, (esperado, recibido, arg) in enumerate(zip(sim.parametros, tipos, argumentos), 1):
                if not self.compatible(esperado, recibido):
                    self._error("SEM-10", arg, f"Argumento {i} de '{nombre}': se esperaba {esperado} y se recibió {recibido}.")
        if en_expresion and sim.tipo is None:
            self._error("SEM-14", ctx.ID(), f"La regla '{nombre}' no retorna un valor y no puede usarse en una expresión.")
        ctx.tipo_kipu = sim.tipo
        return sim.tipo

    def _comparar(self, op, izquierda, derecha, ctx):
        if izquierda is None or derecha is None:
            return BOOLEANO
        if izquierda.es_numerico and derecha.es_numerico:
            return BOOLEANO
        if izquierda.es_monto and derecha.es_monto:
            if izquierda.moneda != derecha.moneda:
                self._error("SEM-03", ctx, f"Monedas incompatibles: no se puede comparar {izquierda} con {derecha}.")
            return BOOLEANO
        if izquierda == derecha and (op in ("==", "!=") or izquierda == PORCENTAJE):
            return BOOLEANO
        self._error("SEM-04", ctx, f"Tipos incompatibles: no se puede comparar {izquierda} con {derecha} usando '{op}'.")
        return BOOLEANO

    def _tipo_binario(self, op, a, b, ctx):
        if a is None or b is None:
            return None
        if op in ("+", "-"):
            if a.es_numerico and b.es_numerico:
                return DECIMAL if DECIMAL in (a, b) else ENTERO
            if a.es_monto and b.es_monto:
                if a.moneda == b.moneda:
                    return a
                self._error("SEM-03", ctx, f"Monedas incompatibles: no se puede operar {a} con {b}; use convertir(...).")
                return None
            if a == PORCENTAJE and b == PORCENTAJE:
                return PORCENTAJE
            if op == "+" and a == TEXTO and b == TEXTO:
                return TEXTO
        elif op == "*":
            if a.es_numerico and b.es_numerico:
                return DECIMAL if DECIMAL in (a, b) else ENTERO
            if a.es_monto and (b.es_numerico or b == PORCENTAJE):
                return a
            if b.es_monto and (a.es_numerico or a == PORCENTAJE):
                return b
            if PORCENTAJE in (a, b) and (a.es_numerico or b.es_numerico or a == b):
                return PORCENTAJE
        elif op == "/":
            if a.es_numerico and b.es_numerico:
                return DECIMAL
            if a.es_monto and b.es_numerico:
                return a
            if a.es_monto and b.es_monto:
                if a.moneda == b.moneda:
                    return DECIMAL
                self._error("SEM-03", ctx, f"Monedas incompatibles: no se puede dividir {a} entre {b}.")
                return None
            if a == PORCENTAJE and b.es_numerico:
                return PORCENTAJE
        elif op == "mod" and a == ENTERO and b == ENTERO:
            return ENTERO
        self._error("SEM-04", ctx, f"Tipos incompatibles: la operación '{op}' no está definida entre {a} y {b}.")
        return None
