"""Módulo para manejar anotaciones del dataset."""

from pathlib import Path
import json


def load_annotations(path: str):
    """Carga un archivo JSON de anotaciones."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_annotations(data, path: str):
    """Guarda anotaciones en JSON."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
