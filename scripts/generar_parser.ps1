# Regenera el parser de Kipu para Python a partir de grammar/Kipu.g4 (requiere Java 11+)
$raiz = Split-Path -Parent $PSScriptRoot
Set-Location $raiz
java -jar lib/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/generated -Xexact-output-dir grammar/Kipu.g4
if ($?) { Write-Host "Parser generado en src/generated" }
