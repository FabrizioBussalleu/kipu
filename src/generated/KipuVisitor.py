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


    # Visit a parse tree produced by KipuParser#listaSentencias.
    def visitListaSentencias(self, ctx:KipuParser.ListaSentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#sentencia.
    def visitSentencia(self, ctx:KipuParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#bloque.
    def visitBloque(self, ctx:KipuParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#declaracion.
    def visitDeclaracion(self, ctx:KipuParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#inicializacion.
    def visitInicializacion(self, ctx:KipuParser.InicializacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipo.
    def visitTipo(self, ctx:KipuParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#asignacion.
    def visitAsignacion(self, ctx:KipuParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#opAsignacion.
    def visitOpAsignacion(self, ctx:KipuParser.OpAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#expresion.
    def visitExpresion(self, ctx:KipuParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#conjuncion.
    def visitConjuncion(self, ctx:KipuParser.ConjuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#negacion.
    def visitNegacion(self, ctx:KipuParser.NegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#igualdad.
    def visitIgualdad(self, ctx:KipuParser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#relacional.
    def visitRelacional(self, ctx:KipuParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#aritmetica.
    def visitAritmetica(self, ctx:KipuParser.AritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#termino.
    def visitTermino(self, ctx:KipuParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#unario.
    def visitUnario(self, ctx:KipuParser.UnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#primario.
    def visitPrimario(self, ctx:KipuParser.PrimarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#literal.
    def visitLiteral(self, ctx:KipuParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#numero.
    def visitNumero(self, ctx:KipuParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#llamada.
    def visitLlamada(self, ctx:KipuParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#argumentos.
    def visitArgumentos(self, ctx:KipuParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#argumentosCola.
    def visitArgumentosCola(self, ctx:KipuParser.ArgumentosColaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#seleccion.
    def visitSeleccion(self, ctx:KipuParser.SeleccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#parteSino.
    def visitParteSino(self, ctx:KipuParser.ParteSinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#colaSino.
    def visitColaSino(self, ctx:KipuParser.ColaSinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#iteracion.
    def visitIteracion(self, ctx:KipuParser.IteracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#pasoOpcional.
    def visitPasoOpcional(self, ctx:KipuParser.PasoOpcionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#regla.
    def visitRegla(self, ctx:KipuParser.ReglaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#parametros.
    def visitParametros(self, ctx:KipuParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#parametrosCola.
    def visitParametrosCola(self, ctx:KipuParser.ParametrosColaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#parametro.
    def visitParametro(self, ctx:KipuParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#tipoRetorno.
    def visitTipoRetorno(self, ctx:KipuParser.TipoRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#retorno.
    def visitRetorno(self, ctx:KipuParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#valorRetorno.
    def visitValorRetorno(self, ctx:KipuParser.ValorRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#llamadaSentencia.
    def visitLlamadaSentencia(self, ctx:KipuParser.LlamadaSentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KipuParser#entradaSalida.
    def visitEntradaSalida(self, ctx:KipuParser.EntradaSalidaContext):
        return self.visitChildren(ctx)



del KipuParser