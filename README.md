# Tesis: Violencia en memes

Este repositorio contiene la estructura base para la investigación sobre detección de violencia en memes mediante enfoques visuales, textuales y multimodales.

## Estructura principal

- `dataset/`: datos crudos, procesados y anotaciones.
- `notebooks/`: secuencia de análisis y experimentación.
- `src/`: código fuente por módulo.
- `models/`: artefactos de modelos entrenados.
- `web/`: backend y frontend para demostración.
- `results/`: figuras, tablas y métricas.
- `docs/`: documentación y protocolo.

## Flujo sugerido

1. Exploración del dataset.
2. Preprocesamiento de imágenes y textos.
3. Extracción de texto con OCR.
4. Preprocesamiento de NLP.
5. Modelos visuales.
6. Modelos textuales.
7. Modelo multimodal.
8. Evaluación final.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Notebooks

- `01_exploracion_dataset.ipynb`
- `02_preprocesamiento.ipynb`
- `03_ocr.ipynb`
- `04_pln.ipynb`
- `05_modelo_visual.ipynb`
- `06_modelo_textual.ipynb`
- `07_modelo_multimodal.ipynb`
- `08_evaluacion.ipynb`

## Interfaces de revisión

Las interfaces HTML necesitan un servidor local para cargar los CSV y las imágenes. Ejecuta el siguiente comando desde la raíz del proyecto:

```powershell
cd C:\Users\santi\Downloads\tesis_violencia_memes EN MI CASO LOCAL
python -m http.server 8765
```

Después abre la interfaz correspondiente:

- Revisión exploratoria LGBTIQ+: [revision_visual_lgbtiq.html](dataset/annotations/lgbtiq_exploracion/revision_visual_lgbtiq.html)
- Revisión exploratoria de mujeres: [revision_mujeres.html](dataset/annotations/mujeres_exploracion/revision_mujeres.html)

También puedes acceder mediante estas URLs:

- `http://localhost:8765/dataset/annotations/lgbtiq_exploracion/revision_visual_lgbtiq.html`
- `http://localhost:8765/dataset/annotations/mujeres_exploracion/revision_mujeres.html`

Mantén abierta la terminal mientras uses las interfaces. Para detener el servidor, presiona `Ctrl+C`.

¿
