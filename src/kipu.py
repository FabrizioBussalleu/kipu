"""Driver del compilador Kipu (Hito 1).

Uso:
    python src/kipu.py <archivo.kp> [--tokens] [--arbol] [--simbolos] [--solo-lexico] [--solo-sintactico]

Fases ejecutadas: análisis léxico, sintáctico y semántico (parcial).
Código de salida: 0 si no hay errores, 1 si hay errores, 2 si el archivo no existe.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from antlr4 import CommonTokenStream, FileStream, InputStream, Token  # noqa: E402
from antlr4.tree.Tree import TerminalNode  # noqa: E402

from errores import ErrorCompilacion, RecolectorErrores  # noqa: E402
from generated.KipuLexer import KipuLexer  # noqa: E402
from generated.KipuParser import KipuParser  # noqa: E402
from semantico import AnalizadorSemantico  # noqa: E402

VERSION = "0.1.0 (Hito 1)"


class ResultadoCompilacion:
    def __init__(self):
        self.tokens = []
        self.arbol = None
        self.parser = None
        self.semantico = None
        self.errores: list[ErrorCompilacion] = []

    @property
    def ok(self) -> bool:
        return not self.errores

    def codigos(self) -> list[str]:
        return [e.codigo for e in self.errores]


def compilar(codigo: str | None = None, ruta: str | None = None, hasta: str = "semantico") -> ResultadoCompilacion:
    """Ejecuta las fases del front end. `hasta` puede ser 'lexico', 'sintactico' o 'semantico'."""
    res = ResultadoCompilacion()
    entrada = FileStream(ruta, encoding="utf-8") if ruta else InputStream(codigo)

    # Fase 1: análisis léxico
    lexer = KipuLexer(entrada)
    err_lex = RecolectorErrores("LEX")
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lex)
    flujo = CommonTokenStream(lexer)
    flujo.fill()
    res.tokens = [t for t in flujo.tokens if t.type != Token.EOF]
    res.errores.extend(err_lex.errores)
    if hasta == "lexico":
        return res

    # Fase 2: análisis sintáctico
    parser = KipuParser(flujo)
    err_sin = RecolectorErrores("SIN")
    parser.removeErrorListeners()
    parser.addErrorListener(err_sin)
    res.arbol = parser.programa()
    res.parser = parser
    res.errores.extend(err_sin.errores)
    if hasta == "sintactico" or res.errores:
        return res

    # Fase 3: análisis semántico (solo si no hubo errores previos)
    sem = AnalizadorSemantico()
    sem.visit(res.arbol)
    res.semantico = sem
    res.errores.extend(sem.errores)
    return res


# ----------------------------------------------------------------------------
# Presentación de resultados
# ----------------------------------------------------------------------------
def imprimir_tokens(res: ResultadoCompilacion) -> None:
    nombres = KipuLexer.symbolicNames
    print(f"{'#':>4}  {'Lín:Col':<9} {'Token':<16} Lexema")
    print("-" * 52)
    for i, t in enumerate(res.tokens, 1):
        print(f"{i:>4}  {f'{t.line}:{t.column + 1}':<9} {nombres[t.type]:<16} {t.text}")


def imprimir_arbol(nodo, parser, prefijo: str = "", ultimo: bool = True, raiz: bool = True) -> None:
    conector = "" if raiz else ("└── " if ultimo else "├── ")
    if isinstance(nodo, TerminalNode):
        tok = nodo.getSymbol()
        if tok.type == Token.EOF:
            etiqueta = "EOF"
        else:
            etiqueta = f"{KipuLexer.symbolicNames[tok.type]} '{tok.text}'"
    else:
        etiqueta = parser.ruleNames[nodo.getRuleIndex()]
        alt = type(nodo).__name__.replace("Context", "")
        if alt[0].lower() + alt[1:] != etiqueta:
            etiqueta += f" <{alt[0].lower() + alt[1:]}>"
    print(prefijo + conector + etiqueta)
    if isinstance(nodo, TerminalNode):
        return
    hijos = list(nodo.getChildren())
    nuevo_prefijo = prefijo + ("" if raiz else ("    " if ultimo else "│   "))
    for i, hijo in enumerate(hijos):
        imprimir_arbol(hijo, parser, nuevo_prefijo, i == len(hijos) - 1, False)


def imprimir_simbolos(res: ResultadoCompilacion) -> None:
    print(f"{'Ámbito':<26} {'Nombre':<18} {'Categoría':<11} {'Línea':<6} Tipo")
    print("-" * 90)
    for ambito in res.semantico.tabla.todos:
        for s in ambito.simbolos.values():
            tipo = str(s.tipo) if s.tipo is not None else "(sin retorno)"
            if s.categoria == "regla":
                tipo = f"({', '.join(map(str, s.parametros))}) -> {tipo}"
            print(f"{ambito.nombre:<26} {s.nombre:<18} {s.categoria:<11} {s.linea:<6} {tipo}")


def main(argv=None) -> int:
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:
            pass

    ap = argparse.ArgumentParser(prog="kipu", description="Compilador del lenguaje Kipu (front end, Hito 1)")
    ap.add_argument("archivo", help="programa fuente .kp")
    ap.add_argument("--tokens", action="store_true", help="muestra la tabla de tokens")
    ap.add_argument("--arbol", action="store_true", help="muestra el árbol sintáctico")
    ap.add_argument("--simbolos", action="store_true", help="muestra la tabla de símbolos")
    ap.add_argument("--solo-lexico", action="store_true", help="ejecuta solo el análisis léxico")
    ap.add_argument("--solo-sintactico", action="store_true", help="ejecuta hasta el análisis sintáctico")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.archivo):
        print(f"Error: no existe el archivo '{args.archivo}'.", file=sys.stderr)
        return 2

    hasta = "lexico" if args.solo_lexico else "sintactico" if args.solo_sintactico else "semantico"
    res = compilar(ruta=args.archivo, hasta=hasta)

    print(f"Kipu {VERSION}  |  {args.archivo}")
    fases = [("LEX", "Análisis léxico"), ("SIN", "Análisis sintáctico"), ("SEM", "Análisis semántico")]
    limite = {"lexico": 1, "sintactico": 2, "semantico": 3}[hasta]
    bloqueado = False
    for i, (fase, nombre) in enumerate(fases[:limite], 1):
        n = sum(1 for e in res.errores if e.fase == fase)
        if bloqueado:
            estado = "OMITIDO (errores en fases previas)"
        elif n:
            estado = f"{n} error(es)"
        else:
            estado = "OK" + (f" ({len(res.tokens)} tokens)" if fase == "LEX" else "")
        print(f"  [{i}/{limite}] {nombre:<20} {estado}")
        if fase == "SIN" and any(e.fase in ("LEX", "SIN") for e in res.errores):
            bloqueado = True

    if args.tokens:
        print()
        imprimir_tokens(res)
    if args.arbol and res.arbol is not None:
        print()
        imprimir_arbol(res.arbol, res.parser)
    if args.simbolos and res.semantico is not None:
        print()
        imprimir_simbolos(res)

    print()
    if res.ok:
        print("Resultado: programa válido, sin errores.")
        return 0
    for e in res.errores:
        print(e)
    print(f"\nResultado: {len(res.errores)} error(es) encontrados.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
