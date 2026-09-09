# Tesis: violencia simbólica en memes

Este repositorio refleja el trabajo realizado y documentado hasta el momento en el avance de tesis, con especial foco en la construcción del corpus, la exploración preliminar y el control del conjunto de datos.

## Estado actual del repositorio

El repositorio conserva únicamente artefactos relacionados con:

- A1. Construcción y recolección inicial del conjunto de datos.
- A2. Protocolo de anotación preliminar.
- A4. Control del conjunto de datos y duplicados.

No se incluye trabajo que implique una anotación completa o una etapa finalizada de `violencia_simbolica`.

## Estructura principal

- `dataset/`: datos fuente, subconjunto español, análisis y resultados auxiliares.
- `docs/`: documentación y registro del inventario del repositorio.
- `archive/revisar/`: artefactos históricos o genéricos que se conservan fuera del núcleo del proyecto para no perder trazabilidad.
- `analisis_exploratorio_lgbtiq.py`: script de exploración preliminar de candidatos LGBTIQ+.
- `generar_candidatos_mujeres.py`: script de exploración preliminar de mujeres.
- `build_dataset_labeled.py`: construcción del subconjunto español con etiquetas válidas de gold_hard.
- `investigate_322.py`: diagnóstico de los casos no etiquetados por empate.
- `analizar_duplicados_exactos.py`: detección de duplicados exactos del conjunto EXIST.
- `analizar_duplicados_conflictivos.py`: análisis de grupos conflictivos.

## Elementos mantenidos

### A1 — Construcción y recolección inicial

- `dataset/raw/EXIST2021-2025_datasets/`: dataset auxiliar de EXIST 2024, guías y metadatos.
- `dataset_exist2024_es_labeled.csv`: subconjunto español de memes con labels válidas YES/NO de EXIST, usado para trabajo preparatorio.
- `candidatos_lgbtiq_exist2024.csv`: listado exploratorio de candidatos LGBTIQ+ presentes en el texto.
- `vocabulario_lgbtiq_exploratorio.txt`: vocabulario usado en la exploración preliminar.
- `dataset/annotations/lgbtiq_exploracion/`: revisión visual y resumen del análisis exploratorio.
- `dataset/annotations/mujeres_exploracion/`: revisión preliminar de casos relacionados con mujeres.

### A2 — Protocolo de anotación

- Se conserva la evidencia de pruebas preliminares y del protocolo de identificación.
- Las pruebas son preliminares y no constituyen una anotación final del dataset.

### A4 — Control del conjunto de datos

- `dataset/metadata/duplicados_exactos.csv`: duplicados exactos documentados.
- `dataset/metadata/duplicados_conflictivos_exist2024.csv`: grupos conflictivos con metadata y observaciones.
- `dataset/metadata/resumen_duplicados_conflictivos.txt`: resumen del análisis.

## Importante sobre etiquetas

La variable principal de la tesis es:

`violencia_simbolica = YES / NO`

Las etiquetas originales de EXIST NO deben tratarse como equivalentes a `violencia_simbolica`. Se conservan como referencia de procedencia y trazabilidad, pero quedan claramente diferenciadas de la variable propia de la tesis.

## Interfaz de revisión

Las interfaces HTML necesitan un servidor local para cargar los CSV y las imágenes. Desde la raíz del proyecto:

```powershell
python -m http.server 8765
```

Y luego abrir:

- `http://localhost:8765/dataset/annotations/lgbtiq_exploracion/revision_visual_lgbtiq.html`
- `http://localhost:8765/dataset/annotations/mujeres_exploracion/revision_mujeres.html`

## Inventario y limpieza

El inventario completo del repositorio y sus decisiones está en:

- [docs/INVENTARIO_REPO.md](docs/INVENTARIO_REPO.md)

Este repositorio se mantiene limpio y coherente con el avance actual, sin adelantar etapas de anotación ni metodologías que no estén documentadas como realizadas.
