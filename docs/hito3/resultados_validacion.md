# Resultados de validación del Hito 3

**Entorno observado:** Windows 11, PowerShell, Python 3.12.7, `antlr4-python3-runtime` 4.13.2, `llvmlite` 0.50.0. Entorno virtual local `.venv`. Fecha: 24 de noviembre de 2026.

| Comando o escenario | Resultado observado |
|---|---|
| `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` antes de refactorizar | 20 pruebas, OK |
| El mismo comando tras la migración y ampliación | 29 pruebas, OK |
| `.\.venv\Scripts\python.exe scripts/verificar_gramatica.py` | Gramática cumple L1 a L6; el script informa 101 reglas |
| `.\.venv\Scripts\python.exe scripts/derivaciones.py` | 28 derivaciones, sin fallos |
| `src/kipu.py ejemplos/visitor_builder.kp --ejecutar` | IR verificado, JIT, salida `22`, código 0 |
| Entrada `3` a `src/kipu.py ejemplos/hito3_tributario.kp --ejecutar` | IR verificado, JIT, `884.64 PEN` y `235.93 USD`, código 0 |
| Prueba de regla recursiva `fact(5)` | IR verificado, JIT, salida `120` |
| Entrada decimal inválida `abc` | Error de entrada controlado en el runtime JIT |
| Ejecutable nativo | No ejecutado: Clang no estaba disponible en PATH ni en las rutas locales comunes revisadas |

La batería de `tests/test_kipu.py` verifica lexer, parser, códigos semánticos, tabla de símbolos, IR, salida JIT, montos en céntimos, reglas, ámbitos, lectura, concatenación y programa tributario. Los casos LLVM comparan la salida con archivos `.esperado`. No se usaron funciones falsas para simular LLVM.

La matriz `docs/hito3/matriz_cumplimiento.md` contrasta la consigna transcrita con la evidencia del repositorio. La prueba nativa de los cambios de entrada y memoria en C sigue pendiente; no se usa como evidencia de ejecución. Los informes del Hito 1 y 2 se conservaron sin cambiar sus resultados históricos.
