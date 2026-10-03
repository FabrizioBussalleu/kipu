# Generated from grammar/Kipu.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KipuParser import KipuParser
else:
    from KipuParser import KipuParser

# This class defines a complete generic visitor for a parse tree produced by KipuParser.

class KipuVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KipuParser#programa.
    def visitPrograma(self, ctx:KipuParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#sentencia.
    def visitSentencia(self, ctx:KipuParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#bloque.
    def visitBloque(self, ctx:KipuParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#declaracionVariable.
    def visitDeclaracionVariable(self, ctx:KipuParser.DeclaracionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#declaracionConstante.
    def visitDeclaracionConstante(self, ctx:KipuParser.DeclaracionConstanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipoEntero.
    def visitTipoEntero(self, ctx:KipuParser.TipoEnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipoDecimal.
    def visitTipoDecimal(self, ctx:KipuParser.TipoDecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipoPorcentaje.
    def visitTipoPorcentaje(self, ctx:KipuParser.TipoPorcentajeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipoBooleano.
    def visitTipoBooleano(self, ctx:KipuParser.TipoBooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipoTexto.
    def visitTipoTexto(self, ctx:KipuParser.TipoTextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipoMonto.
    def visitTipoMonto(self, ctx:KipuParser.TipoMontoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#asignacion.
    def visitAsignacion(self, ctx:KipuParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprY.
    def visitExprY(self, ctx:KipuParser.ExprYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprAditiva.
    def visitExprAditiva(self, ctx:KipuParser.ExprAditivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprRelacional.
    def visitExprRelacional(self, ctx:KipuParser.ExprRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprParentesis.
    def visitExprParentesis(self, ctx:KipuParser.ExprParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprLiteral.
    def visitExprLiteral(self, ctx:KipuParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprLlamada.
    def visitExprLlamada(self, ctx:KipuParser.ExprLlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprNegativo.
    def visitExprNegativo(self, ctx:KipuParser.ExprNegativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprVariable.
    def visitExprVariable(self, ctx:KipuParser.ExprVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprIgualdad.
    def visitExprIgualdad(self, ctx:KipuParser.ExprIgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprConversion.
    def visitExprConversion(self, ctx:KipuParser.ExprConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprO.
    def visitExprO(self, ctx:KipuParser.ExprOContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprMultiplicativa.
    def visitExprMultiplicativa(self, ctx:KipuParser.ExprMultiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#exprNo.
    def visitExprNo(self, ctx:KipuParser.ExprNoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#litMonto.
    def visitLitMonto(self, ctx:KipuParser.LitMontoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#litEntero.
    def visitLitEntero(self, ctx:KipuParser.LitEnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#litDecimal.
    def visitLitDecimal(self, ctx:KipuParser.LitDecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#litPorcentaje.
    def visitLitPorcentaje(self, ctx:KipuParser.LitPorcentajeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#litTexto.
    def visitLitTexto(self, ctx:KipuParser.LitTextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#litBooleano.
    def visitLitBooleano(self, ctx:KipuParser.LitBooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#numero.
    def visitNumero(self, ctx:KipuParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#seleccion.
    def visitSeleccion(self, ctx:KipuParser.SeleccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#iterMientras.
    def visitIterMientras(self, ctx:KipuParser.IterMientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#iterPara.
    def visitIterPara(self, ctx:KipuParser.IterParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#regla.
    def visitRegla(self, ctx:KipuParser.ReglaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#parametros.
    def visitParametros(self, ctx:KipuParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#parametro.
    def visitParametro(self, ctx:KipuParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#retorno.
    def visitRetorno(self, ctx:KipuParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#llamada.
    def visitLlamada(self, ctx:KipuParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#argumentos.
    def visitArgumentos(self, ctx:KipuParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#llamadaSentencia.
    def visitLlamadaSentencia(self, ctx:KipuParser.LlamadaSentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#salida.
    def visitSalida(self, ctx:KipuParser.SalidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#entrada.
    def visitEntrada(self, ctx:KipuParser.EntradaContext):
        return self.visitChildren(ctx)



del KipuParser