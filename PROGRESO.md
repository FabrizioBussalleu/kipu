# Progreso de la finalización de Kipu

## Fase actual

Validación ampliada y preparación de entregables del Hito 3.

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
- Pruebas actuales: 28 `unittest`, todas aprobadas.
- Se prepararon informe, guías, resultados de validación, guion de presentación y un ZIP limpio del repositorio.

## Pendiente

- Buscar indicaciones oficiales y rúbrica; los informes del equipo solo enumeran próximos pasos, sin formato o límites oficiales verificables.
- Ampliar pruebas de borde y revisar limitaciones de funciones anidadas y runtime C.
- El equipo debe obtener la consigna oficial, revisar formato/autoría y probar el runtime C con Clang.
- Convertir los borradores Markdown a los formatos académicos exigidos una vez conocida la consigna.

## Archivos modificados

- `PROGRESO.md`, `src/kipu.py`, `src/ejecutor.py`, `runtime/kipu_runtime.c`, pruebas y ejemplos.
- Nuevos: `src/visitor_semantico.py`, `src/visitor_llvm.py`, `src/tipos_kipu.py`, `src/tabla_simbolos.py`.
- Eliminados tras sustitución: `src/ast_kipu.py`, `src/constructor_ast.py`, `src/semantico.py`, `src/generador_llvm.py`.

## Pruebas ejecutadas

- `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`: 20 pruebas, OK.
- Después de la migración: mismo comando, 23 pruebas, OK.
- Después de ampliar los escenarios: mismo comando, 28 pruebas, OK.
- `scripts/verificar_gramatica.py`: L1 a L6, OK; `scripts/derivaciones.py`: 28 derivaciones, OK.
- `scripts/empaquetar_hito3.py`: ZIP verificado sin `.venv`, cachés, `.ll` ni nombres sensibles.
- `ejemplos/hito3_tributario.kp` con entrada `3`: `884.64 PEN` y `235.93 USD`.
- `ejemplos/visitor_builder.kp`: salida `22`.

## Problemas y decisiones

- El primer intento de instalación quedó bloqueado por DNS de la zona restringida; se completó con acceso autorizado.
- No se modificarán gramática ni informes históricos sin necesidad demostrada.
- Los cambios de código permanecerán en commits locales.
- El archivo de indicaciones oficiales del Hito 3 no está en el repositorio; los entregables documentales se marcarán como borradores sujetos a esa verificación.

## Siguiente acción

Repetir la batería y el empaquetado tras los ajustes finales, revisar el estado Git y dejar los commits únicamente locales.
