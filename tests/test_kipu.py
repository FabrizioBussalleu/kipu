"""Pruebas automáticas del compilador Kipu (Hito 2).

Ejecutar desde la raíz del repositorio:
    python -m unittest discover -s tests -v

Convención de los archivos .kp de prueba: la primera línea indica el resultado esperado.
    // espera: OK
    // espera: SEM-03@4 SEM-03@5      (código de error @ línea, en orden)
Para las pruebas sintácticas inválidas solo se compara el primer error reportado,
porque ANTLR puede emitir errores adicionales durante la recuperación.
Las pruebas de LLVM (tests/llvm) comparan la salida de la ejecución JIT con el archivo .esperado.
"""
import os
import re
import sys
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))
sys.path.insert(0, os.path.join(RAIZ, "tests"))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from antlr4 import CommonTokenStream, InputStream, Token  # noqa: E402

from construcciones import CONSTRUCCIONES  # noqa: E402
from errores import RecolectorErrores  # noqa: E402
from generated.KipuLexer import KipuLexer  # noqa: E402
from generated.KipuParser import KipuParser  # noqa: E402
from kipu import compilar  # noqa: E402
from semantico import DESCRIPCION_ERRORES  # noqa: E402

DIR_PRUEBAS = os.path.join(RAIZ, "tests")


def esperado(ruta: str) -> list[str]:
    with open(ruta, encoding="utf-8") as f:
        cabecera = f.readline().strip()
    assert cabecera.startswith("// espera:"), f"{ruta} no tiene cabecera '// espera:'"
    valor = cabecera.split(":", 1)[1].split()
    return [] if valor == ["OK"] else valor


def obtenido(res) -> list[str]:
    return [f"{e.codigo}@{e.linea}" for e in res.errores]


def archivos(*partes):
    carpeta = os.path.join(DIR_PRUEBAS, *partes)
    return sorted(os.path.join(carpeta, a) for a in os.listdir(carpeta) if a.endswith(".kp"))


def tipos_de_token(codigo: str) -> list[str]:
    lexer = KipuLexer(InputStream(codigo))
    lexer.removeErrorListeners()
    return [KipuLexer.symbolicNames[t.type] for t in lexer.getAllTokens()]


# ----------------------------------------------------------------------------
class PruebasGramatica(unittest.TestCase):
    def test_lineamientos_del_curso(self):
        """Kipu.g4 no usa ?, *, +, subreglas, etiquetas ni literales en el parser."""
        from verificar_gramatica import verificar
        self.assertEqual(verificar(os.path.join(RAIZ, "grammar", "Kipu.g4")), [])

    def test_derivaciones_sin_ambiguedad(self):
        """Los 35 ejemplos se reconocen completos y sin ambigüedad exacta."""
        from derivaciones import analizar, derivacion_izquierda
        from gramatica_bnf import producciones
        prods = producciones()
        for c in CONSTRUCCIONES:
            for ejemplo in c["ejemplos"]:
                with self.subTest(construccion=c["id"], ejemplo=ejemplo):
                    arbol, parser, vig, completo = analizar(ejemplo, c["regla_antlr"])
                    self.assertEqual(vig.errores, [])
                    self.assertEqual(vig.ambiguedades, [])
                    self.assertTrue(completo)
                    for _, prod in derivacion_izquierda(arbol, parser)[1:]:
                        self.assertIn(prod[1], prods[prod[0]])


class PruebasLexicas(unittest.TestCase):
    def test_archivos_lexicos(self):
        for ruta in archivos("lexico"):
            with self.subTest(archivo=os.path.basename(ruta)):
                res = compilar(ruta=ruta, hasta="lexico")
                self.assertEqual(obtenido(res), esperado(ruta), [str(e) for e in res.errores])

    def test_declaracion_monto(self):
        self.assertEqual(
            tipos_de_token("var s: monto<PEN> = 10.50 PEN;"),
            ["VAR", "ID", "DOS_PUNTOS", "MONTO", "MENOR", "MONEDA", "MAYOR", "ASIG",
             "NUM_DECIMAL", "MONEDA", "PUNTO_COMA"],
        )

    def test_porcentaje_vs_numero(self):
        self.assertEqual(tipos_de_token("18% 18 18.5 18.5%"),
                         ["LIT_PORCENTAJE", "NUM_ENTERO", "NUM_DECIMAL", "LIT_PORCENTAJE"])

    def test_palabra_clave_vs_identificador(self):
        self.assertEqual(tipos_de_token("si sino sinoCaso siguiente monto montos año"),
                         ["SI", "SINO", "ID", "ID", "MONTO", "ID", "ID"])

    def test_operadores_compuestos(self):
        self.assertEqual(tipos_de_token("<= >= == != += -= < > ="),
                         ["MENOR_IGUAL", "MAYOR_IGUAL", "IGUAL", "DIFERENTE", "MAS_ASIG",
                          "MENOS_ASIG", "MENOR", "MAYOR", "ASIG"])

    def test_comentarios_ignorados(self):
        self.assertEqual(tipos_de_token("a // comentario\nb"), ["ID", "ID"])

    def test_sin_comentario_de_bloque(self):
        # Por lineamiento se omite el comentario de bloque: /* se reconoce como DIV MULT
        self.assertEqual(tipos_de_token("/* x */"), ["DIV", "MULT", "ID", "MULT", "DIV"])

    def test_fragments_recursivos(self):
        """ID, números y cadenas se reconocen con fragments recursivos (sin * ni +)."""
        self.assertEqual(tipos_de_token('abc123 1234567 3.14159 "con \\"escape\\""'),
                         ["ID", "NUM_ENTERO", "NUM_DECIMAL", "CADENA"])


