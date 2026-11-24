# Guía de demostración del Hito 3

Ejecutar desde la raíz con PowerShell y el entorno virtual del proyecto. Cada comando debe terminar con código 0 salvo el ejemplo inválido.

1. `py -3.12 -m venv .venv` y `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.
2. `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`. Resultado local observado: 29 pruebas, OK.
3. `.\.venv\Scripts\python.exe src/kipu.py ejemplos/visitor_builder.kp --llvm`. Abrir `ejemplos/visitor_builder.ll` y señalar las instrucciones `load`, `add`, `store` y `call`.
4. `.\.venv\Scripts\python.exe src/kipu.py ejemplos/visitor_builder.kp --ejecutar`. Salida observada: `22`.
5. `'3' | .\.venv\Scripts\python.exe src/kipu.py ejemplos/hito3_tributario.kp --ejecutar`. Salidas observadas: `Total sujeto a detracción: 884.64 PEN` y `Equivalente USD: 235.93 USD`.
6. `.\.venv\Scripts\python.exe src/kipu.py tests/semantico/invalidos/06_errores_multiples.kp`. Mostrar códigos, línea y columna; no se genera IR.

Para una demostración interactiva, omitir la tubería del paso 5 y escribir `3` seguido de Enter cuando `leer(cantidad)` espere la entrada. Los archivos `.ll` producidos por la CLI están excluidos de Git.

El guion cronometrado de la demo final está en `docs/hito3/guion_video_5min.md`. El equipo debe grabar y medir el video: este archivo no sustituye ese entregable.

Ejecutable nativo: con Clang instalado, generar un `.ll` y ejecutar `clang ejemplos/visitor_builder.ll runtime/kipu_runtime.c -o visitor_builder.exe`. Este paso está preparado, pero no fue verificado en este Windows porque Clang no estaba disponible. La consigna no exige un EXE expresamente.
