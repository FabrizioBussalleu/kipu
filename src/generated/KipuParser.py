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
        4,1,54,378,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,82,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,114,8,4,1,5,1,5,1,5,3,5,119,8,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,130,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,5,9,145,8,9,10,9,12,9,148,9,9,1,10,1,10,1,10,1,10,1,
        10,1,10,5,10,156,8,10,10,10,12,10,159,9,10,1,11,1,11,1,11,3,11,164,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,175,8,12,
        10,12,12,12,178,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,5,13,195,8,13,10,13,12,13,198,9,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,209,8,14,10,14,
        12,14,212,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,5,15,226,8,15,10,15,12,15,229,9,15,1,16,1,16,1,16,3,16,
        234,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,252,8,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,263,8,18,1,19,1,19,1,20,1,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,21,3,21,276,8,21,1,22,1,22,1,22,1,22,1,22,
        3,22,283,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        3,24,295,8,24,1,25,1,25,3,25,299,8,25,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,316,8,26,1,
        27,1,27,1,27,3,27,321,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,29,1,29,1,29,1,29,3,29,335,8,29,1,30,1,30,1,30,1,30,1,30,3,
        30,342,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,3,32,351,8,32,1,33,
        1,33,1,33,1,33,1,34,1,34,3,34,359,8,34,1,35,1,35,1,35,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,376,8,36,
        1,36,0,6,18,20,24,26,28,30,37,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,0,2,2,0,28,29,36,36,1,0,49,50,392,0,74,1,0,0,0,2,81,1,0,0,
        0,4,92,1,0,0,0,6,94,1,0,0,0,8,113,1,0,0,0,10,118,1,0,0,0,12,129,
        1,0,0,0,14,131,1,0,0,0,16,136,1,0,0,0,18,138,1,0,0,0,20,149,1,0,
        0,0,22,163,1,0,0,0,24,165,1,0,0,0,26,179,1,0,0,0,28,199,1,0,0,0,
        30,213,1,0,0,0,32,233,1,0,0,0,34,251,1,0,0,0,36,262,1,0,0,0,38,264,
        1,0,0,0,40,266,1,0,0,0,42,275,1,0,0,0,44,282,1,0,0,0,46,284,1,0,
        0,0,48,294,1,0,0,0,50,298,1,0,0,0,52,315,1,0,0,0,54,320,1,0,0,0,
        56,322,1,0,0,0,58,334,1,0,0,0,60,341,1,0,0,0,62,343,1,0,0,0,64,350,
        1,0,0,0,66,352,1,0,0,0,68,358,1,0,0,0,70,360,1,0,0,0,72,375,1,0,
        0,0,74,75,3,2,1,0,75,76,5,0,0,1,76,1,1,0,0,0,77,78,3,4,2,0,78,79,
        3,2,1,0,79,82,1,0,0,0,80,82,1,0,0,0,81,77,1,0,0,0,81,80,1,0,0,0,
        82,3,1,0,0,0,83,93,3,8,4,0,84,93,3,14,7,0,85,93,3,46,23,0,86,93,
        3,52,26,0,87,93,3,56,28,0,88,93,3,66,33,0,89,93,3,72,36,0,90,93,
        3,70,35,0,91,93,3,6,3,0,92,83,1,0,0,0,92,84,1,0,0,0,92,85,1,0,0,
        0,92,86,1,0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,
        1,0,0,0,92,91,1,0,0,0,93,5,1,0,0,0,94,95,5,43,0,0,95,96,3,2,1,0,
        96,97,5,44,0,0,97,7,1,0,0,0,98,99,5,1,0,0,99,100,5,52,0,0,100,101,
        5,47,0,0,101,102,3,12,6,0,102,103,3,10,5,0,103,104,5,45,0,0,104,
        114,1,0,0,0,105,106,5,2,0,0,106,107,5,52,0,0,107,108,5,47,0,0,108,
        109,3,12,6,0,109,110,5,36,0,0,110,111,3,18,9,0,111,112,5,45,0,0,
        112,114,1,0,0,0,113,98,1,0,0,0,113,105,1,0,0,0,114,9,1,0,0,0,115,
        116,5,36,0,0,116,119,3,18,9,0,117,119,1,0,0,0,118,115,1,0,0,0,118,
        117,1,0,0,0,119,11,1,0,0,0,120,130,5,3,0,0,121,130,5,4,0,0,122,130,
        5,5,0,0,123,130,5,6,0,0,124,130,5,7,0,0,125,126,5,8,0,0,126,127,
        5,34,0,0,127,128,5,9,0,0,128,130,5,35,0,0,129,120,1,0,0,0,129,121,
        1,0,0,0,129,122,1,0,0,0,129,123,1,0,0,0,129,124,1,0,0,0,129,125,
        1,0,0,0,130,13,1,0,0,0,131,132,5,52,0,0,132,133,3,16,8,0,133,134,
        3,18,9,0,134,135,5,45,0,0,135,15,1,0,0,0,136,137,7,0,0,0,137,17,
        1,0,0,0,138,139,6,9,-1,0,139,140,3,20,10,0,140,146,1,0,0,0,141,142,
        10,2,0,0,142,143,5,23,0,0,143,145,3,20,10,0,144,141,1,0,0,0,145,
        148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,19,1,0,0,0,148,146,
        1,0,0,0,149,150,6,10,-1,0,150,151,3,22,11,0,151,157,1,0,0,0,152,
        153,10,2,0,0,153,154,5,22,0,0,154,156,3,22,11,0,155,152,1,0,0,0,
        156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,21,1,0,0,0,159,
        157,1,0,0,0,160,161,5,24,0,0,161,164,3,22,11,0,162,164,3,24,12,0,
        163,160,1,0,0,0,163,162,1,0,0,0,164,23,1,0,0,0,165,166,6,12,-1,0,
        166,167,3,26,13,0,167,176,1,0,0,0,168,169,10,3,0,0,169,170,5,30,
        0,0,170,175,3,26,13,0,171,172,10,2,0,0,172,173,5,31,0,0,173,175,
        3,26,13,0,174,168,1,0,0,0,174,171,1,0,0,0,175,178,1,0,0,0,176,174,
        1,0,0,0,176,177,1,0,0,0,177,25,1,0,0,0,178,176,1,0,0,0,179,180,6,
        13,-1,0,180,181,3,28,14,0,181,196,1,0,0,0,182,183,10,5,0,0,183,184,
        5,34,0,0,184,195,3,28,14,0,185,186,10,4,0,0,186,187,5,32,0,0,187,
        195,3,28,14,0,188,189,10,3,0,0,189,190,5,35,0,0,190,195,3,28,14,
        0,191,192,10,2,0,0,192,193,5,33,0,0,193,195,3,28,14,0,194,182,1,
        0,0,0,194,185,1,0,0,0,194,188,1,0,0,0,194,191,1,0,0,0,195,198,1,
        0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,27,1,0,0,0,198,196,1,0,
        0,0,199,200,6,14,-1,0,200,201,3,30,15,0,201,210,1,0,0,0,202,203,
        10,3,0,0,203,204,5,37,0,0,204,209,3,30,15,0,205,206,10,2,0,0,206,
        207,5,38,0,0,207,209,3,30,15,0,208,202,1,0,0,0,208,205,1,0,0,0,209,
        212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,29,1,0,0,0,212,210,
        1,0,0,0,213,214,6,15,-1,0,214,215,3,32,16,0,215,227,1,0,0,0,216,
        217,10,4,0,0,217,218,5,39,0,0,218,226,3,32,16,0,219,220,10,3,0,0,
        220,221,5,40,0,0,221,226,3,32,16,0,222,223,10,2,0,0,223,224,5,27,
        0,0,224,226,3,32,16,0,225,216,1,0,0,0,225,219,1,0,0,0,225,222,1,
        0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,31,1,0,
        0,0,229,227,1,0,0,0,230,231,5,38,0,0,231,234,3,32,16,0,232,234,3,
        34,17,0,233,230,1,0,0,0,233,232,1,0,0,0,234,33,1,0,0,0,235,236,5,
        41,0,0,236,237,3,18,9,0,237,238,5,42,0,0,238,252,1,0,0,0,239,240,
        5,21,0,0,240,241,5,41,0,0,241,242,3,18,9,0,242,243,5,46,0,0,243,
        244,5,9,0,0,244,245,5,46,0,0,245,246,3,18,9,0,246,247,5,42,0,0,247,
        252,1,0,0,0,248,252,3,40,20,0,249,252,3,36,18,0,250,252,5,52,0,0,
        251,235,1,0,0,0,251,239,1,0,0,0,251,248,1,0,0,0,251,249,1,0,0,0,
        251,250,1,0,0,0,252,35,1,0,0,0,253,254,3,38,19,0,254,255,5,9,0,0,
        255,263,1,0,0,0,256,263,5,50,0,0,257,263,5,49,0,0,258,263,5,48,0,
        0,259,263,5,51,0,0,260,263,5,25,0,0,261,263,5,26,0,0,262,253,1,0,
        0,0,262,256,1,0,0,0,262,257,1,0,0,0,262,258,1,0,0,0,262,259,1,0,
        0,0,262,260,1,0,0,0,262,261,1,0,0,0,263,37,1,0,0,0,264,265,7,1,0,
        0,265,39,1,0,0,0,266,267,5,52,0,0,267,268,5,41,0,0,268,269,3,42,
        21,0,269,270,5,42,0,0,270,41,1,0,0,0,271,272,3,18,9,0,272,273,3,
        44,22,0,273,276,1,0,0,0,274,276,1,0,0,0,275,271,1,0,0,0,275,274,
        1,0,0,0,276,43,1,0,0,0,277,278,5,46,0,0,278,279,3,18,9,0,279,280,
        3,44,22,0,280,283,1,0,0,0,281,283,1,0,0,0,282,277,1,0,0,0,282,281,
        1,0,0,0,283,45,1,0,0,0,284,285,5,10,0,0,285,286,5,41,0,0,286,287,
        3,18,9,0,287,288,5,42,0,0,288,289,3,6,3,0,289,290,3,48,24,0,290,
        47,1,0,0,0,291,292,5,11,0,0,292,295,3,50,25,0,293,295,1,0,0,0,294,
        291,1,0,0,0,294,293,1,0,0,0,295,49,1,0,0,0,296,299,3,46,23,0,297,
        299,3,6,3,0,298,296,1,0,0,0,298,297,1,0,0,0,299,51,1,0,0,0,300,301,
        5,12,0,0,301,302,5,41,0,0,302,303,3,18,9,0,303,304,5,42,0,0,304,
        305,3,6,3,0,305,316,1,0,0,0,306,307,5,13,0,0,307,308,5,52,0,0,308,
        309,5,14,0,0,309,310,3,18,9,0,310,311,5,15,0,0,311,312,3,18,9,0,
        312,313,3,54,27,0,313,314,3,6,3,0,314,316,1,0,0,0,315,300,1,0,0,
        0,315,306,1,0,0,0,316,53,1,0,0,0,317,318,5,16,0,0,318,321,3,18,9,
        0,319,321,1,0,0,0,320,317,1,0,0,0,320,319,1,0,0,0,321,55,1,0,0,0,
        322,323,5,17,0,0,323,324,5,52,0,0,324,325,5,41,0,0,325,326,3,58,
        29,0,326,327,5,42,0,0,327,328,3,64,32,0,328,329,3,6,3,0,329,57,1,
        0,0,0,330,331,3,62,31,0,331,332,3,60,30,0,332,335,1,0,0,0,333,335,
        1,0,0,0,334,330,1,0,0,0,334,333,1,0,0,0,335,59,1,0,0,0,336,337,5,
        46,0,0,337,338,3,62,31,0,338,339,3,60,30,0,339,342,1,0,0,0,340,342,
        1,0,0,0,341,336,1,0,0,0,341,340,1,0,0,0,342,61,1,0,0,0,343,344,5,
        52,0,0,344,345,5,47,0,0,345,346,3,12,6,0,346,63,1,0,0,0,347,348,
        5,47,0,0,348,351,3,12,6,0,349,351,1,0,0,0,350,347,1,0,0,0,350,349,
        1,0,0,0,351,65,1,0,0,0,352,353,5,18,0,0,353,354,3,68,34,0,354,355,
        5,45,0,0,355,67,1,0,0,0,356,359,3,18,9,0,357,359,1,0,0,0,358,356,
        1,0,0,0,358,357,1,0,0,0,359,69,1,0,0,0,360,361,3,40,20,0,361,362,
        5,45,0,0,362,71,1,0,0,0,363,364,5,19,0,0,364,365,5,41,0,0,365,366,
        3,18,9,0,366,367,3,44,22,0,367,368,5,42,0,0,368,369,5,45,0,0,369,
        376,1,0,0,0,370,371,5,20,0,0,371,372,5,41,0,0,372,373,5,52,0,0,373,
        374,5,42,0,0,374,376,5,45,0,0,375,363,1,0,0,0,375,370,1,0,0,0,376,
        73,1,0,0,0,30,81,92,113,118,129,146,157,163,174,176,194,196,208,
        210,225,227,233,251,262,275,282,294,298,315,320,334,341,350,358,
        375
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
                      "NUM_DECIMAL", "NUM_ENTERO", "CADENA", "ID", "COMENTARIO", 
                      "ESPACIO" ]

    RULE_programa = 0
    RULE_listaSentencias = 1
    RULE_sentencia = 2
    RULE_bloque = 3
    RULE_declaracion = 4
    RULE_inicializacion = 5
    RULE_tipo = 6
    RULE_asignacion = 7
    RULE_opAsignacion = 8
    RULE_expresion = 9
    RULE_conjuncion = 10
    RULE_negacion = 11
    RULE_igualdad = 12
    RULE_relacional = 13
    RULE_aritmetica = 14
    RULE_termino = 15
    RULE_unario = 16
    RULE_primario = 17
    RULE_literal = 18
    RULE_numero = 19
    RULE_llamada = 20
    RULE_argumentos = 21
    RULE_argumentosCola = 22
    RULE_seleccion = 23
    RULE_parteSino = 24
    RULE_colaSino = 25
    RULE_iteracion = 26
    RULE_pasoOpcional = 27
    RULE_regla = 28
    RULE_parametros = 29
    RULE_parametrosCola = 30
    RULE_parametro = 31
    RULE_tipoRetorno = 32
    RULE_retorno = 33
    RULE_valorRetorno = 34
    RULE_llamadaSentencia = 35
    RULE_entradaSalida = 36

    ruleNames =  [ "programa", "listaSentencias", "sentencia", "bloque", 
                   "declaracion", "inicializacion", "tipo", "asignacion", 
                   "opAsignacion", "expresion", "conjuncion", "negacion", 
                   "igualdad", "relacional", "aritmetica", "termino", "unario", 
                   "primario", "literal", "numero", "llamada", "argumentos", 
                   "argumentosCola", "seleccion", "parteSino", "colaSino", 
                   "iteracion", "pasoOpcional", "regla", "parametros", "parametrosCola", 
                   "parametro", "tipoRetorno", "retorno", "valorRetorno", 
                   "llamadaSentencia", "entradaSalida" ]

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
    COMENTARIO=53
    ESPACIO=54

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

        def listaSentencias(self):
            return self.getTypedRuleContext(KipuParser.ListaSentenciasContext,0)


        def EOF(self):
            return self.getToken(KipuParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.listaSentencias()
            self.state = 75
            self.match(KipuParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaSentenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self):
            return self.getTypedRuleContext(KipuParser.SentenciaContext,0)


        def listaSentencias(self):
            return self.getTypedRuleContext(KipuParser.ListaSentenciasContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_listaSentencias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaSentencias" ):
                listener.enterListaSentencias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaSentencias" ):
                listener.exitListaSentencias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaSentencias" ):
                return visitor.visitListaSentencias(self)
            else:
                return visitor.visitChildren(self)




    def listaSentencias(self):

        localctx = KipuParser.ListaSentenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_listaSentencias)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 10, 12, 13, 17, 18, 19, 20, 43, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.sentencia()
                self.state = 78
                self.listaSentencias()
                pass
            elif token in [-1, 44]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 4, self.RULE_sentencia)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.seleccion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.iteracion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.regla()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.retorno()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.entradaSalida()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 90
                self.llamadaSentencia()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 91
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

        def listaSentencias(self):
            return self.getTypedRuleContext(KipuParser.ListaSentenciasContext,0)


        def LLAVE_DER(self):
            return self.getToken(KipuParser.LLAVE_DER, 0)

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
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(KipuParser.LLAVE_IZQ)
            self.state = 95
            self.listaSentencias()
            self.state = 96
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

        def VAR(self):
            return self.getToken(KipuParser.VAR, 0)

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def DOS_PUNTOS(self):
            return self.getToken(KipuParser.DOS_PUNTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(KipuParser.TipoContext,0)


        def inicializacion(self):
            return self.getTypedRuleContext(KipuParser.InicializacionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def CONST(self):
            return self.getToken(KipuParser.CONST, 0)

        def ASIG(self):
            return self.getToken(KipuParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = KipuParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(KipuParser.VAR)
                self.state = 99
                self.match(KipuParser.ID)
                self.state = 100
                self.match(KipuParser.DOS_PUNTOS)
                self.state = 101
                self.tipo()
                self.state = 102
                self.inicializacion()
                self.state = 103
                self.match(KipuParser.PUNTO_COMA)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(KipuParser.CONST)
                self.state = 106
                self.match(KipuParser.ID)
                self.state = 107
                self.match(KipuParser.DOS_PUNTOS)
                self.state = 108
                self.tipo()
                self.state = 109
                self.match(KipuParser.ASIG)
                self.state = 110
                self.expresion(0)
                self.state = 111
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


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(KipuParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = KipuParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inicializacion)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(KipuParser.ASIG)
                self.state = 116
                self.expresion(0)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

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

        def ENTERO(self):
            return self.getToken(KipuParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(KipuParser.DECIMAL, 0)

        def PORCENTAJE(self):
            return self.getToken(KipuParser.PORCENTAJE, 0)

        def BOOLEANO(self):
            return self.getToken(KipuParser.BOOLEANO, 0)

        def TEXTO(self):
            return self.getToken(KipuParser.TEXTO, 0)

        def MONTO(self):
            return self.getToken(KipuParser.MONTO, 0)

        def MENOR(self):
            return self.getToken(KipuParser.MENOR, 0)

        def MONEDA(self):
            return self.getToken(KipuParser.MONEDA, 0)

        def MAYOR(self):
            return self.getToken(KipuParser.MAYOR, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = KipuParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(KipuParser.ENTERO)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(KipuParser.DECIMAL)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(KipuParser.PORCENTAJE)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(KipuParser.BOOLEANO)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.match(KipuParser.TEXTO)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.match(KipuParser.MONTO)
                self.state = 126
                self.match(KipuParser.MENOR)
                self.state = 127
                self.match(KipuParser.MONEDA)
                self.state = 128
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

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def opAsignacion(self):
            return self.getTypedRuleContext(KipuParser.OpAsignacionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

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
        self.enterRule(localctx, 14, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(KipuParser.ID)
            self.state = 132
            self.opAsignacion()
            self.state = 133
            self.expresion(0)
            self.state = 134
            self.match(KipuParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpAsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(KipuParser.ASIG, 0)

        def MAS_ASIG(self):
            return self.getToken(KipuParser.MAS_ASIG, 0)

        def MENOS_ASIG(self):
            return self.getToken(KipuParser.MENOS_ASIG, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_opAsignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAsignacion" ):
                listener.enterOpAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAsignacion" ):
                listener.exitOpAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAsignacion" ):
                return visitor.visitOpAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def opAsignacion(self):

        localctx = KipuParser.OpAsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_opAsignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69524783104) != 0)):
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


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjuncion(self):
            return self.getTypedRuleContext(KipuParser.ConjuncionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def O(self):
            return self.getToken(KipuParser.O, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KipuParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.conjuncion(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KipuParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 141
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 142
                    self.match(KipuParser.O)
                    self.state = 143
                    self.conjuncion(0) 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConjuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negacion(self):
            return self.getTypedRuleContext(KipuParser.NegacionContext,0)


        def conjuncion(self):
            return self.getTypedRuleContext(KipuParser.ConjuncionContext,0)


        def Y(self):
            return self.getToken(KipuParser.Y, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_conjuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjuncion" ):
                listener.enterConjuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjuncion" ):
                listener.exitConjuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjuncion" ):
                return visitor.visitConjuncion(self)
            else:
                return visitor.visitChildren(self)



    def conjuncion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KipuParser.ConjuncionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_conjuncion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.negacion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KipuParser.ConjuncionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conjuncion)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    self.match(KipuParser.Y)
                    self.state = 154
                    self.negacion() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NegacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(KipuParser.NO, 0)

        def negacion(self):
            return self.getTypedRuleContext(KipuParser.NegacionContext,0)


        def igualdad(self):
            return self.getTypedRuleContext(KipuParser.IgualdadContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_negacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegacion" ):
                listener.enterNegacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegacion" ):
                listener.exitNegacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegacion" ):
                return visitor.visitNegacion(self)
            else:
                return visitor.visitChildren(self)




    def negacion(self):

        localctx = KipuParser.NegacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_negacion)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(KipuParser.NO)
                self.state = 161
                self.negacion()
                pass
            elif token in [21, 25, 26, 38, 41, 48, 49, 50, 51, 52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.igualdad(0)
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


    class IgualdadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self):
            return self.getTypedRuleContext(KipuParser.RelacionalContext,0)


        def igualdad(self):
            return self.getTypedRuleContext(KipuParser.IgualdadContext,0)


        def IGUAL(self):
            return self.getToken(KipuParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(KipuParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_igualdad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualdad" ):
                listener.enterIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualdad" ):
                listener.exitIgualdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualdad" ):
                return visitor.visitIgualdad(self)
            else:
                return visitor.visitChildren(self)



    def igualdad(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KipuParser.IgualdadContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_igualdad, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.relacional(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = KipuParser.IgualdadContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_igualdad)
                        self.state = 168
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 169
                        self.match(KipuParser.IGUAL)
                        self.state = 170
                        self.relacional(0)
                        pass

                    elif la_ == 2:
                        localctx = KipuParser.IgualdadContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_igualdad)
                        self.state = 171
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 172
                        self.match(KipuParser.DIFERENTE)
                        self.state = 173
                        self.relacional(0)
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aritmetica(self):
            return self.getTypedRuleContext(KipuParser.AritmeticaContext,0)


        def relacional(self):
            return self.getTypedRuleContext(KipuParser.RelacionalContext,0)


        def MENOR(self):
            return self.getToken(KipuParser.MENOR, 0)

        def MENOR_IGUAL(self):
            return self.getToken(KipuParser.MENOR_IGUAL, 0)

        def MAYOR(self):
            return self.getToken(KipuParser.MAYOR, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(KipuParser.MAYOR_IGUAL, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)



    def relacional(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KipuParser.RelacionalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_relacional, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.aritmetica(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = KipuParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 182
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 183
                        self.match(KipuParser.MENOR)
                        self.state = 184
                        self.aritmetica(0)
                        pass

                    elif la_ == 2:
                        localctx = KipuParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 185
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 186
                        self.match(KipuParser.MENOR_IGUAL)
                        self.state = 187
                        self.aritmetica(0)
                        pass

                    elif la_ == 3:
                        localctx = KipuParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 188
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 189
                        self.match(KipuParser.MAYOR)
                        self.state = 190
                        self.aritmetica(0)
                        pass

                    elif la_ == 4:
                        localctx = KipuParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 191
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 192
                        self.match(KipuParser.MAYOR_IGUAL)
                        self.state = 193
                        self.aritmetica(0)
                        pass

             
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(KipuParser.TerminoContext,0)


        def aritmetica(self):
            return self.getTypedRuleContext(KipuParser.AritmeticaContext,0)


        def SUMA(self):
            return self.getToken(KipuParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(KipuParser.RESTA, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAritmetica" ):
                listener.enterAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAritmetica" ):
                listener.exitAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAritmetica" ):
                return visitor.visitAritmetica(self)
            else:
                return visitor.visitChildren(self)



    def aritmetica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KipuParser.AritmeticaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_aritmetica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = KipuParser.AritmeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_aritmetica)
                        self.state = 202
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 203
                        self.match(KipuParser.SUMA)
                        self.state = 204
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = KipuParser.AritmeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_aritmetica)
                        self.state = 205
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 206
                        self.match(KipuParser.RESTA)
                        self.state = 207
                        self.termino(0)
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unario(self):
            return self.getTypedRuleContext(KipuParser.UnarioContext,0)


        def termino(self):
            return self.getTypedRuleContext(KipuParser.TerminoContext,0)


        def MULT(self):
            return self.getToken(KipuParser.MULT, 0)

        def DIV(self):
            return self.getToken(KipuParser.DIV, 0)

        def MOD(self):
            return self.getToken(KipuParser.MOD, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KipuParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.unario()
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 225
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = KipuParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 216
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 217
                        self.match(KipuParser.MULT)
                        self.state = 218
                        self.unario()
                        pass

                    elif la_ == 2:
                        localctx = KipuParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 219
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 220
                        self.match(KipuParser.DIV)
                        self.state = 221
                        self.unario()
                        pass

                    elif la_ == 3:
                        localctx = KipuParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 222
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 223
                        self.match(KipuParser.MOD)
                        self.state = 224
                        self.unario()
                        pass

             
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RESTA(self):
            return self.getToken(KipuParser.RESTA, 0)

        def unario(self):
            return self.getTypedRuleContext(KipuParser.UnarioContext,0)


        def primario(self):
            return self.getTypedRuleContext(KipuParser.PrimarioContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_unario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnario" ):
                listener.enterUnario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnario" ):
                listener.exitUnario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnario" ):
                return visitor.visitUnario(self)
            else:
                return visitor.visitChildren(self)




    def unario(self):

        localctx = KipuParser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unario)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(KipuParser.RESTA)
                self.state = 231
                self.unario()
                pass
            elif token in [21, 25, 26, 41, 48, 49, 50, 51, 52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.primario()
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


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)


        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def CONVERTIR(self):
            return self.getToken(KipuParser.CONVERTIR, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(KipuParser.COMA)
            else:
                return self.getToken(KipuParser.COMA, i)

        def MONEDA(self):
            return self.getToken(KipuParser.MONEDA, 0)

        def llamada(self):
            return self.getTypedRuleContext(KipuParser.LlamadaContext,0)


        def literal(self):
            return self.getTypedRuleContext(KipuParser.LiteralContext,0)


        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_primario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimario" ):
                listener.enterPrimario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimario" ):
                listener.exitPrimario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = KipuParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primario)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(KipuParser.PAR_IZQ)
                self.state = 236
                self.expresion(0)
                self.state = 237
                self.match(KipuParser.PAR_DER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(KipuParser.CONVERTIR)
                self.state = 240
                self.match(KipuParser.PAR_IZQ)
                self.state = 241
                self.expresion(0)
                self.state = 242
                self.match(KipuParser.COMA)
                self.state = 243
                self.match(KipuParser.MONEDA)
                self.state = 244
                self.match(KipuParser.COMA)
                self.state = 245
                self.expresion(0)
                self.state = 246
                self.match(KipuParser.PAR_DER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.llamada()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.match(KipuParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numero(self):
            return self.getTypedRuleContext(KipuParser.NumeroContext,0)


        def MONEDA(self):
            return self.getToken(KipuParser.MONEDA, 0)

        def NUM_ENTERO(self):
            return self.getToken(KipuParser.NUM_ENTERO, 0)

        def NUM_DECIMAL(self):
            return self.getToken(KipuParser.NUM_DECIMAL, 0)

        def LIT_PORCENTAJE(self):
            return self.getToken(KipuParser.LIT_PORCENTAJE, 0)

        def CADENA(self):
            return self.getToken(KipuParser.CADENA, 0)

        def VERDADERO(self):
            return self.getToken(KipuParser.VERDADERO, 0)

        def FALSO(self):
            return self.getToken(KipuParser.FALSO, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = KipuParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.numero()
                self.state = 254
                self.match(KipuParser.MONEDA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(KipuParser.NUM_ENTERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(KipuParser.NUM_DECIMAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.match(KipuParser.LIT_PORCENTAJE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 259
                self.match(KipuParser.CADENA)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 260
                self.match(KipuParser.VERDADERO)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 261
                self.match(KipuParser.FALSO)
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
        self.enterRule(localctx, 38, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)

        def argumentos(self):
            return self.getTypedRuleContext(KipuParser.ArgumentosContext,0)


        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

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
        self.enterRule(localctx, 40, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(KipuParser.ID)
            self.state = 267
            self.match(KipuParser.PAR_IZQ)
            self.state = 268
            self.argumentos()
            self.state = 269
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

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def argumentosCola(self):
            return self.getTypedRuleContext(KipuParser.ArgumentosColaContext,0)


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
        self.enterRule(localctx, 42, self.RULE_argumentos)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 24, 25, 26, 38, 41, 48, 49, 50, 51, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.expresion(0)
                self.state = 272
                self.argumentosCola()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgumentosColaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(KipuParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def argumentosCola(self):
            return self.getTypedRuleContext(KipuParser.ArgumentosColaContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_argumentosCola

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentosCola" ):
                listener.enterArgumentosCola(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentosCola" ):
                listener.exitArgumentosCola(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentosCola" ):
                return visitor.visitArgumentosCola(self)
            else:
                return visitor.visitChildren(self)




    def argumentosCola(self):

        localctx = KipuParser.ArgumentosColaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_argumentosCola)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(KipuParser.COMA)
                self.state = 278
                self.expresion(0)
                self.state = 279
                self.argumentosCola()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

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


    class SeleccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(KipuParser.SI, 0)

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)


        def parteSino(self):
            return self.getTypedRuleContext(KipuParser.ParteSinoContext,0)


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
        self.enterRule(localctx, 46, self.RULE_seleccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(KipuParser.SI)
            self.state = 285
            self.match(KipuParser.PAR_IZQ)
            self.state = 286
            self.expresion(0)
            self.state = 287
            self.match(KipuParser.PAR_DER)
            self.state = 288
            self.bloque()
            self.state = 289
            self.parteSino()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParteSinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(KipuParser.SINO, 0)

        def colaSino(self):
            return self.getTypedRuleContext(KipuParser.ColaSinoContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_parteSino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParteSino" ):
                listener.enterParteSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParteSino" ):
                listener.exitParteSino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParteSino" ):
                return visitor.visitParteSino(self)
            else:
                return visitor.visitChildren(self)




    def parteSino(self):

        localctx = KipuParser.ParteSinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parteSino)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(KipuParser.SINO)
                self.state = 292
                self.colaSino()
                pass
            elif token in [-1, 1, 2, 10, 12, 13, 17, 18, 19, 20, 43, 44, 52]:
                self.enterOuterAlt(localctx, 2)

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


    class ColaSinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seleccion(self):
            return self.getTypedRuleContext(KipuParser.SeleccionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_colaSino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColaSino" ):
                listener.enterColaSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColaSino" ):
                listener.exitColaSino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColaSino" ):
                return visitor.visitColaSino(self)
            else:
                return visitor.visitChildren(self)




    def colaSino(self):

        localctx = KipuParser.ColaSinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_colaSino)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.seleccion()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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


    class IteracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(KipuParser.MIENTRAS, 0)

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KipuParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KipuParser.ExpresionContext,i)


        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)


        def PARA(self):
            return self.getToken(KipuParser.PARA, 0)

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def DESDE(self):
            return self.getToken(KipuParser.DESDE, 0)

        def HASTA(self):
            return self.getToken(KipuParser.HASTA, 0)

        def pasoOpcional(self):
            return self.getTypedRuleContext(KipuParser.PasoOpcionalContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_iteracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteracion" ):
                listener.enterIteracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteracion" ):
                listener.exitIteracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteracion" ):
                return visitor.visitIteracion(self)
            else:
                return visitor.visitChildren(self)




    def iteracion(self):

        localctx = KipuParser.IteracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_iteracion)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(KipuParser.MIENTRAS)
                self.state = 301
                self.match(KipuParser.PAR_IZQ)
                self.state = 302
                self.expresion(0)
                self.state = 303
                self.match(KipuParser.PAR_DER)
                self.state = 304
                self.bloque()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(KipuParser.PARA)
                self.state = 307
                self.match(KipuParser.ID)
                self.state = 308
                self.match(KipuParser.DESDE)
                self.state = 309
                self.expresion(0)
                self.state = 310
                self.match(KipuParser.HASTA)
                self.state = 311
                self.expresion(0)
                self.state = 312
                self.pasoOpcional()
                self.state = 313
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


    class PasoOpcionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASO(self):
            return self.getToken(KipuParser.PASO, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_pasoOpcional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPasoOpcional" ):
                listener.enterPasoOpcional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPasoOpcional" ):
                listener.exitPasoOpcional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPasoOpcional" ):
                return visitor.visitPasoOpcional(self)
            else:
                return visitor.visitChildren(self)




    def pasoOpcional(self):

        localctx = KipuParser.PasoOpcionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_pasoOpcional)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(KipuParser.PASO)
                self.state = 318
                self.expresion(0)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)

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

        def parametros(self):
            return self.getTypedRuleContext(KipuParser.ParametrosContext,0)


        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def tipoRetorno(self):
            return self.getTypedRuleContext(KipuParser.TipoRetornoContext,0)


        def bloque(self):
            return self.getTypedRuleContext(KipuParser.BloqueContext,0)


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
        self.enterRule(localctx, 56, self.RULE_regla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(KipuParser.REGLA)
            self.state = 323
            self.match(KipuParser.ID)
            self.state = 324
            self.match(KipuParser.PAR_IZQ)
            self.state = 325
            self.parametros()
            self.state = 326
            self.match(KipuParser.PAR_DER)
            self.state = 327
            self.tipoRetorno()
            self.state = 328
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

        def parametro(self):
            return self.getTypedRuleContext(KipuParser.ParametroContext,0)


        def parametrosCola(self):
            return self.getTypedRuleContext(KipuParser.ParametrosColaContext,0)


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
        self.enterRule(localctx, 58, self.RULE_parametros)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.parametro()
                self.state = 331
                self.parametrosCola()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

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


    class ParametrosColaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(KipuParser.COMA, 0)

        def parametro(self):
            return self.getTypedRuleContext(KipuParser.ParametroContext,0)


        def parametrosCola(self):
            return self.getTypedRuleContext(KipuParser.ParametrosColaContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_parametrosCola

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosCola" ):
                listener.enterParametrosCola(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosCola" ):
                listener.exitParametrosCola(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosCola" ):
                return visitor.visitParametrosCola(self)
            else:
                return visitor.visitChildren(self)




    def parametrosCola(self):

        localctx = KipuParser.ParametrosColaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parametrosCola)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(KipuParser.COMA)
                self.state = 337
                self.parametro()
                self.state = 338
                self.parametrosCola()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 62, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(KipuParser.ID)
            self.state = 344
            self.match(KipuParser.DOS_PUNTOS)
            self.state = 345
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOS_PUNTOS(self):
            return self.getToken(KipuParser.DOS_PUNTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(KipuParser.TipoContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_tipoRetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoRetorno" ):
                listener.enterTipoRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoRetorno" ):
                listener.exitTipoRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoRetorno" ):
                return visitor.visitTipoRetorno(self)
            else:
                return visitor.visitChildren(self)




    def tipoRetorno(self):

        localctx = KipuParser.TipoRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_tipoRetorno)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(KipuParser.DOS_PUNTOS)
                self.state = 348
                self.tipo()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)

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


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(KipuParser.RETORNAR, 0)

        def valorRetorno(self):
            return self.getTypedRuleContext(KipuParser.ValorRetornoContext,0)


        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

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
        self.enterRule(localctx, 66, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(KipuParser.RETORNAR)
            self.state = 353
            self.valorRetorno()
            self.state = 354
            self.match(KipuParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def getRuleIndex(self):
            return KipuParser.RULE_valorRetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValorRetorno" ):
                listener.enterValorRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValorRetorno" ):
                listener.exitValorRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValorRetorno" ):
                return visitor.visitValorRetorno(self)
            else:
                return visitor.visitChildren(self)




    def valorRetorno(self):

        localctx = KipuParser.ValorRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_valorRetorno)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 24, 25, 26, 38, 41, 48, 49, 50, 51, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.expresion(0)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 70, self.RULE_llamadaSentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.llamada()
            self.state = 361
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

        def MOSTRAR(self):
            return self.getToken(KipuParser.MOSTRAR, 0)

        def PAR_IZQ(self):
            return self.getToken(KipuParser.PAR_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(KipuParser.ExpresionContext,0)


        def argumentosCola(self):
            return self.getTypedRuleContext(KipuParser.ArgumentosColaContext,0)


        def PAR_DER(self):
            return self.getToken(KipuParser.PAR_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(KipuParser.PUNTO_COMA, 0)

        def LEER(self):
            return self.getToken(KipuParser.LEER, 0)

        def ID(self):
            return self.getToken(KipuParser.ID, 0)

        def getRuleIndex(self):
            return KipuParser.RULE_entradaSalida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntradaSalida" ):
                listener.enterEntradaSalida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntradaSalida" ):
                listener.exitEntradaSalida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntradaSalida" ):
                return visitor.visitEntradaSalida(self)
            else:
                return visitor.visitChildren(self)




    def entradaSalida(self):

        localctx = KipuParser.EntradaSalidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_entradaSalida)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(KipuParser.MOSTRAR)
                self.state = 364
                self.match(KipuParser.PAR_IZQ)
                self.state = 365
                self.expresion(0)
                self.state = 366
                self.argumentosCola()
                self.state = 367
                self.match(KipuParser.PAR_DER)
                self.state = 368
                self.match(KipuParser.PUNTO_COMA)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(KipuParser.LEER)
                self.state = 371
                self.match(KipuParser.PAR_IZQ)
                self.state = 372
                self.match(KipuParser.ID)
                self.state = 373
                self.match(KipuParser.PAR_DER)
                self.state = 374
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
        self._predicates[9] = self.expresion_sempred
        self._predicates[10] = self.conjuncion_sempred
        self._predicates[12] = self.igualdad_sempred
        self._predicates[13] = self.relacional_sempred
        self._predicates[14] = self.aritmetica_sempred
        self._predicates[15] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def conjuncion_sempred(self, localctx:ConjuncionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def igualdad_sempred(self, localctx:IgualdadContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def relacional_sempred(self, localctx:RelacionalContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def aritmetica_sempred(self, localctx:AritmeticaContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




