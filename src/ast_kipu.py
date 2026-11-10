"""Árbol de sintaxis abstracta (AST) de Kipu.

El constructor (constructor_ast.py) transforma el árbol de análisis de ANTLR en estos nodos.
El analizador semántico anota cada expresión con su tipo (atributo `tipo`) y cada uso de
variable con su símbolo (atributo `simbolo`); el generador de código LLVM usa esas anotaciones.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


# ----------------------------------------------------------------------------
# Tipos del lenguaje
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
# Nodos
# ----------------------------------------------------------------------------
@dataclass
class Nodo:
    linea: int = field(default=0, kw_only=True)
    columna: int = field(default=0, kw_only=True)


# --- Expresiones ---------------------------------------------------------------
@dataclass
class Expr(Nodo):
    tipo: Optional[Tipo] = field(default=None, kw_only=True, repr=False)


@dataclass
class Literal(Expr):
    clase: str                     # entero, decimal, porcentaje, monto, texto, booleano
    valor: object                  # int, Decimal, str o bool
    moneda: Optional[str] = None


@dataclass
class Variable(Expr):
    nombre: str
    simbolo: object = field(default=None, repr=False)


@dataclass
class Binaria(Expr):
    op: str                        # o y == != < <= > >= + - * / mod
    izq: Expr
    der: Expr


@dataclass
class Unaria(Expr):
    op: str                        # - no
    expr: Expr


@dataclass
class Llamada(Expr):
    nombre: str
    args: list
    simbolo: object = field(default=None, repr=False)


@dataclass
class Conversion(Expr):
    expr: Expr
    moneda: str
    tasa: Expr


# --- Sentencias ------------------------------------------------------------------
@dataclass
class Bloque(Nodo):
    sentencias: list


@dataclass
class Declaracion(Nodo):
    constante: bool
    nombre: str
    tipo_decl: Tipo
    valor: Optional[Expr]
    simbolo: object = field(default=None, repr=False)


@dataclass
class Asignacion(Nodo):
    nombre: str
    op: str                        # = += -=
    valor: Expr
    simbolo: object = field(default=None, repr=False)


@dataclass
class Si(Nodo):
    ramas: list                    # [(condicion, Bloque)], la primera es el "si"
    sino: Optional[Bloque]


@dataclass
class Mientras(Nodo):
    condicion: Expr
    cuerpo: Bloque


@dataclass
class Para(Nodo):
    variable: str
    desde: Expr
    hasta: Expr
    paso: Optional[Expr]
    cuerpo: Bloque
    simbolo: object = field(default=None, repr=False)


@dataclass
class Parametro(Nodo):
    nombre: str
    tipo_decl: Tipo


@dataclass
class Regla(Nodo):
    nombre: str
    parametros: list
    tipo_retorno: Optional[Tipo]
    cuerpo: Bloque


@dataclass
class Retornar(Nodo):
    valor: Optional[Expr]


@dataclass
class Mostrar(Nodo):
    args: list


@dataclass
class Leer(Nodo):
    nombre: str
    simbolo: object = field(default=None, repr=False)


@dataclass
class LlamadaSentencia(Nodo):
    llamada: Llamada


@dataclass
class Programa(Nodo):
    sentencias: list


# Escala de representación interna (usada por el generador de código)
ESCALA_MONTO = 100          # montos en céntimos
ESCALA_PORCENTAJE = 10000   # porcentajes como fracción x 10^4 (18% -> 1800)


def a_escala(valor: Decimal, escala: int) -> int:
    """Convierte un Decimal a entero escalado con redondeo half-up."""
    from decimal import ROUND_HALF_UP
    return int((valor * escala).quantize(Decimal(1), rounding=ROUND_HALF_UP))
