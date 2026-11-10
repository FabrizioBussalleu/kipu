# Guion de la presentación, Hito 2: Kipu

Duración estimada: 8 a 9 minutos. Los textos son una guía para decirlos con naturalidad, no para leerlos. El mismo texto está en las notas del orador de cada diapositiva del .pptx.

## Fabrizio Bussalleu Salcedo (diapositivas 1 a 4, aprox. 2:00)

**Diapositiva 1. Portada**
Buenos días. Somos Fabrizio Bussalleu, Jose Luis Sancho y Marco Cabrera, y presentamos el Hito 2 de Kipu, nuestro lenguaje de dominio específico para reglas tributarias y montos monetarios. En este hito actualizamos la gramática, completamos el analizador semántico, definimos la arquitectura y el plan de validación, y empezamos la generación de código con LLVM.

**Diapositiva 2. Problemática**
Recordemos el problema. En el Perú, las reglas como el IGV, las detracciones o el tipo de cambio se programan a mano en Excel o en lenguajes de propósito general. Eso trae cuatro problemas: los decimales en punto flotante no representan bien los céntimos, nada impide sumar soles con dólares, un contador no puede leer ese código y los errores se descubren tarde. Las bibliotecas de dinero existen, pero validan la moneda recién cuando el programa ya se está ejecutando.

**Diapositiva 3. Propuesta**
Nuestra propuesta es que el monto con su moneda sea un tipo del lenguaje. En este ejemplo declaramos el IGV como porcentaje, definimos una regla que lo calcula, verificamos si corresponde detracción y convertimos el total a dólares. La sintaxis está en español, monto en soles y monto en dólares son tipos distintos y, como novedad de este hito, el código generado guarda cada monto como un entero en céntimos, así que no hay error de redondeo.

**Diapositiva 4. Objetivos y estado**
Estos son nuestros objetivos y su estado. Los cuatro primeros están completos: léxico, gramática actualizada, lexer y parser, y el analizador semántico, que verifica 14 errores cuando el hito pedía 6. El quinto, la generación de LLVM IR, está en avance y se completa en el Hito 3. Además presentamos la arquitectura y un plan de validación con 128 casos automáticos. Jose Luis les explica ahora los conceptos y la gramática.

## Jose Luis Sancho Navarro (diapositivas 5 a 10, aprox. 3:30)

**Diapositiva 5. Conceptos clave (1/2)**
Gracias, Fabrizio. Primero, las definiciones que usamos. Un compilador traduce un programa fuente a otro equivalente y reporta errores; en nuestro caso, de Kipu a LLVM IR. Un token es una categoría, como ID; el lexema es el texto concreto, como subtotal; y el patrón es la expresión regular que lo describe. Una gramática libre de contexto tiene no terminales, terminales, producciones y un símbolo inicial. La producción épsilon es la cadena vacía y nos permite escribir listas y opcionales con recursión. En una derivación más a la izquierda siempre reemplazamos el no terminal de más a la izquierda, y una gramática es ambigua si una cadena tiene dos árboles.

**Diapositiva 6. Conceptos clave (2/2)**
Para el análisis semántico y el back end usamos estos conceptos. El AST es un árbol que conserva solo la estructura con significado. El análisis semántico verifica lo que la gramática no puede, como declarar antes de usar. La tabla de símbolos guarda cada identificador con su tipo, y el ámbito es la región donde ese nombre es visible. El sistema de tipos asigna un tipo a cada expresión, con coerción de entero a decimal. Finalmente, LLVM IR es una representación intermedia en forma SSA, organizada en bloques básicos, que ejecutamos con un compilador JIT.

**Diapositiva 7. Construcciones del lenguaje**
Kipu mantiene sus siete construcciones: declaración, asignación, expresiones, selectivas, iterativas, reglas y entrada y salida. Cada una tiene cinco ejemplos y los 35 se validan automáticamente con el parser. Abajo está la precedencia de operadores, de mayor a menor.

