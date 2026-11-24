# Kipu: informe técnico del Hito 3

**Estado:** borrador técnico para revisión del equipo, 24 de noviembre de 2026. No se localizó en el repositorio la consigna oficial ni la rúbrica del Hito 3; el formato y la extensión finales requieren cotejo con esos documentos.

## 1. Problema y objetivo

Kipu permite expresar cálculos tributarios en español con tipos de dinero, porcentajes y monedas. El compilador rechaza operaciones incompatibles antes de generar código. La meta del Hito 3 es completar la traducción a LLVM IR y validar su ejecución. La refactorización atiende la observación del profesor: conectar el Visitor generado por ANTLR con `IRBuilder` de manera visible y facilitar la explicación de las clases.

## 2. Lenguaje y gramática

La fuente vigente es `grammar/Kipu.g4`. Contiene declaraciones `var` y `const`, asignaciones, expresiones con precedencia, bloques, `si`/`sino`, `mientras`, `para`, reglas con parámetros y retorno, llamadas, `leer`, `mostrar` y `convertir`. Los tipos son `entero`, `decimal`, `porcentaje`, `booleano`, `texto` y `monto<M>` para PEN, USD y EUR. No se alteró la gramática durante esta fase. Los archivos generados de ANTLR 4.13.2 están en `src/generated/`.

El lexer reconoce palabras reservadas, identificadores, literales, operadores y comentarios de línea. El parser devuelve el árbol de contextos de ANTLR. La gramática mantiene los lineamientos L1 a L6 que verifica `scripts/verificar_gramatica.py`; `scripts/derivaciones.py` comprobó 28 derivaciones.

## 3. Arquitectura

```mermaid
flowchart LR
    K[Fuente .kp] --> L[KipuLexer]
    L --> P[KipuParser]
    P --> A[Árbol ANTLR]
    A --> S[VisitorSemantico]
    S -->|sin errores| V[LLVMVisitor e IRBuilder]
    V --> IR[LLVM IR]
    IR --> C[Verificador LLVM]
    C --> J[JIT MCJIT]
```

`src/kipu.py` muestra cada fase. `VisitorSemantico` y `LLVMVisitor` heredan directamente de `KipuVisitor`. La tabla de símbolos está en `src/tabla_simbolos.py`; los tipos, en `src/tipos_kipu.py`. El Visitor semántico anota cada contexto relevante con `tipo_kipu` o `simbolo`. El Visitor LLVM consulta esas anotaciones y emite IR con `self.builder`, una instancia de `ir.IRBuilder`. No se construye un AST propio. Los cuatro módulos de la arquitectura anterior fueron retirados del código vigente; el historial Git los conserva.

En `LLVMVisitor.visitDeclaracion`, `self.builder.store` inicializa la variable. `visitAsignacion` combina `load`, operación y `store`. Los métodos de expresiones usan operaciones enteras o decimales según el tipo. `visitSeleccion` e `visitIteracion` crean bloques y saltos. `visitRegla` crea el cuerpo de la función; `visitLlamada` emite `call`; `visitRetorno` emite `ret` o `ret_void`. La entrada y la salida llaman al runtime.

## 4. Análisis semántico

`VisitorSemantico` mantiene ámbitos anidados y símbolos con nombre, categoría, tipo, ubicación y tipos de parámetros. Registra las reglas globales antes de recorrer las sentencias para permitir llamadas adelantadas. Conserva los códigos SEM-01 a SEM-14 del Hito 2: no declarado, redeclarado, monedas y tipos incompatibles, constante modificada, condición no booleana, retorno fuera de regla o incompatible, número y tipo de argumentos, retorno ausente, porcentaje fuera de rango, división literal por cero y uso de regla sin valor en expresión. Los errores incluyen línea y columna. Si hay un error léxico, sintáctico o semántico, `src/kipu.py` no inicia la generación LLVM.

## 5. Tipos en LLVM

| Tipo Kipu | Tipo LLVM | Representación |
|---|---|---|
| entero | i64 | entero con signo |
| decimal | double | punto flotante de doble precisión |
| porcentaje | i64 | fracción multiplicada por 10 000; `18%` = `1800` |
| monto<M> | i64 | céntimos; `249.90 PEN` = `24990` |
| booleano | i1 | 0 o 1 |
| texto | i8* | UTF-8 terminado en cero |

La suma y resta de montos operan con enteros exactos. La multiplicación por porcentajes usa `kipu.div_redondeo`, que redondea a céntimos con la regla half-up. Las operaciones que pasan por `double`, como conversión por una tasa decimal, se redondean al regresar a céntimos. Los montos de monedas distintas requieren `convertir` explícito.

## 6. Generación y ejecución

El Hito 3 añade reglas con y sin retorno, parámetros, llamadas, recursión, `leer` y concatenación de textos a las operaciones, decisiones, ciclos y salida ya existentes. `src/ejecutor.py` registra funciones de entrada y salida para el JIT con `ctypes`; `runtime/kipu_runtime.c` provee equivalentes para un ejecutable nativo. `src/kipu.py` verifica el módulo con LLVM antes de escribir el archivo `.ll` o ejecutarlo. La ejecución nativa con Clang quedó sin comprobar en esta máquina porque `clang` no estaba disponible en PATH.

## 7. Plan y resultados de validación

1. Ejecutar `python scripts/verificar_gramatica.py` y `python scripts/derivaciones.py`.
2. Ejecutar `python -m unittest discover -s tests -v`.
3. Generar y verificar LLVM IR de todos los casos de `tests/llvm`.
4. Ejecutar por JIT los programas válidos y comparar la salida con `.esperado`.
5. Ejecutar `ejemplos/visitor_builder.kp` y `ejemplos/hito3_tributario.kp` en PowerShell.

Resultados medidos en Windows 11 con Python 3.12.7, ANTLR runtime 4.13.2 y llvmlite 0.50.0: línea base Hito 2, 20/20 pruebas; versión refactorizada, 28/28; verificación L1 a L6 aprobada; 28 derivaciones sin fallo. Con entrada `3`, el programa tributario mostró `884.64 PEN` y `235.93 USD`. El ejemplo mínimo mostró `22`. Los casos LLVM de prueba pasaron por el verificador y JIT. La validación nativa con Clang no se ejecutó.

## 8. Conclusiones y límites

La conexión directa entre el árbol de ANTLR y `IRBuilder` quedó visible en métodos `visit` explícitos. Los 14 códigos semánticos conservaron su cobertura y las pruebas pasaron tras la migración. La representación entera de montos mantiene el cálculo de céntimos y el redondeo previsto.

El generador admite reglas globales; una regla declarada dentro de un bloque produce `GEN-01` con explicación. La entrada nativa en C no tiene la misma validación de texto que el JIT de Python y aún necesita prueba con Clang. El equipo debe cotejar este informe con la consigna, la rúbrica, el límite de páginas, las reglas de autoría y el formato de entrega oficiales antes de presentarlo. Las contribuciones individuales del Hito 3 requieren confirmación humana.
