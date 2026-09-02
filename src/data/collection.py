"""Funciones para cargar y organizar el dataset."""

from pathlib import Path
from typing import List


def list_image_files(dataset_dir: str) -> List[str]:
    """Devuelve la lista de imágenes en una carpeta."""
    root = Path(dataset_dir)
    return [str(path) for path in root.rglob("*.png") if path.is_file()] + [
        str(path) for path in root.rglob("*.jpg") if path.is_file()
    ]
