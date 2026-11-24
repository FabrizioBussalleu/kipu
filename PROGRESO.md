# Progreso de la finalización de Kipu

## Fase actual

Correcciones locales terminadas; revisión final del equipo pendiente.

## Completado

- Se verificó que `cambios-Luciano` parte de `origin/main` (`e9eaedd`) y contiene Hito 2.
- Se comprobó el árbol de trabajo limpio antes de modificar archivos.
- Se inventariaron gramática, código, pruebas, ejemplos y documentación histórica.
- Se creó `.venv` en Windows con Python 3.12.7, ANTLR 4.13.2 y llvmlite 0.50.0.
- Línea base: 20 pruebas `unittest` aprobadas.
- Java 21 disponible; Clang no aparece en PATH.
- `VisitorSemantico` y `LLVMVisitor` recorren directamente el árbol de ANTLR; el segundo contiene `IRBuilder`.
- Se retiraron de la implementación activa el AST, su constructor y los módulos anteriores de semántica y LLVM.
- LLVM genera reglas, llamadas, retornos, lectura, concatenación y variables globales.
- Se verificó por JIT la recursión, retornos por ambas ramas, lectura de cinco tipos y el ejemplo tributario interactivo.
- Pruebas actuales: 29 `unittest`, todas aprobadas.
- Se prepararon informe, guías, resultados de validación, guion de presentación y un ZIP limpio del repositorio.
- Se cotejaron los Hitos 1–3 y la rúbrica de la transcripción recibida en `docs/hito3/matriz_cumplimiento.md`.
- Se incorporaron los 35 ejemplos, token/lexema, BNF y referencias a 28 derivaciones al contenido consolidado del informe.
- Se preparó un guion cronometrado de video de 4:45 y una propuesta explícita sobre reglas locales, sin cambiar el lenguaje.
- Se mejoraron nombres del Visitor y la validación de entrada del runtime JIT; el runtime C ahora registra textos para liberarlos al salir.

## Pendiente

- El equipo debe confirmar la intención original de las reglas locales y aprobar o rechazar la restricción semántica propuesta.
- El equipo debe contrastar la transcripción con el PDF original, revisar autoría y consultar al docente la asistencia externa permitida y la contradicción sobre «50 %» del Hito 3.
- Producir y revisar la presentación PDF y grabar/medir el video final de máximo cinco minutos.
- Probar el runtime C con un compilador local si el equipo requiere ejecutable nativo; la consigna no exige EXE expresamente.

## Archivos modificados

- `PROGRESO.md`, `src/kipu.py`, `src/ejecutor.py`, `runtime/kipu_runtime.c`, pruebas y ejemplos.
- Nuevos: `src/visitor_semantico.py`, `src/visitor_llvm.py`, `src/tipos_kipu.py`, `src/tabla_simbolos.py`.
- Eliminados tras sustitución: `src/ast_kipu.py`, `src/constructor_ast.py`, `src/semantico.py`, `src/generador_llvm.py`.

## Pruebas ejecutadas

- `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`: 20 pruebas, OK.
- Después de la migración: mismo comando, 23 pruebas, OK.
- Después de ampliar los escenarios: mismo comando, 29 pruebas, OK.
- `scripts/verificar_gramatica.py`: L1 a L6, OK; `scripts/derivaciones.py`: 28 derivaciones, OK.
- `scripts/empaquetar_hito3.py`: ZIP verificado sin `.venv`, cachés, `.ll` ni nombres sensibles.
- `ejemplos/hito3_tributario.kp` con entrada `3`: `884.64 PEN` y `235.93 USD`.
- `ejemplos/visitor_builder.kp`: salida `22`.

## Problemas y decisiones

- El primer intento de instalación quedó bloqueado por DNS de la zona restringida; se completó con acceso autorizado.
- No se modificarán gramática ni informes históricos sin necesidad demostrada.
- Los cambios de código permanecerán en commits locales.
- La transcripción de la consigna y rúbrica fue aportada después de la primera fase y se conservó en `docs/hito3/`. No se adjuntó el PDF original.
- El informe histórico del Hito 1 tiene 11 páginas frente al máximo transcrito de cinco más carátula; no se modificó retrospectivamente.
- Clang no apareció en PATH ni en rutas locales comunes. La revisión del C es estática; no se informa como prueba nativa.

## Siguiente acción

El equipo revisa la matriz y la propuesta sobre reglas locales, confirma autoría con el docente, prepara la presentación PDF y graba el video de máximo cinco minutos. Los commits permanecen locales hasta autorización de publicación.
