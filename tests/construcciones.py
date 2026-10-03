"""Construcciones del lenguaje Kipu con 5 ejemplos cada una.

Fuente única: las pruebas sintácticas (test_kipu.py), las derivaciones más a la
izquierda (scripts/derivaciones.py) y el informe usan estos mismos ejemplos.

Cada construcción indica la regla inicial de ANTLR con la que se valida y el
símbolo inicial de la gramática libre de contexto del informe.
"""

CONSTRUCCIONES = [
    {
        "id": "G1",
        "nombre": "Declaración de variables y constantes",
        "regla_antlr": "declaracion",
        "simbolo": "decl",
        "ejemplos": [
            "var cantidad: entero = 3;",
            "const IGV: porcentaje = 18%;",
            "var subtotal: monto<PEN> = 1250.50 PEN;",
            'var razonSocial: texto = "Elaris SAC";',
            "var esAgenteRetencion: booleano;",
        ],
        "derivar": [0, 1, 2, 4],
    },
    {
        "id": "G2",
        "nombre": "Asignación",
        "regla_antlr": "asignacion",
        "simbolo": "asig",
        "ejemplos": [
            "cantidad = 5;",
            "subtotal = precio * cantidad;",
            "total += igv;",
            "saldo -= 150.00 PEN;",
            "exonerado = falso;",
        ],
        "derivar": [0, 1, 2, 3],
    },
    {
        "id": "G3",
        "nombre": "Expresiones aritméticas, monetarias, relacionales y lógicas",
        "regla_antlr": "expresion",
        "simbolo": "expr",
        "ejemplos": [
            "precio * cantidad + flete",
            "base * 18%",
            "(total - detraccion) / 2",
            "total >= 700.00 PEN y no exonerado",
            "convertir(neto, USD, 3.75)",
        ],
        "derivar": [0, 2, 3, 4],
    },
    {
        "id": "G4",
        "nombre": "Sentencias selectivas",
        "regla_antlr": "seleccion",
        "simbolo": "sel",
        "ejemplos": [
            "si (total > 700.00 PEN) { detraccion = total * 12%; }",
            "si (esExportacion) { igv = 0.00 PEN; } sino { igv = base * 18%; }",
            "si (tipo == 1) { tasa = 12%; } sino si (tipo == 2) { tasa = 10%; } sino { tasa = 4%; }",
            'si (no pagado y diasAtraso > 30) { mostrar("Factura vencida"); }',
            "si (saldo <= 0.00 PEN) { cancelado = verdadero; } sino { saldo -= cuota; }",
        ],
        "derivar": [0, 1, 2, 3],
    },
    {
        "id": "G5",
        "nombre": "Sentencias iterativas",
        "regla_antlr": "iteracion",
        "simbolo": "iter",
        "ejemplos": [
            "mientras (saldo > 0.00 PEN) { saldo -= cuota; }",
            "para mes desde 1 hasta 12 { total += cuota; }",
            "para i desde 1 hasta n paso 2 { mostrar(i); }",
            "mientras (intentos < 3 y no validado) { intentos += 1; }",
            "para anio desde 2020 hasta 2026 { si (anio mod 4 == 0) { dias = 366; } }",
        ],
        "derivar": [0, 1, 2, 3],
    },
    {
        "id": "G6",
        "nombre": "Reglas (funciones), retorno y llamadas",
        "regla_antlr": "regla",
        "simbolo": "def_regla",
        "ejemplos": [
            "regla calcularIgv(base: monto<PEN>): monto<PEN> { retornar base * 18%; }",
            "regla esMayor(a: entero, b: entero): booleano { retornar a > b; }",
            'regla imprimirCabecera() { mostrar("FACTURA ELECTRONICA"); }',
            "regla cuota(total: monto<PEN>, n: entero): monto<PEN> { retornar total / n; }",
            "regla neto(total: monto<PEN>, tasa: porcentaje): monto<PEN> { retornar total - calcularDescuento(total, tasa); }",
        ],
        "derivar": [0, 1, 2, 3],
    },
    {
        "id": "G7",
        "nombre": "Entrada y salida",
        "regla_antlr": "entradaSalida",
        "simbolo": "es",
        "ejemplos": [
            'mostrar("Total:", total);',
            "mostrar(subtotal + igv);",
            "leer(cantidad);",
            'mostrar("IGV", calcularIgv(base), "Neto", neto);',
            "leer(precioUnitario);",
        ],
        "derivar": [0, 1, 2, 3],
    },
]
