"""Símbolos y ámbitos del análisis semántico de Kipu."""
from dataclasses import dataclass, field
from tipos_kipu import Tipo


@dataclass(eq=False)
class Simbolo:
    nombre: str
    categoria: str
    tipo: Tipo | None
    linea: int
    columna: int
    parametros: list = field(default_factory=list)
    ambito: str = ""


@dataclass
class Ambito:
    nombre: str
    padre: "Ambito | None"
    simbolos: dict = field(default_factory=dict)

    def buscar_local(self, nombre):
        return self.simbolos.get(nombre)

    def buscar(self, nombre):
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
        self.todos = [self.global_]

    def abrir(self, nombre):
        self.actual = Ambito(nombre, self.actual)
        self.todos.append(self.actual)

    def cerrar(self):
        self.actual = self.actual.padre
