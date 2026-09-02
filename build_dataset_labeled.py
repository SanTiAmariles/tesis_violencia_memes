#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construir dataset_exist2024_es_labeled.csv
Solo registros con etiqueta consolidada YES/NO de gold_hard.
Excluir los 322 casos con empate 3-3.
"""

import json
import csv
from pathlib import Path

# Rutas
project = Path(r'c:\Users\santi\Downloads\tesis_violencia_memes')
train_path = project / 'dataset/raw/EXIST2021-2025_datasets/2024 EXIST/EXIST 2024 Memes Dataset/training/EXIST2024_training.json'
gold_hard_path = project / 'dataset/raw/EXIST2021-2025_datasets/2024 EXIST/evaluation/golds/EXIST2024_training_task4_gold_hard.json'
out_path = project / 'dataset_exist2024_es_labeled.csv'

print("=" * 100)
print("CONSTRUYENDO: dataset_exist2024_es_labeled.csv")
print("Solo registros con etiqueta consolidada (excluir 322 casos con empate)")
print("=" * 100)

# Cargar training
print("\n[1/4] Cargando EXIST2024_training.json...")
with train_path.open('r', encoding='utf-8') as f:
    training = json.load(f)
print(f"   ✓ {len(training)} registros totales cargados")

# Cargar gold_hard
print("\n[2/4] Cargando EXIST2024_training_task4_gold_hard.json...")
with gold_hard_path.open('r', encoding='utf-8') as f:
    gold_hard_list = json.load(f)
print(f"   ✓ {len(gold_hard_list)} etiquetas gold cargadas")

# Crear mapeo gold_hard SOLO con etiquetas YES/NO válidas
# Esto automáticamente excluye los 322 casos con empate que no tienen gold_hard
gold_hard_map = {}
for item in gold_hard_list:
    gold_id = str(item['id'])
    value = item.get('value', '')
    # Solo incluir si el valor es YES o NO
    if value in ['YES', 'NO']:
        gold_hard_map[gold_id] = value

print(f"   ✓ Gold_hard map creado con {len(gold_hard_map)} IDs válidos (solo YES/NO)")

# Filtrar y relacionar
print("\n[3/4] Filtrando registros en español con etiqueta válida...")
rows = []
seen_ids = set()
duplicates = []

count_es = 0
yes_count = 0
no_count = 0
no_label_count = 0

for key, rec in training.items():
    # Filtrar por idioma
    if rec.get('lang') != 'es':
        continue

    id_exist = str(rec.get('id_EXIST', key))

    # Buscar en gold_hard SOLO si tiene etiqueta válida
    if id_exist not in gold_hard_map:
        # Este es uno de los 322 empatados o sin etiqueta
        no_label_count += 1
        continue

    # Si llegamos aquí, tenemos una etiqueta válida
    count_es += 1
    label = gold_hard_map[id_exist]

    # Contar etiquetas
    if label == 'YES':
        yes_count += 1
    elif label == 'NO':
        no_count += 1

    # Detectar duplicados
    if id_exist in seen_ids:
        duplicates.append(id_exist)
    else:
        seen_ids.add(id_exist)

    # Agregar fila
    rows.append({
        'id_EXIST': id_exist,
        'texto': rec.get('text', ''),
        'imagen': rec.get('meme', ''),
        'path_memes': rec.get('path_memes', ''),
        'etiqueta_EXIST': label,
    })

print(f"   ✓ {count_es} memes españoles con etiqueta válida")
print(f"   ✓ {no_label_count} memes españoles EXCLUIDOS (sin etiqueta en gold_hard)")

# Escribir CSV
print("\n[4/4] Escribiendo CSV...")
with out_path.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['id_EXIST', 'texto', 'imagen', 'path_memes', 'etiqueta_EXIST'])
    writer.writeheader()
    writer.writerows(rows)
print(f"   ✓ {len(rows)} registros escritos en {out_path}")

# Validaciones
print("\n" + "=" * 100)
print("VALIDACIÓN FINAL")
print("=" * 100)

print(f"\n✓ Total de registros en CSV: {count_es}")
print(f"✓ Etiquetados como YES: {yes_count}")
print(f"✓ Etiquetados como NO: {no_count}")
print(f"✓ Registros sin etiqueta (excluidos): {no_label_count}")
print(f"✓ IDs duplicados: {len(duplicates)}")

# Validar que no hay registros vacíos
print(f"\n✓ Validación de integridad:")
empty_labels = sum(1 for row in rows if not row['etiqueta_EXIST'])
print(f"   Registros con etiqueta vacía: {empty_labels}")
if empty_labels == 0:
    print(f"   ✅ OK: No hay registros con etiqueta vacía")

# Mostrar muestra del CSV
print("\n" + "=" * 100)
print("MUESTRA DEL CSV (primeros 10 registros):")
print("=" * 100)
for i, row in enumerate(rows[:10], 1):
    print(f"\n[{i}] id_EXIST: {row['id_EXIST']} | etiqueta_EXIST: {row['etiqueta_EXIST']}")
    print(f"    texto: {row['texto'][:75]}...")
    print(f"    imagen: {row['imagen']}")
    print(f"    path_memes: {row['path_memes']}")

print("\n" + "=" * 100)
print(f"✅ DATASET FINAL CREADO EXITOSAMENTE")
print(f"   Archivo: {out_path}")
print(f"   Registros: {len(rows)} (1712 esperados)")
print(f"   YES: {yes_count}")
print(f"   NO: {no_count}")
print("=" * 100)

# Confirmación de valores esperados
expected_total = 1712
expected_yes = 1073
expected_no = 639

if len(rows) == expected_total and yes_count == expected_yes and no_count == expected_no and empty_labels == 0 and len(duplicates) == 0:
    print("✅ TODAS LAS VALIDACIONES PASARON CORRECTAMENTE")
else:
    print("⚠️ ADVERTENCIA: Valores no coinciden con lo esperado")
    print(f"   Esperado: {expected_total} registros, {expected_yes} YES, {expected_no} NO")
    print(f"   Obtenido: {len(rows)} registros, {yes_count} YES, {no_count} NO")
