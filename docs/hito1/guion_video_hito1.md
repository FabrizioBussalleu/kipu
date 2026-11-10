# Guion del video de demostración, Hito 1 (máximo 5 minutos)

Preparación antes de grabar:

- Terminal (PowerShell) abierta en la carpeta `kipu`, con fuente grande (18 pt o más).
- VS Code abierto con `grammar/Kipu.g4` y `ejemplos/facturacion.kp`.
- Ejecutar una vez `python -m pip install -r requirements.txt` para que no aparezca la instalación en el video.

| Tiempo | Qué se muestra | Qué se dice (idea, no leer) |
|---|---|---|
| 0:00 a 0:30 | Diapositiva de portada y problemática | Presentar al equipo. En Perú las reglas de IGV y detracciones se programan en Excel o en lenguajes generales; ahí aparecen errores de redondeo y de monedas mezcladas que recién se detectan en una fiscalización. Kipu hace de los montos con moneda un tipo del lenguaje. |
| 0:30 a 1:10 | `ejemplos/facturacion.kp` en el editor | Recorrer el programa: constantes `IGV` y `TASA_DETRACCION`, una `regla`, el `si ... sino`, `convertir` a dólares. Resaltar que `monto<PEN>` y `monto<USD>` son tipos distintos. |
| 1:10 a 1:50 | `grammar/Kipu.g4` (sección léxica y de expresiones) | Mostrar las palabras clave antes de `ID`, los literales `LIT_PORCENTAJE`, `NUM_DECIMAL`, `MONEDA`, y la regla `expresion` con su orden de precedencia. |
| 1:50 a 2:30 | `python src/kipu.py ejemplos/facturacion.kp --tokens` | Analizador léxico: cada token con línea, columna y lexema. Luego `python src/kipu.py tests/lexico/05_simbolos_invalidos.kp --solo-lexico` para ver `LEX-01` con `#`, `@` y `$`. |
| 2:30 a 3:15 | `python src/kipu.py ejemplos/facturacion.kp --arbol` (subir hasta el inicio) y `python src/kipu.py tests/sintactico/invalidos/02_parentesis_sin_cerrar.kp` | Analizador sintáctico: árbol generado por ANTLR y un error `SIN-01` en español: "falta ')' antes de '{'". |
| 3:15 a 4:15 | `python src/kipu.py ejemplos/facturacion.kp --simbolos` y `python src/kipu.py tests/semantico/invalidos/06_errores_multiples.kp` | Analizador semántico: tabla de símbolos con ámbitos. Luego cuatro errores en una pasada: constante modificada, suma PEN con USD, variable no declarada y redeclaración del contador. |
| 4:15 a 4:45 | `python -m unittest discover -s tests -v` y `python scripts/derivaciones.py` | 68 casos de prueba aprobados; las 28 derivaciones se generan y verifican contra la gramática del informe. |
| 4:45 a 5:00 | Diapositiva de próximos pasos | Hito 2: semántica completa. Hito 3: LLVM con montos como enteros en céntimos. Cierre: "si la regla no tiene sentido contable, no compila". |

Consejo: grabar cada bloque por separado y unirlos, así se controla mejor el límite de 5 minutos.
