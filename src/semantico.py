"""Analizador semántico de Kipu (Hito 1: verificación parcial).

Errores semánticos verificados en este hito:
  SEM-01  Identificador no declarado (variable, constante o regla).
  SEM-02  Identificador redeclarado en el mismo ámbito.
  SEM-03  Monedas incompatibles (operar o asignar montos de distinta moneda sin convertir).
  SEM-04  Tipos incompatibles (asignación, inicialización u operación con tipos no permitidos).
  SEM-05  Modificación de una constante.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from antlr4 import ParserRuleContext

from errores import ErrorCompilacion
from generated.KipuParser import KipuParser
from generated.KipuVisitor import KipuVisitor


# ----------------------------------------------------------------------------
# Sistema de tipos
# ----------------------------------------------------------------------------
@dataclass(frozen=True)
class Tipo:
    nombre: str                    # entero, decimal, porcentaje, booleano, texto, monto
    moneda: Optional[str] = None   # solo para monto

    def __str__(self) -> str:
        return f"monto<{self.moneda}>" if self.nombre == "monto" else self.nombre

    @property
    def es_numerico(self) -> bool:
        return self.nombre in ("entero", "decimal")

    @property
    def es_monto(self) -> bool:
        return self.nombre == "monto"


ENTERO = Tipo("entero")
DECIMAL = Tipo("decimal")
PORCENTAJE = Tipo("porcentaje")
BOOLEANO = Tipo("booleano")
TEXTO = Tipo("texto")


def monto(moneda: str) -> Tipo:
    return Tipo("monto", moneda)


# ----------------------------------------------------------------------------
# Tabla de símbolos
# ----------------------------------------------------------------------------
@dataclass
class Simbolo:
    nombre: str
    categoria: str                 # variable, constante, parametro, regla, contador
    tipo: Optional[Tipo]
    linea: int
    columna: int
    parametros: list = field(default_factory=list)   # solo reglas: lista de Tipo


@dataclass
class Ambito:
    nombre: str
    padre: Optional["Ambito"]
    simbolos: dict = field(default_factory=dict)

    def buscar_local(self, nombre: str) -> Optional[Simbolo]:
        return self.simbolos.get(nombre)

    def buscar(self, nombre: str) -> Optional[Simbolo]:
        ambito = self
        while ambito is not None:
            if nombre in ambito.simbolos:
                return ambito.simbolos[nombre]
            ambito = ambito.padre
        return None


class TablaSimbolos:
    def __init__(self):
        self.global_ = Ambito("global", None)
        self.actual = self.global_
        self.todos: list[Ambito] = [self.global_]

    def abrir(self, nombre: str) -> None:
        self.actual = Ambito(nombre, self.actual)
        self.todos.append(self.actual)

    def cerrar(self) -> None:
        self.actual = self.actual.padre


# ----------------------------------------------------------------------------
# Analizador semántico
# ----------------------------------------------------------------------------
class AnalizadorSemantico(KipuVisitor):
    def __init__(self):
        self.tabla = TablaSimbolos()
        self.errores: list[ErrorCompilacion] = []

    # --- utilidades -------------------------------------------------------------
    def _error(self, codigo: str, token_o_ctx, mensaje: str) -> None:
        token = token_o_ctx.start if isinstance(token_o_ctx, ParserRuleContext) else token_o_ctx
        self.errores.append(ErrorCompilacion("SEM", codigo, token.line, token.column + 1, mensaje))

    def _declarar(self, simbolo: Simbolo, token) -> None:
        previo = self.tabla.actual.buscar_local(simbolo.nombre)
        if previo is not None:
            self._error(
                "SEM-02", token,
                f"'{simbolo.nombre}' ya fue declarado en este ámbito (línea {previo.linea}).",
            )
            return
        self.tabla.actual.simbolos[simbolo.nombre] = simbolo

    def _compatible_asignacion(self, destino: Optional[Tipo], origen: Optional[Tipo], ctx, nombre: str) -> None:
        if destino is None or origen is None or destino == origen:
            return
        if destino == DECIMAL and origen == ENTERO:          # ensanchamiento permitido
            return
        if destino.es_monto and origen.es_monto:
            self._error(
                "SEM-03", ctx,
                f"Monedas incompatibles: no se puede asignar {origen} a '{nombre}' de tipo {destino}; "
                f"use convertir(expr, {destino.moneda}, tipo_cambio).",
            )
            return
        self._error("SEM-04", ctx, f"Tipos incompatibles: no se puede asignar {origen} a '{nombre}' de tipo {destino}.")

    def _tipo_aritmetico(self, op: str, a: Optional[Tipo], b: Optional[Tipo], ctx) -> Optional[Tipo]:
        if a is None or b is None:
            return None
        if op in ("+", "-"):
            if a.es_numerico and b.es_numerico:
                return DECIMAL if DECIMAL in (a, b) else ENTERO
            if a.es_monto and b.es_monto:
                if a.moneda != b.moneda:
                    verbo = "sumar" if op == "+" else "restar"
                    self._error("SEM-03", ctx, f"Monedas incompatibles: no se puede {verbo} {a} con {b}; use convertir(...).")
                    return None
                return a
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
                if a.moneda != b.moneda:
                    self._error("SEM-03", ctx, f"Monedas incompatibles: no se puede dividir {a} entre {b}.")
                    return None
                return DECIMAL
            if a == PORCENTAJE and b.es_numerico:
                return PORCENTAJE
        elif op == "mod":
            if a == ENTERO and b == ENTERO:
                return ENTERO
        self._error("SEM-04", ctx, f"Tipos incompatibles: la operación '{op}' no está definida entre {a} y {b}.")
        return None

    # --- programa y sentencias ---------------------------------------------------
    def visitPrograma(self, ctx: KipuParser.ProgramaContext):
        # Primera pasada: registrar reglas globales para permitir llamadas antes de su definición.
        for sent in ctx.sentencia():
            if sent.regla() is not None:
                self._registrar_regla(sent.regla())
        for sent in ctx.sentencia():
            self.visit(sent)
        self.errores.sort(key=lambda e: (e.linea, e.columna))
        return None

    def _registrar_regla(self, ctx: KipuParser.ReglaContext) -> Simbolo:
        tipo_ret = self.visit(ctx.tipo()) if ctx.tipo() is not None else None
        params = []
        if ctx.parametros() is not None:
            params = [self.visit(p.tipo()) for p in ctx.parametros().parametro()]
        simbolo = Simbolo(ctx.ID().getText(), "regla", tipo_ret, ctx.ID().symbol.line, ctx.ID().symbol.column, params)
        self._declarar(simbolo, ctx.ID().symbol)
        ctx.registrada = True
        return simbolo

    def visitBloque(self, ctx: KipuParser.BloqueContext):
        self.tabla.abrir(f"bloque (línea {ctx.start.line})")
        for sent in ctx.sentencia():
            self.visit(sent)
        self.tabla.cerrar()
        return None

    # 1. Declaraciones -------------------------------------------------------------
    def visitDeclaracionVariable(self, ctx: KipuParser.DeclaracionVariableContext):
        tipo = self.visit(ctx.tipo())
        nombre = ctx.ID().getText()
        if ctx.expresion() is not None:
            self._compatible_asignacion(tipo, self.visit(ctx.expresion()), ctx.expresion(), nombre)
        self._declarar(Simbolo(nombre, "variable", tipo, ctx.ID().symbol.line, ctx.ID().symbol.column), ctx.ID().symbol)
        return None

    def visitDeclaracionConstante(self, ctx: KipuParser.DeclaracionConstanteContext):
        tipo = self.visit(ctx.tipo())
        nombre = ctx.ID().getText()
        self._compatible_asignacion(tipo, self.visit(ctx.expresion()), ctx.expresion(), nombre)
        self._declarar(Simbolo(nombre, "constante", tipo, ctx.ID().symbol.line, ctx.ID().symbol.column), ctx.ID().symbol)
        return None

    def visitTipoEntero(self, ctx):
        return ENTERO

    def visitTipoDecimal(self, ctx):
        return DECIMAL

    def visitTipoPorcentaje(self, ctx):
        return PORCENTAJE

    def visitTipoBooleano(self, ctx):
        return BOOLEANO

    def visitTipoTexto(self, ctx):
        return TEXTO

    def visitTipoMonto(self, ctx: KipuParser.TipoMontoContext):
        return monto(ctx.MONEDA().getText())

    # 2. Asignación ------------------------------------------------------------------
    def visitAsignacion(self, ctx: KipuParser.AsignacionContext):
        nombre = ctx.ID().getText()
        tipo_expr = self.visit(ctx.expresion())
        simbolo = self.tabla.actual.buscar(nombre)
        if simbolo is None:
            self._error("SEM-01", ctx.ID().symbol, f"'{nombre}' no ha sido declarado.")
            return None
        if simbolo.categoria == "constante":
            self._error("SEM-05", ctx.ID().symbol, f"No se puede modificar la constante '{nombre}'.")
            return None
        if simbolo.categoria == "regla":
            self._error("SEM-04", ctx.ID().symbol, f"'{nombre}' es una regla y no puede recibir una asignación.")
            return None
        op = ctx.op.text
        if op in ("+=", "-="):
            tipo_expr = self._tipo_aritmetico(op[0], simbolo.tipo, tipo_expr, ctx.expresion())
        self._compatible_asignacion(simbolo.tipo, tipo_expr, ctx.expresion(), nombre)
        return None

    # 4 y 5. Control de flujo ----------------------------------------------------------
    def visitSeleccion(self, ctx: KipuParser.SeleccionContext):
        for expr in ctx.expresion():
            self.visit(expr)
        for bloque in ctx.bloque():
            self.visit(bloque)
        return None

    def visitIterMientras(self, ctx: KipuParser.IterMientrasContext):
        self.visit(ctx.expresion())
        self.visit(ctx.bloque())
        return None

    def visitIterPara(self, ctx: KipuParser.IterParaContext):
        for expr in ctx.expresion():
            self.visit(expr)
        self.tabla.abrir(f"para {ctx.ID().getText()} (línea {ctx.start.line})")
        self._declarar(Simbolo(ctx.ID().getText(), "contador", ENTERO, ctx.ID().symbol.line, ctx.ID().symbol.column), ctx.ID().symbol)
        # El cuerpo comparte ámbito con el contador: redeclararlo dentro es un error (SEM-02).
        for sent in ctx.bloque().sentencia():
            self.visit(sent)
        self.tabla.cerrar()
        return None

    # 6. Reglas --------------------------------------------------------------------------
    def visitRegla(self, ctx: KipuParser.ReglaContext):
        if not getattr(ctx, "registrada", False):     # regla anidada: se registra al visitarla
            self._registrar_regla(ctx)
        self.tabla.abrir(f"regla {ctx.ID().getText()}")
        if ctx.parametros() is not None:
            for p in ctx.parametros().parametro():
                self._declarar(
                    Simbolo(p.ID().getText(), "parametro", self.visit(p.tipo()), p.ID().symbol.line, p.ID().symbol.column),
                    p.ID().symbol,
                )
        for sent in ctx.bloque().sentencia():
            self.visit(sent)
        self.tabla.cerrar()
        return None

    def visitRetorno(self, ctx: KipuParser.RetornoContext):
        if ctx.expresion() is not None:
            self.visit(ctx.expresion())
        return None

    def visitLlamada(self, ctx: KipuParser.LlamadaContext):
        nombre = ctx.ID().getText()
        if ctx.argumentos() is not None:
            for arg in ctx.argumentos().expresion():
                self.visit(arg)
        simbolo = self.tabla.actual.buscar(nombre)
        if simbolo is None:
            self._error("SEM-01", ctx.ID().symbol, f"La regla '{nombre}' no ha sido declarada.")
            return None
        if simbolo.categoria != "regla":
            self._error("SEM-04", ctx.ID().symbol, f"'{nombre}' es de tipo {simbolo.tipo} y no puede invocarse como regla.")
            return None
        return simbolo.tipo

    def visitLlamadaSentencia(self, ctx):
        self.visit(ctx.llamada())
        return None

    # 7. Entrada y salida ---------------------------------------------------------------
    def visitSalida(self, ctx: KipuParser.SalidaContext):
        for arg in ctx.argumentos().expresion():
            self.visit(arg)
        return None

    def visitEntrada(self, ctx: KipuParser.EntradaContext):
        nombre = ctx.ID().getText()
        simbolo = self.tabla.actual.buscar(nombre)
        if simbolo is None:
            self._error("SEM-01", ctx.ID().symbol, f"'{nombre}' no ha sido declarado.")
        elif simbolo.categoria == "constante":
            self._error("SEM-05", ctx.ID().symbol, f"No se puede leer un valor sobre la constante '{nombre}'.")
        return None

    # 3. Expresiones ----------------------------------------------------------------------
    def visitExprParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def visitExprLlamada(self, ctx):
        return self.visit(ctx.llamada())

    def visitExprConversion(self, ctx: KipuParser.ExprConversionContext):
        origen = self.visit(ctx.expresion(0))
        tasa = self.visit(ctx.expresion(1))
        if origen is not None and not origen.es_monto:
            self._error("SEM-04", ctx.expresion(0), f"convertir(...) requiere un monto como primer argumento, se recibió {origen}.")
        if tasa is not None and not tasa.es_numerico:
            self._error("SEM-04", ctx.expresion(1), f"El tipo de cambio debe ser entero o decimal, se recibió {tasa}.")
        return monto(ctx.MONEDA().getText())

    def visitExprNegativo(self, ctx):
        t = self.visit(ctx.expresion())
        if t is not None and not (t.es_numerico or t.es_monto or t == PORCENTAJE):
            self._error("SEM-04", ctx, f"Tipos incompatibles: el operador '-' no se aplica a {t}.")
            return None
        return t

    def visitExprNo(self, ctx):
        t = self.visit(ctx.expresion())
        if t is not None and t != BOOLEANO:
            self._error("SEM-04", ctx, f"Tipos incompatibles: el operador 'no' requiere booleano, se recibió {t}.")
        return BOOLEANO

    def visitExprMultiplicativa(self, ctx):
        return self._tipo_aritmetico(ctx.op.text, self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)), ctx)

    def visitExprAditiva(self, ctx):
        return self._tipo_aritmetico(ctx.op.text, self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)), ctx)

    def _comparar(self, ctx, solo_orden: bool):
        a, b = self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1))
        op = ctx.op.text
        if a is None or b is None:
            return BOOLEANO
        if a.es_numerico and b.es_numerico:
            return BOOLEANO
        if a.es_monto and b.es_monto:
            if a.moneda != b.moneda:
                self._error("SEM-03", ctx, f"Monedas incompatibles: no se puede comparar {a} con {b}.")
            return BOOLEANO
        if a == b and (not solo_orden or a == PORCENTAJE):
            return BOOLEANO
        self._error("SEM-04", ctx, f"Tipos incompatibles: no se puede comparar {a} con {b} usando '{op}'.")
        return BOOLEANO

    def visitExprRelacional(self, ctx):
        return self._comparar(ctx, solo_orden=True)

    def visitExprIgualdad(self, ctx):
        return self._comparar(ctx, solo_orden=False)

    def _logica(self, ctx, op: str):
        for expr in ctx.expresion():
            t = self.visit(expr)
            if t is not None and t != BOOLEANO:
                self._error("SEM-04", expr, f"Tipos incompatibles: el operador '{op}' requiere booleanos, se recibió {t}.")
        return BOOLEANO

    def visitExprY(self, ctx):
        return self._logica(ctx, "y")

    def visitExprO(self, ctx):
        return self._logica(ctx, "o")

    def visitExprLiteral(self, ctx):
        return self.visit(ctx.literal())

    def visitExprVariable(self, ctx):
        nombre = ctx.ID().getText()
        simbolo = self.tabla.actual.buscar(nombre)
        if simbolo is None:
            self._error("SEM-01", ctx.ID().symbol, f"'{nombre}' no ha sido declarado.")
            return None
        if simbolo.categoria == "regla":
            self._error("SEM-04", ctx.ID().symbol, f"'{nombre}' es una regla; debe invocarse con paréntesis.")
            return None
        return simbolo.tipo

    # Literales -----------------------------------------------------------------------------
    def visitLitMonto(self, ctx):
        return monto(ctx.MONEDA().getText())

    def visitLitEntero(self, ctx):
        return ENTERO

    def visitLitDecimal(self, ctx):
        return DECIMAL

    def visitLitPorcentaje(self, ctx):
        return PORCENTAJE

    def visitLitTexto(self, ctx):
        return TEXTO

    def visitLitBooleano(self, ctx):
        return BOOLEANO
