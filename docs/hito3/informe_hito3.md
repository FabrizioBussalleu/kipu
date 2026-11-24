# Kipu: informe técnico del Hito 3

**Estado:** contenido técnico para revisión del equipo, 24 de noviembre de 2026. Se contrastó con la transcripción `PAUTAS_ENTREGA_FINAL.md` aportada por el estudiante; no se adjuntó el PDF original. La consigna exige presentación final en PDF y video de máximo cinco minutos. No fija límite independiente de páginas para el informe del Hito 3. La matriz detallada está en `docs/hito3/matriz_cumplimiento.md`.

## 1. Problema y objetivo

Kipu permite expresar cálculos tributarios en español con tipos de dinero, porcentajes y monedas. El compilador rechaza operaciones incompatibles antes de generar código. La meta del Hito 3 es completar la traducción a LLVM IR y validar su ejecución. La refactorización atiende la observación del profesor: conectar el Visitor generado por ANTLR con `IRBuilder` de manera visible y facilitar la explicación de las clases.

## 2. Lenguaje y gramática

La fuente vigente es `grammar/Kipu.g4`. Contiene declaraciones `var` y `const`, asignaciones, expresiones con precedencia, bloques, `si`/`sino`, `mientras`, `para`, reglas con parámetros y retorno, llamadas, `leer`, `mostrar` y `convertir`. Los tipos son `entero`, `decimal`, `porcentaje`, `booleano`, `texto` y `monto<M>` para PEN, USD y EUR. No se alteró la gramática durante esta fase. Los archivos generados de ANTLR 4.13.2 están en `src/generated/`.

El lexer reconoce palabras reservadas, identificadores, literales, operadores y comentarios de línea. El parser devuelve el árbol de contextos de ANTLR. La gramática mantiene los lineamientos L1 a L6 que verifica `scripts/verificar_gramatica.py`; `scripts/derivaciones.py` comprobó 28 derivaciones.

La consigna acumula los Hitos 1 y 2 en el informe final. La problemática, objetivos y siete construcciones se documentan aquí y en el anexo A. El anexo B contiene token y lexema. `docs/hito3/gramatica_bnf.txt` recoge las producciones por construcción; `docs/anexo_derivaciones.md` incorpora cuatro derivaciones más a la izquierda por cada G1–G7. El Hito 1 exigía al menos dos errores semánticos y el Hito 2 elevó el mínimo a seis; Kipu conserva catorce. La arquitectura y el plan de validación se actualizan en las secciones 3 y 7. El informe histórico del Hito 1 tiene 11 páginas, superior al límite de cinco más carátula de la consigna transcrita; se conserva sin alterarlo y se registra la discrepancia en la matriz.

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

Resultados medidos en Windows 11 con Python 3.12.7, ANTLR runtime 4.13.2 y llvmlite 0.50.0: línea base Hito 2, 20/20 pruebas; versión refactorizada, 29/29; verificación L1 a L6 aprobada; 28 derivaciones sin fallo. Con entrada `3`, el programa tributario mostró `884.64 PEN` y `235.93 USD`. El ejemplo mínimo mostró `22`. Los casos LLVM de prueba pasaron por el verificador y JIT. La validación nativa con Clang no se ejecutó.

## 8. Conclusiones y límites

La conexión directa entre el árbol de ANTLR y `IRBuilder` quedó visible en métodos `visit` explícitos. Los 14 códigos semánticos conservaron su cobertura y las pruebas pasaron tras la migración. La representación entera de montos mantiene el cálculo de céntimos y el redondeo previsto.

El generador admite reglas globales; una regla declarada dentro de un bloque produce `GEN-01` con explicación. `docs/hito3/propuesta_reglas_locales.md` plantea restringirlas semánticamente si el equipo aprueba ese alcance; no se cambió silenciosamente el lenguaje. La entrada y la memoria del runtime C se revisaron, pero aún necesitan compilación y ejecución con Clang para declararse verificadas. La consigna no exige EXE expresamente. La presentación PDF y el video final requieren producción y revisión directas de los integrantes. También deben verificar la autoría y consultar al docente qué asistencia externa está permitida; este informe no atribuye contribuciones individuales.

## Anexo A. Cinco ejemplos por construcción

Los 35 ejemplos siguientes se extraen de `tests/construcciones.py`, fuente usada por las pruebas del parser.

### G1. Declaración de variables y constantes

```kipu
var cantidad: entero = 3;
const IGV: porcentaje = 18%;
var subtotal: monto<PEN> = 1250.50 PEN;
var razonSocial: texto = "Elaris SAC";
var esAgenteRetencion: booleano;
```

### G2. Asignación

```kipu
cantidad = 5;
subtotal = precio * cantidad;
total += igv;
saldo -= 150.00 PEN;
exonerado = falso;
```

### G3. Expresiones aritméticas, monetarias, relacionales y lógicas

```kipu
precio * cantidad + flete
base * 18%
(total - detraccion) / 2
total >= 700.00 PEN y no exonerado
convertir(neto, USD, 3.75)
```

