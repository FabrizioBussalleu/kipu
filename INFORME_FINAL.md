# Informe de trabajo en la rama cambios-Luciano

**Fecha de verificación local:** 24 de noviembre de 2026. **Estado:** implementación y pruebas JIT completas para los casos documentados; entrega académica pendiente de revisión directa del equipo. Se contrastó la transcripción de la consigna final aportada por el estudiante, conservada en `docs/hito3/PAUTAS_ENTREGA_FINAL.md`; el PDF original no se adjuntó.

## 1. Estado inicial

La rama partió de `origin/main` en `e9eaedd`, que contenía `develop` y `feature/hito2`; el árbol estaba limpio. La arquitectura activa era árbol ANTLR → `ConstructorAST` → AST propio → `AnalizadorSemantico` → `GeneradorLLVM`. El generador informaba `GEN-01` para reglas; `leer` y concatenación de textos no estaban generados. En Windows se instalaron dependencias en `.venv` y se ejecutaron 20 pruebas `unittest`, todas aprobadas.

## 2. Estado final y arquitectura

El flujo vigente es fuente Kipu → `KipuLexer` → `KipuParser` → árbol ANTLR → `VisitorSemantico` → `LLVMVisitor` con `IRBuilder` → LLVM IR → verificación → JIT. La CLI y el JIT se ejecutaron en Windows 11. El árbol propio y su constructor se retiraron de la implementación; Git conserva su historial. Las 29 pruebas actuales pasan.

## 3. Cambios de código

- Creados: `src/tipos_kipu.py`, `src/tabla_simbolos.py`, `src/visitor_semantico.py` y `src/visitor_llvm.py`.
- Modificados: `src/kipu.py`, `src/ejecutor.py`, `runtime/kipu_runtime.c`, `tests/test_kipu.py` y el caso 06 de `tests/llvm`.
- Eliminados tras la migración: `src/ast_kipu.py`, `src/constructor_ast.py`, `src/semantico.py` y `src/generador_llvm.py`.
- Nuevos ejemplos: `ejemplos/visitor_builder.kp` y `ejemplos/hito3_tributario.kp`.
- Documentación creada o actualizada: `README.md`, `PROGRESO.md`, este informe y `docs/hito3/`.

## 4. Observaciones del profesor

| Observación | Atención verificable |
|---|---|
| Usar Visitor y Builder para conectar | `LLVMVisitor` hereda de `KipuVisitor`, crea `self.builder = ir.IRBuilder(...)` y sus métodos `visit` emiten instrucciones LLVM directamente. |
| Código difícil de entender | El driver muestra las fases en orden; tipos y símbolos están en módulos pequeños; las operaciones se agrupan por regla gramatical. La guía de sustentación recorre un ejemplo real. |
| Clases difíciles de identificar | `VisitorSemantico`, `LLVMVisitor`, `Simbolo`, `Ambito` y `TablaSimbolos` tienen responsabilidades explícitas. |

## 5. Funcionalidades

Se conservaron declaraciones, constantes, asignaciones, expresiones y sus precedencias, condicionales, ciclos, conversión de monedas, montos en céntimos, porcentajes, redondeo, ámbitos y los 14 códigos SEM-01 a SEM-14. Se añadieron a la generación LLVM las reglas globales con parámetros y retorno, llamadas (incluida recursión), `leer`, concatenación de textos y acceso a variables globales desde reglas. El IR pasa por `verificar_ir` antes de entregarse o ejecutarse.

## 6. Validación realizada

| Verificación | Línea base | Resultado actual |
|---|---:|---:|
| `unittest discover -s tests -v` | 20/20 | 29/29 |
| Gramática L1 a L6 | No repetida como línea base separada | Aprobada; 101 reglas informadas por el script |
| Derivaciones | No repetida como línea base separada | 28 generadas sin fallos |
| LLVM IR y JIT de casos válidos | 5 casos con salida esperada y detracciones | 6 casos con salida esperada, detracciones y pruebas nuevas |
| Ejemplo mínimo en Windows | No existía | `22` |
| Ejemplo tributario con entrada `3` en Windows | No existía | `884.64 PEN`; `235.93 USD` |
| Ejecutable nativo con Clang | Sin prueba de esta sesión | Sin prueba: Clang no estaba disponible |

Las pruebas de entrada usan `io.StringIO` como fuente de datos, pero generan y ejecutan LLVM IR real con MCJIT. La línea de comandos también se ejecutó desde PowerShell con entrada por tubería.

## 7. Matriz de requisitos y evidencia

La matriz detallada en `docs/hito3/matriz_cumplimiento.md` contrasta las páginas 1–5 de la consigna transcrita, cada requisito acumulado de Hitos 1, 2 y 3, y las cuatro categorías de la rúbrica. Contiene evidencia, prueba, resultado, estado y acción pendiente. La rúbrica no permite asignar una nota automática: documentos, código, exposición y respuestas a preguntas son juzgados por el docente. El texto del Hito 3 repite «50 % de implementación» pese a la exigencia general de compilador completo; el equipo debe consultar la interpretación, sin usar esa frase para reducir el alcance.