**Diapositiva 8. Analizador léxico**
En el analizador léxico, cada símbolo, operador y palabra reservada es un token con nombre, y las reservadas se declaran antes que ID para tener prioridad. El cambio importante es que ya no usamos asterisco ni más en el lexer: los identificadores, números y cadenas se construyen con fragments recursivos y una alternativa vacía, como ven en ID_COLA. También eliminamos el comentario de bloque; solo queda el comentario de línea.

**Diapositiva 9. Gramática actualizada**
Esta es la gramática actualizada. A la izquierda, cómo estaba en el Hito 1, con asterisco, signo de interrogación y etiquetas. A la derecha, la forma estándar del curso: las listas son recursivas con épsilon, los opcionales usan una alternativa vacía y la precedencia se define por niveles, como en termino. Además, un script revisa automáticamente los seis lineamientos cada vez que corremos las pruebas, y hoy la gramática los cumple todos.

**Diapositiva 10. Validación de la gramática**
Para validar la gramática, cada ejemplo se analiza con ANTLR y activamos la detección exacta de ambigüedad. Como la gramática ya está en BNF pura, recorrer el árbol en preorden da directamente la derivación más a la izquierda, y verificamos que cada paso sea una producción de la gramática. Aquí ven la derivación de cantidad igual 5. Los 35 ejemplos se aceptan, generamos 28 derivaciones y no hay ambigüedades. Marco les explica la parte semántica y el back end.

## Marco Antonio Luciano Cabrera Díaz (diapositivas 11 a 16, aprox. 3:30)

**Diapositiva 11. Analizador semántico completo**
Gracias, Jose Luis. El analizador semántico ahora verifica 14 errores. A los cinco del Hito 1 sumamos condición no booleana, retornar fuera de una regla, valor de retorno incompatible, número y tipo de argumentos, reglas que no retornan en todos los caminos, porcentajes fuera de rango, división entre cero y reglas sin valor usadas en una expresión. Para saber si una regla retorna siempre hacemos un análisis de caminos: por ejemplo, un si sin sino no garantiza el retorno.

**Diapositiva 12. Arquitectura del compilador**
Esta es la arquitectura. El programa pasa por el analizador léxico y el sintáctico de ANTLR, luego construimos un AST que aplana las listas recursivas, el analizador semántico lo anota con tipos y símbolos, y el generador produce LLVM IR, que se ejecuta con el JIT o se compila con clang. Todas las fases reportan sus errores a un gestor común, con código, línea y columna.

**Diapositiva 13. Avance del back end: LLVM IR**
En el back end, la decisión clave es cómo representar los tipos. Un monto es un entero de 64 bits en céntimos y un porcentaje es una fracción por diez mil. Así, multiplicar un precio por el IGV es una multiplicación entera seguida de una división con redondeo half-up, sin punto flotante. Ya generamos declaraciones, asignaciones, expresiones, convertir, condicionales, ciclos y mostrar; las reglas y las llamadas quedan para el Hito 3.

**Diapositiva 14. Funcionamiento**
Aquí vemos el compilador funcionando. Este programa liquida cuatro facturas con IGV, aplica detracción a las que superan 700 soles y convierte el total a dólares. Los resultados los verificamos a mano: por ejemplo, el IGV de 134.946 se redondea a 134.95. Además, el ejecutable nativo compilado con clang da exactamente la misma salida.

**Diapositiva 15. Plan de validación**
Todo esto está respaldado por un plan de validación en siete niveles, desde los lineamientos de la gramática hasta la ejecución del código generado, con 128 casos automáticos y todos aprobados. Cada prueba indica qué error espera y en qué línea, y GitHub Actions las corre en Ubuntu y Windows en cada cambio. También probamos casos límite de redondeo, como montos negativos.

**Diapositiva 16. Próximos pasos y cierre**
Para el Hito 3 completaremos el back end con reglas, llamadas y leer, generaremos ejecutables nativos y reportaremos los resultados finales de la validación. En resumen: en Kipu, si la regla no tiene sentido contable, no compila. Muchas gracias, quedamos atentos a sus preguntas.
