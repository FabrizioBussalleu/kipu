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


    # Enter a parse tree produced by KipuParser#declaracionVariable.
    def enterDeclaracionVariable(self, ctx:KipuParser.DeclaracionVariableContext):
        pass

    # Exit a parse tree produced by KipuParser#declaracionVariable.
    def exitDeclaracionVariable(self, ctx:KipuParser.DeclaracionVariableContext):
        pass


    # Enter a parse tree produced by KipuParser#declaracionConstante.
    def enterDeclaracionConstante(self, ctx:KipuParser.DeclaracionConstanteContext):
        pass

    # Exit a parse tree produced by KipuParser#declaracionConstante.
    def exitDeclaracionConstante(self, ctx:KipuParser.DeclaracionConstanteContext):
        pass


    # Enter a parse tree produced by KipuParser#tipoEntero.
    def enterTipoEntero(self, ctx:KipuParser.TipoEnteroContext):
        pass

    # Exit a parse tree produced by KipuParser#tipoEntero.
    def exitTipoEntero(self, ctx:KipuParser.TipoEnteroContext):
        pass


    # Enter a parse tree produced by KipuParser#tipoDecimal.
    def enterTipoDecimal(self, ctx:KipuParser.TipoDecimalContext):
        pass

    # Exit a parse tree produced by KipuParser#tipoDecimal.
    def exitTipoDecimal(self, ctx:KipuParser.TipoDecimalContext):
        pass


    # Enter a parse tree produced by KipuParser#tipoPorcentaje.
    def enterTipoPorcentaje(self, ctx:KipuParser.TipoPorcentajeContext):
        pass

    # Exit a parse tree produced by KipuParser#tipoPorcentaje.
    def exitTipoPorcentaje(self, ctx:KipuParser.TipoPorcentajeContext):
        pass


    # Enter a parse tree produced by KipuParser#tipoBooleano.
    def enterTipoBooleano(self, ctx:KipuParser.TipoBooleanoContext):
        pass

    # Exit a parse tree produced by KipuParser#tipoBooleano.
    def exitTipoBooleano(self, ctx:KipuParser.TipoBooleanoContext):
        pass


    # Enter a parse tree produced by KipuParser#tipoTexto.
    def enterTipoTexto(self, ctx:KipuParser.TipoTextoContext):
        pass

    # Exit a parse tree produced by KipuParser#tipoTexto.
    def exitTipoTexto(self, ctx:KipuParser.TipoTextoContext):
        pass


    # Enter a parse tree produced by KipuParser#tipoMonto.
    def enterTipoMonto(self, ctx:KipuParser.TipoMontoContext):
        pass

    # Exit a parse tree produced by KipuParser#tipoMonto.
    def exitTipoMonto(self, ctx:KipuParser.TipoMontoContext):
        pass


    # Enter a parse tree produced by KipuParser#asignacion.
    def enterAsignacion(self, ctx:KipuParser.AsignacionContext):
        pass

    # Exit a parse tree produced by KipuParser#asignacion.
    def exitAsignacion(self, ctx:KipuParser.AsignacionContext):
        pass


    # Enter a parse tree produced by KipuParser#exprY.
    def enterExprY(self, ctx:KipuParser.ExprYContext):
        pass

    # Exit a parse tree produced by KipuParser#exprY.
    def exitExprY(self, ctx:KipuParser.ExprYContext):
        pass


    # Enter a parse tree produced by KipuParser#exprAditiva.
    def enterExprAditiva(self, ctx:KipuParser.ExprAditivaContext):
        pass

    # Exit a parse tree produced by KipuParser#exprAditiva.
    def exitExprAditiva(self, ctx:KipuParser.ExprAditivaContext):
        pass


    # Enter a parse tree produced by KipuParser#exprRelacional.
    def enterExprRelacional(self, ctx:KipuParser.ExprRelacionalContext):
        pass

    # Exit a parse tree produced by KipuParser#exprRelacional.
    def exitExprRelacional(self, ctx:KipuParser.ExprRelacionalContext):
        pass


    # Enter a parse tree produced by KipuParser#exprParentesis.
    def enterExprParentesis(self, ctx:KipuParser.ExprParentesisContext):
        pass

    # Exit a parse tree produced by KipuParser#exprParentesis.
    def exitExprParentesis(self, ctx:KipuParser.ExprParentesisContext):
        pass


    # Enter a parse tree produced by KipuParser#exprLiteral.
    def enterExprLiteral(self, ctx:KipuParser.ExprLiteralContext):
        pass

    # Exit a parse tree produced by KipuParser#exprLiteral.
    def exitExprLiteral(self, ctx:KipuParser.ExprLiteralContext):
        pass


    # Enter a parse tree produced by KipuParser#exprLlamada.
    def enterExprLlamada(self, ctx:KipuParser.ExprLlamadaContext):
        pass

    # Exit a parse tree produced by KipuParser#exprLlamada.
    def exitExprLlamada(self, ctx:KipuParser.ExprLlamadaContext):
        pass


    # Enter a parse tree produced by KipuParser#exprNegativo.
    def enterExprNegativo(self, ctx:KipuParser.ExprNegativoContext):
        pass

    # Exit a parse tree produced by KipuParser#exprNegativo.
    def exitExprNegativo(self, ctx:KipuParser.ExprNegativoContext):
        pass


    # Enter a parse tree produced by KipuParser#exprVariable.
    def enterExprVariable(self, ctx:KipuParser.ExprVariableContext):
        pass

    # Exit a parse tree produced by KipuParser#exprVariable.
    def exitExprVariable(self, ctx:KipuParser.ExprVariableContext):
        pass


    # Enter a parse tree produced by KipuParser#exprIgualdad.
    def enterExprIgualdad(self, ctx:KipuParser.ExprIgualdadContext):
        pass

    # Exit a parse tree produced by KipuParser#exprIgualdad.
    def exitExprIgualdad(self, ctx:KipuParser.ExprIgualdadContext):
        pass


    # Enter a parse tree produced by KipuParser#exprConversion.
    def enterExprConversion(self, ctx:KipuParser.ExprConversionContext):
        pass

    # Exit a parse tree produced by KipuParser#exprConversion.
    def exitExprConversion(self, ctx:KipuParser.ExprConversionContext):
        pass


    # Enter a parse tree produced by KipuParser#exprO.
    def enterExprO(self, ctx:KipuParser.ExprOContext):
        pass

    # Exit a parse tree produced by KipuParser#exprO.
    def exitExprO(self, ctx:KipuParser.ExprOContext):
        pass


    # Enter a parse tree produced by KipuParser#exprMultiplicativa.
    def enterExprMultiplicativa(self, ctx:KipuParser.ExprMultiplicativaContext):
        pass

    # Exit a parse tree produced by KipuParser#exprMultiplicativa.
    def exitExprMultiplicativa(self, ctx:KipuParser.ExprMultiplicativaContext):
        pass


    # Enter a parse tree produced by KipuParser#exprNo.
    def enterExprNo(self, ctx:KipuParser.ExprNoContext):
        pass

    # Exit a parse tree produced by KipuParser#exprNo.
    def exitExprNo(self, ctx:KipuParser.ExprNoContext):
        pass


    # Enter a parse tree produced by KipuParser#litMonto.
    def enterLitMonto(self, ctx:KipuParser.LitMontoContext):
        pass

    # Exit a parse tree produced by KipuParser#litMonto.
    def exitLitMonto(self, ctx:KipuParser.LitMontoContext):
        pass


    # Enter a parse tree produced by KipuParser#litEntero.
    def enterLitEntero(self, ctx:KipuParser.LitEnteroContext):
        pass

    # Exit a parse tree produced by KipuParser#litEntero.
    def exitLitEntero(self, ctx:KipuParser.LitEnteroContext):
        pass


    # Enter a parse tree produced by KipuParser#litDecimal.
    def enterLitDecimal(self, ctx:KipuParser.LitDecimalContext):
        pass

    # Exit a parse tree produced by KipuParser#litDecimal.
    def exitLitDecimal(self, ctx:KipuParser.LitDecimalContext):
        pass


    # Enter a parse tree produced by KipuParser#litPorcentaje.
    def enterLitPorcentaje(self, ctx:KipuParser.LitPorcentajeContext):
        pass

    # Exit a parse tree produced by KipuParser#litPorcentaje.
    def exitLitPorcentaje(self, ctx:KipuParser.LitPorcentajeContext):
        pass


    # Enter a parse tree produced by KipuParser#litTexto.
    def enterLitTexto(self, ctx:KipuParser.LitTextoContext):
        pass

    # Exit a parse tree produced by KipuParser#litTexto.
    def exitLitTexto(self, ctx:KipuParser.LitTextoContext):
        pass


    # Enter a parse tree produced by KipuParser#litBooleano.
    def enterLitBooleano(self, ctx:KipuParser.LitBooleanoContext):
        pass

    # Exit a parse tree produced by KipuParser#litBooleano.
    def exitLitBooleano(self, ctx:KipuParser.LitBooleanoContext):
        pass


    # Enter a parse tree produced by KipuParser#numero.
    def enterNumero(self, ctx:KipuParser.NumeroContext):
        pass

    # Exit a parse tree produced by KipuParser#numero.
    def exitNumero(self, ctx:KipuParser.NumeroContext):
        pass


    # Enter a parse tree produced by KipuParser#seleccion.
    def enterSeleccion(self, ctx:KipuParser.SeleccionContext):
        pass

    # Exit a parse tree produced by KipuParser#seleccion.
    def exitSeleccion(self, ctx:KipuParser.SeleccionContext):
        pass


    # Enter a parse tree produced by KipuParser#iterMientras.
    def enterIterMientras(self, ctx:KipuParser.IterMientrasContext):
        pass

    # Exit a parse tree produced by KipuParser#iterMientras.
    def exitIterMientras(self, ctx:KipuParser.IterMientrasContext):
        pass


    # Enter a parse tree produced by KipuParser#iterPara.
    def enterIterPara(self, ctx:KipuParser.IterParaContext):
        pass

    # Exit a parse tree produced by KipuParser#iterPara.
    def exitIterPara(self, ctx:KipuParser.IterParaContext):
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


    # Enter a parse tree produced by KipuParser#parametro.
    def enterParametro(self, ctx:KipuParser.ParametroContext):
        pass

    # Exit a parse tree produced by KipuParser#parametro.
    def exitParametro(self, ctx:KipuParser.ParametroContext):
        pass


    # Enter a parse tree produced by KipuParser#retorno.
    def enterRetorno(self, ctx:KipuParser.RetornoContext):
        pass

    # Exit a parse tree produced by KipuParser#retorno.
    def exitRetorno(self, ctx:KipuParser.RetornoContext):
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


    # Enter a parse tree produced by KipuParser#llamadaSentencia.
    def enterLlamadaSentencia(self, ctx:KipuParser.LlamadaSentenciaContext):
        pass

    # Exit a parse tree produced by KipuParser#llamadaSentencia.
    def exitLlamadaSentencia(self, ctx:KipuParser.LlamadaSentenciaContext):
        pass


    # Enter a parse tree produced by KipuParser#salida.
    def enterSalida(self, ctx:KipuParser.SalidaContext):
        pass

    # Exit a parse tree produced by KipuParser#salida.
    def exitSalida(self, ctx:KipuParser.SalidaContext):
        pass


    # Enter a parse tree produced by KipuParser#entrada.
    def enterEntrada(self, ctx:KipuParser.EntradaContext):
        pass

    # Exit a parse tree produced by KipuParser#entrada.
    def exitEntrada(self, ctx:KipuParser.EntradaContext):
        pass



del KipuParser