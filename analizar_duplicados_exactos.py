#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el inventario de duplicados exactos del directorio dataset."""

import csv
import hashlib
import re
from collections import defaultdict
from pathlib import Path

PROJECT = Path(__file__).resolve().parent
DATASET_DIR = PROJECT / "dataset"
OUTPUT = PROJECT / "dataset/metadata/duplicados_exactos.csv"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".jfif", ".avif", ".svg"}
ID_PATTERN = re.compile(r"^(\d+)$")
FIELDS = ["grupo_duplicado", "archivo", "ruta", "tamaño_bytes", "hash", "posible_id_EXIST"]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def possible_id(path):
    match = ID_PATTERN.fullmatch(path.stem)
    return match.group(1) if match else ""


def main():
    images = sorted(
        path for path in DATASET_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )
    by_hash = defaultdict(list)
    for path in images:
        by_hash[sha256(path)].append(path)

    duplicate_hashes = sorted((digest, paths) for digest, paths in by_hash.items() if len(paths) > 1)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    same_id_groups = 0
    different_id_groups = 0
    unclear_files = []
    redundant_same_id = []

    for group_number, (digest, paths) in enumerate(duplicate_hashes, 1):
        ids = {possible_id(path) for path in paths}
        if "" in ids:
            unclear_files.extend(path for path in paths if not possible_id(path))
        if len(ids) == 1 and "" not in ids:
            same_id_groups += 1
            redundant_same_id.extend(paths[1:])
        else:
            different_id_groups += 1
        for path in sorted(paths):
            rows.append({
                "grupo_duplicado": f"DUP-{group_number:03d}",
                "archivo": path.name,
                "ruta": path.relative_to(PROJECT).as_posix(),
                "tamaño_bytes": path.stat().st_size,
                "hash": digest,
                "posible_id_EXIST": possible_id(path),
            })

    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    duplicate_files = len(rows)
    redundant_copies = duplicate_files - len(duplicate_hashes)
    print(f"Imágenes analizadas: {len(images)}")
    print(f"Grupos duplicados exactos: {len(duplicate_hashes)}")
    print(f"Archivos involucrados: {duplicate_files}")
    print(f"Copias redundantes dentro de grupos: {redundant_copies}")
    print(f"Grupos con el mismo ID: {same_id_groups}")
    print(f"Grupos con IDs diferentes: {different_id_groups}")
    print(f"Archivos sin posible ID claro: {len(unclear_files)}")
    print(f"Archivos potencialmente redundantes por mismo contenido e ID: {len(redundant_same_id)}")
    print(f"Informe: {OUTPUT}")


if __name__ == "__main__":
    main()
