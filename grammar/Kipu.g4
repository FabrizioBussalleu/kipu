/*
 * Kipu: lenguaje de dominio específico para reglas tributarias y montos monetarios.
 * Teoría de Compiladores (1ACC0218), UPC, ciclo 2026-2. Hito 1.
 *
 * Gramática combinada ANTLR4 (analizador léxico + analizador sintáctico).
 * Generación del parser para Python:
 *   java -jar lib/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/generated -Xexact-output-dir grammar/Kipu.g4
 */
grammar Kipu;

// ============================================================================
// ANALIZADOR SINTÁCTICO
// ============================================================================

programa
    : sentencia* EOF
    ;

sentencia
    : declaracion
    | asignacion
    | seleccion
    | iteracion
    | regla
    | retorno
    | entradaSalida
    | llamadaSentencia
    | bloque
    ;

bloque
    : LLAVE_IZQ sentencia* LLAVE_DER
    ;

// --- 1. Declaración de variables y constantes -------------------------------
declaracion
    : VAR ID DOS_PUNTOS tipo (ASIG expresion)? PUNTO_COMA      # declaracionVariable
    | CONST ID DOS_PUNTOS tipo ASIG expresion PUNTO_COMA       # declaracionConstante
    ;

tipo
    : ENTERO                              # tipoEntero
    | DECIMAL                             # tipoDecimal
    | PORCENTAJE                          # tipoPorcentaje
    | BOOLEANO                            # tipoBooleano
    | TEXTO                               # tipoTexto
    | MONTO MENOR MONEDA MAYOR            # tipoMonto
    ;

// --- 2. Asignación ------------------------------------------------------------
asignacion
    : ID op=(ASIG | MAS_ASIG | MENOS_ASIG) expresion PUNTO_COMA
    ;

// --- 3. Expresiones (aritméticas, monetarias, relacionales y lógicas) --------
// El orden de las alternativas define la precedencia (de mayor a menor).
expresion
    : PAR_IZQ expresion PAR_DER                                               # exprParentesis
    | CONVERTIR PAR_IZQ expresion COMA MONEDA COMA expresion PAR_DER           # exprConversion
    | llamada                                                                 # exprLlamada
    | RESTA expresion                                                         # exprNegativo
    | expresion op=(MULT | DIV | MOD) expresion                               # exprMultiplicativa
    | expresion op=(SUMA | RESTA) expresion                                   # exprAditiva
    | expresion op=(MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL) expresion      # exprRelacional
    | expresion op=(IGUAL | DIFERENTE) expresion                              # exprIgualdad
    | NO expresion                                                            # exprNo
    | expresion Y expresion                                                   # exprY
    | expresion O expresion                                                   # exprO
    | literal                                                                 # exprLiteral
    | ID                                                                      # exprVariable
    ;

literal
    : numero MONEDA          # litMonto
    | NUM_ENTERO             # litEntero
    | NUM_DECIMAL            # litDecimal
    | LIT_PORCENTAJE         # litPorcentaje
    | CADENA                 # litTexto
    | (VERDADERO | FALSO)    # litBooleano
    ;

numero
    : NUM_ENTERO
    | NUM_DECIMAL
    ;

// --- 4. Sentencias selectivas -------------------------------------------------
seleccion
    : SI PAR_IZQ expresion PAR_DER bloque
      (SINO SI PAR_IZQ expresion PAR_DER bloque)*
      (SINO bloque)?
    ;

// --- 5. Sentencias iterativas ---------------------------------------------
iteracion
    : MIENTRAS PAR_IZQ expresion PAR_DER bloque                                  # iterMientras
    | PARA ID DESDE expresion HASTA expresion (PASO expresion)? bloque           # iterPara
    ;

// --- 6. Reglas (funciones), llamadas y retorno ---------------------------------
regla
    : REGLA ID PAR_IZQ parametros? PAR_DER (DOS_PUNTOS tipo)? bloque
    ;

