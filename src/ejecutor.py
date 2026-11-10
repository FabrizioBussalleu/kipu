"""Ejecución JIT del LLVM IR generado para Kipu, usando llvmlite (MCJIT).

Provee el runtime de salida (kipu_imprimir_*) como funciones de Python expuestas por ctypes,
de modo que el mismo IR funciona en Windows, Linux y macOS sin depender de printf.
Para un ejecutable nativo se usa runtime/kipu_runtime.c (Hito 3).
"""
from __future__ import annotations

import ctypes
import sys

import llvmlite.binding as llvm

MONEDAS = ["PEN", "USD", "EUR"]
_inicializado = False


def _inicializar() -> None:
    global _inicializado
    if _inicializado:
        return
    try:                       # llvmlite < 0.45 requiere initialize(); en versiones nuevas ya no existe
        llvm.initialize()
    except Exception:          # noqa: BLE001
        pass
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    _inicializado = True


# --- formato de valores (idéntico al de runtime/kipu_runtime.c) ----------------------
def formato_monto(centimos: int, moneda: int) -> str:
    signo = "-" if centimos < 0 else ""
    c = abs(centimos)
    return f"{signo}{c // 100}.{c % 100:02d} {MONEDAS[moneda]}"


def formato_porcentaje(valor: int) -> str:
    signo = "-" if valor < 0 else ""
    v = abs(valor)                       # fracción x 10^4: 1800 -> 18%, 1250 -> 12.5%
    entero, resto = divmod(v, 100)
    if resto == 0:
        return f"{signo}{entero}%"
    return f"{signo}{entero}.{resto:02d}".rstrip("0") + "%"


def formato_decimal(x: float) -> str:
    s = f"{x:.6f}".rstrip("0")
    return s + "0" if s.endswith(".") else s


class Runtime:
    """Implementa las funciones kipu_imprimir_* y acumula la salida."""

    def __init__(self, eco: bool = True):
        self.salida: list[str] = []
        self.eco = eco
        V = None
        fns = {
            "kipu_imprimir_entero": (ctypes.CFUNCTYPE(V, ctypes.c_int64), lambda v: self._w(str(v))),
            "kipu_imprimir_decimal": (ctypes.CFUNCTYPE(V, ctypes.c_double), lambda v: self._w(formato_decimal(v))),
            "kipu_imprimir_monto": (ctypes.CFUNCTYPE(V, ctypes.c_int64, ctypes.c_int32),
                                    lambda c, m: self._w(formato_monto(c, m))),
            "kipu_imprimir_porcentaje": (ctypes.CFUNCTYPE(V, ctypes.c_int64), lambda v: self._w(formato_porcentaje(v))),
            "kipu_imprimir_booleano": (ctypes.CFUNCTYPE(V, ctypes.c_int32),
                                       lambda v: self._w("verdadero" if v else "falso")),
            "kipu_imprimir_texto": (ctypes.CFUNCTYPE(V, ctypes.c_char_p), lambda s: self._w(s.decode("utf-8"))),
            "kipu_imprimir_separador": (ctypes.CFUNCTYPE(V), lambda: self._w(" ")),
            "kipu_imprimir_fin_linea": (ctypes.CFUNCTYPE(V), lambda: self._w("\n")),
            "kipu_texto_igual": (ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p),
                                 lambda a, b: int(a == b)),
        }
        self._refs = []                   # mantiene vivos los callbacks
        for nombre, (proto, fn) in fns.items():
            cb = proto(fn)
            self._refs.append(cb)
            llvm.add_symbol(nombre, ctypes.cast(cb, ctypes.c_void_p).value)

    def _w(self, texto: str) -> None:
        self.salida.append(texto)
        if self.eco:
            sys.stdout.write(texto)

    @property
    def texto(self) -> str:
        return "".join(self.salida)


def verificar_ir(codigo_ir: str):
    _inicializar()
    modulo = llvm.parse_assembly(codigo_ir)
    modulo.verify()
    return modulo


def ejecutar(codigo_ir: str, eco: bool = True) -> tuple[int, str]:
    """Compila el IR con MCJIT, ejecuta main() y devuelve (código de salida, salida estándar)."""
    _inicializar()
    runtime = Runtime(eco=eco)
    modulo = verificar_ir(codigo_ir)
    triple = llvm.get_process_triple()
    if sys.platform.startswith("win") and not triple.endswith("-elf"):
        triple += "-elf"          # MCJIT en Windows trabaja con objetos ELF en memoria
    modulo.triple = triple
    destino = llvm.Target.from_triple(triple).create_target_machine()
    with llvm.create_mcjit_compiler(modulo, destino) as motor:
        motor.finalize_object()
        motor.run_static_constructors()
        direccion = motor.get_function_address("main")
        main = ctypes.CFUNCTYPE(ctypes.c_int32)(direccion)
        codigo = main()
    return codigo, runtime.texto
