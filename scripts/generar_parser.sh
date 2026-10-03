#!/usr/bin/env sh
# Regenera el parser de Kipu para Python a partir de grammar/Kipu.g4 (requiere Java 11+)
cd "$(dirname "$0")/.." || exit 1
java -jar lib/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/generated -Xexact-output-dir grammar/Kipu.g4 && echo "Parser generado en src/generated"
