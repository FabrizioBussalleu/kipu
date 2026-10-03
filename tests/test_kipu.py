"""Pruebas automáticas del front end de Kipu (Hito 1).

Ejecutar desde la raíz del repositorio:
    python -m unittest discover -s tests -v

Convención de los archivos .kp de prueba: la primera línea indica el resultado esperado.
    // espera: OK
    // espera: SEM-03@4 SEM-03@5      (código de error @ línea, en orden)
Para las pruebas sintácticas inválidas solo se compara el primer error reportado,
porque ANTLR puede emitir errores adicionales durante la recuperación.
"""
import os
import sys
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))
sys.path.insert(0, os.path.join(RAIZ, "tests"))

from antlr4 import CommonTokenStream, InputStream, Token  # noqa: E402

from construcciones import CONSTRUCCIONES  # noqa: E402
from errores import RecolectorErrores  # noqa: E402
from generated.KipuLexer import KipuLexer  # noqa: E402
from generated.KipuParser import KipuParser  # noqa: E402
from kipu import compilar  # noqa: E402

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
        self.assertEqual(tipos_de_token("si sino sinoCaso siguiente monto montos"),
                         ["SI", "SINO", "ID", "ID", "MONTO", "ID"])

    def test_operadores_compuestos(self):
        self.assertEqual(tipos_de_token("<= >= == != += -= < > ="),
                         ["MENOR_IGUAL", "MAYOR_IGUAL", "IGUAL", "DIFERENTE", "MAS_ASIG",
                          "MENOS_ASIG", "MENOR", "MAYOR", "ASIG"])

    def test_comentarios_ignorados(self):
        self.assertEqual(tipos_de_token("a // comentario\n/* bloque\n */ b"), ["ID", "ID"])


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
