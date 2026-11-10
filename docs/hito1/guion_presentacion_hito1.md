# Guion de la presentación, Hito 1: Kipu

Duración estimada: 5 a 6 minutos. Los textos son una guía para decirlos con naturalidad, no para leerlos.

## Fabrizio Bussalleu Salcedo (diapositivas 1 a 4, aprox. 1:20)

**Diapositiva 1. Portada**
Buenos días. Somos Fabrizio Bussalleu, José Luis Sancho y Marco Cabrera, y les presentamos Kipu: un lenguaje de dominio específico para escribir reglas tributarias y cálculos con montos. El nombre viene del quipu, el sistema de cuerdas y nudos que usaban los incas para llevar sus cuentas.

**Diapositiva 2. Problemática**
En el Perú casi toda venta formal pasa por reglas tributarias: el IGV de 18 %, las detracciones, las retenciones y el tipo de cambio. Hoy esas reglas se escriben en Excel o se programan a mano en lenguajes como JavaScript o Python, y ahí aparecen cuatro problemas. Primero, los decimales: en punto flotante, 0.1 más 0.2 no da exactamente 0.3. Segundo, nada impide sumar soles con dólares. Tercero, un contador no puede leer ni auditar ese código. Y cuarto, los errores se descubren tarde, a veces recién en una fiscalización. Existen bibliotecas de dinero, pero validan la moneda cuando el programa ya se está ejecutando, no antes.

**Diapositiva 3. Propuesta**
Nuestra propuesta es que el monto con su moneda sea un tipo del lenguaje. En este ejemplo declaramos el IGV como porcentaje, definimos una regla que lo calcula y convertimos el total a dólares con la función convertir. La sintaxis está en español, monto en soles y monto en dólares son tipos distintos, y si alguien intenta mezclarlos, el programa no compila.

**Diapositiva 4. Objetivos**
Nuestro objetivo general es construir un compilador para Kipu con ANTLR4 y LLVM que verifique la coherencia de tipos y monedas antes de ejecutar. Lo dividimos en cinco objetivos específicos: los tres primeros, léxico, gramática y parser, se cumplen en este hito; la semántica empieza ahora y se completa en el Hito 2, y la generación de código con LLVM llega en el Hito 3. José Luis les explica cómo está construido el lenguaje.

## José Luis Sancho Navarro (diapositivas 5 a 8, aprox. 2:00)

**Diapositiva 5. Construcciones del lenguaje**
Gracias, Fabrizio. Kipu tiene siete construcciones: declaración de variables y constantes, asignación, expresiones, sentencias selectivas, iterativas, reglas, que son nuestras funciones, y entrada y salida. Para cada una definimos cinco ejemplos, 35 en total, y todos se validan automáticamente con el parser. Abajo ven la precedencia de operadores: primero paréntesis y llamadas, luego multiplicación y división, después suma y resta, comparaciones y al final los operadores lógicos no, y, o.

**Diapositiva 6. Analizador léxico**
El analizador léxico está en el archivo Kipu.g4 y reconoce 52 tokens: 26 palabras clave, las monedas PEN, USD y EUR, 13 operadores, 7 delimitadores, los literales y los identificadores. Dos decisiones importantes: las palabras clave se declaran antes que los identificadores, para que "si" sea palabra reservada y no una variable, y ANTLR siempre toma la coincidencia más larga, así que menor o igual se reconoce como un solo token. A la derecha ven la salida real del compilador con cada token, su línea y su columna. Si aparece un símbolo que no pertenece al lenguaje, como un numeral, se reporta el error LEX-01.

**Diapositiva 7. Analizador sintáctico**
Para la gramática libre de contexto usamos un no terminal por cada nivel de precedencia: expr para el "o", conj para el "y", y así hasta llegar a prim, que son los paréntesis, las llamadas, los literales y los identificadores. A la derecha está la derivación más a la izquierda de "cantidad igual 5": se parte de asig y siempre se reemplaza el no terminal de más a la izquierda hasta llegar solo a terminales. En ANTLR la misma precedencia se escribe con recursión por la izquierda, y los errores sintácticos se muestran en español con el código SIN-01.

**Diapositiva 8. Validación de la gramática**
Para no hacer las derivaciones a mano y equivocarnos, las generamos con un script. Cada ejemplo pasa por el lexer de ANTLR, luego un parser Earley lo reconoce con la gramática del informe, se comprueba que exista un único árbol y ese árbol se recorre en preorden, que es justamente la derivación más a la izquierda. El resultado: los 35 ejemplos son aceptados, generamos 28 derivaciones, cuatro por gramática, y no encontramos ninguna ambigüedad. Marco les explica ahora la parte semántica.

## Marco Antonio Luciano Cabrera Díaz (diapositivas 9 a 12, aprox. 2:00)

**Diapositiva 9. Analizador semántico**
Gracias, José Luis. El analizador semántico recorre el árbol con un visitor y mantiene una tabla de símbolos por ámbitos: global, dentro de cada regla, dentro de cada bloque y dentro de cada para. En este hito verifica cinco errores: identificador no declarado, redeclaración en el mismo ámbito, monedas incompatibles, tipos incompatibles y modificar una constante. A la derecha están las reglas de tipos: dos montos de la misma moneda se pueden sumar; un monto por un número o un porcentaje sigue siendo monto; y la única forma de cambiar de moneda es con convertir. Cuando una expresión tiene error, la marcamos como desconocida para no generar errores en cascada.

**Diapositiva 10. Funcionamiento**
Aquí un ejemplo real. Este programa consolida ventas del año y tiene cuatro errores distintos. En la línea 6 se intenta modificar la constante UIT. En la línea 7 se suman ventas en soles con ventas en dólares. En la línea 8 se usa una variable que nunca se declaró. Y en la línea 9 se vuelve a declarar mes, que ya es el contador del para. El compilador encuentra los cuatro en una sola pasada y cada uno con su código, línea y columna.

**Diapositiva 11. Pruebas y repositorio**
Todo el trabajo está respaldado por 68 casos de prueba automáticos: 11 léxicos, 47 sintácticos y 10 semánticos, y todos pasan. Cada archivo de prueba indica en su primera línea qué resultado espera, así que la prueba compara exactamente el código y la línea de cada error. A la derecha ven la estructura del repositorio: la gramática, el driver, el analizador semántico, las pruebas y la documentación.

**Diapositiva 12. Próximos pasos y cierre**
Con esto cerramos el Hito 1. En el Hito 2 completaremos la semántica con al menos seis errores, como condiciones que no son booleanas, tipos de retorno y número de argumentos en las llamadas, además de la arquitectura y el plan de validación. En el Hito 3 generaremos código con LLVM representando cada monto como un entero en céntimos, para eliminar por completo el error de redondeo. En resumen: en Kipu, si la regla no tiene sentido contable, no compila. Muchas gracias, quedamos atentos a sus preguntas.
