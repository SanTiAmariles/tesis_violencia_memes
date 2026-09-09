"""Funciones auxiliares para preparación de datos."""

from pathlib import Path


def ensure_directory(path: str) -> Path:
    """Crea un directorio y devuelve la ruta."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory
