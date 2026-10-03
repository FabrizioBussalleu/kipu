# Generated from grammar/Kipu.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,55,264,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        56,8,1,1,2,1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,73,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        85,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,96,8,4,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,124,8,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,144,8,6,10,
        6,12,6,147,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,157,8,7,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,173,8,9,10,
        9,12,9,176,9,9,1,9,1,9,3,9,180,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,196,8,10,1,10,1,10,
        3,10,200,8,10,1,11,1,11,1,11,1,11,3,11,206,8,11,1,11,1,11,1,11,3,
        11,211,8,11,1,11,1,11,1,12,1,12,1,12,5,12,218,8,12,10,12,12,12,221,
        9,12,1,13,1,13,1,13,1,13,1,14,1,14,3,14,229,8,14,1,14,1,14,1,15,
        1,15,1,15,3,15,236,8,15,1,15,1,15,1,16,1,16,1,16,5,16,243,8,16,10,
        16,12,16,246,9,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,3,18,262,8,18,1,18,0,1,12,19,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,0,7,2,0,28,29,36,36,2,0,27,
        27,39,40,1,0,37,38,1,0,32,35,1,0,30,31,1,0,25,26,1,0,49,50,289,0,
        41,1,0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,84,1,0,0,0,8,95,1,0,0,0,10,
        97,1,0,0,0,12,123,1,0,0,0,14,156,1,0,0,0,16,158,1,0,0,0,18,160,1,
        0,0,0,20,199,1,0,0,0,22,201,1,0,0,0,24,214,1,0,0,0,26,222,1,0,0,
        0,28,226,1,0,0,0,30,232,1,0,0,0,32,239,1,0,0,0,34,247,1,0,0,0,36,
        261,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,
        0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,
        1,0,0,0,46,56,3,6,3,0,47,56,3,10,5,0,48,56,3,18,9,0,49,56,3,20,10,
        0,50,56,3,22,11,0,51,56,3,28,14,0,52,56,3,36,18,0,53,56,3,34,17,
        0,54,56,3,4,2,0,55,46,1,0,0,0,55,47,1,0,0,0,55,48,1,0,0,0,55,49,
        1,0,0,0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,
        55,54,1,0,0,0,56,3,1,0,0,0,57,61,5,43,0,0,58,60,3,2,1,0,59,58,1,
        0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,
        61,1,0,0,0,64,65,5,44,0,0,65,5,1,0,0,0,66,67,5,1,0,0,67,68,5,52,
        0,0,68,69,5,47,0,0,69,72,3,8,4,0,70,71,5,36,0,0,71,73,3,12,6,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,45,0,0,75,85,1,0,
        0,0,76,77,5,2,0,0,77,78,5,52,0,0,78,79,5,47,0,0,79,80,3,8,4,0,80,
        81,5,36,0,0,81,82,3,12,6,0,82,83,5,45,0,0,83,85,1,0,0,0,84,66,1,
        0,0,0,84,76,1,0,0,0,85,7,1,0,0,0,86,96,5,3,0,0,87,96,5,4,0,0,88,
        96,5,5,0,0,89,96,5,6,0,0,90,96,5,7,0,0,91,92,5,8,0,0,92,93,5,34,
        0,0,93,94,5,9,0,0,94,96,5,35,0,0,95,86,1,0,0,0,95,87,1,0,0,0,95,
        88,1,0,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,0,96,9,1,0,0,
        0,97,98,5,52,0,0,98,99,7,0,0,0,99,100,3,12,6,0,100,101,5,45,0,0,
        101,11,1,0,0,0,102,103,6,6,-1,0,103,104,5,41,0,0,104,105,3,12,6,
        0,105,106,5,42,0,0,106,124,1,0,0,0,107,108,5,21,0,0,108,109,5,41,
        0,0,109,110,3,12,6,0,110,111,5,46,0,0,111,112,5,9,0,0,112,113,5,
        46,0,0,113,114,3,12,6,0,114,115,5,42,0,0,115,124,1,0,0,0,116,124,
        3,30,15,0,117,118,5,38,0,0,118,124,3,12,6,10,119,120,5,24,0,0,120,
        124,3,12,6,5,121,124,3,14,7,0,122,124,5,52,0,0,123,102,1,0,0,0,123,
        107,1,0,0,0,123,116,1,0,0,0,123,117,1,0,0,0,123,119,1,0,0,0,123,
        121,1,0,0,0,123,122,1,0,0,0,124,145,1,0,0,0,125,126,10,9,0,0,126,
        127,7,1,0,0,127,144,3,12,6,10,128,129,10,8,0,0,129,130,7,2,0,0,130,
        144,3,12,6,9,131,132,10,7,0,0,132,133,7,3,0,0,133,144,3,12,6,8,134,
        135,10,6,0,0,135,136,7,4,0,0,136,144,3,12,6,7,137,138,10,4,0,0,138,
        139,5,22,0,0,139,144,3,12,6,5,140,141,10,3,0,0,141,142,5,23,0,0,
        142,144,3,12,6,4,143,125,1,0,0,0,143,128,1,0,0,0,143,131,1,0,0,0,
        143,134,1,0,0,0,143,137,1,0,0,0,143,140,1,0,0,0,144,147,1,0,0,0,
        145,143,1,0,0,0,145,146,1,0,0,0,146,13,1,0,0,0,147,145,1,0,0,0,148,
        149,3,16,8,0,149,150,5,9,0,0,150,157,1,0,0,0,151,157,5,50,0,0,152,
        157,5,49,0,0,153,157,5,48,0,0,154,157,5,51,0,0,155,157,7,5,0,0,156,
        148,1,0,0,0,156,151,1,0,0,0,156,152,1,0,0,0,156,153,1,0,0,0,156,
        154,1,0,0,0,156,155,1,0,0,0,157,15,1,0,0,0,158,159,7,6,0,0,159,17,
        1,0,0,0,160,161,5,10,0,0,161,162,5,41,0,0,162,163,3,12,6,0,163,164,
        5,42,0,0,164,174,3,4,2,0,165,166,5,11,0,0,166,167,5,10,0,0,167,168,
        5,41,0,0,168,169,3,12,6,0,169,170,5,42,0,0,170,171,3,4,2,0,171,173,
        1,0,0,0,172,165,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,
        1,0,0,0,175,179,1,0,0,0,176,174,1,0,0,0,177,178,5,11,0,0,178,180,
        3,4,2,0,179,177,1,0,0,0,179,180,1,0,0,0,180,19,1,0,0,0,181,182,5,
        12,0,0,182,183,5,41,0,0,183,184,3,12,6,0,184,185,5,42,0,0,185,186,
        3,4,2,0,186,200,1,0,0,0,187,188,5,13,0,0,188,189,5,52,0,0,189,190,
        5,14,0,0,190,191,3,12,6,0,191,192,5,15,0,0,192,195,3,12,6,0,193,
        194,5,16,0,0,194,196,3,12,6,0,195,193,1,0,0,0,195,196,1,0,0,0,196,
        197,1,0,0,0,197,198,3,4,2,0,198,200,1,0,0,0,199,181,1,0,0,0,199,
        187,1,0,0,0,200,21,1,0,0,0,201,202,5,17,0,0,202,203,5,52,0,0,203,
        205,5,41,0,0,204,206,3,24,12,0,205,204,1,0,0,0,205,206,1,0,0,0,206,
        207,1,0,0,0,207,210,5,42,0,0,208,209,5,47,0,0,209,211,3,8,4,0,210,
        208,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,213,3,4,2,0,213,
        23,1,0,0,0,214,219,3,26,13,0,215,216,5,46,0,0,216,218,3,26,13,0,
        217,215,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,
        220,25,1,0,0,0,221,219,1,0,0,0,222,223,5,52,0,0,223,224,5,47,0,0,
        224,225,3,8,4,0,225,27,1,0,0,0,226,228,5,18,0,0,227,229,3,12,6,0,
        228,227,1,0,0,0,228,229,1,0,0,0,229,230,1,0,0,0,230,231,5,45,0,0,
        231,29,1,0,0,0,232,233,5,52,0,0,233,235,5,41,0,0,234,236,3,32,16,
        0,235,234,1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,0,237,238,5,42,0,
        0,238,31,1,0,0,0,239,244,3,12,6,0,240,241,5,46,0,0,241,243,3,12,
        6,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,
        0,0,245,33,1,0,0,0,246,244,1,0,0,0,247,248,3,30,15,0,248,249,5,45,
        0,0,249,35,1,0,0,0,250,251,5,19,0,0,251,252,5,41,0,0,252,253,3,32,
        16,0,253,254,5,42,0,0,254,255,5,45,0,0,255,262,1,0,0,0,256,257,5,
        20,0,0,257,258,5,41,0,0,258,259,5,52,0,0,259,260,5,42,0,0,260,262,
        5,45,0,0,261,250,1,0,0,0,261,256,1,0,0,0,262,37,1,0,0,0,21,41,55,
        61,72,84,95,123,143,145,156,174,179,195,199,205,210,219,228,235,
        244,261
    ]

