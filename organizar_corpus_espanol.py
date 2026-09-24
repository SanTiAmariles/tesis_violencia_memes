from pathlib import Path
import csv
import hashlib
import json
import shutil

root = Path(r'c:\Users\santi\Downloads\tesis\tesis_violencia_memes')
source_root = root / 'dataset' / 'raw'
corpus_dir = root / 'dataset' / 'corpus_espanol'
metadata_dir = root / 'dataset' / 'metadata'

categories = [
    'Anti feminismo',
    'Apariencia física',
    'Burla',
    'Estándar',
    'Estereotipación',
    'LGBT',
    'Machismo',
    'Misoginia',
    'Sexualizacion',
    'Violencia',
]

# Reset only the new organized corpus copies; original sources remain untouched.
if corpus_dir.exists():
    shutil.rmtree(corpus_dir)

(corpus_dir / 'TODOS').mkdir(parents=True, exist_ok=True)
(corpus_dir / 'CLASIFICADOS').mkdir(parents=True, exist_ok=True)
(corpus_dir / 'POR_CLASIFICAR').mkdir(parents=True, exist_ok=True)
(corpus_dir / 'COLECCION_PROPIA').mkdir(parents=True, exist_ok=True)

for cat in categories:
    (corpus_dir / 'CLASIFICADOS' / cat).mkdir(parents=True, exist_ok=True)

# Load Spanish EXIST records from training metadata
train_json = root / 'dataset/raw/EXIST2021-2025_datasets/2024 EXIST/EXIST 2024 Memes Dataset/training/EXIST2024_training.json'
train_data = json.loads(train_json.read_text(encoding='utf-8'))
spanish_records = {str(v['id_EXIST']): v for v in train_data.values() if str(v.get('lang', '')).lower() == 'es'}

# Locate source files for EXIST Spanish records and currently classified categories
exist_meme_root = root / 'dataset/raw/EXIST2021-2025_datasets/2024 EXIST/EXIST 2024 Memes Dataset/training/memes'
existing_category_files = {}
for cat in categories:
    cat_dir = exist_meme_root / cat
    if not cat_dir.exists():
        continue
    existing_category_files[cat] = []
    for p in sorted(cat_dir.iterdir(), key=lambda x: x.name.lower()):
        if p.is_file():
            existing_category_files[cat].append(p)

# Build a mapping of source file to category for existing classified files (exactly preserving current classification)
classified_by_stem = {}
for cat, files in existing_category_files.items():
    for p in files:
        classified_by_stem.setdefault(p.stem, []).append(cat)

# Build list of EXIST source files to copy
exist_source_files = []
for sid in sorted(spanish_records.keys(), key=lambda s: int(s)):
    record = spanish_records[sid]
    candidates = []
    meme_name = str(record.get('meme') or '').strip()
    if meme_name:
        candidates.append(exist_meme_root / meme_name)
    path_memes = str(record.get('path_memes') or '').strip()
    if path_memes:
        rel = path_memes.replace('memes/', '', 1) if path_memes.startswith('memes/') else path_memes
        candidates.append(exist_meme_root / rel)
    selected = None
    for cand in candidates:
        if cand.exists():
            selected = cand
            break
    if selected is None:
        for p in exist_meme_root.rglob('*'):
            if p.is_file() and p.stem == sid:
                selected = p
                break
    if selected is None:
        raise FileNotFoundError(f'No source file found for EXIST id {sid}')
    exist_source_files.append((sid, selected))

# Copy EXIST raws to CLASIFICADOS and POR_CLASIFICAR, preserving original filenames.
# The classification work already exists in the source directories; we copy those files exactly.
for cat, files in existing_category_files.items():
    for src in files:
        dst = corpus_dir / 'CLASIFICADOS' / cat / src.name
        if not dst.exists():
            shutil.copy2(src, dst)

# Determine POR_CLASIFICAR = Spanish EXIST not present in any current category
classified_stems = set(classified_by_stem.keys())
por_clasificar_ids = [sid for sid in spanish_records if sid not in classified_stems]
for sid in por_clasificar_ids:
    record = spanish_records[sid]
    candidates = []
    meme_name = str(record.get('meme') or '').strip()
    if meme_name:
        candidates.append(exist_meme_root / meme_name)
    path_memes = str(record.get('path_memes') or '').strip()
    if path_memes:
        rel = path_memes.replace('memes/', '', 1) if path_memes.startswith('memes/') else path_memes
        candidates.append(exist_meme_root / rel)
    selected = None
    for cand in candidates:
        if cand.exists():
            selected = cand
            break
    if selected is None:
        for p in exist_meme_root.rglob('*'):
            if p.is_file() and p.stem == sid:
                selected = p
                break
    if selected is None:
        raise FileNotFoundError(f'No POR_CLASIFICAR file found for EXIST id {sid}')
    dst = corpus_dir / 'POR_CLASIFICAR' / selected.name
    if not dst.exists():
        shutil.copy2(selected, dst)

