# Kipu

**Kipu** es un lenguaje de dominio específico para escribir reglas tributarias y cálculos con montos monetarios (IGV, detracciones, conversiones de moneda) en español. Sus tipos `monto<PEN>`, `monto<USD>`, `monto<EUR>` y `porcentaje` son nativos: el compilador rechaza antes de ejecutar las operaciones sin sentido contable, como sumar soles con dólares, y el código generado opera con céntimos exactos.

Proyecto del curso **Teoría de Compiladores (1ACC0218)**, UPC, ciclo 2026-2, sección 4889.
Integrantes: Fabrizio Bussalleu Salcedo, Jose Luis Sancho Navarro y Marco Antonio Luciano Cabrera Díaz.

```kipu
const IGV: porcentaje = 18%;

regla calcularIgv(base: monto<PEN>): monto<PEN> {
    retornar base * IGV;
}

var subtotal: monto<PEN> = 250.00 PEN * 3;
var total: monto<PEN> = subtotal + calcularIgv(subtotal);
var enDolares: monto<USD> = convertir(total, USD, 0.2667);
```

## Estado

| Hito | Contenido | Estado |
|---|---|---|
| 1 | Analizadores léxico, sintáctico y semántico parcial en ANTLR4 | Entregado |
| 2 | Gramática actualizada (forma estándar), semántico completo (14 errores), arquitectura, plan de validación, avance de LLVM IR | Entregado |
| 3 | Generación de código completa con LLVM, resultados de la validación y conclusiones | Semana 15 |

## Requisitos

- Python 3.10 o superior
- `antlr4-python3-runtime==4.13.2` y `llvmlite` (ver `requirements.txt`). El parser ya está generado en `src/generated`, así que no se necesita Java para usar el compilador.
- Opcional: Java 11+ para regenerar el parser; clang para generar ejecutables nativos.

## Instalación

En PowerShell (Windows):

```powershell
cd kipu
python -m pip install -r requirements.txt
```

## Uso

```powershell
python src/kipu.py ejemplos/facturacion.kp                 # front end completo
python src/kipu.py ejemplos/facturacion.kp --tokens        # tabla de tokens (léxico)
python src/kipu.py ejemplos/facturacion.kp --arbol         # árbol sintáctico
python src/kipu.py ejemplos/facturacion.kp --simbolos      # tabla de símbolos
python src/kipu.py ejemplos/detracciones.kp --llvm         # genera ejemplos/detracciones.ll
python src/kipu.py ejemplos/detracciones.kp --ejecutar     # genera el IR y lo ejecuta (JIT)
```

Opciones adicionales: `--solo-lexico` y `--solo-sintactico`. El programa devuelve 0 si no hay errores y 1 si los hay.

Ejecutable nativo (opcional, requiere clang): `clang ejemplos/detracciones.ll runtime/kipu_runtime.c -o detracciones`.

### Códigos de error

| Código | Fase | Descripción |
|---|---|---|
| LEX-01 | Léxico | Símbolo no reconocido o cadena sin cerrar |
| SIN-01 | Sintáctico | Construcción inválida (mensaje de ANTLR traducido) |
| SEM-01 | Semántico | Identificador no declarado |
| SEM-02 | Semántico | Identificador redeclarado en el mismo ámbito |
| SEM-03 | Semántico | Monedas incompatibles |
| SEM-04 | Semántico | Tipos incompatibles |
| SEM-05 | Semántico | Modificación de una constante |
| SEM-06 | Semántico | Condición no booleana |
| SEM-07 | Semántico | `retornar` fuera de una regla |
| SEM-08 | Semántico | Valor de retorno incompatible |
| SEM-09 | Semántico | Número de argumentos incorrecto |
| SEM-10 | Semántico | Tipo de argumento incompatible |
| SEM-11 | Semántico | Regla que no retorna en todos los caminos |
| SEM-12 | Semántico | Porcentaje fuera de rango (0 % a 100 %) |
| SEM-13 | Semántico | División entre cero literal |
| SEM-14 | Semántico | Regla sin valor usada en una expresión |
| GEN-01 | Generación | Construcción cuya generación LLVM se completa en el Hito 3 |

## Gramática

`grammar/Kipu.g4` sigue la forma estándar del curso: todo símbolo es un token con nombre, no se usan `?`, `*`, `+` ni subreglas agrupadas (listas y opcionales con recursión y alternativa vacía, también en el lexer con fragments recursivos), la precedencia se define por niveles y no hay comentario de bloque. Se verifica con:

```powershell
python scripts/verificar_gramatica.py     # lineamientos L1 a L6
python scripts/gramatica_bnf.py           # imprime la gramática en notación de producciones
python scripts/derivaciones.py            # 28 derivaciones más a la izquierda verificadas
```

## Pruebas

```powershell
python -m unittest discover -s tests -v
```

Cada archivo `.kp` de `tests/` declara en su primera línea el resultado esperado, por ejemplo `// espera: OK` o `// espera: SEM-03@4 SEM-03@5` (código@línea). Las pruebas de `tests/llvm` comparan la salida de la ejecución JIT con su archivo `.esperado`. GitHub Actions corre todo en Ubuntu y Windows en cada push (`.github/workflows/pruebas.yml`).

## Estructura

```
kipu/
├── grammar/Kipu.g4               gramática ANTLR4 (lexer + parser) en forma estándar
├── src/
│   ├── kipu.py                   driver del compilador
│   ├── errores.py                errores léxicos y sintácticos en español
│   ├── ast_kipu.py               nodos del AST y tipos
│   ├── constructor_ast.py        árbol de ANTLR -> AST
│   ├── semantico.py              analizador semántico y tabla de símbolos
│   ├── generador_llvm.py         generación de LLVM IR (llvmlite)
│   ├── ejecutor.py               ejecución JIT y runtime de salida
│   └── generated/                parser generado por ANTLR 4.13.2 (Python3)
├── runtime/kipu_runtime.c        runtime para ejecutables nativos
├── ejemplos/                     facturacion.kp, detracciones.kp
├── tests/                        lexico, sintactico, semantico, llvm, construcciones.py, test_kipu.py
├── scripts/                      verificar_gramatica.py, gramatica_bnf.py, derivaciones.py, generar_parser.*
├── lib/antlr-4.13.2-complete.jar
├── .github/workflows/pruebas.yml integración continua
└── docs/
    ├── hito1/                    informe, anexo, presentación y guiones del Hito 1
    ├── hito2/                    informe, anexo, presentación, guiones y preguntas del Hito 2
    ├── anexo_derivaciones.md     derivaciones vigentes (generadas)
    └── derivaciones.json
```

## Entregables del Hito 2 (`docs/hito2/`)

- Informe: `2026-11-10_UPC_Kipu_Informe_Hito2_v1.0.pdf` (y `.docx`)
- Anexo A, derivaciones: `2026-11-10_UPC_Kipu_Anexo-Derivaciones_Hito2_v1.0.pdf` (y `.docx`)
- Presentación: `2026-11-10_UPC_Kipu_Presentacion_Hito2_v1.0.pdf` (y `.pptx` editable)
- Guion de la presentación, guion del video y preguntas probables

Entregables del Hito 1 (`docs/hito1/`): `Informe_TrabajoParcial_Kipu.pdf`, `Presentacion_Kipu.pdf` y el enlace al video en `Enlace_Video_Demo.txt`.
