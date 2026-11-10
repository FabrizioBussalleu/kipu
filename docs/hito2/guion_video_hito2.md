# Guion del video de demostración, Hito 2 (máximo 5 minutos)

Preparación antes de grabar:

- PowerShell abierto en la carpeta `kipu`, con fuente grande (18 pt o más).
- Ejecutar una vez `python -m pip install -r requirements.txt` para que la instalación no salga en el video.
- VS Code abierto con `grammar/Kipu.g4`, `ejemplos/detracciones.kp` y `tests/semantico/invalidos/06_errores_multiples.kp`.

| Tiempo | Quién | Qué se muestra | Qué se dice (idea, no leer) |
|---|---|---|---|
| 0:00 a 0:30 | Fabrizio | Diapositivas 1 y 3 | Presentar al equipo y a Kipu: un lenguaje donde el monto con su moneda es un tipo; si la regla no tiene sentido contable, no compila. En este hito: gramática actualizada, semántico completo y primer código LLVM. |
| 0:30 a 1:20 | Jose Luis | `grammar/Kipu.g4` y `python scripts/verificar_gramatica.py` | Mostrar `listaSentencias`, `inicializacion` con alternativa vacía, `termino` por niveles y el fragment `ID_COLA`. Correr el verificador: cumple los 6 lineamientos (sin ?, *, + ni subreglas). |
| 1:20 a 2:00 | Jose Luis | `python src/kipu.py ejemplos/facturacion.kp --tokens` y luego `--arbol` | Analizador léxico (tokens con línea y columna) y árbol sintáctico; mostrar un nodo con ε. |
| 2:00 a 2:30 | Jose Luis | `python scripts/derivaciones.py` y `docs/anexo_derivaciones.md` | 35 ejemplos aceptados sin ambigüedad y 28 derivaciones más a la izquierda verificadas. |
| 2:30 a 3:30 | Marco | `python src/kipu.py tests/semantico/invalidos/06_errores_multiples.kp` y `python src/kipu.py tests/semantico/invalidos/12_regla_sin_retorno.kp` | Errores semánticos con código, línea y columna. Explicar SEM-11: un si sin sino no garantiza el retorno. Mencionar que son 14 errores. |
| 3:30 a 4:30 | Marco | `python src/kipu.py ejemplos/detracciones.kp --ejecutar` y abrir `ejemplos/detracciones.ll` | Generación de LLVM IR y ejecución JIT. En el `.ll`, mostrar que 249.90 PEN es `24990` (céntimos) y la llamada a `kipu.div_redondeo`. Leer el total: 2701.12 PEN = 720.30 USD. |
| 4:30 a 5:00 | Marco | `python -m unittest discover -s tests -v` (final) y diapositiva 16 | Todas las pruebas aprobadas. Próximo hito: reglas y llamadas en LLVM y ejecutables nativos. Cierre. |

Consejo: grabar cada bloque por separado y unirlos; así es más fácil respetar los 5 minutos.
