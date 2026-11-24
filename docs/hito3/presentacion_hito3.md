# Presentación final de Kipu

**Estado:** contenido de diapositivas para revisión del equipo. La consigna exige exportar la presentación final a PDF. El equipo debe preparar ese PDF, ensayar la exposición formal y confirmar que domina las preguntas; la rúbrica reserva evaluación para documentos, código, exposición e interrogación.

## 1. Kipu y el problema

Kipu expresa reglas tributarias con montos y monedas tipados. Una suma de PEN con USD se rechaza antes de ejecutar.

## 2. Lenguaje y ejemplo

Mostrar `monto<PEN>`, `porcentaje`, `convertir` y una regla `totalConIgv` del programa `ejemplos/hito3_tributario.kp`.

## 3. Arquitectura final

Fuente → lexer → parser → árbol ANTLR → Visitor semántico → Visitor LLVM con IRBuilder → IR verificado → JIT. Explicar que se retiró el AST propio tras la observación del profesor.

## 4. Semántica

Tabla de símbolos por ámbitos. Mostrar SEM-03 por monedas incompatibles y los otros códigos SEM-01 a SEM-14. Ningún error semántico produce IR.

## 5. Visitor e IRBuilder

Mostrar `ejemplos/visitor_builder.kp`. Señalar `LLVMVisitor.visitAsignacion` y el `load`, `add`, `store` del IR. Resultado JIT: `22`.

## 6. Dinero y LLVM

`249.90 PEN` → `i64 24990`; `18%` → `i64 1800`. Multiplicación y división con redondeo half-up. Tipos restantes: `i64`, `double`, `i1`, `i8*`.

## 7. Funciones, control y entrada

Explicar bloques de `si`, `mientras` y `para`; `ir.Function`, parámetros, `call` y `ret`; runtime para `leer` y `mostrar`.

## 8. Validación

20 pruebas iniciales, 29 finales; L1 a L6 aprobados; 28 derivaciones comprobadas; IR verificado y JIT en Windows. Programa con entrada 3: `884.64 PEN` y `235.93 USD`.

## 9. Límites y cierre

Clang no estaba disponible para probar el ejecutable nativo. Las reglas locales siguen fuera de la generación LLVM y su restricción semántica está propuesta para aprobación. Mostrar qué debe revisar y presentar personalmente el equipo: autoría, PDF final, video de hasta cinco minutos y respuestas técnicas.
