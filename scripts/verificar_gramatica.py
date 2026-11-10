"""Verifica que grammar/Kipu.g4 cumpla los lineamientos del curso para gramáticas ANTLR4.

Reglas verificadas:
  L1. El parser no contiene literales: todo símbolo, operador y palabra reservada es un token con nombre.
  L2. No se usa el operador ? (opcionales con alternativa vacía).
  L3. No se usan los operadores * ni + de repetición (ni en el parser ni en el lexer).
  L4. No hay subreglas agrupadas con paréntesis ni asignaciones de etiquetas (op=...).
  L5. Las palabras reservadas se declaran antes que ID.
  L6. No existe regla para el comentario de bloque /* */.
Los caracteres * + ? ( ) dentro de literales ('*') o conjuntos ([0-9]) no cuentan: son símbolos
del lenguaje, no operadores de la gramática.

Uso: python scripts/verificar_gramatica.py [ruta.g4]
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def tokenizar_g4(texto: str):
    """Devuelve una lista de (tipo, valor): LIT, SET, COMENT, OTRO."""
    i, n, out = 0, len(texto), []
    while i < n:
        c = texto[i]
        if texto.startswith("//", i):
            j = texto.find("\n", i)
            j = n if j < 0 else j
            i = j
            continue
        if texto.startswith("/*", i):
            j = texto.index("*/", i) + 2
            i = j
            continue
        if c == "'":
            j = i + 1
            while texto[j] != "'":
                j += 2 if texto[j] == "\\" else 1
            out.append(("LIT", texto[i:j + 1]))
            i = j + 1
            continue
        if c == "[":
            j = i + 1
            while texto[j] != "]":
                j += 2 if texto[j] == "\\" else 1
            out.append(("SET", texto[i:j + 1]))
            i = j + 1
            continue
        out.append(("OTRO", c))
        i += 1
    return out


def reglas(texto: str):
    """Separa la gramática en reglas: lista de (nombre, es_fragment, [(tipo, valor)])."""
    toks = tokenizar_g4(texto)
    resultado, actual = [], []
    for t in toks:
        if t == ("OTRO", ";"):
            resultado.append(actual)
            actual = []
        else:
            actual.append(t)
    salida = []
    for r in resultado:
        cabecera = "".join(v for tipo, v in r if tipo == "OTRO").strip()
        if cabecera.startswith("grammar"):
            continue
        texto_regla = "".join(v for _, v in r)
        m = re.match(r"\s*(fragment\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*:", texto_regla)
        if not m:
            continue
        idx = texto_regla.index(":", m.start(2))
        # cuerpo: tokens después del ':'
        acumulado, cuerpo = 0, []
        for tipo, v in r:
            if acumulado > idx:
                cuerpo.append((tipo, v))
            acumulado += len(v)
        salida.append((m.group(2), bool(m.group(1)), cuerpo))
    return salida


def verificar(ruta: str) -> list[str]:
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()
    errores = []
    lista = reglas(texto)
    for nombre, es_fragment, cuerpo in lista:
        es_parser = nombre[0].islower()
        fuera = "".join(v for tipo, v in cuerpo if tipo == "OTRO")
        sin_accion = re.sub(r"->\s*skip", "", fuera)
        if es_parser and any(tipo == "LIT" for tipo, _ in cuerpo):
            lits = [v for tipo, v in cuerpo if tipo == "LIT"]
            errores.append(f"L1 {nombre}: literales en el parser {lits}")
        if "?" in sin_accion:
            errores.append(f"L2 {nombre}: usa el operador ?")
        if "*" in sin_accion or "+" in sin_accion:
            errores.append(f"L3 {nombre}: usa * o + como operador de repetición")
        if "(" in sin_accion or ")" in sin_accion:
            errores.append(f"L4 {nombre}: usa subreglas agrupadas con paréntesis")
        if "=" in sin_accion or "#" in sin_accion:
            errores.append(f"L4 {nombre}: usa etiquetas (op=, x=) o alternativas etiquetadas (#)")
        if any(tipo == "LIT" and "/*" in v for tipo, v in cuerpo):
            errores.append(f"L6 {nombre}: define el comentario de bloque /* */")
    # L5: palabras reservadas antes que ID
    orden = [n for n, frag, _ in lista if n[0].isupper() and not frag]
    if "ID" in orden:
        pos_id = orden.index("ID")
        for nombre, frag, cuerpo in lista:
            if frag or not nombre[0].isupper():
                continue
            lits = [v.strip("'") for tipo, v in cuerpo if tipo == "LIT"]
            otros = [v for tipo, v in cuerpo if tipo == "OTRO" and v.strip() and v not in "|"]
            if lits and not otros and all(re.fullmatch(r"[A-Za-z]+", x) for x in lits):
                if orden.index(nombre) > pos_id:
                    errores.append(f"L5 {nombre}: palabra reservada declarada después de ID")
    else:
        errores.append("L5: no existe el token ID")
    return errores


def main() -> int:
    ruta = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "grammar", "Kipu.g4")
    errores = verificar(ruta)
    n_reglas = len(reglas(open(ruta, encoding="utf-8").read()))
    if errores:
        print(f"{ruta}: {len(errores)} incumplimiento(s)")
        for e in errores:
            print("  " + e)
        return 1
    print(f"{ruta}: {n_reglas} reglas, cumple los lineamientos L1 a L6.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