parametros
    : parametro (COMA parametro)*
    ;

parametro
    : ID DOS_PUNTOS tipo
    ;

retorno
    : RETORNAR expresion? PUNTO_COMA
    ;

llamada
    : ID PAR_IZQ argumentos? PAR_DER
    ;

argumentos
    : expresion (COMA expresion)*
    ;

llamadaSentencia
    : llamada PUNTO_COMA
    ;

// --- 7. Entrada y salida -------------------------------------------------------
entradaSalida
    : MOSTRAR PAR_IZQ argumentos PAR_DER PUNTO_COMA        # salida
    | LEER PAR_IZQ ID PAR_DER PUNTO_COMA                   # entrada
    ;

// ============================================================================
// ANALIZADOR LÉXICO
// ============================================================================

// --- Palabras clave: declaración ----------------------------------------------
VAR         : 'var' ;
CONST       : 'const' ;

// --- Palabras clave: tipos de datos -------------------------------------------
ENTERO      : 'entero' ;
DECIMAL     : 'decimal' ;
PORCENTAJE  : 'porcentaje' ;
BOOLEANO    : 'booleano' ;
TEXTO       : 'texto' ;
MONTO       : 'monto' ;

// --- Monedas (ISO 4217) -------------------------------------------------------
MONEDA      : 'PEN' | 'USD' | 'EUR' ;

// --- Palabras clave: control de flujo ------------------------------------------
SI          : 'si' ;
SINO        : 'sino' ;
MIENTRAS    : 'mientras' ;
PARA        : 'para' ;
DESDE       : 'desde' ;
HASTA       : 'hasta' ;
PASO        : 'paso' ;

// --- Palabras clave: reglas, E/S y conversión ---------------------------------
REGLA       : 'regla' ;
RETORNAR    : 'retornar' ;
MOSTRAR     : 'mostrar' ;
LEER        : 'leer' ;
CONVERTIR   : 'convertir' ;

// --- Operadores lógicos y literales booleanos ----------------------------------
Y           : 'y' ;
O           : 'o' ;
NO          : 'no' ;
VERDADERO   : 'verdadero' ;
FALSO       : 'falso' ;
MOD         : 'mod' ;

// --- Operadores -------------------------------------------------------------
MAS_ASIG    : '+=' ;
MENOS_ASIG  : '-=' ;
IGUAL       : '==' ;
DIFERENTE   : '!=' ;
MENOR_IGUAL : '<=' ;
MAYOR_IGUAL : '>=' ;
MENOR       : '<' ;
MAYOR       : '>' ;
ASIG        : '=' ;
SUMA        : '+' ;
RESTA       : '-' ;
MULT        : '*' ;
DIV         : '/' ;

// --- Delimitadores ------------------------------------------------------------
PAR_IZQ     : '(' ;
PAR_DER     : ')' ;
LLAVE_IZQ   : '{' ;
LLAVE_DER   : '}' ;
PUNTO_COMA  : ';' ;
COMA        : ',' ;
DOS_PUNTOS  : ':' ;

// --- Literales ----------------------------------------------------------------
LIT_PORCENTAJE : DIGITO+ ('.' DIGITO+)? '%' ;
NUM_DECIMAL    : DIGITO+ '.' DIGITO+ ;
NUM_ENTERO     : DIGITO+ ;
CADENA         : '"' ( ~["\\\r\n] | '\\' . )* '"' ;

// --- Identificadores (después de las palabras clave) ------------------------
ID          : LETRA (LETRA | DIGITO)* ;

// --- Elementos ignorados -------------------------------------------------------
COMENTARIO_LINEA  : '//' ~[\r\n]* -> skip ;
COMENTARIO_BLOQUE : '/*' .*? '*/' -> skip ;
ESPACIO           : [ \t\r\n]+ -> skip ;

fragment DIGITO : [0-9] ;
fragment LETRA  : [a-zA-Z_áéíóúÁÉÍÓÚñÑ] ;
