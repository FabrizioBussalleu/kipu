"""Genera y verifica las derivaciones más a la izquierda de los ejemplos de cada construcción.

Como Kipu.g4 está en forma estándar (BNF pura), el árbol de análisis de ANTLR corresponde
exactamente a la gramática del informe. Para cada ejemplo:
  1. Se analiza con la regla inicial de su construcción (parser ANTLR de Kipu).
  2. Se exige que no haya errores y que se consuma toda la entrada.
  3. Se activa la detección exacta de ambigüedad de ANTLR (LL_EXACT_AMBIG_DETECTION):
     cualquier ambigüedad reportada hace fallar la verificación.
  4. El árbol se recorre en preorden: reemplazar siempre el no terminal de más a la
     izquierda por los hijos de su nodo es, por definición, la derivación más a la izquierda.
  5. Se comprueba que cada paso aplique una producción existente en Kipu.g4.

Salida: docs/derivaciones.json y docs/anexo_derivaciones.md
Uso: python scripts/derivaciones.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))
sys.path.insert(0, os.path.join(RAIZ, "tests"))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from antlr4 import CommonTokenStream, InputStream, Token  # noqa: E402
from antlr4.atn.PredictionMode import PredictionMode  # noqa: E402
from antlr4.error.ErrorListener import ErrorListener  # noqa: E402
from antlr4.tree.Tree import TerminalNode  # noqa: E402

from construcciones import CONSTRUCCIONES  # noqa: E402
from generated.KipuLexer import KipuLexer  # noqa: E402
from generated.KipuParser import KipuParser  # noqa: E402
from gramatica_bnf import GRUPOS, producciones  # noqa: E402


class Vigilante(ErrorListener):
    def __init__(self):
        self.errores, self.ambiguedades = [], []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"{line}:{column} {msg}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        if exact:
            self.ambiguedades.append((startIndex, stopIndex, str(ambigAlts)))


def analizar(codigo: str, regla: str):
    lexer = KipuLexer(InputStream(codigo))
    lexer.removeErrorListeners()
    tokens = CommonTokenStream(lexer)
    parser = KipuParser(tokens)
    parser.removeErrorListeners()
    vig = Vigilante()
    parser.addErrorListener(vig)
    parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION
    arbol = getattr(parser, regla)()
    completo = parser.getCurrentToken().type == Token.EOF
    return arbol, parser, vig, completo


def simbolo(nodo, parser) -> str:
    if isinstance(nodo, TerminalNode):
        return KipuLexer.symbolicNames[nodo.getSymbol().type]
    return parser.ruleNames[nodo.getRuleIndex()]


def derivacion_izquierda(arbol, parser):
    """Lista de pasos; cada paso = (forma sentencial, producción aplicada)."""
    forma = [arbol]
    pasos = [([simbolo(arbol, parser)], None)]
    while True:
        idx = next((i for i, x in enumerate(forma) if not isinstance(x, TerminalNode)), None)
        if idx is None:
            break
        nodo = forma[idx]
        hijos = list(nodo.getChildren()) if nodo.getChildCount() else []
        produccion = (simbolo(nodo, parser), [simbolo(h, parser) for h in hijos])
        forma = forma[:idx] + hijos + forma[idx + 1:]
        pasos.append(([simbolo(x, parser) for x in forma], produccion))
    return pasos


def main() -> int:
    prods = producciones()
    resultado, fallos = [], 0
    for c in CONSTRUCCIONES:
        entrada = {"id": c["id"], "nombre": c["nombre"], "simbolo": c["simbolo"], "derivaciones": []}
        aceptados = 0
        for i, ejemplo in enumerate(c["ejemplos"]):
            arbol, parser, vig, completo = analizar(ejemplo, c["regla_antlr"])
            if vig.errores or not completo or vig.ambiguedades:
                print(f"[FALLA] {c['id']}.{i + 1} {ejemplo}: errores={vig.errores} completo={completo} "
                      f"ambiguedades={vig.ambiguedades}")
                fallos += 1
                continue
            aceptados += 1
            if i not in c["derivar"]:
                continue
            pasos = derivacion_izquierda(arbol, parser)
            for forma, prod in pasos[1:]:
                nt, cuerpo = prod
                if cuerpo not in prods[nt]:
                    print(f"[FALLA] {c['id']}.{i + 1}: producción inexistente {nt} -> {cuerpo}")
                    fallos += 1
            lexemas = [t.text for t in KipuLexer(InputStream(ejemplo)).getAllTokens()]
            entrada["derivaciones"].append({
                "ejemplo": ejemplo,
                "tokens": pasos[-1][0],
                "lexemas": lexemas,
                "pasos": [forma for forma, _ in pasos],
                "producciones": [None] + [f"{nt} → {' '.join(cu) if cu else 'ε'}" for _, (nt, cu) in pasos[1:]],
            })
        resultado.append(entrada)
        print(f"{c['id']}: {aceptados}/5 ejemplos aceptados sin ambigüedad, "
              f"{len(entrada['derivaciones'])} derivaciones generadas")

    docs = os.path.join(RAIZ, "docs")
    os.makedirs(docs, exist_ok=True)
    with open(os.path.join(docs, "derivaciones.json"), "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=1)

    titulos = {gid: t for gid, t, _ in GRUPOS}
    md = ["# Anexo A: derivaciones más a la izquierda (Hito 2)", "",
          "Generado y verificado con `python scripts/derivaciones.py` a partir de la gramática actualizada",
          "(grammar/Kipu.g4). En cada paso se reemplaza el no terminal de más a la izquierda por el cuerpo de",
          "una de sus producciones; los terminales son los nombres de token del lexer.", ""]
    for g in resultado:
        md += [f"## {g['id']}. {titulos[g['id']]}", ""]
        for n, d in enumerate(g["derivaciones"], 1):
            md += [f"### Ejemplo {g['id']}.{n}", "", "```kipu", d["ejemplo"], "```", "",
                   "Cadena de tokens: `" + " ".join(d["tokens"]) + "`", "", "```"]
            for k, paso in enumerate(d["pasos"]):
                linea = ("     " if k == 0 else "⇒lm  ") + " ".join(paso)
                md.append(linea)
            md += ["```", ""]
    with open(os.path.join(docs, "anexo_derivaciones.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    total = sum(len(g["derivaciones"]) for g in resultado)
    print(f"{total} derivaciones escritas en docs/. " + ("Sin fallos." if not fallos else f"{fallos} fallo(s)."))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