# Copy collection own files into COLECCION_PROPIA preserving original names
own_dir = root / 'dataset/raw/LGBTQ'
for src in sorted(own_dir.iterdir(), key=lambda p: p.name.lower()):
    if src.is_file():
        dst = corpus_dir / 'COLECCION_PROPIA' / src.name
        if not dst.exists():
            shutil.copy2(src, dst)

# Build TODO list: all Spanish EXIST + all own collection files
# Each gets an internal unique MEME-XXXX ID; originals remain untouched.
rows = []
count = 1

# Add EXIST records first in stable order
for sid, src in exist_source_files:
    new_id = f'MEME-{count:04d}'
    new_name = f'{new_id}{src.suffix}'
    tgt = corpus_dir / 'TODOS' / new_name
    shutil.copy2(src, tgt)
    category_name = ''
    for cat, files in existing_category_files.items():
        if any(f.resolve() == src.resolve() for f in files):
            category_name = cat
            break
    rows.append({
        'ID_nuevo': new_id,
        'ID_original': sid,
        'archivo_original': src.name,
        'ruta_original': str(src.relative_to(root)).replace('\\', '/'),
        'archivo_normalizado': new_name,
        'fuente': 'EXIST',
        'clasificacion_previa': category_name,
        'estado_clasificacion': 'CLASIFICADO' if category_name else 'POR_CLASIFICAR',
    })
    count += 1

# Add own collection after existence records
for src in sorted(own_dir.iterdir(), key=lambda p: p.name.lower()):
    if src.is_file():
        new_id = f'MEME-{count:04d}'
        new_name = f'{new_id}{src.suffix}'
        tgt = corpus_dir / 'TODOS' / new_name
        shutil.copy2(src, tgt)
        rows.append({
            'ID_nuevo': new_id,
            'ID_original': src.stem,
            'archivo_original': src.name,
            'ruta_original': str(src.relative_to(root)).replace('\\', '/'),
            'archivo_normalizado': new_name,
            'fuente': 'COLECCION_PROPIA',
            'clasificacion_previa': '',
            'estado_clasificacion': 'POR_CLASIFICAR',
        })
        count += 1

metadata_dir.mkdir(parents=True, exist_ok=True)
master_path = metadata_dir / 'corpus_espanol_master.csv'
with master_path.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['ID_nuevo','ID_original','archivo_original','ruta_original','archivo_normalizado','fuente','clasificacion_previa','estado_clasificacion'])
    writer.writeheader()
    writer.writerows(rows)

# Duplicate register (exact SHA-256) is for EXIST raw tree; not deleting anything.
hash_map = {}
for p in sorted(exist_meme_root.rglob('*')):
    if p.is_file():
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        hash_map.setdefault(digest, []).append(str(p.relative_to(root)).replace('\\', '/'))

duplicate_groups = [paths for paths in hash_map.values() if len(paths) > 1]

duplicates_path = metadata_dir / 'duplicados_exist.csv'
with duplicates_path.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['grupo', 'sha256', 'ruta'])
    for idx, group in enumerate(duplicate_groups, start=1):
        digest = hashlib.sha256((root / group[0].replace('/', '\\')).read_bytes()).hexdigest()
        for path in group:
            writer.writerow([f'G{idx}', digest, path])

print(f'TODOS={len(rows)}')
print(f'EXIST={sum(1 for r in rows if r["fuente"] == "EXIST")}')
print(f'COLECCION_PROPIA={sum(1 for r in rows if r["fuente"] == "COLECCION_PROPIA")}')
print(f'CLASIFICADOS={sum(1 for r in rows if r["estado_clasificacion"] == "CLASIFICADO")}')
print(f'POR_CLASIFICAR={sum(1 for r in rows if r["estado_clasificacion"] == "POR_CLASIFICAR")}')
print(f'MASTER_CSV={master_path}')
print(f'DUPLICATES_CSV={duplicates_path}')
