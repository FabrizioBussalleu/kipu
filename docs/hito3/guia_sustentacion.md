# Guía de sustentación de Kipu

## Recorrido del compilador

1. El lexer generado de `grammar/Kipu.g4` transforma caracteres en tokens: `VAR`, `ID`, `NUM_DECIMAL`, `MONEDA`, etc. `src/kipu.py:compilar` crea `KipuLexer` y `CommonTokenStream`.
2. `KipuParser.programa()` aplica la gramática y crea contextos como `DeclaracionContext` y `AritmeticaContext`. Ese árbol conserva la estructura del programa.
3. `src/visitor_semantico.py:VisitorSemantico.visitPrograma` registra las reglas globales y visita las sentencias. `visitDeclaracion` agrega símbolos; `visitPrimario` resuelve identificadores; `_tipo_binario` comprueba operaciones. `src/tabla_simbolos.py:Ambito.buscar` recorre el ámbito actual y sus padres.
4. Si no hay errores, `src/visitor_llvm.py:LLVMVisitor.visitPrograma` crea `main`, un bloque de entrada y un `ir.IRBuilder`. Cada método `visit` recibe un contexto ANTLR, lee su tipo o símbolo y llama al builder.
5. `src/ejecutor.py:verificar_ir` pide a LLVM que compruebe el módulo. `ejecutar` compila el IR en memoria con MCJIT y ejecuta `main`.

## Del programa a LLVM IR

Programa `ejemplos/visitor_builder.kp`:

```kipu
var base: entero = 20;
base += 2;
mostrar(base);
```

`visitDeclaracion` crea almacenamiento `i64` y guarda 20. `visitAsignacion` carga el valor, usa `builder.add` con 2 y guarda 22. `visitEntradaSalida` llama a `kipu_imprimir_entero`. LLVM verifica el módulo y el JIT imprime `22`. Para ver el IR, ejecutar `python src/kipu.py ejemplos/visitor_builder.kp --llvm` y buscar `load`, `add`, `store` y `call`.

## Conceptos para explicar

- **Visitor:** clase que recorre los contextos del parser; ANTLR elige `visitDeclaracion`, `visitSeleccion` y los demás métodos según la regla gramatical.
- **IRBuilder:** objeto de llvmlite que agrega instrucciones al bloque LLVM actual. Se crea en `LLVMVisitor` y aparece en los métodos `visit`.
- **Tabla de símbolos:** diccionario por ámbito que asocia nombres a tipo, categoría y posición. Al entrar en un bloque se abre un ámbito y al salir se cierra.
- **Variable:** `alloca` para locales o variable global LLVM para símbolos globales, luego `store` y `load`.
- **Expresión:** los métodos de precedencia `visitExpresion` a `visitTermino` visitan izquierda y derecha y eligen operaciones enteras, decimales o monetarias.
- **Condicional:** `visitSeleccion` crea bloques para la condición, cada rama y el final; usa `cbranch` y `branch`.
- **Ciclos:** `visitIteracion` crea bloques de condición, cuerpo y salida para `mientras` y `para`.
- **Función:** `visitRegla` crea `ir.Function`, asigna parámetros a variables locales y termina con `ret` o `ret_void`; `visitLlamada` emite `call`.
- **Dinero:** `monto<PEN>` se guarda en céntimos `i64`; `18%` se guarda como 1800; `kipu.div_redondeo` aplica half-up.
- **Entrada y salida:** `leer` y `mostrar` generan llamadas al runtime de Python en JIT o al runtime C para ejecutable nativo.

## Preguntas probables

**¿Por qué dos Visitors?** El semántico determina si las operaciones tienen sentido y anota tipos y símbolos. El Visitor LLVM solo se ejecuta si el árbol es válido; así no tiene que decidir nuevamente si una suma mezcla monedas.

**¿Dónde está la conexión Visitor con Builder?** En `LLVMVisitor.visitAsignacion`: se visita la expresión, se carga la variable cuando corresponde y se llama a `self.builder.store`. La misma relación aparece en `visitSeleccion` con `cbranch`.

**¿Por qué no hay AST propio?** Los contextos de ANTLR contienen la estructura necesaria. Los Visitors recorren directamente ese árbol y comparten anotaciones pequeñas, sin transformar el programa en otra jerarquía de nodos.

**¿Cómo se evitan errores de céntimos?** Los montos se almacenan como enteros en céntimos. La multiplicación por porcentaje divide con redondeo half-up. Las conversiones con tasa decimal sí usan `double` de forma intermedia y vuelven a céntimos con redondeo.

**¿Qué pasa con un error semántico?** `compilar` conserva el código y la ubicación del error y detiene el proceso antes de crear LLVM IR.

**¿Qué falta validar?** Clang no estaba disponible en el Windows de esta revisión. También hace falta contrastar la entrega con la consigna oficial y confirmar aportes individuales.
