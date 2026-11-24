/*
 * Runtime de Kipu para ejecutables nativos.
 * Implementa las funciones de salida que invoca el LLVM IR generado por src/generador_llvm.py.
 * Su formato es idéntico al del runtime JIT (src/ejecutor.py).
 *
 * Compilación nativa (requiere clang):
 *   python src/kipu.py programa.kp --llvm programa.ll
 *   clang programa.ll runtime/kipu_runtime.c -o programa
 */
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static const char *MONEDAS[] = {"PEN", "USD", "EUR"};

void kipu_imprimir_entero(int64_t v) { printf("%lld", (long long)v); }

void kipu_imprimir_decimal(double x) {
    char buf[64];
    snprintf(buf, sizeof buf, "%.6f", x);
    size_t n = strlen(buf);
    while (n > 0 && buf[n - 1] == '0') buf[--n] = '\0';
    if (n > 0 && buf[n - 1] == '.') { buf[n] = '0'; buf[n + 1] = '\0'; }
    fputs(buf, stdout);
}

void kipu_imprimir_monto(int64_t centimos, int32_t moneda) {
    int64_t c = centimos < 0 ? -centimos : centimos;
    printf("%s%lld.%02lld %s", centimos < 0 ? "-" : "", (long long)(c / 100), (long long)(c % 100), MONEDAS[moneda]);
}

void kipu_imprimir_porcentaje(int64_t v) {
    int64_t a = v < 0 ? -v : v;          /* fracción x 10^4: 1800 -> 18%, 1250 -> 12.5% */
    int64_t entero = a / 100, resto = a % 100;
    if (resto == 0) {
        printf("%s%lld%%", v < 0 ? "-" : "", (long long)entero);
    } else if (resto % 10 == 0) {
        printf("%s%lld.%lld%%", v < 0 ? "-" : "", (long long)entero, (long long)(resto / 10));
    } else {
        printf("%s%lld.%02lld%%", v < 0 ? "-" : "", (long long)entero, (long long)resto);
    }
}

void kipu_imprimir_booleano(int32_t b) { fputs(b ? "verdadero" : "falso", stdout); }
void kipu_imprimir_texto(const char *s) { fputs(s, stdout); }
void kipu_imprimir_separador(void) { putchar(' '); }
void kipu_imprimir_fin_linea(void) { putchar('\n'); }
int32_t kipu_texto_igual(const char *a, const char *b) { return strcmp(a, b) == 0; }

char *kipu_texto_concatenar(const char *a, const char *b) {
    size_t tam = strlen(a) + strlen(b) + 1;
    char *resultado = malloc(tam);
    if (!resultado) { fputs("Sin memoria para texto Kipu\n", stderr); exit(1); }
    strcpy(resultado, a);
    strcat(resultado, b);
    return resultado;
}

static void kipu_linea(char *texto, size_t capacidad) {
    if (!fgets(texto, (int)capacidad, stdin)) {
        fputs("Error al leer entrada Kipu\n", stderr);
        exit(1);
    }
    texto[strcspn(texto, "\r\n")] = '\0';
}

int64_t kipu_leer_entero(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    return (int64_t)strtoll(texto, NULL, 10);
}
double kipu_leer_decimal(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    return strtod(texto, NULL);
}
int64_t kipu_leer_monto(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    double escalado = strtod(texto, NULL) * 100.0;
    return (int64_t)(escalado >= 0 ? escalado + 0.5 : escalado - 0.5);
}
int64_t kipu_leer_porcentaje(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    double escalado = strtod(texto, NULL) * 100.0;
    return (int64_t)(escalado >= 0 ? escalado + 0.5 : escalado - 0.5);
}
int32_t kipu_leer_booleano(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    return strcmp(texto, "verdadero") == 0;
}
char *kipu_leer_texto(void) {
    char texto[4096]; kipu_linea(texto, sizeof texto);
    size_t tam = strlen(texto) + 1;
    char *resultado = malloc(tam);
    if (!resultado) { fputs("Sin memoria para texto Kipu\n", stderr); exit(1); }
    memcpy(resultado, texto, tam);
    return resultado;
}
