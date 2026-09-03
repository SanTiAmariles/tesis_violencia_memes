#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Identifica candidatos potencialmente relacionados con contenido LGBTIQ+.

La salida es exploratoria: una coincidencia léxica no implica LGBTfobia,
violencia ni violencia simbólica. El CSV de entrada nunca se modifica.
"""

import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

PROJECT = Path(__file__).resolve().parent
INPUT_PATH = PROJECT / "dataset_exist2024_es_labeled.csv"
VOCAB_PATH = PROJECT / "vocabulario_lgbtiq_exploratorio.txt"
OUTPUT_PATH = PROJECT / "candidatos_lgbtiq_exist2024.csv"
FIELDS = ["id_EXIST", "texto", "imagen", "path_memes", "etiqueta_EXIST"]
OUTPUT_FIELDS = FIELDS + ["termino_detectado"]


def normalize(value):
    """Normaliza solo para comparar; conserva intactos los valores originales."""
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.casefold().replace("-", " ")
    return re.sub(r"\s+", " ", value).strip()


def load_vocabulary():
    terms = []
    normalized_terms = set()
    for raw_line in VOCAB_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("["):
            continue
        normalized_line = normalize(line)
        if normalized_line not in normalized_terms:
            terms.append(line)
            normalized_terms.add(normalized_line)
    return terms


def make_patterns(terms):
    patterns = []
    for term in terms:
        normalized_term = normalize(term)
        # \w boundaries avoid matching 'bi' inside 'bisexual', for example.
        pattern_text = re.escape(normalized_term).replace(r"\ ", r"\s+")
        patterns.append((term, re.compile(r"(?<!\w)" + pattern_text + r"(?!\w)")))
    return patterns


def shorten(text, length=220):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= length else text[: length - 3] + "..."


def main():
    terms = load_vocabulary()
    patterns = make_patterns(terms)
    with INPUT_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    candidates = []
    term_counts = Counter()
    for row in rows:
        normalized_text = normalize(row["texto"])
        found = [term for term, pattern in patterns if pattern.search(normalized_text)]
        if found:
            candidate = {field: row[field] for field in FIELDS}
            candidate["termino_detectado"] = "|".join(found)
            candidates.append(candidate)
            term_counts.update(found)

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(candidates)

    yes_count = sum(row["etiqueta_EXIST"] == "YES" for row in candidates)
    no_count = sum(row["etiqueta_EXIST"] == "NO" for row in candidates)
    total_matches = sum(term_counts.values())
    candidate_ids = {row["id_EXIST"] for row in candidates}

    print("=" * 88)
    print("ANALISIS EXPLORATORIO: CANDIDATOS POTENCIALMENTE RELACIONADOS")
    print("CON CONTENIDO LGBTIQ+")
    print("=" * 88)
    print(f"Total de memes analizados: {len(rows)}")
    print(f"Memes con al menos una coincidencia: {len(candidates)}")
    print(f"Porcentaje de candidatos: {len(candidates) / len(rows) * 100:.2f}%")
    print(f"Memes sin coincidencias: {len(rows) - len(candidates)}")
    print(f"Numero total de coincidencias: {total_matches}")
    print(f"Candidatos con etiqueta_EXIST = YES: {yes_count}")
    print(f"Candidatos con etiqueta_EXIST = NO: {no_count}")
    print(f"Archivo creado: {OUTPUT_PATH}")

    print("\n30 terminos mas frecuentes:")
    for position, (term, count) in enumerate(term_counts.most_common(30), 1):
        print(f"{position:2}. {term}: {count}")

    print("\n20 ejemplos variados de candidatos:")
    if candidates:
        step = max(1, len(candidates) // 20)
        selected = candidates[::step][:20]
        for row in selected:
            print(f"\nid_EXIST: {row['id_EXIST']}")
            print(f"texto: {shorten(row['texto'])}")
            print(f"termino_detectado: {row['termino_detectado']}")
            print(f"etiqueta_EXIST: {row['etiqueta_EXIST']}")

    image_only_note = (
        "No es posible cuantificar con estos datos cuántos memes contienen una "
        "referencia únicamente visual. Como máximo, cualquiera de los "
        f"{len(rows)} memes analizados podría requerir revisión visual; el CSV "
        "solo permite identificar referencias presentes en la columna texto."
    )
    print("\nLimitaciones:")
    print(f"- Referencias solo en imagen no detectables: {image_only_note}")
    print("- Origen del texto: la presencia de texto OCR y metadatos concatenados parece")
    print("  posible en algunos registros, pero este análisis no puede establecer su")
    print("  procedencia con certeza sin contrastar el JSON original y la imagen.")
    print("- Normalizacion: se ignoran mayusculas y tildes, y se aceptan espacios")
    print("  variables y guiones en expresiones. Emojis, errores OCR, abreviaturas y")
    print("  texto exclusivamente visual pueden producir falsos negativos o positivos.")
    print("- Interpretacion: estos resultados son candidatos potencialmente relacionados")
    print("  con contenido LGBTIQ+; no son clasificaciones de LGBTfobia, violencia ni")
    print("  violencia simbolica. La decisión requiere revisión humana y protocolo.")

    if len(candidate_ids) != len(candidates):
        raise ValueError("Se detectaron IDs duplicados en candidatos inesperadamente")


if __name__ == "__main__":
    main()
