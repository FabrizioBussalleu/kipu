# Propuesta para decidir el alcance de las reglas locales

**Estado:** propuesta para aprobación del equipo; no modifica el compilador ni la gramática.

La consigna oficial transcrita exige construcciones de lenguaje y generación de código final, pero no menciona reglas anidadas. Los cinco ejemplos G6 de `tests/construcciones.py` y los informes de Hitos 1 y 2 presentan reglas globales. Sin embargo, la gramática vigente permite que `regla` aparezca dentro de cualquier `bloque`, porque `sentencia` incluye `regla` y `bloque` contiene `listaSentencias`. El Visitor semántico acepta una regla local; `LLVMVisitor` devuelve `GEN-01` al generarla. Hay una diferencia real entre front end y back end.

Se propone que el equipo elija y documente una de estas decisiones:

1. **Restringir reglas al ámbito global.** Añadir una validación semántica explícita en `visitRegla` con un código nuevo, ubicación y mensaje en español; conservar la gramática o ajustarla solo si el docente lo pide. Actualizar pruebas y documentación. Esta opción simplifica LLVM, pero reduce el lenguaje que hoy acepta el parser y por eso requiere aprobación del equipo.
2. **Admitir reglas locales.** Definir el alcance exacto de captura de variables externas y generar funciones LLVM para ellas, con pruebas de ámbitos y llamadas. Esta opción amplía trabajo y debe elegirse si las reglas anidadas forman parte de la especificación acordada.

Hasta esa decisión, `GEN-01` sigue siendo el comportamiento explícito y probado para reglas locales. No se presenta esa construcción como cubierta por el back end. La recomendación técnica es la opción 1 si el equipo confirma que la especificación pretendía reglas globales; la consigna y los ejemplos disponibles no prueban por sí solos esa intención.
