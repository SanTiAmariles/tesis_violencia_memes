#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Investigar por qué 322 memes españoles no tienen etiqueta en gold_hard.
"""

import json
from pathlib import Path
from collections import defaultdict

# Rutas
project = Path(r'c:\Users\santi\Downloads\tesis_violencia_memes')
train_path = project / 'dataset/raw/EXIST2021-2025_datasets/2024 EXIST/EXIST 2024 Memes Dataset/training/EXIST2024_training.json'
gold_hard_path = project / 'dataset/raw/EXIST2021-2025_datasets/2024 EXIST/evaluation/golds/EXIST2024_training_task4_gold_hard.json'
gold_soft_path = project / 'dataset/raw/EXIST2021-2025_datasets/2024 EXIST/evaluation/golds/EXIST2024_training_task4_gold_soft.json'

print("=" * 100)
print("INVESTIGACIÓN: ¿Por qué 322 memes españoles no tienen gold_hard?")
print("=" * 100)

# Cargar datos
print("\n[CARGA] Leyendo archivos...")
with train_path.open('r', encoding='utf-8') as f:
    training = json.load(f)
with gold_hard_path.open('r', encoding='utf-8') as f:
    gold_hard_list = json.load(f)
with gold_soft_path.open('r', encoding='utf-8') as f:
    gold_soft_list = json.load(f)

# Crear mapeos
gold_hard_ids = {str(item['id']): item['value'] for item in gold_hard_list}
gold_soft_map = {str(item['id']): item['value'] for item in gold_soft_list}

print(f"   Training: {len(training)} registros")
print(f"   Gold Hard: {len(gold_hard_ids)} IDs")
print(f"   Gold Soft: {len(gold_soft_map)} IDs")

# Identificar 322 sin gold_hard
print("\n[ANÁLISIS] Identificando 322 memes españoles sin gold_hard...")
missing_hard = []
for key, rec in training.items():
    if rec.get('lang') != 'es':
        continue
    id_exist = str(rec.get('id_EXIST', key))
    if id_exist not in gold_hard_ids:
        missing_hard.append({
            'id': id_exist,
            'record': rec
        })

print(f"   ✓ {len(missing_hard)} memes sin gold_hard encontrados")

# Analizar cada uno
print("\n[ESTADÍSTICAS] Analizando casos...")
stats = {
    'has_6_annotations': 0,
    'majority_yes': 0,
    'majority_no': 0,
    'tied_3_3': 0,
    'in_gold_soft': 0,
    'not_in_gold_soft': 0,
    'tied_in_soft': 0,
    'other': 0,
}

detailed_cases = []

for item in missing_hard:
    id_exist = item['id']
    rec = item['record']
    labels = rec.get('labels_task4', [])
    
    # Contar anotaciones
    yes_count = labels.count('YES')
    no_count = labels.count('NO')
    
    case_info = {
        'id': id_exist,
        'annotations': labels,
        'yes_count': yes_count,
        'no_count': no_count,
        'in_gold_soft': id_exist in gold_soft_map,
        'text': rec.get('text', '')[:60],
    }
    
    # Contar anotaciones válidas
    if len(labels) == 6:
        stats['has_6_annotations'] += 1
    
    # Contar distribuciones
    if yes_count > no_count:
        stats['majority_yes'] += 1
    elif no_count > yes_count:
        stats['majority_no'] += 1
    elif yes_count == no_count == 3:
        stats['tied_3_3'] += 1
    
    # Chequear gold_soft
    if id_exist in gold_soft_map:
        stats['in_gold_soft'] += 1
        soft_value = gold_soft_map[id_exist]
        if soft_value.get('YES') == 0.5 and soft_value.get('NO') == 0.5:
            stats['tied_in_soft'] += 1
        case_info['soft_value'] = soft_value
    else:
        stats['not_in_gold_soft'] += 1
    
    detailed_cases.append(case_info)

# Mostrar estadísticas
print("\n" + "=" * 100)
print("ESTADÍSTICAS RESUMIDAS DE LOS 322 SIN GOLD_HARD")
print("=" * 100)

print(f"\n✓ Tienen 6 anotaciones: {stats['has_6_annotations']} / 322")
print(f"✓ Mayoría YES: {stats['majority_yes']} / 322")
print(f"✓ Mayoría NO: {stats['majority_no']} / 322")
print(f"✓ Empate 3-3: {stats['tied_3_3']} / 322")

print(f"\n✓ Aparecen en gold_soft: {stats['in_gold_soft']} / 322")
print(f"✓ NO aparecen en gold_soft: {stats['not_in_gold_soft']} / 322")
print(f"✓ En gold_soft con empate 0.5-0.5: {stats['tied_in_soft']} / 322")

# Ejemplos de casos específicos
print("\n" + "=" * 100)
print("EJEMPLOS CONCRETOS")
print("=" * 100)

# Ejemplo 1: Con mayoría YES
print("\n[EJEMPLO 1] Meme con mayoría YES (4-2) en annotations pero SIN gold_hard:")
example_yes = next((c for c in detailed_cases if c['yes_count'] > c['no_count']), None)
if example_yes:
    print(f"  ID: {example_yes['id']}")
    print(f"  Labels task4: {example_yes['annotations']}")
    print(f"  Distribución: {example_yes['yes_count']} YES, {example_yes['no_count']} NO")
    print(f"  En gold_soft: {example_yes['in_gold_soft']}")
    if example_yes['in_gold_soft']:
        print(f"  Gold_soft value: {example_yes['soft_value']}")
    print(f"  Texto: {example_yes['text']}")

# Ejemplo 2: Con mayoría NO
print("\n[EJEMPLO 2] Meme con mayoría NO (1-5) en annotations pero SIN gold_hard:")
example_no = next((c for c in detailed_cases if c['no_count'] > c['yes_count']), None)
if example_no:
    print(f"  ID: {example_no['id']}")
    print(f"  Labels task4: {example_no['annotations']}")
    print(f"  Distribución: {example_no['yes_count']} YES, {example_no['no_count']} NO")
    print(f"  En gold_soft: {example_no['in_gold_soft']}")
    if example_no['in_gold_soft']:
        print(f"  Gold_soft value: {example_no['soft_value']}")
    print(f"  Texto: {example_no['text']}")

# Ejemplo 3: Empate
print("\n[EJEMPLO 3] Meme con empate 3-3 en annotations pero SIN gold_hard:")
example_tie = next((c for c in detailed_cases if c['yes_count'] == 3 and c['no_count'] == 3), None)
if example_tie:
    print(f"  ID: {example_tie['id']}")
    print(f"  Labels task4: {example_tie['annotations']}")
    print(f"  Distribución: {example_tie['yes_count']} YES, {example_tie['no_count']} NO (EMPATE)")
    print(f"  En gold_soft: {example_tie['in_gold_soft']}")
    if example_tie['in_gold_soft']:
        print(f"  Gold_soft value: {example_tie['soft_value']}")
    print(f"  Texto: {example_tie['text']}")

# Ejemplo 4: Sin gold_soft
print("\n[EJEMPLO 4] Meme que NO aparece NI en gold_soft NI en gold_hard:")
example_orphan = next((c for c in detailed_cases if not c['in_gold_soft']), None)
if example_orphan:
    print(f"  ID: {example_orphan['id']}")
    print(f"  Labels task4: {example_orphan['annotations']}")
    print(f"  Distribución: {example_orphan['yes_count']} YES, {example_orphan['no_count']} NO")
    print(f"  En gold_soft: {example_orphan['in_gold_soft']}")
    print(f"  Texto: {example_orphan['text']}")

# Mostrar más ejemplos
print("\n" + "=" * 100)
print("PRIMEROS 10 CASOS COMPLETOS DE LOS 322 SIN GOLD_HARD")
print("=" * 100)

for i, case in enumerate(detailed_cases[:10], 1):
    in_soft = "✓" if case['in_gold_soft'] else "✗"
    tie_marker = " [EMPATE]" if case['yes_count'] == case['no_count'] else ""
    print(f"\n[{i}] ID: {case['id']} | Gold_soft: {in_soft} | {case['yes_count']}Y-{case['no_count']}N{tie_marker}")
    print(f"    Annotations: {case['annotations']}")
    if case['in_gold_soft']:
        print(f"    Gold_soft: {case['soft_value']}")
    print(f"    Texto: {case['text']}")

# Guardar reporte
report_path = project / 'investigacion_322_sin_gold_hard.txt'
with report_path.open('w', encoding='utf-8') as f:
    f.write("=" * 100 + "\n")
    f.write("INVESTIGACIÓN: ¿Por qué 322 memes españoles no tienen gold_hard?\n")
    f.write("=" * 100 + "\n\n")
    
    f.write("ESTADÍSTICAS RESUMIDAS:\n")
    f.write("-" * 100 + "\n")
    f.write(f"Total sin gold_hard: 322\n")
    f.write(f"Con 6 anotaciones: {stats['has_6_annotations']}\n")
    f.write(f"Mayoría YES: {stats['majority_yes']}\n")
    f.write(f"Mayoría NO: {stats['majority_no']}\n")
    f.write(f"Empate 3-3: {stats['tied_3_3']}\n")
    f.write(f"En gold_soft: {stats['in_gold_soft']}\n")
    f.write(f"NO en gold_soft: {stats['not_in_gold_soft']}\n")
    f.write(f"En gold_soft con empate 0.5-0.5: {stats['tied_in_soft']}\n\n")
    
    f.write("TODOS LOS 322 CASOS:\n")
    f.write("-" * 100 + "\n")
    for case in detailed_cases:
        in_soft = "SÍ" if case['in_gold_soft'] else "NO"
        f.write(f"ID: {case['id']} | Gold_soft: {in_soft} | {case['yes_count']}Y-{case['no_count']}N | {case['annotations']}\n")
        if case['in_gold_soft']:
            f.write(f"  Soft: {case['soft_value']}\n")

print("\n" + "=" * 100)
print(f"✅ Reporte guardado en: {report_path}")
print("=" * 100)
