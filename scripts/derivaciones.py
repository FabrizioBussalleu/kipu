"""Genera y verifica las derivaciones más a la izquierda de los ejemplos de cada construcción.

1. Tokeniza cada ejemplo con el analizador léxico generado por ANTLR (src/generated).
2. Reconoce la secuencia de tokens con la gramática BNF del informe (scripts/gramatica_bnf.py)
   usando un parser Earley (lark), y verifica que no haya ambigüedad.
3. Recorre el árbol en preorden para producir la derivación más a la izquierda (⇒lm).
4. Verifica además que todos los programas válidos de tests/sintactico/validos sean
   aceptados por la gramática BNF (consistencia entre el informe y Kipu.g4).

Salida: docs/derivaciones.json y docs/anexo_derivaciones.md

Requiere: pip install lark
Uso: python scripts/derivaciones.py
"""
import json
import os
import sys

from lark import Lark, Tree

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))
sys.path.insert(0, os.path.join(RAIZ, "tests"))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from antlr4 import InputStream  # noqa: E402

from construcciones import CONSTRUCCIONES  # noqa: E402
from generated.KipuLexer import KipuLexer  # noqa: E402
from gramatica_bnf import CLASE_TOKEN, GRAMATICAS, PRODUCCIONES, TERMINALES  # noqa: E402

CODIGO = {t: f"t{i:03d}" for i, t in enumerate(TERMINALES)}
TERMINAL_DE_CODIGO = {v: k for k, v in CODIGO.items()}


def gramatica_lark() -> str:
    lineas = []
    for nt, alts in PRODUCCIONES.items():
        cuerpo = " | ".join(" ".join(CODIGO[s].upper() if s in CODIGO else s for s in alt) for alt in alts)
        lineas.append(f"{nt}: {cuerpo}")
    for t, c in CODIGO.items():
        lineas.append(f'{c.upper()}: "{c}"')
    lineas.append('%ignore " "')
    return "\n".join(lineas)


def tokenizar(codigo: str) -> list[tuple[str, str]]:
    """Devuelve pares (terminal de la gramática, lexema)."""
    lexer = KipuLexer(InputStream(codigo))
    salida = []
    for t in lexer.getAllTokens():
        nombre = KipuLexer.symbolicNames[t.type]
        salida.append((CLASE_TOKEN.get(nombre, t.text), t.text))
    return salida


def tiene_ambiguedad(arbol) -> bool:
    return any(isinstance(n, Tree) and n.data == "_ambig" for n in arbol.iter_subtrees())


def derivacion_izquierda(arbol: Tree) -> list[list[str]]:
    """Cada paso es la forma sentencial como lista de símbolos."""
    forma = [arbol]
    pasos = [[arbol.data]]
    while True:
        idx = next((i for i, x in enumerate(forma) if isinstance(x, Tree)), None)
        if idx is None:
            break
        nodo = forma[idx]
        forma = forma[:idx] + list(nodo.children) + forma[idx + 1:]
        pasos.append([x.data if isinstance(x, Tree) else TERMINAL_DE_CODIGO[str(x)] for x in forma])
    return pasos


def main() -> int:
    gramatica = gramatica_lark()
    parsers = {}

    def parser(inicio):
        if inicio not in parsers:
            parsers[inicio] = Lark(gramatica, start=inicio, parser="earley",
                                   keep_all_tokens=True, ambiguity="explicit")
        return parsers[inicio]

    resultado = []
    fallos = 0
    for c in CONSTRUCCIONES:
        entrada = {"id": c["id"], "nombre": c["nombre"], "simbolo": c["simbolo"], "derivaciones": []}
        for i, ejemplo in enumerate(c["ejemplos"]):
            tokens = tokenizar(ejemplo)
            cadena = " ".join(CODIGO[t] for t, _ in tokens)
            try:
                arbol = parser(c["simbolo"]).parse(cadena)
            except Exception as exc:  # noqa: BLE001
                print(f"[FALLA] {c['id']} ejemplo {i + 1}: {ejemplo}\n        {exc}")
                fallos += 1
                continue
            if tiene_ambiguedad(arbol):
                print(f"[AMBIGUA] {c['id']} ejemplo {i + 1}: {ejemplo}")
                fallos += 1
                continue
            if i in c["derivar"]:
                pasos = derivacion_izquierda(arbol)
                entrada["derivaciones"].append({
                    "ejemplo": ejemplo,
                    "tokens": [t for t, _ in tokens],
                    "lexemas": [lx for _, lx in tokens],
                    "pasos": pasos,
                })
        resultado.append(entrada)
        print(f"{c['id']}: 5/5 ejemplos reconocidos por la BNF, {len(entrada['derivaciones'])} derivaciones generadas")

    # Consistencia con programas completos
    carpeta = os.path.join(RAIZ, "tests", "sintactico", "validos")
    for archivo in sorted(os.listdir(carpeta)):
        with open(os.path.join(carpeta, archivo), encoding="utf-8") as f:
            codigo = f.read()
        cadena = " ".join(CODIGO[t] for t, _ in tokenizar(codigo))
        try:
            arbol = parser("programa").parse(cadena)
            estado = "AMBIGUO" if tiene_ambiguedad(arbol) else "OK"
        except Exception:  # noqa: BLE001
            estado = "FALLA"
        if estado != "OK":
            fallos += 1
        print(f"BNF acepta {archivo}: {estado}")

    docs = os.path.join(RAIZ, "docs")
    os.makedirs(docs, exist_ok=True)
    with open(os.path.join(docs, "derivaciones.json"), "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=1)

    md = ["# Anexo: derivaciones más a la izquierda", "",
          "Generado y verificado automáticamente con `python scripts/derivaciones.py`.",
          "Cada ejemplo se tokeniza con el lexer ANTLR de Kipu y se deriva con la gramática BNF del informe.", ""]
    for g in resultado:
        titulo = next(t for gid, t, _ in GRAMATICAS if gid == g["id"])
        md += [f"## {g['id']}. {titulo}", ""]
        for n, d in enumerate(g["derivaciones"], 1):
            md += [f"### Ejemplo {g['id']}.{n}", "", "```kipu", d["ejemplo"], "```", "",
                   "Tokens: `" + " ".join(d["tokens"]) + "`", "", "```"]
            for k, paso in enumerate(d["pasos"]):
                md.append(("    " if k == 0 else "⇒lm ") + " ".join(paso))
            md += ["```", ""]
    with open(os.path.join(docs, "anexo_derivaciones.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print("Sin fallos." if not fallos else f"{fallos} fallo(s).")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
