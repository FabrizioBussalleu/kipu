"""Gramática libre de contexto de Kipu en la notación del curso (BNF, sin EBNF).

Convención (Aho, Lam, Sethi y Ullman):
  * No terminales: nombres en minúscula y cursiva (expr, decl, sentencias).
  * Terminales: en negrita; son palabras clave y símbolos tal como se escriben
    (var, :, ;) o clases de token del analizador léxico (id, num_ent, num_dec,
    lit_porc, cadena, moneda).
  * A → α | β separa alternativas; ε es la cadena vacía.

Es la misma fuente que usa scripts/derivaciones.py para verificar las derivaciones
más a la izquierda y que usa el informe para imprimir las producciones.
"""

EPS = []  # alternativa vacía (ε)

# Cada gramática: (id, título, [(no_terminal, [alternativas])]); cada alternativa es una lista de símbolos.
GRAMATICAS = [
    ("G0", "Estructura general del programa", [
        ("programa", [["sentencias"]]),
        ("sentencias", [["sentencia", "sentencias"], EPS]),
        ("sentencia", [["decl"], ["asig"], ["sel"], ["iter"], ["def_regla"], ["ret"], ["es"], ["llam_sent"], ["bloque"]]),
        ("bloque", [["{", "sentencias", "}"]]),
    ]),
    ("G1", "Declaración de variables y constantes", [
        ("decl", [["var", "id", ":", "tipo", "init", ";"], ["const", "id", ":", "tipo", "=", "expr", ";"]]),
        ("init", [["=", "expr"], EPS]),
        ("tipo", [["entero"], ["decimal"], ["porcentaje"], ["booleano"], ["texto"], ["monto", "<", "moneda", ">"]]),
    ]),
    ("G2", "Asignación", [
        ("asig", [["id", "op_asig", "expr", ";"]]),
        ("op_asig", [["="], ["+="], ["-="]]),
    ]),
    ("G3", "Expresiones", [
        ("expr", [["expr", "o", "conj"], ["conj"]]),
        ("conj", [["conj", "y", "neg"], ["neg"]]),
        ("neg", [["no", "neg"], ["igu"]]),
        ("igu", [["igu", "op_igu", "rel"], ["rel"]]),
        ("op_igu", [["=="], ["!="]]),
        ("rel", [["rel", "op_rel", "arit"], ["arit"]]),
        ("op_rel", [["<"], ["<="], [">"], [">="]]),
        ("arit", [["arit", "op_sum", "term"], ["term"]]),
        ("op_sum", [["+"], ["-"]]),
        ("term", [["term", "op_mul", "unario"], ["unario"]]),
        ("op_mul", [["*"], ["/"], ["mod"]]),
        ("unario", [["-", "unario"], ["prim"]]),
        ("prim", [["(", "expr", ")"], ["convertir", "(", "expr", ",", "moneda", ",", "expr", ")"],
                  ["llamada"], ["lit"], ["id"]]),
        ("lit", [["num", "moneda"], ["num_ent"], ["num_dec"], ["lit_porc"], ["cadena"], ["verdadero"], ["falso"]]),
        ("num", [["num_ent"], ["num_dec"]]),
        ("llamada", [["id", "(", "args", ")"]]),
        ("args", [["expr", "args_resto"], EPS]),
        ("args_resto", [[",", "expr", "args_resto"], EPS]),
    ]),
    ("G4", "Sentencias selectivas", [
        ("sel", [["si", "(", "expr", ")", "bloque", "sino_parte"]]),
        ("sino_parte", [["sino", "sino_cola"], EPS]),
        ("sino_cola", [["sel"], ["bloque"]]),
    ]),
    ("G5", "Sentencias iterativas", [
        ("iter", [["mientras", "(", "expr", ")", "bloque"],
                  ["para", "id", "desde", "expr", "hasta", "expr", "paso_opc", "bloque"]]),
        ("paso_opc", [["paso", "expr"], EPS]),
    ]),
    ("G6", "Reglas (funciones), retorno y llamadas", [
        ("def_regla", [["regla", "id", "(", "params", ")", "tipo_ret", "bloque"]]),
        ("params", [["param", "params_resto"], EPS]),
        ("params_resto", [[",", "param", "params_resto"], EPS]),
        ("param", [["id", ":", "tipo"]]),
        ("tipo_ret", [[":", "tipo"], EPS]),
        ("ret", [["retornar", "ret_expr", ";"]]),
        ("ret_expr", [["expr"], EPS]),
        ("llam_sent", [["llamada", ";"]]),
    ]),
    ("G7", "Entrada y salida", [
        ("es", [["mostrar", "(", "expr", "args_resto", ")", ";"], ["leer", "(", "id", ")", ";"]]),
    ]),
]

PRODUCCIONES = {nt: alts for _, _, prods in GRAMATICAS for nt, alts in prods}
NO_TERMINALES = set(PRODUCCIONES)
TERMINALES = sorted({s for alts in PRODUCCIONES.values() for alt in alts for s in alt if s not in NO_TERMINALES})

# Clases de token del lexer ANTLR que aparecen como terminales abstractos en la gramática.
CLASE_TOKEN = {
    "ID": "id",
    "NUM_ENTERO": "num_ent",
    "NUM_DECIMAL": "num_dec",
    "LIT_PORCENTAJE": "lit_porc",
    "CADENA": "cadena",
    "MONEDA": "moneda",
}


def texto_produccion(nt: str, alts) -> str:
    cuerpo = " | ".join(" ".join(a) if a else "ε" for a in alts)
    return f"{nt} → {cuerpo}"


if __name__ == "__main__":
    for gid, titulo, prods in GRAMATICAS:
        print(f"{gid}. {titulo}")
        for nt, alts in prods:
            print("   ", texto_produccion(nt, alts))
    print("\nTerminales:", " ".join(TERMINALES))
