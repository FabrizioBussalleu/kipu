# Preguntas probables del profesor y cómo responderlas (Hito 2)

La rúbrica asigna puntos a las preguntas. Estas son las más probables, con una respuesta corta y correcta.

## Conceptos

**¿Qué diferencia hay entre token, lexema y patrón?**
El token es la categoría (por ejemplo `ID` o `MONEDA`), el lexema es el texto concreto del programa (`subtotal`, `PEN`) y el patrón es la expresión regular que describe qué lexemas pertenecen al token (`LETRA ID_COLA`).

**¿Qué es una gramática libre de contexto?**
Es una cuádrupla G = (N, T, P, S): no terminales, terminales, producciones de la forma A → α y un símbolo inicial. En Kipu: 37 no terminales, 52 tokens, 92 producciones y S = `programa`.

**¿Qué es una derivación más a la izquierda?**
Una derivación en la que, en cada paso, se reemplaza el no terminal que está más a la izquierda en la forma sentencial.

**¿Cuándo una gramática es ambigua? ¿La suya lo es?**
Cuando una cadena tiene más de un árbol de análisis. Verificamos los 35 ejemplos con la detección exacta de ambigüedad de ANTLR y no hubo ninguna. Además, la precedencia por niveles y los bloques obligatorios evitan los casos clásicos (precedencia de operadores y el "else colgante").

**¿Cómo definen la precedencia y la asociatividad?**
Con un no terminal por nivel: `expresion` (o), `conjuncion` (y), `negacion` (no), `igualdad`, `relacional`, `aritmetica` (+, -), `termino` (*, /, mod), `unario` y `primario`. La recursión por la izquierda (`aritmetica → aritmetica SUMA termino`) da asociatividad izquierda: `a - b - c` es `(a - b) - c`.

**¿ANTLR acepta recursión por la izquierda?**
Sí, ANTLR4 acepta recursión directa por la izquierda y la reescribe internamente; el árbol que construye conserva la forma de la gramática.

**¿Qué es la tabla de símbolos y qué es un ámbito?**
La tabla guarda cada identificador con su categoría, tipo y ubicación. El ámbito es la región donde un nombre es visible. En Kipu hay ámbito global, de regla (compartido con sus parámetros), de bloque y de `para` (compartido con el contador).

**¿Qué es el AST y por qué lo usan?**
Es un árbol que conserva solo la estructura con significado. La gramática en forma estándar genera árboles muy profundos (listas recursivas y un nivel por precedencia); el AST los reduce a nodos como `Binaria(op, izq, der)` y lo usan tanto el semántico como el generador.

**¿Qué es LLVM IR y qué es SSA?**
LLVM IR es una representación intermedia tipada, independiente de la máquina. En SSA cada valor se asigna una sola vez; por eso las variables de Kipu se guardan con `alloca` y se leen con `load`.

## Decisiones del proyecto

**¿Por qué los montos son enteros en céntimos?**
Porque el punto flotante no representa con exactitud los céntimos. Con enteros, sumar y restar es exacto, y el redondeo solo ocurre en multiplicaciones y divisiones, con una regla explícita (half-up) en `kipu.div_redondeo`.

**¿Cómo se representa un porcentaje?**
Como entero por 10 000: 18 % es 1800 y 12.5 % es 1250. `monto * porcentaje` es `monto * p / 10000` con redondeo.

**¿Por qué quitaron el comentario de bloque?**
Porque su regla léxica necesita el operador `*` (`.*?`), que no se permite en la forma estándar. Solo queda el comentario de línea, definido con un fragment recursivo.

**¿Cómo escriben `ID` sin `*`?**
`ID : LETRA ID_COLA ;` y `fragment ID_COLA : LETRA ID_COLA | DIGITO ID_COLA | ;`. La alternativa vacía corta la recursión.

**¿Cómo detectan que una regla no retorna en todos los caminos (SEM-11)?**
Con un análisis de caminos sobre el AST: una lista de sentencias retorna siempre si tiene un `retornar`, un bloque que retorna siempre o un `si` con `sino` donde todas las ramas retornan siempre. Un ciclo no garantiza el retorno porque puede no ejecutarse.

**¿Qué falta para el Hito 3?**
Generar LLVM IR para reglas, llamadas, `retornar` y `leer`; generar ejecutables nativos con clang; y reportar los resultados finales de la validación.
