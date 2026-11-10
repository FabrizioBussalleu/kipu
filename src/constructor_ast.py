"""Construye el AST de Kipu a partir del árbol de análisis generado por ANTLR.

La gramática está en forma estándar (listas con recursión y alternativa vacía, precedencia
por niveles), así que este módulo "aplana" las listas recursivas y convierte los niveles de
precedencia en nodos binarios.
"""
from __future__ import annotations

from decimal import Decimal

from antlr4.tree.Tree import TerminalNode

import ast_kipu as A
from generated.KipuLexer import KipuLexer as L
from generated.KipuParser import KipuParser as P
from generated.KipuVisitor import KipuVisitor

OPERADORES = {
    L.O: "o", L.Y: "y", L.IGUAL: "==", L.DIFERENTE: "!=", L.MENOR: "<", L.MENOR_IGUAL: "<=",
    L.MAYOR: ">", L.MAYOR_IGUAL: ">=", L.SUMA: "+", L.RESTA: "-", L.MULT: "*", L.DIV: "/",
    L.MOD: "mod", L.ASIG: "=", L.MAS_ASIG: "+=", L.MENOS_ASIG: "-=",
}


def _pos(nodo) -> dict:
    tok = nodo.getSymbol() if isinstance(nodo, TerminalNode) else nodo.start
    return {"linea": tok.line, "columna": tok.column + 1}


def _terminal(ctx, i: int) -> int:
    hijo = ctx.getChild(i)
    return hijo.getSymbol().type if isinstance(hijo, TerminalNode) else -1


def _texto_cadena(lexema: str) -> str:
    cuerpo = lexema[1:-1]
    salida, i = [], 0
    escapes = {"n": "\n", "t": "\t", '"': '"', "\\": "\\"}
    while i < len(cuerpo):
        if cuerpo[i] == "\\" and i + 1 < len(cuerpo):
            salida.append(escapes.get(cuerpo[i + 1], cuerpo[i + 1]))
            i += 2
        else:
            salida.append(cuerpo[i])
            i += 1
    return "".join(salida)


