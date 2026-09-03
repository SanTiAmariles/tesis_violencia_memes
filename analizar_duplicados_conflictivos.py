#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analiza los duplicados exactos con etiquetas EXIST contradictorias."""

import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

PROJECT = Path(__file__).resolve().parent
DATASET = PROJECT / "dataset_exist2024_es_labeled.csv"
TRAINING = PROJECT / "dataset/raw/EXIST2021-2025_datasets/2024 EXIST/EXIST 2024 Memes Dataset/training/EXIST2024_training.json"
GOLD_HARD = PROJECT / "dataset/raw/EXIST2021-2025_datasets/2024 EXIST/evaluation/golds/EXIST2024_training_task4_gold_hard.json"
GOLD_SOFT = PROJECT / "dataset/raw/EXIST2021-2025_datasets/2024 EXIST/evaluation/golds/EXIST2024_training_task4_gold_soft.json"
IMAGE_DIR = TRAINING.parent / "memes"
OUTPUT = PROJECT / "dataset/metadata/duplicados_conflictivos_exist2024.csv"
SUMMARY = PROJECT / "dataset/metadata/resumen_duplicados_conflictivos.txt"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".jfif", ".avif", ".svg"}
FIELDS = ["grupo_duplicado", "id_exist", "imagen", "hash", "etiqueta_gold_hard", "gold_soft_yes", "gold_soft_no", "texto", "lang", "split", "recomendacion", "motivo"]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def image_by_id():
    result = {}
    for path in IMAGE_DIR.iterdir():
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS and re.fullmatch(r"\d+", path.stem):
            result[path.stem] = path
    return result


def soft_values(soft, id_exist):
    value = soft.get(id_exist, {})
    return value.get("YES", "") if isinstance(value, dict) else "", value.get("NO", "") if isinstance(value, dict) else ""


def main():
    with DATASET.open("r", encoding="utf-8-sig", newline="") as handle:
        dataset_rows = list(csv.DictReader(handle))
    with TRAINING.open("r", encoding="utf-8") as handle:
        training = json.load(handle)
    with GOLD_HARD.open("r", encoding="utf-8") as handle:
        hard_list = json.load(handle)
    with GOLD_SOFT.open("r", encoding="utf-8") as handle:
        soft_list = json.load(handle)

    ids = {row["id_EXIST"] for row in dataset_rows}
    hard = {str(item["id"]): item.get("value", "") for item in hard_list}
    soft = {str(item["id"]): item.get("value", {}) for item in soft_list}
    images = image_by_id()
    by_hash = defaultdict(list)
    for id_exist in ids:
        if id_exist in images:
            by_hash[sha256(images[id_exist])].append(id_exist)

    conflicts = []
    for digest, id_list in sorted(by_hash.items()):
        labels = {hard.get(id_exist, "") for id_exist in id_list}
        if len(id_list) < 2 or len(labels) < 2:
            continue
        conflicts.append((digest, sorted(id_list)))

    rows_by_id = {row["id_EXIST"]: row for row in dataset_rows}
    output_rows = []
    summary_rows = []
    for number, (digest, id_list) in enumerate(conflicts, 1):
        group = f"DUP-CONFLICT-{number:03d}"
        complete = all(id_exist in rows_by_id and id_exist in images and id_exist in hard and id_exist in soft for id_exist in id_list)
        recommendation = "CONSERVAR AMBOS" if complete else "REVISAR MANUALMENTE"
        reason = (
            "Hash idéntico entre IDs distintos; ambos registros tienen imagen, texto, idioma, split, "
            "gold_hard y gold_soft disponibles. No existe evidencia objetiva de que uno sea inválido; "
            "gold_soft documenta la distribución, pero no elimina la contradicción de gold_hard."
            if complete else
            "Falta información objetiva en al menos uno de los registros; no es posible decidir automáticamente."
        )
        summary_rows.append((group, id_list, recommendation))
        for id_exist in id_list:
            row = rows_by_id[id_exist]
            soft_yes, soft_no = soft_values(soft, id_exist)
            record = training.get(id_exist, {})
            output_rows.append({
                "grupo_duplicado": group,
                "id_exist": id_exist,
                "imagen": images[id_exist].name if id_exist in images else "",
                "hash": digest,
                "etiqueta_gold_hard": hard.get(id_exist, ""),
                "gold_soft_yes": soft_yes,
                "gold_soft_no": soft_no,
                "texto": record.get("text", row.get("texto", "")),
                "lang": record.get("lang", ""),
                "split": record.get("split", ""),
                "recomendacion": recommendation,
                "motivo": reason,
            })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(output_rows)

    manually_reviewed = sum(recommendation == "REVISAR MANUALMENTE" for _, _, recommendation in summary_rows)
    objectively_treated = len(summary_rows) - manually_reviewed
    lines = [
        "RESUMEN DE DUPLICADOS CONFLICTIVOS EXIST 2024",
        "===============================================",
        "",
        f"Número de grupos conflictivos: {len(summary_rows)}",
        f"Número total de IDs involucrados: {len(output_rows)}",
        f"Grupos con tratamiento objetivo posible: {objectively_treated}",
        f"Grupos que requieren revisión manual: {manually_reviewed}",
        "",
        "Recomendación general:",
        "Conservar ambos registros. Son IDs distintos con imágenes binarias idénticas,",
        "pero no hay evidencia objetiva para eliminar uno. La contradicción YES/NO de",
        "gold_hard debe conservarse y documentarse; gold_soft sirve como evidencia",
        "comparativa, no como reclasificación automática.",
        "",
        "Detalle por grupo:",
    ]
    for group, id_list, recommendation in summary_rows:
        labels = ", ".join(f"{id_exist}={hard.get(id_exist, '')}" for id_exist in id_list)
        lines.append(f"- {group}: IDs {', '.join(id_list)}; {labels}; {recommendation}")
    lines.extend([
        "",
        "Limitaciones:",
        "- El análisis compara hashes y metadatos; no interpreta el contenido de los memes.",
        "- No se modificaron imágenes, JSON ni dataset_exist2024_es_labeled.csv.",
    ])
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("GRUPOS CONFLICTIVOS EXIST 2024")
    print("=" * 72)
    print(f"{'Grupo':<22} {'IDs y gold_hard':<38} Recomendación")
    for group, id_list, recommendation in summary_rows:
        labels = " | ".join(f"{id_exist}:{hard.get(id_exist, '')}" for id_exist in id_list)
        print(f"{group:<22} {labels:<38} {recommendation}")
    print("=" * 72)
    print(f"Grupos: {len(summary_rows)} | IDs: {len(output_rows)} | Objetivos: {objectively_treated} | Manuales: {manually_reviewed}")
    print(f"CSV: {OUTPUT}")
    print(f"Resumen: {SUMMARY}")


if __name__ == "__main__":
    main()
