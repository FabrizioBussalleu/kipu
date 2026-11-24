/*
 * Runtime de Kipu para ejecutables nativos.
 * Implementa la entrada y salida que invoca src/visitor_llvm.py.
 *
 * Compilación nativa (requiere clang):
 *   python src/kipu.py programa.kp --llvm programa.ll
 *   clang programa.ll runtime/kipu_runtime.c -o programa
 */
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>

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

/* Los textos dinámicos permanecen vivos hasta que termina el programa. */
struct CadenaDinamica {
    char *datos;
    struct CadenaDinamica *siguiente;
};
static struct CadenaDinamica *cadenas = NULL;

static void liberar_cadenas(void) {
    while (cadenas != NULL) {
        struct CadenaDinamica *actual = cadenas;
        cadenas = actual->siguiente;
        free(actual->datos);
        free(actual);
    }
}

static char *nueva_cadena(size_t tam) {
    static int limpieza_registrada = 0;
    if (!limpieza_registrada) {
        if (atexit(liberar_cadenas) != 0) { fputs("Error de memoria Kipu\n", stderr); exit(1); }
        limpieza_registrada = 1;
    }
    struct CadenaDinamica *nodo = malloc(sizeof *nodo);
    if (nodo == NULL) { fputs("Sin memoria para texto Kipu\n", stderr); exit(1); }
    nodo->datos = malloc(tam);
    if (nodo->datos == NULL) { free(nodo); fputs("Sin memoria para texto Kipu\n", stderr); exit(1); }
    nodo->siguiente = cadenas;
    cadenas = nodo;
    return nodo->datos;
}

char *kipu_texto_concatenar(const char *a, const char *b) {
    size_t largo_a = strlen(a), largo_b = strlen(b);
    if (largo_a > SIZE_MAX - largo_b - 1) { fputs("Texto Kipu demasiado largo\n", stderr); exit(1); }
    char *resultado = nueva_cadena(largo_a + largo_b + 1);
    memcpy(resultado, a, largo_a);
    memcpy(resultado + largo_a, b, largo_b + 1);
    return resultado;
}

static void error_entrada(const char *detalle) {
    fprintf(stderr, "Entrada Kipu inválida: %s\n", detalle);
    exit(1);
}

static void kipu_linea(char *texto, size_t capacidad) {
    if (!fgets(texto, (int)capacidad, stdin)) error_entrada("no se recibió una línea");
    size_t largo = strcspn(texto, "\r\n");
    if (texto[largo] == '\0') {
        int caracter = getchar();
        if (caracter != '\n' && caracter != EOF) {
            while ((caracter = getchar()) != '\n' && caracter != EOF) { }
            error_entrada("línea demasiado larga");
        }
    }
    texto[largo] = '\0';
}

static void fin_numero(const char *fin) {
    while (isspace((unsigned char)*fin)) fin++;
    if (*fin != '\0') error_entrada("sobran caracteres después del número");
}

/* Conversión decimal exacta a centésimos con redondeo half-up. */
static int64_t leer_centesimos(const char *texto, int porcentaje) {
    const unsigned char *cursor = (const unsigned char *)texto;
    while (isspace(*cursor)) cursor++;
    int negativo = *cursor == '-';
    if (*cursor == '-' || *cursor == '+') cursor++;
    if (!isdigit(*cursor)) error_entrada("se esperaba un número decimal");
    int64_t unidades = 0;
    while (isdigit(*cursor)) {
        int digito = *cursor++ - '0';
        if (unidades > (INT64_MAX / 100 - digito) / 10) error_entrada("número fuera de rango");
        unidades = unidades * 10 + digito;
    }
    int centesimos = 0, tercer_decimal = 0, posicion = 0, decimal_no_cero = 0;
    if (*cursor == '.') {
        cursor++;
        if (!isdigit(*cursor)) error_entrada("faltan decimales");
        while (isdigit(*cursor)) {
            if (*cursor != '0') decimal_no_cero = 1;
            if (posicion == 0) centesimos += (*cursor - '0') * 10;
            if (posicion == 1) centesimos += *cursor - '0';
            if (posicion == 2) tercer_decimal = *cursor - '0';
            posicion++;
            cursor++;
        }
    }
    if (porcentaje && *cursor == '%') cursor++;
    while (isspace(*cursor)) cursor++;
    if (*cursor != '\0') error_entrada("sobran caracteres después del número");
    if (porcentaje && (negativo || unidades > 100 || (unidades == 100 && decimal_no_cero)))
        error_entrada("porcentaje fuera de 0 a 100");
    int redondeo = tercer_decimal >= 5;
    if (unidades > (INT64_MAX - centesimos - redondeo) / 100) error_entrada("número fuera de rango");
    int64_t valor = unidades * 100 + centesimos + redondeo;
    return negativo ? -valor : valor;
}

int64_t kipu_leer_entero(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    char *fin;
    errno = 0;
    long long valor = strtoll(texto, &fin, 10);
    if (errno == ERANGE || fin == texto) error_entrada("entero inválido o fuera de rango");
    fin_numero(fin);
    return (int64_t)valor;
}
double kipu_leer_decimal(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    char *fin;
    errno = 0;
    double valor = strtod(texto, &fin);
    if (errno == ERANGE || fin == texto || !isfinite(valor)) error_entrada("decimal inválido o fuera de rango");
    fin_numero(fin);
    return valor;
}
int64_t kipu_leer_monto(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    return leer_centesimos(texto, 0);
}
int64_t kipu_leer_porcentaje(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    return leer_centesimos(texto, 1);
}
int32_t kipu_leer_booleano(void) {
    char texto[256]; kipu_linea(texto, sizeof texto);
    if (strcmp(texto, "verdadero") == 0) return 1;
    if (strcmp(texto, "falso") == 0) return 0;
    error_entrada("se esperaba verdadero o falso");
    return 0;
}
char *kipu_leer_texto(void) {
    char texto[4096]; kipu_linea(texto, sizeof texto);
    size_t tam = strlen(texto) + 1;
    char *resultado = nueva_cadena(tam);
    memcpy(resultado, texto, tam);
    return resultado;
}
