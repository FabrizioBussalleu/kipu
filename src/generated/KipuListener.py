# Generated from grammar/Kipu.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KipuParser import KipuParser
else:
    from KipuParser import KipuParser

# This class defines a complete listener for a parse tree produced by KipuParser.
class KipuListener(ParseTreeListener):

    # Enter a parse tree produced by KipuParser#programa.
    def enterPrograma(self, ctx:KipuParser.ProgramaContext):
        pass

    # Exit a parse tree produced by KipuParser#programa.
    def exitPrograma(self, ctx:KipuParser.ProgramaContext):
        pass


    # Enter a parse tree produced by KipuParser#listaSentencias.
    def enterListaSentencias(self, ctx:KipuParser.ListaSentenciasContext):
        pass

    # Exit a parse tree produced by KipuParser#listaSentencias.
    def exitListaSentencias(self, ctx:KipuParser.ListaSentenciasContext):
        pass


    # Enter a parse tree produced by KipuParser#sentencia.
    def enterSentencia(self, ctx:KipuParser.SentenciaContext):
        pass

    # Exit a parse tree produced by KipuParser#sentencia.
    def exitSentencia(self, ctx:KipuParser.SentenciaContext):
        pass


    # Enter a parse tree produced by KipuParser#bloque.
    def enterBloque(self, ctx:KipuParser.BloqueContext):
        pass

    # Exit a parse tree produced by KipuParser#bloque.
    def exitBloque(self, ctx:KipuParser.BloqueContext):
        pass


    # Enter a parse tree produced by KipuParser#declaracion.
    def enterDeclaracion(self, ctx:KipuParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by KipuParser#declaracion.
    def exitDeclaracion(self, ctx:KipuParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by KipuParser#inicializacion.
    def enterInicializacion(self, ctx:KipuParser.InicializacionContext):
        pass

    # Exit a parse tree produced by KipuParser#inicializacion.
    def exitInicializacion(self, ctx:KipuParser.InicializacionContext):
        pass


    # Enter a parse tree produced by KipuParser#tipo.
    def enterTipo(self, ctx:KipuParser.TipoContext):
        pass

    # Exit a parse tree produced by KipuParser#tipo.
    def exitTipo(self, ctx:KipuParser.TipoContext):
        pass


    # Enter a parse tree produced by KipuParser#asignacion.
    def enterAsignacion(self, ctx:KipuParser.AsignacionContext):
        pass

    # Exit a parse tree produced by KipuParser#asignacion.
    def exitAsignacion(self, ctx:KipuParser.AsignacionContext):
        pass


    # Enter a parse tree produced by KipuParser#opAsignacion.
    def enterOpAsignacion(self, ctx:KipuParser.OpAsignacionContext):
        pass

    # Exit a parse tree produced by KipuParser#opAsignacion.
    def exitOpAsignacion(self, ctx:KipuParser.OpAsignacionContext):
        pass


    # Enter a parse tree produced by KipuParser#expresion.
    def enterExpresion(self, ctx:KipuParser.ExpresionContext):
        pass

    # Exit a parse tree produced by KipuParser#expresion.
    def exitExpresion(self, ctx:KipuParser.ExpresionContext):
        pass


    # Enter a parse tree produced by KipuParser#conjuncion.
    def enterConjuncion(self, ctx:KipuParser.ConjuncionContext):
        pass

    # Exit a parse tree produced by KipuParser#conjuncion.
    def exitConjuncion(self, ctx:KipuParser.ConjuncionContext):
        pass


    # Enter a parse tree produced by KipuParser#negacion.
    def enterNegacion(self, ctx:KipuParser.NegacionContext):
        pass

    # Exit a parse tree produced by KipuParser#negacion.
    def exitNegacion(self, ctx:KipuParser.NegacionContext):
        pass


    # Enter a parse tree produced by KipuParser#igualdad.
    def enterIgualdad(self, ctx:KipuParser.IgualdadContext):
        pass

    # Exit a parse tree produced by KipuParser#igualdad.
    def exitIgualdad(self, ctx:KipuParser.IgualdadContext):
        pass


    # Enter a parse tree produced by KipuParser#relacional.
    def enterRelacional(self, ctx:KipuParser.RelacionalContext):
        pass

    # Exit a parse tree produced by KipuParser#relacional.
    def exitRelacional(self, ctx:KipuParser.RelacionalContext):
        pass


    # Enter a parse tree produced by KipuParser#aritmetica.
    def enterAritmetica(self, ctx:KipuParser.AritmeticaContext):
        pass

    # Exit a parse tree produced by KipuParser#aritmetica.
    def exitAritmetica(self, ctx:KipuParser.AritmeticaContext):
        pass


    # Enter a parse tree produced by KipuParser#termino.
    def enterTermino(self, ctx:KipuParser.TerminoContext):
        pass

    # Exit a parse tree produced by KipuParser#termino.
    def exitTermino(self, ctx:KipuParser.TerminoContext):
        pass


    # Enter a parse tree produced by KipuParser#unario.
    def enterUnario(self, ctx:KipuParser.UnarioContext):
        pass

    # Exit a parse tree produced by KipuParser#unario.
    def exitUnario(self, ctx:KipuParser.UnarioContext):
        pass


    # Enter a parse tree produced by KipuParser#primario.
    def enterPrimario(self, ctx:KipuParser.PrimarioContext):
        pass

    # Exit a parse tree produced by KipuParser#primario.
    def exitPrimario(self, ctx:KipuParser.PrimarioContext):
        pass


    # Enter a parse tree produced by KipuParser#literal.
    def enterLiteral(self, ctx:KipuParser.LiteralContext):
        pass

    # Exit a parse tree produced by KipuParser#literal.
    def exitLiteral(self, ctx:KipuParser.LiteralContext):
        pass


    # Enter a parse tree produced by KipuParser#numero.
    def enterNumero(self, ctx:KipuParser.NumeroContext):
        pass

    # Exit a parse tree produced by KipuParser#numero.
    def exitNumero(self, ctx:KipuParser.NumeroContext):
        pass


    # Enter a parse tree produced by KipuParser#llamada.
    def enterLlamada(self, ctx:KipuParser.LlamadaContext):
        pass

    # Exit a parse tree produced by KipuParser#llamada.
    def exitLlamada(self, ctx:KipuParser.LlamadaContext):
        pass


    # Enter a parse tree produced by KipuParser#argumentos.
    def enterArgumentos(self, ctx:KipuParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by KipuParser#argumentos.
    def exitArgumentos(self, ctx:KipuParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by KipuParser#argumentosCola.
    def enterArgumentosCola(self, ctx:KipuParser.ArgumentosColaContext):
        pass

    # Exit a parse tree produced by KipuParser#argumentosCola.
    def exitArgumentosCola(self, ctx:KipuParser.ArgumentosColaContext):
        pass


    # Enter a parse tree produced by KipuParser#seleccion.
    def enterSeleccion(self, ctx:KipuParser.SeleccionContext):
        pass

    # Exit a parse tree produced by KipuParser#seleccion.
    def exitSeleccion(self, ctx:KipuParser.SeleccionContext):
        pass


    # Enter a parse tree produced by KipuParser#parteSino.
    def enterParteSino(self, ctx:KipuParser.ParteSinoContext):
        pass

    # Exit a parse tree produced by KipuParser#parteSino.
    def exitParteSino(self, ctx:KipuParser.ParteSinoContext):
        pass


    # Enter a parse tree produced by KipuParser#colaSino.
    def enterColaSino(self, ctx:KipuParser.ColaSinoContext):
        pass

    # Exit a parse tree produced by KipuParser#colaSino.
    def exitColaSino(self, ctx:KipuParser.ColaSinoContext):
        pass


    # Enter a parse tree produced by KipuParser#iteracion.
    def enterIteracion(self, ctx:KipuParser.IteracionContext):
        pass

    # Exit a parse tree produced by KipuParser#iteracion.
    def exitIteracion(self, ctx:KipuParser.IteracionContext):
        pass


    # Enter a parse tree produced by KipuParser#pasoOpcional.
    def enterPasoOpcional(self, ctx:KipuParser.PasoOpcionalContext):
        pass

    # Exit a parse tree produced by KipuParser#pasoOpcional.
    def exitPasoOpcional(self, ctx:KipuParser.PasoOpcionalContext):
        pass


    # Enter a parse tree produced by KipuParser#regla.
    def enterRegla(self, ctx:KipuParser.ReglaContext):
        pass

    # Exit a parse tree produced by KipuParser#regla.
    def exitRegla(self, ctx:KipuParser.ReglaContext):
        pass


    # Enter a parse tree produced by KipuParser#parametros.
    def enterParametros(self, ctx:KipuParser.ParametrosContext):
        pass

    # Exit a parse tree produced by KipuParser#parametros.
    def exitParametros(self, ctx:KipuParser.ParametrosContext):
        pass


    # Enter a parse tree produced by KipuParser#parametrosCola.
    def enterParametrosCola(self, ctx:KipuParser.ParametrosColaContext):
        pass

    # Exit a parse tree produced by KipuParser#parametrosCola.
    def exitParametrosCola(self, ctx:KipuParser.ParametrosColaContext):
        pass


    # Enter a parse tree produced by KipuParser#parametro.
    def enterParametro(self, ctx:KipuParser.ParametroContext):
        pass

    # Exit a parse tree produced by KipuParser#parametro.
    def exitParametro(self, ctx:KipuParser.ParametroContext):
        pass


    # Enter a parse tree produced by KipuParser#tipoRetorno.
    def enterTipoRetorno(self, ctx:KipuParser.TipoRetornoContext):
        pass

    # Exit a parse tree produced by KipuParser#tipoRetorno.
    def exitTipoRetorno(self, ctx:KipuParser.TipoRetornoContext):
        pass


    # Enter a parse tree produced by KipuParser#retorno.
    def enterRetorno(self, ctx:KipuParser.RetornoContext):
        pass

    # Exit a parse tree produced by KipuParser#retorno.
    def exitRetorno(self, ctx:KipuParser.RetornoContext):
        pass


    # Enter a parse tree produced by KipuParser#valorRetorno.
    def enterValorRetorno(self, ctx:KipuParser.ValorRetornoContext):
        pass

    # Exit a parse tree produced by KipuParser#valorRetorno.
    def exitValorRetorno(self, ctx:KipuParser.ValorRetornoContext):
        pass


    # Enter a parse tree produced by KipuParser#llamadaSentencia.
    def enterLlamadaSentencia(self, ctx:KipuParser.LlamadaSentenciaContext):
        pass

    # Exit a parse tree produced by KipuParser#llamadaSentencia.
    def exitLlamadaSentencia(self, ctx:KipuParser.LlamadaSentenciaContext):
        pass


    # Enter a parse tree produced by KipuParser#entradaSalida.
    def enterEntradaSalida(self, ctx:KipuParser.EntradaSalidaContext):
        pass

    # Exit a parse tree produced by KipuParser#entradaSalida.
    def exitEntradaSalida(self, ctx:KipuParser.EntradaSalidaContext):
        pass



del KipuParser