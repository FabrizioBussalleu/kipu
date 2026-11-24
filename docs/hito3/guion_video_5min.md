# Guion de demostración final de Kipu

**Duración prevista:** 4 minutos 45 segundos. Es un guion para que los integrantes lo revisen, ensayen y graben personalmente. La consigna exige un video de funcionamiento de máximo cinco minutos; este archivo no es el video ni demuestra su duración real.

| Tiempo | Pantalla | Explicación y acción |
|---|---|---|
| 0:00–0:25 | Portada y `ejemplos/hito3_tributario.kp` | Presentar el problema: cálculos tributarios con monedas y porcentajes. Señalar `monto<PEN>` y la conversión explícita a USD. |
| 0:25–0:55 | Diagrama del informe Hito 3 | Seguir fuente → lexer → parser → árbol ANTLR → Visitor semántico → Visitor LLVM → IR verificado → JIT. |
| 0:55–1:30 | `src/visitor_semantico.py`, prueba inválida | Ejecutar `.\.venv\Scripts\python.exe src/kipu.py tests/semantico/invalidos/06_errores_multiples.kp`. Mostrar códigos, línea y columna; explicar que el IR no se genera con errores. |
| 1:30–2:15 | `ejemplos/visitor_builder.kp` y `src/visitor_llvm.py` | Ejecutar el ejemplo con `--llvm`. Señalar `visitAsignacion` y las instrucciones `load`, `add`, `store` en el `.ll`; explicar `self.builder`. |
| 2:15–2:40 | Consola JIT | Ejecutar `visitor_builder.kp --ejecutar`; comprobar salida `22`. |
| 2:40–3:35 | `ejemplos/hito3_tributario.kp` y consola | Ejecutar `'3' \| .\.venv\Scripts\python.exe src/kipu.py ejemplos/hito3_tributario.kp --ejecutar`. Mostrar `884.64 PEN` y `235.93 USD`; explicar céntimos y redondeo half-up. |
| 3:35–4:10 | Pruebas y derivaciones | Mostrar `python -m unittest discover -s tests -q` con 29 pruebas aprobadas, `scripts/verificar_gramatica.py` y `scripts/derivaciones.py` con 28 derivaciones. |
| 4:10–4:45 | Conclusiones y límites | Explicar que la arquitectura responde a la observación del profesor. Declarar que Clang/EXE no se verificó y que una regla local todavía produce `GEN-01`. Cerrar sin atribuir trabajo a una persona sin confirmación. |

Preparación antes de grabar: instalar dependencias, cerrar notificaciones, generar el `.ll` de demostración y ensayar los comandos. Medir el archivo final; si supera cinco minutos, recortar la narración antes de la entrega. El equipo decide quién presenta cada sección y verifica las reglas de autoría y asistencia externa con el docente.
