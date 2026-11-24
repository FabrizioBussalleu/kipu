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

## Requisitos

- Python 3.10 o superior
- `antlr4-python3-runtime==4.13.2` y `llvmlite` (ver `requirements.txt`). El parser ya está generado en `src/generated`, así que no se necesita Java para usar el compilador.
- Opcional: Java 11+ para regenerar el parser; clang para generar ejecutables nativos.

## Instalación

En PowerShell (Windows 11):

```powershell
cd kipu
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Uso

```powershell
.\.venv\Scripts\python.exe src/kipu.py ejemplos/facturacion.kp                 # front end completo
.\.venv\Scripts\python.exe src/kipu.py ejemplos/facturacion.kp --tokens        # tabla de tokens (léxico)
.\.venv\Scripts\python.exe src/kipu.py ejemplos/facturacion.kp --arbol         # árbol sintáctico
.\.venv\Scripts\python.exe src/kipu.py ejemplos/facturacion.kp --simbolos      # tabla de símbolos
.\.venv\Scripts\python.exe src/kipu.py ejemplos/detracciones.kp --llvm         # genera ejemplos/detracciones.ll
.\.venv\Scripts\python.exe src/kipu.py ejemplos/detracciones.kp --ejecutar     # genera el IR y lo ejecuta (JIT)
.\.venv\Scripts\python.exe src/kipu.py ejemplos/visitor_builder.kp --ejecutar
'3' | .\.venv\Scripts\python.exe src/kipu.py ejemplos/hito3_tributario.kp --ejecutar
```

Opciones adicionales: `--solo-lexico` y `--solo-sintactico`. El programa devuelve 0 si no hay errores y 1 si los hay.

Ejecutable nativo (opcional, requiere Clang): `clang ejemplos/detracciones.ll runtime/kipu_runtime.c -o detracciones.exe`. En la validación local de Windows de esta rama Clang no estaba disponible, por lo que ese comando no se verificó.

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
| GEN-01 | Generación | Fallo de generación LLVM (incluye reglas locales) |

## Gramática

`grammar/Kipu.g4` sigue la forma estándar del curso: todo símbolo es un token con nombre, no se usan `?`, `*`, `+` ni subreglas agrupadas (listas y opcionales con recursión y alternativa vacía, también en el lexer con fragments recursivos), la precedencia se define por niveles y no hay comentario de bloque. Se verifica con:

```powershell
.\.venv\Scripts\python.exe scripts/verificar_gramatica.py     # lineamientos L1 a L6
.\.venv\Scripts\python.exe scripts/gramatica_bnf.py           # imprime la gramática en notación de producciones
.\.venv\Scripts\python.exe scripts/derivaciones.py            # 28 derivaciones más a la izquierda verificadas
```

## Pruebas

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Cada archivo `.kp` de `tests/` declara en su primera línea el resultado esperado, por ejemplo `// espera: OK` o `// espera: SEM-03@4 SEM-03@5` (código@línea). Las pruebas de `tests/llvm` comparan la salida de la ejecución JIT con su archivo `.esperado`. GitHub Actions corre todo en Ubuntu y Windows en cada push (`.github/workflows/pruebas.yml`).
