# Kipu

**Kipu** es un lenguaje de dominio específico para escribir reglas tributarias y cálculos con montos monetarios (IGV, detracciones, conversiones de moneda) en español. Sus tipos `monto<PEN>`, `monto<USD>`, `monto<EUR>` y `porcentaje` son nativos, de modo que el compilador rechaza antes de ejecutar operaciones sin sentido contable, como sumar soles con dólares.

Proyecto del curso **Teoría de Compiladores (1ACC0218)**, UPC, ciclo 2026-2.

```kipu
const IGV: porcentaje = 18%;

regla calcularIgv(base: monto<PEN>): monto<PEN> {
    retornar base * IGV;
}

var subtotal: monto<PEN> = 250.00 PEN * 3;
var total: monto<PEN> = subtotal + calcularIgv(subtotal);
var enDolares: monto<USD> = convertir(total, USD, 3.75);
```

## Estado

| Hito | Contenido | Estado |
|---|---|---|
| 1 | Analizadores léxico, sintáctico y semántico parcial (5 errores) en ANTLR4 | Entregado |
| 2 | Analizador semántico completo (6 o más errores), arquitectura, plan de validación | Pendiente (semana 12) |
| 3 | Generación de código con LLVM (montos como `i64` en céntimos) | Pendiente (semana 15) |

## Requisitos

- Python 3.10 o superior
- `antlr4-python3-runtime==4.13.2` (el parser ya está generado en `src/generated`, no se necesita Java para usarlo)
- Opcional: Java 11+ para regenerar el parser, y `lark` para regenerar las derivaciones

## Instalación

En PowerShell (Windows):

```powershell
cd kipu
python -m pip install -r requirements.txt
```

## Uso

```powershell
python src/kipu.py ejemplos/facturacion.kp
python src/kipu.py ejemplos/facturacion.kp --tokens      # tabla de tokens (analizador léxico)
python src/kipu.py ejemplos/facturacion.kp --arbol       # árbol sintáctico
python src/kipu.py ejemplos/facturacion.kp --simbolos    # tabla de símbolos
python src/kipu.py tests/semantico/invalidos/06_errores_multiples.kp
```

Opciones adicionales: `--solo-lexico` y `--solo-sintactico` detienen el proceso en esa fase. El programa devuelve código de salida 0 si no hay errores y 1 si los hay.

Formato de los errores: `[CÓDIGO] línea L:C  mensaje`.

| Código | Fase | Descripción |
|---|---|---|
| LEX-01 | Léxico | Símbolo no reconocido o cadena sin cerrar |
| SIN-01 | Sintáctico | Construcción inválida (mensaje de ANTLR traducido al español) |
| SEM-01 | Semántico | Identificador no declarado |
| SEM-02 | Semántico | Identificador redeclarado en el mismo ámbito |
| SEM-03 | Semántico | Monedas incompatibles |
| SEM-04 | Semántico | Tipos incompatibles |
| SEM-05 | Semántico | Modificación de una constante |

## Pruebas

```powershell
python -m unittest discover -s tests -v
```

Cada archivo `.kp` de `tests/` declara en su primera línea el resultado esperado, por ejemplo `// espera: OK` o `// espera: SEM-03@4 SEM-03@5` (código@línea). Los 35 ejemplos de las construcciones del informe están en `tests/construcciones.py` y se validan con la regla ANTLR correspondiente.

## Estructura

```
kipu/
├── grammar/Kipu.g4            gramática ANTLR4 (lexer + parser)
├── src/
│   ├── kipu.py                driver del compilador
│   ├── errores.py             listeners de errores léxicos y sintácticos
│   ├── semantico.py           analizador semántico y tabla de símbolos
│   └── generated/             parser generado por ANTLR 4.13.2 (Python3)
├── ejemplos/                  programas de demostración
├── tests/                     pruebas léxicas, sintácticas y semánticas
├── scripts/
│   ├── generar_parser.ps1     regenera src/generated (Windows)
│   ├── generar_parser.sh      regenera src/generated (Linux/macOS)
│   ├── gramatica_bnf.py       gramática BNF del informe (notación del curso)
│   └── derivaciones.py        genera y verifica las derivaciones más a la izquierda
├── lib/antlr-4.13.2-complete.jar
└── docs/                      informe, anexo de derivaciones, presentación y guion del video
```

## Regenerar el parser y las derivaciones

```powershell
powershell -ExecutionPolicy Bypass -File scripts/generar_parser.ps1
python -m pip install lark
python scripts/derivaciones.py
```

## Entregables del Hito 1

- Informe: `docs/2026-09-29_UPC_Kipu_Informe_Hito1_v1.0.pdf` (y `.docx` editable)
- Anexo A, derivaciones: `docs/2026-09-29_UPC_Kipu_Anexo-Derivaciones_Hito1_v1.0.pdf` (y `docs/anexo_derivaciones.md`)
- Presentación: `docs/2026-09-29_UPC_Kipu_Presentacion_Hito1_v1.0.pdf`
- Guion del video de demostración: `docs/guion_video_hito1.md`