### G4. Sentencias selectivas

```kipu
si (total > 700.00 PEN) { detraccion = total * 12%; }
si (esExportacion) { igv = 0.00 PEN; } sino { igv = base * 18%; }
si (tipo == 1) { tasa = 12%; } sino si (tipo == 2) { tasa = 10%; } sino { tasa = 4%; }
si (no pagado y diasAtraso > 30) { mostrar("Factura vencida"); }
si (saldo <= 0.00 PEN) { cancelado = verdadero; } sino { saldo -= cuota; }
```

### G5. Sentencias iterativas

```kipu
mientras (saldo > 0.00 PEN) { saldo -= cuota; }
para mes desde 1 hasta 12 { total += cuota; }
para i desde 1 hasta n paso 2 { mostrar(i); }
mientras (intentos < 3 y no validado) { intentos += 1; }
para anio desde 2020 hasta 2026 { si (anio mod 4 == 0) { dias = 366; } }
```

### G6. Reglas (funciones), retorno y llamadas

```kipu
regla calcularIgv(base: monto<PEN>): monto<PEN> { retornar base * 18%; }
regla esMayor(a: entero, b: entero): booleano { retornar a > b; }
regla imprimirCabecera() { mostrar("FACTURA ELECTRONICA"); }
regla cuota(total: monto<PEN>, n: entero): monto<PEN> { retornar total / n; }
regla neto(total: monto<PEN>, tasa: porcentaje): monto<PEN> { retornar total - calcularDescuento(total, tasa); }
```

### G7. Entrada y salida

```kipu
mostrar("Total:", total);
mostrar(subtotal + igv);
leer(cantidad);
mostrar("IGV", calcularIgv(base), "Neto", neto);
leer(precioUnitario);
```

## Anexo B. Léxico en formato token y lexema

Esta tabla reproduce las reglas de token de `grammar/Kipu.g4`; las expresiones y fragments completos están en ese archivo.

| Token | Lexema o regla léxica |
|---|---|
| `VAR` | `'var'` |
| `CONST` | `'const'` |
| `ENTERO` | `'entero'` |
| `DECIMAL` | `'decimal'` |
| `PORCENTAJE` | `'porcentaje'` |
| `BOOLEANO` | `'booleano'` |
| `TEXTO` | `'texto'` |
| `MONTO` | `'monto'` |
| `MONEDA` | `'PEN' \| 'USD' \| 'EUR'` |
| `SI` | `'si'` |
| `SINO` | `'sino'` |
| `MIENTRAS` | `'mientras'` |
| `PARA` | `'para'` |
| `DESDE` | `'desde'` |
| `HASTA` | `'hasta'` |
| `PASO` | `'paso'` |
| `REGLA` | `'regla'` |
| `RETORNAR` | `'retornar'` |
| `MOSTRAR` | `'mostrar'` |
| `LEER` | `'leer'` |
| `CONVERTIR` | `'convertir'` |
| `Y` | `'y'` |
| `O` | `'o'` |
| `NO` | `'no'` |
| `VERDADERO` | `'verdadero'` |
| `FALSO` | `'falso'` |
| `MOD` | `'mod'` |
| `MAS_ASIG` | `'+='` |
| `MENOS_ASIG` | `'-='` |
| `IGUAL` | `'=='` |
| `DIFERENTE` | `'!='` |
| `MENOR_IGUAL` | `'<='` |
| `MAYOR_IGUAL` | `'>='` |
| `MENOR` | `'<'` |
| `MAYOR` | `'>'` |
| `ASIG` | `'='` |
| `SUMA` | `'+'` |
| `RESTA` | `'-'` |
| `MULT` | `'*'` |
| `DIV` | `'/'` |
| `PAR_IZQ` | `'('` |
| `PAR_DER` | `')'` |
| `LLAVE_IZQ` | `'{'` |
| `LLAVE_DER` | `'}'` |
| `PUNTO_COMA` | `';'` |
| `COMA` | `','` |
| `DOS_PUNTOS` | `':'` |
| `LIT_PORCENTAJE` | `DIGITOS '%' \| DIGITOS '.' DIGITOS '%'` |
| `NUM_DECIMAL` | `DIGITOS '.' DIGITOS` |
| `NUM_ENTERO` | `DIGITOS` |
| `CADENA` | `'"' CADENA_COLA '"'` |
| `ID` | `LETRA ID_COLA` |
| `COMENTARIO` | `'//' COMENTARIO_COLA -> skip` |
| `ESPACIO` | `BLANCO ESPACIO_COLA -> skip` |

## Anexo C. Gramática y derivaciones

La notación de producciones vigente se adjunta en `docs/hito3/gramatica_bnf.txt`. Las 28 derivaciones más a la izquierda de cuatro ejemplos por cada G1–G7 están en `docs/anexo_derivaciones.md`; `scripts/derivaciones.py` regeneró y verificó ese anexo. La fuente ejecutable sigue siendo `grammar/Kipu.g4`.