class PruebasSintacticas(unittest.TestCase):
    def test_programas_validos(self):
        for ruta in archivos("sintactico", "validos"):
            with self.subTest(archivo=os.path.basename(ruta)):
                res = compilar(ruta=ruta, hasta="sintactico")
                self.assertEqual(obtenido(res), [], [str(e) for e in res.errores])

    def test_programas_invalidos(self):
        for ruta in archivos("sintactico", "invalidos"):
            with self.subTest(archivo=os.path.basename(ruta)):
                res = compilar(ruta=ruta, hasta="sintactico")
                self.assertTrue(res.errores, "se esperaba al menos un error sintáctico")
                self.assertEqual(obtenido(res)[:1], esperado(ruta), [str(e) for e in res.errores])

    def test_ejemplos_de_cada_construccion(self):
        """Los 5 ejemplos de cada construcción se reconocen con su regla ANTLR."""
        for c in CONSTRUCCIONES:
            for ejemplo in c["ejemplos"]:
                with self.subTest(construccion=c["id"], ejemplo=ejemplo):
                    lexer = KipuLexer(InputStream(ejemplo))
                    parser = KipuParser(CommonTokenStream(lexer))
                    errores = RecolectorErrores("SIN")
                    parser.removeErrorListeners()
                    parser.addErrorListener(errores)
                    getattr(parser, c["regla_antlr"])()
                    self.assertEqual(errores.errores, [])
                    self.assertEqual(parser.getCurrentToken().type, Token.EOF, "no se consumió toda la entrada")


class PruebasSemanticas(unittest.TestCase):
    def test_programas_validos(self):
        for ruta in archivos("semantico", "validos") + archivos("..", "ejemplos"):
            with self.subTest(archivo=os.path.basename(ruta)):
                res = compilar(ruta=ruta)
                self.assertEqual(obtenido(res), [], [str(e) for e in res.errores])

    def test_programas_invalidos(self):
        for ruta in archivos("semantico", "invalidos"):
            with self.subTest(archivo=os.path.basename(ruta)):
                res = compilar(ruta=ruta)
                self.assertEqual(obtenido(res), esperado(ruta), [str(e) for e in res.errores])

    def test_cobertura_de_errores(self):
        """Cada error semántico SEM-01 a SEM-14 tiene al menos dos casos de prueba negativos."""
        conteo = {codigo: 0 for codigo in DESCRIPCION_ERRORES}
        for ruta in archivos("semantico", "invalidos"):
            for marca in esperado(ruta):
                conteo[marca.split("@")[0]] += 1
        faltantes = {c: n for c, n in conteo.items() if n < 2}
        self.assertEqual(faltantes, {}, "códigos con menos de 2 casos")


class PruebasLLVM(unittest.TestCase):
    def test_ir_valido_y_salida_esperada(self):
        """El IR generado pasa el verificador de LLVM y la ejecución JIT produce la salida esperada."""
        from ejecutor import ejecutar, verificar_ir
        rutas = [r for r in archivos("llvm") if os.path.exists(r[:-3] + ".esperado")]
        self.assertGreaterEqual(len(rutas), 5)
        for ruta in rutas:
            with self.subTest(archivo=os.path.basename(ruta)):
                res = compilar(ruta=ruta, hasta="llvm")
                self.assertEqual(obtenido(res), [], [str(e) for e in res.errores])
                verificar_ir(res.ir)
                codigo, salida = ejecutar(res.ir, eco=False)
                with open(ruta[:-3] + ".esperado", encoding="utf-8") as f:
                    self.assertEqual(salida, f.read())
                self.assertEqual(codigo, 0)

    def test_construccion_pendiente(self):
        for ruta in archivos("llvm"):
            if os.path.exists(ruta[:-3] + ".esperado"):
                continue
            with self.subTest(archivo=os.path.basename(ruta)):
                res = compilar(ruta=ruta, hasta="llvm")
                self.assertEqual(obtenido(res), esperado(ruta))

    def test_ejemplo_detracciones(self):
        from ejecutor import ejecutar
        res = compilar(ruta=os.path.join(RAIZ, "ejemplos", "detracciones.kp"), hasta="llvm")
        self.assertTrue(res.ok, [str(e) for e in res.errores])
        _, salida = ejecutar(res.ir, eco=False)
        self.assertIn("Total cobrado: 2701.12 PEN = 720.30 USD", salida)

    def test_montos_en_centimos(self):
        res = compilar(codigo="var m: monto<PEN> = 1250.50 PEN;\nmostrar(m);", hasta="llvm")
        self.assertTrue(re.search(r"store i64 125050", res.ir), "el monto debe almacenarse en céntimos (i64)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