class KipuParser ( Parser ):

    grammarFileName = "Kipu.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'const'", "'entero'", "'decimal'", 
                     "'porcentaje'", "'booleano'", "'texto'", "'monto'", 
                     "<INVALID>", "'si'", "'sino'", "'mientras'", "'para'", 
                     "'desde'", "'hasta'", "'paso'", "'regla'", "'retornar'", 
                     "'mostrar'", "'leer'", "'convertir'", "'y'", "'o'", 
                     "'no'", "'verdadero'", "'falso'", "'mod'", "'+='", 
                     "'-='", "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'{'", 
                     "'}'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "VAR", "CONST", "ENTERO", "DECIMAL", 
                      "PORCENTAJE", "BOOLEANO", "TEXTO", "MONTO", "MONEDA", 
                      "SI", "SINO", "MIENTRAS", "PARA", "DESDE", "HASTA", 
                      "PASO", "REGLA", "RETORNAR", "MOSTRAR", "LEER", "CONVERTIR", 
                      "Y", "O", "NO", "VERDADERO", "FALSO", "MOD", "MAS_ASIG", 
                      "MENOS_ASIG", "IGUAL", "DIFERENTE", "MENOR_IGUAL", 
                      "MAYOR_IGUAL", "MENOR", "MAYOR", "ASIG", "SUMA", "RESTA", 
                      "MULT", "DIV", "PAR_IZQ", "PAR_DER", "LLAVE_IZQ", 
                      "LLAVE_DER", "PUNTO_COMA", "COMA", "DOS_PUNTOS", "LIT_PORCENTAJE", 
                      "NUM_DECIMAL", "NUM_ENTERO", "CADENA", "ID", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE", "ESPACIO" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_bloque = 2
    RULE_declaracion = 3
    RULE_tipo = 4
    RULE_asignacion = 5
    RULE_expresion = 6
    RULE_literal = 7
    RULE_numero = 8
    RULE_seleccion = 9
    RULE_iteracion = 10
    RULE_regla = 11
    RULE_parametros = 12
    RULE_parametro = 13
    RULE_retorno = 14
    RULE_llamada = 15
    RULE_argumentos = 16
    RULE_llamadaSentencia = 17
    RULE_entradaSalida = 18

    ruleNames =  [ "programa", "sentencia", "bloque", "declaracion", "tipo", 
                   "asignacion", "expresion", "literal", "numero", "seleccion", 
                   "iteracion", "regla", "parametros", "parametro", "retorno", 
                   "llamada", "argumentos", "llamadaSentencia", "entradaSalida" ]

    EOF = Token.EOF
    VAR=1
    CONST=2
    ENTERO=3
    DECIMAL=4
    PORCENTAJE=5
    BOOLEANO=6
    TEXTO=7
    MONTO=8
    MONEDA=9
    SI=10
    SINO=11
    MIENTRAS=12
    PARA=13
    DESDE=14
    HASTA=15
    PASO=16
    REGLA=17
    RETORNAR=18
    MOSTRAR=19
    LEER=20
    CONVERTIR=21
    Y=22
    O=23
    NO=24
    VERDADERO=25
    FALSO=26
    MOD=27
    MAS_ASIG=28
    MENOS_ASIG=29
    IGUAL=30
    DIFERENTE=31
    MENOR_IGUAL=32
    MAYOR_IGUAL=33
    MENOR=34
    MAYOR=35
    ASIG=36
    SUMA=37
    RESTA=38
    MULT=39
    DIV=40
    PAR_IZQ=41
    PAR_DER=42
    LLAVE_IZQ=43
    LLAVE_DER=44
    PUNTO_COMA=45
    COMA=46
    DOS_PUNTOS=47
    LIT_PORCENTAJE=48
    NUM_DECIMAL=49
    NUM_ENTERO=50
    CADENA=51
    ID=52
    COMENTARIO_LINEA=53
    COMENTARIO_BLOQUE=54
    ESPACIO=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KipuParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(KipuParser.SentenciaContext,i)


        def getRuleIndex(self):
            return KipuParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = KipuParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4512395722372102) != 0):
                self.state = 38
                self.sentencia()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(KipuParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(KipuParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(KipuParser.AsignacionContext,0)


        def seleccion(self):
            return self.getTypedRuleContext(KipuParser.SeleccionContext,0)


        def iteracion(self):
            return self.getTypedRuleContext(KipuParser.IteracionContext,0)


        def regla(self):
            return self.getTypedRuleContext(KipuParser.ReglaContext,0)


        def retorno(self):
            return self.getTypedRuleContext(KipuParser.RetornoContext,0)


        def entradaSalida(self):
            return self.getTypedRuleContext(KipuParser.EntradaSalidaContext,0)


        def llamadaSentencia(self):
            return self.getTypedRuleContext(KipuParser.LlamadaSentenciaContext,0)


        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = KipuParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.seleccion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.iteracion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.regla()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.retorno()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.entradaSalida()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.llamadaSentencia()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_IZQ(self):
            return self.getToken(KipuParser.LLAVE_IZQ, 0)

        def LLAVE_DER(self):
            return self.getToken(KipuParser.LLAVE_DER, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(KipuParser.SentenciaContext,i)


        def getRuleIndex(self):
            return KipuParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = KipuParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(KipuParser.LLAVE_IZQ)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4512395722372102) != 0):
                self.state = 58
                self.sentencia()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(KipuParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KipuParser.RULE_declaracion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaracionVariableContext(DeclaracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.DeclaracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(KipuParser.VAR, 0)
        def ID(self):
            return self.getToken(KipuParser.ID, 0)
        def DOS_PUNTOS(self):
            return self.getToken(KipuParser.DOS_PUNTOS, 0)
        def tipo(self):
            return self.getTypedRuleContext(KipuParser.TipoContext,0)

        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)
        def ASIG(self):
            return self.getToken(KipuParser.ASIG, 0)
        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionVariable" ):
                listener.enterDeclaracionVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionVariable" ):
                listener.exitDeclaracionVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionVariable" ):
                return visitor.visitDeclaracionVariable(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracionConstanteContext(DeclaracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.DeclaracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONST(self):
            return self.getToken(KipuParser.CONST, 0)
        def ID(self):
            return self.getToken(KipuParser.ID, 0)
        def DOS_PUNTOS(self):
            return self.getToken(KipuParser.DOS_PUNTOS, 0)
        def tipo(self):
            return self.getTypedRuleContext(KipuParser.TipoContext,0)

        def ASIG(self):
            return self.getToken(KipuParser.ASIG, 0)
        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)

        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionConstante" ):
                listener.enterDeclaracionConstante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionConstante" ):
                listener.exitDeclaracionConstante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionConstante" ):
                return visitor.visitDeclaracionConstante(self)
            else:
                return visitor.visitChildren(self)



    def declaracion(self):

        localctx = KipuParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = KipuParser.DeclaracionVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(KipuParser.VAR)
                self.state = 67
                self.match(KipuParser.ID)
                self.state = 68
                self.match(KipuParser.DOS_PUNTOS)
                self.state = 69
                self.tipo()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 70
                    self.match(KipuParser.ASIG)
                    self.state = 71
                    self.expresion(0)


                self.state = 74
                self.match(KipuParser.PUNTO_COMA)
                pass
            elif token in [2]:
                localctx = KipuParser.DeclaracionConstanteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(KipuParser.CONST)
                self.state = 77
                self.match(KipuParser.ID)
                self.state = 78
                self.match(KipuParser.DOS_PUNTOS)
                self.state = 79
                self.tipo()
                self.state = 80
                self.match(KipuParser.ASIG)
                self.state = 81
                self.expresion(0)
                self.state = 82
                self.match(KipuParser.PUNTO_COMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KipuParser.RULE_tipo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TipoMontoContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MONTO(self):
            return self.getToken(KipuParser.MONTO, 0)
        def MENOR(self):
            return self.getToken(KipuParser.MENOR, 0)
        def MONEDA(self):
            return self.getToken(KipuParser.MONEDA, 0)
        def MAYOR(self):
            return self.getToken(KipuParser.MAYOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoMonto" ):
                listener.enterTipoMonto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoMonto" ):
                listener.exitTipoMonto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoMonto" ):
                return visitor.visitTipoMonto(self)
            else:
                return visitor.visitChildren(self)


    class TipoDecimalContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(KipuParser.DECIMAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoDecimal" ):
                listener.enterTipoDecimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoDecimal" ):
                listener.exitTipoDecimal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoDecimal" ):
                return visitor.visitTipoDecimal(self)
            else:
                return visitor.visitChildren(self)


    class TipoEnteroContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ENTERO(self):
            return self.getToken(KipuParser.ENTERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoEntero" ):
                listener.enterTipoEntero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoEntero" ):
                listener.exitTipoEntero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoEntero" ):
                return visitor.visitTipoEntero(self)
            else:
                return visitor.visitChildren(self)


    class TipoBooleanoContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEANO(self):
            return self.getToken(KipuParser.BOOLEANO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoBooleano" ):
                listener.enterTipoBooleano(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoBooleano" ):
                listener.exitTipoBooleano(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoBooleano" ):
                return visitor.visitTipoBooleano(self)
            else:
                return visitor.visitChildren(self)


    class TipoPorcentajeContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PORCENTAJE(self):
            return self.getToken(KipuParser.PORCENTAJE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoPorcentaje" ):
                listener.enterTipoPorcentaje(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoPorcentaje" ):
                listener.exitTipoPorcentaje(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoPorcentaje" ):
                return visitor.visitTipoPorcentaje(self)
            else:
                return visitor.visitChildren(self)


    class TipoTextoContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXTO(self):
            return self.getToken(KipuParser.TEXTO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoTexto" ):
                listener.enterTipoTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoTexto" ):
                listener.exitTipoTexto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoTexto" ):
                return visitor.visitTipoTexto(self)
            else:
                return visitor.visitChildren(self)



    def tipo(self):

        localctx = KipuParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = KipuParser.TipoEnteroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(KipuParser.ENTERO)
                pass
            elif token in [4]:
                localctx = KipuParser.TipoDecimalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(KipuParser.DECIMAL)
                pass
            elif token in [5]:
                localctx = KipuParser.TipoPorcentajeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(KipuParser.PORCENTAJE)
                pass
            elif token in [6]:
                localctx = KipuParser.TipoBooleanoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.match(KipuParser.BOOLEANO)
                pass
            elif token in [7]:
                localctx = KipuParser.TipoTextoContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.match(KipuParser.TEXTO)
                pass
            elif token in [8]:
                localctx = KipuParser.TipoMontoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.match(KipuParser.MONTO)
                self.state = 92
                self.match(KipuParser.MENOR)
                self.state = 93
                self.match(KipuParser.MONEDA)
                self.state = 94
                self.match(KipuParser.MAYOR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def ASIG(self):
            return self.getToken(KipuParser.ASIG, 0)

        def MAS_ASIG(self):
            return self.getToken(KipuParser.MAS_ASIG, 0)

        def MENOS_ASIG(self):
            return self.getToken(KipuParser.MENOS_ASIG, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = KipuParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(KipuParser.ID)
            self.state = 98
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69524783104) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 99
            self.expresion(0)
            self.state = 100
            self.match(KipuParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KipuParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprYContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def Y(self):
            return self.getToken(KipuParser.Y, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprY" ):
                listener.enterExprY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprY" ):
                listener.exitExprY(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprY" ):
                return visitor.visitExprY(self)
            else:
                return visitor.visitChildren(self)


    class ExprAditivaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def SUMA(self):
            return self.getToken(KipuParser.SUMA, 0)
        def RESTA(self):
            return self.getToken(KipuParser.RESTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAditiva" ):
                listener.enterExprAditiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAditiva" ):
                listener.exitExprAditiva(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAditiva" ):
                return visitor.visitExprAditiva(self)
            else:
                return visitor.visitChildren(self)


    class ExprRelacionalContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def MENOR(self):
            return self.getToken(KipuParser.MENOR, 0)
        def MENOR_IGUAL(self):
            return self.getToken(KipuParser.MENOR_IGUAL, 0)
        def MAYOR(self):
            return self.getToken(KipuParser.MAYOR, 0)
        def MAYOR_IGUAL(self):
            return self.getToken(KipuParser.MAYOR_IGUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRelacional" ):
                listener.enterExprRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRelacional" ):
                listener.exitExprRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacional" ):
                return visitor.visitExprRelacional(self)
            else:
                return visitor.visitChildren(self)


    class ExprParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)
        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)

        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParentesis" ):
                listener.enterExprParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParentesis" ):
                listener.exitExprParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParentesis" ):
                return visitor.visitExprParentesis(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(KipuParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteral" ):
                listener.enterExprLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteral" ):
                listener.exitExprLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteral" ):
                return visitor.visitExprLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprLlamadaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def llamada(self):
            return self.getTypedRuleContext(KipuParser.LlamadaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLlamada" ):
                listener.enterExprLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLlamada" ):
                listener.exitExprLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLlamada" ):
                return visitor.visitExprLlamada(self)
            else:
                return visitor.visitChildren(self)


    class ExprNegativoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RESTA(self):
            return self.getToken(KipuParser.RESTA, 0)
        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNegativo" ):
                listener.enterExprNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNegativo" ):
                listener.exitExprNegativo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNegativo" ):
                return visitor.visitExprNegativo(self)
            else:
                return visitor.visitChildren(self)


    class ExprVariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprVariable" ):
                listener.enterExprVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprVariable" ):
                listener.exitExprVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprVariable" ):
                return visitor.visitExprVariable(self)
            else:
                return visitor.visitChildren(self)


    class ExprIgualdadContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def IGUAL(self):
            return self.getToken(KipuParser.IGUAL, 0)
        def DIFERENTE(self):
            return self.getToken(KipuParser.DIFERENTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprIgualdad" ):
                listener.enterExprIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprIgualdad" ):
                listener.exitExprIgualdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIgualdad" ):
                return visitor.visitExprIgualdad(self)
            else:
                return visitor.visitChildren(self)


    class ExprConversionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONVERTIR(self):
            return self.getToken(KipuParser.CONVERTIR, 0)
        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.COMA)
            else:
                return self.getToken(KipuParser.COMA, i)
        def MONEDA(self):
            return self.getToken(KipuParser.MONEDA, 0)
        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprConversion" ):
                listener.enterExprConversion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprConversion" ):
                listener.exitExprConversion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprConversion" ):
                return visitor.visitExprConversion(self)
            else:
                return visitor.visitChildren(self)


    class ExprOContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def O(self):
            return self.getToken(KipuParser.O, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprO" ):
                listener.enterExprO(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprO" ):
                listener.exitExprO(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprO" ):
                return visitor.visitExprO(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultiplicativaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def MULT(self):
            return self.getToken(KipuParser.MULT, 0)
        def DIV(self):
            return self.getToken(KipuParser.DIV, 0)
        def MOD(self):
            return self.getToken(KipuParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultiplicativa" ):
                listener.enterExprMultiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultiplicativa" ):
                listener.exitExprMultiplicativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultiplicativa" ):
                return visitor.visitExprMultiplicativa(self)
            else:
                return visitor.visitChildren(self)


    class ExprNoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NO(self):
            return self.getToken(KipuParser.NO, 0)
        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNo" ):
                listener.enterExprNo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNo" ):
                listener.exitExprNo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNo" ):
                return visitor.visitExprNo(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KipuParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = KipuParser.ExprParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 103
                self.match(KipuParser.PAR_IZQ)
                self.state = 104
                self.expresion(0)
                self.state = 105
                self.match(KipuParser.PAR_DER)
                pass

            elif la_ == 2:
                localctx = KipuParser.ExprConversionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(KipuParser.CONVERTIR)
                self.state = 108
                self.match(KipuParser.PAR_IZQ)
                self.state = 109
                self.expresion(0)
                self.state = 110
                self.match(KipuParser.COMA)
                self.state = 111
                self.match(KipuParser.MONEDA)
                self.state = 112
                self.match(KipuParser.COMA)
                self.state = 113
                self.expresion(0)
                self.state = 114
                self.match(KipuParser.PAR_DER)
                pass

            elif la_ == 3:
                localctx = KipuParser.ExprLlamadaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.llamada()
                pass

            elif la_ == 4:
                localctx = KipuParser.ExprNegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(KipuParser.RESTA)
                self.state = 118
                self.expresion(10)
                pass

            elif la_ == 5:
                localctx = KipuParser.ExprNoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(KipuParser.NO)
                self.state = 120
                self.expresion(5)
                pass

            elif la_ == 6:
                localctx = KipuParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.literal()
                pass

            elif la_ == 7:
                localctx = KipuParser.ExprVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(KipuParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 143
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = KipuParser.ExprMultiplicativaContext(self, KipuParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 125
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 126
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1649401659392) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expresion(10)
                        pass

                    elif la_ == 2:
                        localctx = KipuParser.ExprAditivaContext(self, KipuParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 128
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 129
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==37 or _la==38):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expresion(9)
                        pass

                    elif la_ == 3:
                        localctx = KipuParser.ExprRelacionalContext(self, KipuParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 131
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 132
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expresion(8)
                        pass

                    elif la_ == 4:
                        localctx = KipuParser.ExprIgualdadContext(self, KipuParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 134
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 135
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        self.expresion(7)
                        pass

                    elif la_ == 5:
                        localctx = KipuParser.ExprYContext(self, KipuParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 137
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 138
                        self.match(KipuParser.Y)
                        self.state = 139
                        self.expresion(5)
                        pass

                    elif la_ == 6:
                        localctx = KipuParser.ExprOContext(self, KipuParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 140
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 141
                        self.match(KipuParser.O)
                        self.state = 142
                        self.expresion(4)
                        pass

             
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KipuParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LitMontoContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numero(self):
            return self.getTypedRuleContext(KipuParser.NumeroContext,0)

        def MONEDA(self):
            return self.getToken(KipuParser.MONEDA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitMonto" ):
                listener.enterLitMonto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitMonto" ):
                listener.exitLitMonto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitMonto" ):
                return visitor.visitLitMonto(self)
            else:
                return visitor.visitChildren(self)


    class LitEnteroContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM_ENTERO(self):
            return self.getToken(KipuParser.NUM_ENTERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitEntero" ):
                listener.enterLitEntero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitEntero" ):
                listener.exitLitEntero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitEntero" ):
                return visitor.visitLitEntero(self)
            else:
                return visitor.visitChildren(self)


    class LitDecimalContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM_DECIMAL(self):
            return self.getToken(KipuParser.NUM_DECIMAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitDecimal" ):
                listener.enterLitDecimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitDecimal" ):
                listener.exitLitDecimal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitDecimal" ):
                return visitor.visitLitDecimal(self)
            else:
                return visitor.visitChildren(self)


    class LitTextoContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CADENA(self):
            return self.getToken(KipuParser.CADENA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitTexto" ):
                listener.enterLitTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitTexto" ):
                listener.exitLitTexto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitTexto" ):
                return visitor.visitLitTexto(self)
            else:
                return visitor.visitChildren(self)


    class LitBooleanoContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VERDADERO(self):
            return self.getToken(KipuParser.VERDADERO, 0)
        def FALSO(self):
            return self.getToken(KipuParser.FALSO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitBooleano" ):
                listener.enterLitBooleano(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitBooleano" ):
                listener.exitLitBooleano(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitBooleano" ):
                return visitor.visitLitBooleano(self)
            else:
                return visitor.visitChildren(self)


    class LitPorcentajeContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIT_PORCENTAJE(self):
            return self.getToken(KipuParser.LIT_PORCENTAJE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitPorcentaje" ):
                listener.enterLitPorcentaje(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitPorcentaje" ):
                listener.exitLitPorcentaje(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitPorcentaje" ):
                return visitor.visitLitPorcentaje(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = KipuParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = KipuParser.LitMontoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.numero()
                self.state = 149
                self.match(KipuParser.MONEDA)
                pass

            elif la_ == 2:
                localctx = KipuParser.LitEnteroContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(KipuParser.NUM_ENTERO)
                pass

            elif la_ == 3:
                localctx = KipuParser.LitDecimalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.match(KipuParser.NUM_DECIMAL)
                pass

            elif la_ == 4:
                localctx = KipuParser.LitPorcentajeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.match(KipuParser.LIT_PORCENTAJE)
                pass

            elif la_ == 5:
                localctx = KipuParser.LitTextoContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.match(KipuParser.CADENA)
                pass

            elif la_ == 6:
                localctx = KipuParser.LitBooleanoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_ENTERO(self):
            return self.getToken(KipuParser.NUM_ENTERO, 0)

        def NUM_DECIMAL(self):
            return self.getToken(KipuParser.NUM_DECIMAL, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)




    def numero(self):

        localctx = KipuParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==49 or _la==50):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeleccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.SI)
            else:
                return self.getToken(KipuParser.SI, i)

        def PAR_IZQ(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.PAR_IZQ)
            else:
                return self.getToken(KipuParser.PAR_IZQ, i)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)


        def PAR_DER(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.PAR_DER)
            else:
                return self.getToken(KipuParser.PAR_DER, i)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.BloqueContext)
            else:
                return self.getTypedRuleContext(KipuParser.BloqueContext,i)


        def SINO(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.SINO)
            else:
                return self.getToken(KipuParser.SINO, i)

        def getRuleIndex(self):
            return KipuParser.RULE_seleccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeleccion" ):
                listener.enterSeleccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeleccion" ):
                listener.exitSeleccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeleccion" ):
                return visitor.visitSeleccion(self)
            else:
                return visitor.visitChildren(self)




    def seleccion(self):

        localctx = KipuParser.SeleccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_seleccion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(KipuParser.SI)
            self.state = 161
            self.match(KipuParser.PAR_IZQ)
            self.state = 162
            self.expresion(0)
            self.state = 163
            self.match(KipuParser.PAR_DER)
            self.state = 164
            self.bloque()
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.match(KipuParser.SINO)
                    self.state = 166
                    self.match(KipuParser.SI)
                    self.state = 167
                    self.match(KipuParser.PAR_IZQ)
                    self.state = 168
                    self.expresion(0)
                    self.state = 169
                    self.match(KipuParser.PAR_DER)
                    self.state = 170
                    self.bloque() 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 177
                self.match(KipuParser.SINO)
                self.state = 178
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IteracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KipuParser.RULE_iteracion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IterMientrasContext(IteracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.IteracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MIENTRAS(self):
            return self.getToken(KipuParser.MIENTRAS, 0)
        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)
        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)

        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)
        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterMientras" ):
                listener.enterIterMientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterMientras" ):
                listener.exitIterMientras(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterMientras" ):
                return visitor.visitIterMientras(self)
            else:
                return visitor.visitChildren(self)


    class IterParaContext(IteracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.IteracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARA(self):
            return self.getToken(KipuParser.PARA, 0)
        def ID(self):
            return self.getToken(KipuParser.ID, 0)
        def DESDE(self):
            return self.getToken(KipuParser.DESDE, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)

        def HASTA(self):
            return self.getToken(KipuParser.HASTA, 0)
        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)

        def PASO(self):
            return self.getToken(KipuParser.PASO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterPara" ):
                listener.enterIterPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterPara" ):
                listener.exitIterPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterPara" ):
                return visitor.visitIterPara(self)
            else:
                return visitor.visitChildren(self)



    def iteracion(self):

        localctx = KipuParser.IteracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_iteracion)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = KipuParser.IterMientrasContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(KipuParser.MIENTRAS)
                self.state = 182
                self.match(KipuParser.PAR_IZQ)
                self.state = 183
                self.expresion(0)
                self.state = 184
                self.match(KipuParser.PAR_DER)
                self.state = 185
                self.bloque()
                pass
            elif token in [13]:
                localctx = KipuParser.IterParaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(KipuParser.PARA)
                self.state = 188
                self.match(KipuParser.ID)
                self.state = 189
                self.match(KipuParser.DESDE)
                self.state = 190
                self.expresion(0)
                self.state = 191
                self.match(KipuParser.HASTA)
                self.state = 192
                self.expresion(0)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 193
                    self.match(KipuParser.PASO)
                    self.state = 194
                    self.expresion(0)


                self.state = 197
                self.bloque()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReglaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGLA(self):
            return self.getToken(KipuParser.REGLA, 0)

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)

        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)


        def parametros(self):
            return self.getTypedRuleContext(KipuParser.ParametrosContext,0)


        def DOS_PUNTOS(self):
            return self.getToken(KipuParser.DOS_PUNTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(KipuParser.TipoContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_regla

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegla" ):
                listener.enterRegla(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegla" ):
                listener.exitRegla(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegla" ):
                return visitor.visitRegla(self)
            else:
                return visitor.visitChildren(self)




    def regla(self):

        localctx = KipuParser.ReglaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_regla)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(KipuParser.REGLA)
            self.state = 202
            self.match(KipuParser.ID)
            self.state = 203
            self.match(KipuParser.PAR_IZQ)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 204
                self.parametros()


            self.state = 207
            self.match(KipuParser.PAR_DER)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 208
                self.match(KipuParser.DOS_PUNTOS)
                self.state = 209
                self.tipo()


            self.state = 212
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ParametroContext)
            else:
                return self.getTypedRuleContext(KipuParser.ParametroContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.COMA)
            else:
                return self.getToken(KipuParser.COMA, i)

        def getRuleIndex(self):
            return KipuParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = KipuParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.parametro()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 215
                self.match(KipuParser.COMA)
                self.state = 216
                self.parametro()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def DOS_PUNTOS(self):
            return self.getToken(KipuParser.DOS_PUNTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(KipuParser.TipoContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = KipuParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(KipuParser.ID)
            self.state = 223
            self.match(KipuParser.DOS_PUNTOS)
            self.state = 224
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(KipuParser.RETORNAR, 0)

        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = KipuParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_retorno)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(KipuParser.RETORNAR)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8728198298730496) != 0):
                self.state = 227
                self.expresion(0)


            self.state = 230
            self.match(KipuParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)

        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def argumentos(self):
            return self.getTypedRuleContext(KipuParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = KipuParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_llamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(KipuParser.ID)
            self.state = 233
            self.match(KipuParser.PAR_IZQ)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8728198298730496) != 0):
                self.state = 234
                self.argumentos()


            self.state = 237
            self.match(KipuParser.PAR_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.COMA)
            else:
                return self.getToken(KipuParser.COMA, i)

        def getRuleIndex(self):
            return KipuParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = KipuParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.expresion(0)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 240
                self.match(KipuParser.COMA)
                self.state = 241
                self.expresion(0)
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaSentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llamada(self):
            return self.getTypedRuleContext(KipuParser.LlamadaContext,0)


        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_llamadaSentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaSentencia" ):
                listener.enterLlamadaSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaSentencia" ):
                listener.exitLlamadaSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaSentencia" ):
                return visitor.visitLlamadaSentencia(self)
            else:
                return visitor.visitChildren(self)




    def llamadaSentencia(self):

        localctx = KipuParser.LlamadaSentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_llamadaSentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.llamada()
            self.state = 248
            self.match(KipuParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaSalidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KipuParser.RULE_entradaSalida

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EntradaContext(EntradaSalidaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.EntradaSalidaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEER(self):
            return self.getToken(KipuParser.LEER, 0)
        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)
        def ID(self):
            return self.getToken(KipuParser.ID, 0)
        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)
        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada" ):
                listener.enterEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada" ):
                listener.exitEntrada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrada" ):
                return visitor.visitEntrada(self)
            else:
                return visitor.visitChildren(self)


    class SalidaContext(EntradaSalidaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KipuParser.EntradaSalidaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOSTRAR(self):
            return self.getToken(KipuParser.MOSTRAR, 0)
        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)
        def argumentos(self):
            return self.getTypedRuleContext(KipuParser.ArgumentosContext,0)

        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)
        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSalida" ):
                listener.enterSalida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSalida" ):
                listener.exitSalida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSalida" ):
                return visitor.visitSalida(self)
            else:
                return visitor.visitChildren(self)



    def entradaSalida(self):

        localctx = KipuParser.EntradaSalidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_entradaSalida)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = KipuParser.SalidaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(KipuParser.MOSTRAR)
                self.state = 251
                self.match(KipuParser.PAR_IZQ)
                self.state = 252
                self.argumentos()
                self.state = 253
                self.match(KipuParser.PAR_DER)
                self.state = 254
                self.match(KipuParser.PUNTO_COMA)
                pass
            elif token in [20]:
                localctx = KipuParser.EntradaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(KipuParser.LEER)
                self.state = 257
                self.match(KipuParser.PAR_IZQ)
                self.state = 258
                self.match(KipuParser.ID)
                self.state = 259
                self.match(KipuParser.PAR_DER)
                self.state = 260
                self.match(KipuParser.PUNTO_COMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




