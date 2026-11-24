"""Crea un ZIP de entrega a partir de los archivos versionados y nuevos del proyecto."""
from pathlib import Path
import subprocess
import zipfile


RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "entregables" / "kipu_hito3.zip"
EXCLUIR = {".git", ".venv", "venv", "__pycache__", "entregables"}
SUFIJOS_PROHIBIDOS = {".pyc", ".ll", ".exe", ".tmp", ".log"}
NOMBRES_SENSIBLES = {".env", "credentials", "credentials.json", "id_rsa", "id_ed25519"}


def incluir(ruta: Path) -> bool:
    partes = set(ruta.parts)
    if partes & EXCLUIR:
        return False
    if ruta.suffix.lower() in SUFIJOS_PROHIBIDOS:
        return False
    if ruta.name.lower() in NOMBRES_SENSIBLES:
        return False
    return ruta.is_file()


def main():
    resultado = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=RAIZ, capture_output=True, check=True,
    )
    nombres = [Path(nombre.decode("utf-8")) for nombre in resultado.stdout.split(b"\0") if nombre]
    archivos = sorted((ruta for ruta in nombres if incluir(RAIZ / ruta)), key=str)
    DESTINO.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(DESTINO, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for ruta in archivos:
            zip_file.write(RAIZ / ruta, arcname=f"kipu/{ruta.as_posix()}")
    with zipfile.ZipFile(DESTINO) as zip_file:
        zip_file.testzip()
    print(f"ZIP verificado: {DESTINO} ({len(archivos)} archivos)")


if __name__ == "__main__":
    main()