| Requisito conocido | Implementación | Prueba o evidencia | Estado |
|---|---|---|---|
| Gramática y parser | `grammar/Kipu.g4`, `src/generated/` | Verificador L1 a L6, derivaciones y pruebas sintácticas | Verificado |
| Semántica y 14 errores | `src/visitor_semantico.py`, `src/tabla_simbolos.py` | Casos semánticos válidos e inválidos | Verificado |
| Visitor conectado a IRBuilder | `src/visitor_llvm.py` | Ejemplo `visitor_builder.kp`, IR y JIT | Verificado |
| Montos, tipos y monedas | `src/tipos_kipu.py`, `src/visitor_llvm.py` | Pruebas de céntimos, redondeo, conversión y programa tributario | Verificado en JIT |
| Reglas, llamadas y retorno | `LLVMVisitor.visitRegla`, `visitLlamada`, `visitRetorno` | Caso LLVM 06, recursión y retorno en ramas | Verificado para reglas globales |
| `leer` y concatenación | Visitor y runtime Python/C | Pruebas de entrada y texto en JIT | Verificado en JIT; C sin prueba nativa |
| LLVM IR válido | `src/kipu.py`, `ejecutor.verificar_ir` | Pruebas y CLI | Verificado en casos ejecutados |
| Ejecutable nativo | `runtime/kipu_runtime.c` | Comando documentado | Pendiente de Clang |
| Validación final y conclusiones | `docs/hito3/informe_hito3.md`, este informe | 29 pruebas, ejemplos y límites consignados | Contenido técnico preparado |
| Presentación y sustentación | `docs/hito3/presentacion_hito3.md`, `guia_sustentacion.md` | Guion y recorrido paso a paso | Contenido preparado; PDF y exposición pendientes |

## 8. Instalación y comandos exactos en Windows

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe scripts/verificar_gramatica.py
.\.venv\Scripts\python.exe scripts/derivaciones.py
.\.venv\Scripts\python.exe src/kipu.py ejemplos/visitor_builder.kp --ejecutar
'3' | .\.venv\Scripts\python.exe src/kipu.py ejemplos/hito3_tributario.kp --ejecutar
```

Con Clang instalado, el comando **pendiente de comprobar** es `clang ejemplos/visitor_builder.ll runtime/kipu_runtime.c -o visitor_builder.exe`.

## 9. Entregables y decisiones

`docs/hito3/informe_hito3.md` reúne la descripción técnica acumulada y anexos; `matriz_cumplimiento.md`, el cotejo por página y rúbrica; `presentacion_hito3.md`, la secuencia de diapositivas; `guia_demostracion.md`, `guia_sustentacion.md` y `guion_video_5min.md`, los recorridos de exposición; `resultados_validacion.md`, las mediciones. `PROGRESO.md` permite retomar el trabajo. `scripts/empaquetar_hito3.py` crea `entregables/kipu_hito3.zip` y excluye `.venv`, cachés, credenciales y `.ll` temporales.

La gramática y los informes históricos no se alteraron. Se usaron contextos ANTLR con anotaciones simples (`tipo_kipu`, `simbolo`) en lugar de otro AST. Los montos se mantienen en `i64` de céntimos; `double` solo interviene en cálculos de tasa decimal y operaciones del tipo decimal. Se conservaron los códigos de error semántico para facilitar la comparación con Hito 2.

## 10. Limitaciones y revisión humana

- Una regla declarada dentro de un bloque sigue produciendo `GEN-01`. La consigna no exige explícitamente reglas anidadas, pero la gramática actual las admite. `docs/hito3/propuesta_reglas_locales.md` plantea una restricción semántica al ámbito global para aprobación del equipo; no se aplicó sin esa decisión.
- El runtime C ahora valida entrada numérica, rangos, longitud de línea y booleanos, redondea montos sin punto flotante y libera textos dinámicos al salir. **No se compiló ni ejecutó con Clang**, así que estos cambios no cuentan aún como prueba nativa. Clang no estaba en PATH ni en las rutas locales comunes revisadas; la consigna no exige EXE.
- El informe histórico de Hito 1 tiene 11 páginas frente al máximo transcrito de cinco más carátula. Se conservó sin alteraciones. El Hito 3 no fija límite independiente de páginas.
- La presentación final debe ser PDF y la demo final debe ser un video de máximo cinco minutos. Ambos requieren producción, revisión y participación directa del equipo; los Markdown son contenido preparado, no entregables finales en esos formatos.
- El equipo debe revisar autoría y contribuciones, confirmar con el docente la asistencia externa permitida, verificar la entrega histórica y enviar los archivos a la plataforma universitaria. Este trabajo no atribuye esas acciones a integrantes concretos.
- Los commits de desarrollo permanecen locales en `cambios-Luciano`; solo se publicó la rama vacía inicial según la autorización recibida.
