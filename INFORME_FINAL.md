# Informe de trabajo en la rama cambios-Luciano

**Fecha de verificación local:** 24 de noviembre de 2026. **Estado:** implementación y pruebas JIT completas para los casos documentados; entrega académica pendiente de cotejo con la consigna oficial y de prueba nativa con Clang.

## 1. Estado inicial

La rama partió de `origin/main` en `e9eaedd`, que contenía `develop` y `feature/hito2`; el árbol estaba limpio. La arquitectura activa era árbol ANTLR → `ConstructorAST` → AST propio → `AnalizadorSemantico` → `GeneradorLLVM`. El generador informaba `GEN-01` para reglas; `leer` y concatenación de textos no estaban generados. En Windows se instalaron dependencias en `.venv` y se ejecutaron 20 pruebas `unittest`, todas aprobadas.

## 2. Estado final y arquitectura

El flujo vigente es fuente Kipu → `KipuLexer` → `KipuParser` → árbol ANTLR → `VisitorSemantico` → `LLVMVisitor` con `IRBuilder` → LLVM IR → verificación → JIT. La CLI y el JIT se ejecutaron en Windows 11. El árbol propio y su constructor se retiraron de la implementación; Git conserva su historial. Las 28 pruebas actuales pasan.

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
| `unittest discover -s tests -v` | 20/20 | 28/28 |
| Gramática L1 a L6 | No repetida como línea base separada | Aprobada; 101 reglas informadas por el script |
| Derivaciones | No repetida como línea base separada | 28 generadas sin fallos |
| LLVM IR y JIT de casos válidos | 5 casos con salida esperada y detracciones | 6 casos con salida esperada, detracciones y pruebas nuevas |
| Ejemplo mínimo en Windows | No existía | `22` |
| Ejemplo tributario con entrada `3` en Windows | No existía | `884.64 PEN`; `235.93 USD` |
| Ejecutable nativo con Clang | Sin prueba de esta sesión | Sin prueba: Clang no estaba disponible |

Las pruebas de entrada usan `io.StringIO` como fuente de datos, pero generan y ejecutan LLVM IR real con MCJIT. La línea de comandos también se ejecutó desde PowerShell con entrada por tubería.

## 7. Matriz de requisitos y evidencia

No se encontró la consigna ni la rúbrica oficial del Hito 3 en el repositorio. Esta matriz usa los compromisos declarados por el equipo en la sección «Próximos pasos» del informe del Hito 2 y los puntos del encargo recibido; **no sustituye la matriz oficial**.

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
| Validación final y conclusiones | `docs/hito3/informe_hito3.md`, este informe | 28 pruebas, ejemplos y límites consignados | Borrador sujeto a consigna |
| Presentación y sustentación | `docs/hito3/presentacion_hito3.md`, `guia_sustentacion.md` | Guion y recorrido paso a paso | Contenido preparado; formato final pendiente |

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

`docs/hito3/informe_hito3.md` reúne la descripción técnica; `presentacion_hito3.md`, la secuencia de diapositivas; `guia_demostracion.md` y `guia_sustentacion.md`, los recorridos de exposición; `resultados_validacion.md`, las mediciones. `PROGRESO.md` permite retomar el trabajo. `scripts/empaquetar_hito3.py` crea `entregables/kipu_hito3.zip` y excluye `.venv`, cachés, credenciales y `.ll` temporales.

La gramática y los informes históricos no se alteraron. Se usaron contextos ANTLR con anotaciones simples (`tipo_kipu`, `simbolo`) en lugar de otro AST. Los montos se mantienen en `i64` de céntimos; `double` solo interviene en cálculos de tasa decimal y operaciones del tipo decimal. Se conservaron los códigos de error semántico para facilitar la comparación con Hito 2.

## 10. Limitaciones y revisión humana

- Una regla declarada dentro de un bloque no se genera en LLVM y recibe `GEN-01`; las reglas globales sí funcionan.
- No se probó `runtime/kipu_runtime.c` con Clang en Windows ni Linux. La entrada en C necesita una revisión de validación y memoria antes de usarla como evidencia de entrega.
- Falta obtener y cotejar la consigna oficial, rúbrica, límites de páginas, formato de informe y reglas sobre autoría y herramientas. Los archivos Markdown son borradores de contenido, no se presentan como PDF o PPTX finales.
- El equipo debe revisar el contenido, confirmar contribuciones individuales, grabar cualquier video exigido, ejecutar la prueba nativa y enviar los archivos a la plataforma universitaria. Este trabajo no atribuye esas acciones a integrantes concretos.
- Los commits de desarrollo permanecen locales en `cambios-Luciano`; solo se publicó la rama vacía inicial según la autorización recibida.
