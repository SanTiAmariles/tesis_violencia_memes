#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera una selección exploratoria de memes relacionados con mujeres."""

import csv
import re
import unicodedata
from pathlib import Path

PROJECT = Path(__file__).resolve().parent
INPUT = PROJECT / "dataset_exist2024_es_labeled.csv"
BASE = PROJECT / "dataset/annotations/mujeres_exploracion"
VOCABULARY = BASE / "vocabulario_mujeres_exploratorio.txt"
CANDIDATES = BASE / "candidatos_mujeres_exist2024.csv"
REVIEW = BASE / "candidatos_mujeres_revision.csv"

CANDIDATE_FIELDS = ["ID", "texto", "etiqueta_EXIST", "termino(s)_coincidente(s)", "ruta_meme"]
REVIEW_FIELDS = [
    "ID", "texto", "etiqueta_EXIST", "termino(s)_coincidente(s)", "ruta_meme",
    "referencia_mujeres", "criterio_violencia", "clasificacion_preliminar",
    "dificultad", "justificacion", "observaciones",
]


def normalize(value):
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.casefold().replace("-", " ")
    return re.sub(r"\s+", " ", value).strip()


def load_terms():
    terms = []
    normalized = set()
    for raw in VOCABULARY.read_text(encoding="utf-8").splitlines():
        term = raw.strip()
        if not term or term.startswith("#") or term.startswith("["):
            continue
        key = normalize(term)
        if key not in normalized:
            terms.append(term)
            normalized.add(key)
    return terms


def patterns_for(terms):
    patterns = []
    for term in terms:
        expression = re.escape(normalize(term)).replace(r"\ ", r"\s+")
        patterns.append((term, re.compile(r"(?<!\w)" + expression + r"(?!\w)")))
    return patterns


def main():
    terms = load_terms()
    patterns = patterns_for(terms)
    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        source = list(csv.DictReader(handle))

    candidates = []
    for row in source:
        text = normalize(row["texto"])
        found = [term for term, pattern in patterns if pattern.search(text)]
        if found:
            candidates.append({
                "ID": row["id_EXIST"],
                "texto": row["texto"],
                "etiqueta_EXIST": row["etiqueta_EXIST"],
                "termino(s)_coincidente(s)": "|".join(found),
                "ruta_meme": row["path_memes"],
            })

    BASE.mkdir(parents=True, exist_ok=True)
    with CANDIDATES.open("w", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=CANDIDATE_FIELDS).writeheader()
        csv.DictWriter(handle, fieldnames=CANDIDATE_FIELDS).writerows(candidates)

    with REVIEW.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REVIEW_FIELDS)
        writer.writeheader()
        for row in candidates:
            writer.writerow({**row, "referencia_mujeres": "", "criterio_violencia": "", "clasificacion_preliminar": "", "dificultad": "", "justificacion": "", "observaciones": ""})

    print(f"Memes analizados: {len(source)}")
    print(f"Candidatos encontrados: {len(candidates)}")
    print(f"YES: {sum(row['etiqueta_EXIST'] == 'YES' for row in candidates)}")
    print(f"NO: {sum(row['etiqueta_EXIST'] == 'NO' for row in candidates)}")
    print(f"Términos disponibles: {len(terms)}")
    print(f"Archivos: {CANDIDATES} | {REVIEW}")


if __name__ == "__main__":
    main()