class ConstructorAST(KipuVisitor):
    # --- estructura general ---------------------------------------------------
    def visitPrograma(self, ctx: P.ProgramaContext):
        return A.Programa(self._lista_sentencias(ctx.listaSentencias()), linea=1, columna=1)

    def _lista_sentencias(self, ctx) -> list:
        salida = []
        while ctx is not None and ctx.sentencia() is not None:
            salida.append(self.visit(ctx.sentencia()))
            ctx = ctx.listaSentencias()
        return salida

    def visitSentencia(self, ctx: P.SentenciaContext):
        return self.visit(ctx.getChild(0))

    def visitBloque(self, ctx: P.BloqueContext):
        return A.Bloque(self._lista_sentencias(ctx.listaSentencias()), **_pos(ctx))

    # --- G1 declaraciones ----------------------------------------------------------
    def visitDeclaracion(self, ctx: P.DeclaracionContext):
        constante = ctx.CONST() is not None
        if constante:
            valor = self.visit(ctx.expresion())
        else:
            ini = ctx.inicializacion()
            valor = self.visit(ini.expresion()) if ini.expresion() is not None else None
        return A.Declaracion(constante, ctx.ID().getText(), self.visit(ctx.tipo()), valor, **_pos(ctx.ID()))

    def visitTipo(self, ctx: P.TipoContext):
        if ctx.MONTO() is not None:
            return A.monto(ctx.MONEDA().getText())
        return A.Tipo(ctx.getText())

    # --- G2 asignación ----------------------------------------------------------------
    def visitAsignacion(self, ctx: P.AsignacionContext):
        op = OPERADORES[ctx.opAsignacion().getChild(0).getSymbol().type]
        return A.Asignacion(ctx.ID().getText(), op, self.visit(ctx.expresion()), **_pos(ctx.ID()))

    # --- G3 expresiones (niveles de precedencia) ---------------------------------------
    def _binaria_o_paso(self, ctx):
        """Niveles 'a : a OP b | b': con 3 hijos crea un nodo binario; con 1 hijo lo delega."""
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        izq = self.visit(ctx.getChild(0))
        der = self.visit(ctx.getChild(2))
        op = OPERADORES[_terminal(ctx, 1)]
        return A.Binaria(op, izq, der, linea=izq.linea, columna=izq.columna)

    visitExpresion = _binaria_o_paso
    visitConjuncion = _binaria_o_paso
    visitIgualdad = _binaria_o_paso
    visitRelacional = _binaria_o_paso
    visitAritmetica = _binaria_o_paso
    visitTermino = _binaria_o_paso

    def visitNegacion(self, ctx: P.NegacionContext):
        if ctx.NO() is not None:
            return A.Unaria("no", self.visit(ctx.negacion()), **_pos(ctx))
        return self.visit(ctx.igualdad())

    def visitUnario(self, ctx: P.UnarioContext):
        if ctx.RESTA() is not None:
            return A.Unaria("-", self.visit(ctx.unario()), **_pos(ctx))
        return self.visit(ctx.primario())

    def visitPrimario(self, ctx: P.PrimarioContext):
        if ctx.CONVERTIR() is not None:
            return A.Conversion(self.visit(ctx.expresion(0)), ctx.MONEDA().getText(),
                                self.visit(ctx.expresion(1)), **_pos(ctx))
        if ctx.PAR_IZQ() is not None:
            return self.visit(ctx.expresion(0))
        if ctx.llamada() is not None:
            return self.visit(ctx.llamada())
        if ctx.literal() is not None:
            return self.visit(ctx.literal())
        return A.Variable(ctx.ID().getText(), **_pos(ctx))

    def visitLiteral(self, ctx: P.LiteralContext):
        pos = _pos(ctx)
        if ctx.numero() is not None:
            return A.Literal("monto", Decimal(ctx.numero().getText()), ctx.MONEDA().getText(), **pos)
        tok = ctx.getChild(0).getSymbol()
        texto = tok.text
        if tok.type == L.NUM_ENTERO:
            return A.Literal("entero", int(texto), **pos)
        if tok.type == L.NUM_DECIMAL:
            return A.Literal("decimal", Decimal(texto), **pos)
        if tok.type == L.LIT_PORCENTAJE:
            return A.Literal("porcentaje", Decimal(texto[:-1]), **pos)
        if tok.type == L.CADENA:
            return A.Literal("texto", _texto_cadena(texto), **pos)
        return A.Literal("booleano", tok.type == L.VERDADERO, **pos)

    def visitLlamada(self, ctx: P.LlamadaContext):
        args = []
        a = ctx.argumentos()
        if a.expresion() is not None:
            args.append(self.visit(a.expresion()))
            args.extend(self._cola_argumentos(a.argumentosCola()))
        return A.Llamada(ctx.ID().getText(), args, **_pos(ctx.ID()))

    def _cola_argumentos(self, ctx) -> list:
        salida = []
        while ctx is not None and ctx.expresion() is not None:
            salida.append(self.visit(ctx.expresion()))
            ctx = ctx.argumentosCola()
        return salida

    # --- G4 selectivas ----------------------------------------------------------------
    def visitSeleccion(self, ctx: P.SeleccionContext):
        ramas = [(self.visit(ctx.expresion()), self.visit(ctx.bloque()))]
        sino = None
        parte = ctx.parteSino()
        while parte is not None and parte.SINO() is not None:
            cola = parte.colaSino()
            if cola.seleccion() is not None:
                sel = cola.seleccion()
                ramas.append((self.visit(sel.expresion()), self.visit(sel.bloque())))
                parte = sel.parteSino()
            else:
                sino = self.visit(cola.bloque())
                parte = None
        return A.Si(ramas, sino, **_pos(ctx))

    # --- G5 iterativas --------------------------------------------------------------------
    def visitIteracion(self, ctx: P.IteracionContext):
        if ctx.MIENTRAS() is not None:
            return A.Mientras(self.visit(ctx.expresion(0)), self.visit(ctx.bloque()), **_pos(ctx))
        paso_ctx = ctx.pasoOpcional()
        paso = self.visit(paso_ctx.expresion()) if paso_ctx.expresion() is not None else None
        return A.Para(ctx.ID().getText(), self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)),
                      paso, self.visit(ctx.bloque()), **_pos(ctx))

    # --- G6 reglas -----------------------------------------------------------------------
    def visitRegla(self, ctx: P.ReglaContext):
        params = []
        p = ctx.parametros()
        if p.parametro() is not None:
            params.append(self._parametro(p.parametro()))
            cola = p.parametrosCola()
            while cola is not None and cola.parametro() is not None:
                params.append(self._parametro(cola.parametro()))
                cola = cola.parametrosCola()
        tr = ctx.tipoRetorno()
        tipo_ret = self.visit(tr.tipo()) if tr.tipo() is not None else None
        return A.Regla(ctx.ID().getText(), params, tipo_ret, self.visit(ctx.bloque()), **_pos(ctx.ID()))

    def _parametro(self, ctx: P.ParametroContext) -> A.Parametro:
        return A.Parametro(ctx.ID().getText(), self.visit(ctx.tipo()), **_pos(ctx.ID()))

    def visitRetorno(self, ctx: P.RetornoContext):
        v = ctx.valorRetorno()
        return A.Retornar(self.visit(v.expresion()) if v.expresion() is not None else None, **_pos(ctx))

    def visitLlamadaSentencia(self, ctx: P.LlamadaSentenciaContext):
        llamada = self.visit(ctx.llamada())
        return A.LlamadaSentencia(llamada, linea=llamada.linea, columna=llamada.columna)

    # --- G7 entrada y salida ----------------------------------------------------------------
    def visitEntradaSalida(self, ctx: P.EntradaSalidaContext):
        if ctx.MOSTRAR() is not None:
            args = [self.visit(ctx.expresion())] + self._cola_argumentos(ctx.argumentosCola())
            return A.Mostrar(args, **_pos(ctx))
        return A.Leer(ctx.ID().getText(), **_pos(ctx.ID()))
