"""Manejo de errores léxicos y sintácticos de Kipu (mensajes en español)."""
import re
from dataclasses import dataclass

from antlr4.error.ErrorListener import ErrorListener


@dataclass
class ErrorCompilacion:
    fase: str          # "LEX", "SIN" o "SEM"
    codigo: str        # p. ej. "LEX-01", "SIN-01", "SEM-03"
    linea: int
    columna: int
    mensaje: str

    def __str__(self) -> str:
        return f"[{self.codigo}] línea {self.linea}:{self.columna}  {self.mensaje}"


def _traducir_mensaje_sintactico(msg: str) -> str:
    """Traduce los mensajes estándar de ANTLR4 al español."""
    reglas = [
        (r"^missing (.+) at (.+)$", r"falta \1 antes de \2"),
        (r"^mismatched input (.+) expecting (.+)$", r"entrada inesperada \1, se esperaba \2"),
        (r"^extraneous input (.+) expecting (.+)$", r"símbolo sobrante \1, se esperaba \2"),
        (r"^no viable alternative at input (.+)$", r"no se reconoce una construcción válida en \1"),
        (r"^token recognition error at: (.+)$", r"símbolo no reconocido \1"),
    ]
    cadena = re.match(r"^token recognition error at: '(\".*)'$", msg, re.S)
    if cadena:
        texto = cadena.group(1).replace("\\n", "").replace("\\r", "").rstrip("\n\r")
        return f"cadena de texto sin cerrar: {texto}"
    for patron, reemplazo in reglas:
        if re.match(patron, msg):
            texto = re.sub(patron, reemplazo, msg)
            return texto.replace("<EOF>", "fin de archivo")
    return msg.replace("<EOF>", "fin de archivo")


class RecolectorErrores(ErrorListener):
    """Listener que acumula los errores en lugar de imprimirlos en consola."""

    def __init__(self, fase: str):
        super().__init__()
        self.fase = fase
        self.errores: list[ErrorCompilacion] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        codigo = "LEX-01" if self.fase == "LEX" else "SIN-01"
        self.errores.append(
            ErrorCompilacion(self.fase, codigo, line, column + 1, _traducir_mensaje_sintactico(msg))
        )
