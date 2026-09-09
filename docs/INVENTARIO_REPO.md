# Inventario del repositorio y decisiones de limpieza

Este inventario se elaboró para dejar el repositorio alineado con el trabajo realmente realizado y documentado en el avance de tesis, sin avanzar etapas que aún no están consolidadas.

## Convención

- Sí = sí está evidenciado en el avance de tesis o en la evidencia del trabajo realizado.
- No = no forma parte del trabajo actual y/o es un artefacto genérico o temporal.
- REVISAR = se conserva por precaución, pero no se utiliza como parte del trabajo definitivo.

| Archivo/carpeta | Para qué se utilizó | Evidenciado en AVANCE TESIS | Decisión |
| --- | --- | --- | --- |
| [README.md](../README.md) | Documento principal del repositorio y estado actual del proyecto. | Sí | Conserva y actualiza |
| [dataset/](../dataset) | Contenedor del conjunto de datos bruto, derivado y análisis de calidad. | Sí | Conserva |
| [dataset/raw/EXIST2021-2025_datasets/](../dataset/raw/EXIST2021-2025_datasets) | Fuente auxiliar original de EXIST 2024 y sus guías de anotación. | Sí | Conserva |
| [dataset/annotations/lgbtiq_exploracion/](../dataset/annotations/lgbtiq_exploracion) | Exploración de candidatos LGBTIQ+ mediante vocabulario sobre el texto y revisión visual preliminar. | Sí | Conserva |
| [dataset/annotations/mujeres_exploracion/](../dataset/annotations/mujeres_exploracion) | Exploración preliminar de casos relacionados con mujeres y pruebas del protocolo. | Sí | Conserva |
| [dataset/metadata/](../dataset/metadata) | Detección de duplicados exactos y grupos conflictivos de EXIST. | Sí | Conserva |
| [dataset_exist2024_es_labeled.csv](../dataset_exist2024_es_labeled.csv) | Subconjunto español de EXIST 2024 con etiquetas YES/NO válidas de gold_hard; base de trabajo. | Sí | Conserva |
| [candidatos_lgbtiq_exist2024.csv](../candidatos_lgbtiq_exist2024.csv) | Resultado de la exploración léxica LGBTIQ+. | Sí | Conserva |
| [vocabulario_lgbtiq_exploratorio.txt](../vocabulario_lgbtiq_exploratorio.txt) | Vocabulario exploratorio para buscar referencias LGBTIQ+ en texto. | Sí | Conserva |
| [analisis_exploratorio_lgbtiq.py](../analisis_exploratorio_lgbtiq.py) | Script que identifica candidatos LGBTIQ+ de forma exploratoria. | Sí | Conserva |
| [generar_candidatos_mujeres.py](../generar_candidatos_mujeres.py) | Script de exploración preliminar de mujeres. | Sí | Conserva |
| [build_dataset_labeled.py](../build_dataset_labeled.py) | Genera el subconjunto final español de EXIST con etiquetas válidas. | Sí | Conserva |
| [investigate_322.py](../investigate_322.py) | Diagnóstico de los casos sin etiqueta en gold_hard; confirma el empate 3-3. | Sí | Conserva |
| [analizar_duplicados_exactos.py](../analizar_duplicados_exactos.py) | Análisis de duplicados exactos sobre el subconjunto español. | Sí | Conserva |
| [analizar_duplicados_conflictivos.py](../analizar_duplicados_conflictivos.py) | Identificación de duplicados conflictivos con etiquetas diacrónicas/contradictorias. | Sí | Conserva |
| [archive/revisar/](../archive/revisar) | Carpeta de revisión para artefactos genéricos, temporales o no evidenciados. | No | Reorganiza / REVISAR |
| [archive/revisar/notebooks/](../archive/revisar/notebooks) | Pipelines genéricos de ML y notebooks no alineados con la tesis actual. | No | REVISAR |
| [archive/revisar/src/](../archive/revisar/src) | Estructura de código genérica del proyecto-scaffold, no parte del trabajo evidenciado. | No | REVISAR |
| [archive/revisar/models/](../archive/revisar/models) | Modelos y artefactos generados no documentados como parte del avance actual. | No | REVISAR |
| [archive/revisar/web/](../archive/revisar/web) | Backend/frontend genérico de demostración no evidenciado. | No | REVISAR |
| [archive/revisar/results/](../archive/revisar/results) | Resultados genéricos no vinculados con la fase actual. | No | REVISAR |
| [archive/revisar/requirements.txt](../archive/revisar/requirements.txt) | Dependencias del scaffold; no forman parte del trabajo actual. | No | REVISAR |

## Notas clave

- Las etiquetas originales de EXIST se conservan solo como referencia de procedencia y trazabilidad.
- No se consideran equivalentes a la variable tesis `violencia_simbolica`.
- La anotación propia de `violencia_simbolica = YES/NO` no se da por finalizada ni se implementa como etapa formal en esta estructura.
- Los archivos de revisión se mantienen fuera de la raíz para no borrar información útil, sin convertirlos en parte del trabajo definitivo.
