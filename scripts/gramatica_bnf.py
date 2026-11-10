"""Extrae la gramática libre de contexto de grammar/Kipu.g4 en notación de producciones.

Como Kipu.g4 está en forma estándar (sin ?, *, + ni subreglas), cada regla del parser es
directamente un conjunto de producciones A -> α1 | α2 | ... | ε. Este módulo es la fuente que
usan el informe y las derivaciones, así que la gramática del informe coincide regla por regla
con la implementación.

Uso: python scripts/gramatica_bnf.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from verificar_gramatica import reglas  # noqa: E402

RUTA_G4 = os.path.join(RAIZ, "grammar", "Kipu.g4")

# Agrupación de las reglas del parser por construcción (para el informe)
GRUPOS = [
    ("G0", "Estructura general del programa", ["programa", "listaSentencias", "sentencia", "bloque"]),
    ("G1", "Declaración de variables y constantes", ["declaracion", "inicializacion", "tipo"]),
    ("G2", "Asignación", ["asignacion", "opAsignacion"]),
    ("G3", "Expresiones", ["expresion", "conjuncion", "negacion", "igualdad", "relacional", "aritmetica",
                           "termino", "unario", "primario", "literal", "numero", "llamada", "argumentos",
                           "argumentosCola"]),
    ("G4", "Sentencias selectivas", ["seleccion", "parteSino", "colaSino"]),
    ("G5", "Sentencias iterativas", ["iteracion", "pasoOpcional"]),
    ("G6", "Reglas (funciones), retorno y llamadas", ["regla", "parametros", "parametrosCola", "parametro",
                                                      "tipoRetorno", "retorno", "valorRetorno", "llamadaSentencia"]),
    ("G7", "Entrada y salida", ["entradaSalida"]),
]


def producciones() -> dict:
    """{no_terminal: [[símbolos], ...]} en el orden de Kipu.g4; [] representa ε."""
    with open(RUTA_G4, encoding="utf-8") as f:
        texto = f.read()
    salida = {}
    for nombre, es_fragment, cuerpo in reglas(texto):
        if not nombre[0].islower():
            continue
        cadena = "".join(v for _, v in cuerpo)
        alternativas = [alt.split() for alt in cadena.split("|")]
        salida[nombre] = alternativas
    return salida


def no_terminales() -> set:
    return set(producciones())


def texto_produccion(nt: str, alts) -> str:
    cuerpo = " | ".join(" ".join(a) if a else "ε" for a in alts)
    return f"{nt} → {cuerpo}"


def verificar_grupos() -> None:
    prods = producciones()
    agrupadas = [r for _, _, rs in GRUPOS for r in rs]
    faltan = set(prods) - set(agrupadas)
    sobran = set(agrupadas) - set(prods)
    assert not faltan and not sobran, f"grupos desalineados: faltan {faltan}, sobran {sobran}"


if __name__ == "__main__":
    verificar_grupos()
    prods = producciones()
    for gid, titulo, nombres in GRUPOS:
        print(f"{gid}. {titulo}")
        for nt in nombres:
            print("   ", texto_produccion(nt, prods[nt]))
    print(f"\n{len(prods)} no terminales, {sum(len(a) for a in prods.values())} producciones.")
