"""Tipos y escalas del lenguaje Kipu, independientes del árbol sintáctico."""
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class Tipo:
    nombre: str
    moneda: str | None = None

    def __str__(self):
        return f"monto<{self.moneda}>" if self.nombre == "monto" else self.nombre

    @property
    def es_numerico(self):
        return self.nombre in ("entero", "decimal")

    @property
    def es_monto(self):
        return self.nombre == "monto"


ENTERO = Tipo("entero")
DECIMAL = Tipo("decimal")
PORCENTAJE = Tipo("porcentaje")
BOOLEANO = Tipo("booleano")
TEXTO = Tipo("texto")
ESCALA_MONTO = 100
ESCALA_PORCENTAJE = 10000


def monto(moneda):
    return Tipo("monto", moneda)


def a_escala(valor: Decimal, escala: int) -> int:
    return int((valor * escala).quantize(Decimal(1), rounding=ROUND_HALF_UP))
