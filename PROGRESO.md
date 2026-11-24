# Progreso de la finalización de Kipu

## Fase actual

Auditoría y preparación de la migración a Visitors de ANTLR.

## Completado

- Se verificó que `cambios-Luciano` parte de `origin/main` (`e9eaedd`) y contiene Hito 2.
- Se comprobó el árbol de trabajo limpio antes de modificar archivos.
- Se inventariaron gramática, código, pruebas, ejemplos y documentación histórica.
- Se creó `.venv` en Windows con Python 3.12.7, ANTLR 4.13.2 y llvmlite 0.50.0.
- Línea base: 20 pruebas `unittest` aprobadas.
- Java 21 disponible; Clang no aparece en PATH.

## Pendiente

- Revisar a fondo informes y buscar indicaciones oficiales y rúbrica; no se han identificado archivos oficiales independientes en el repositorio.
- Migrar semántica y LLVM a Visitors directos, completar Hito 3, ampliar pruebas y ejemplos.
- Preparar informe, guía, presentación y paquete de entrega.

## Archivos modificados

- `PROGRESO.md`.

## Pruebas ejecutadas

- `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`: 20 pruebas, OK.

## Problemas y decisiones

- El primer intento de instalación quedó bloqueado por DNS de la zona restringida; se completó con acceso autorizado.
- No se modificarán gramática ni informes históricos sin necesidad demostrada.
- Los cambios de código permanecerán en commits locales.

## Siguiente acción

Migrar el análisis semántico y verificar paridad de los 14 errores existentes.
