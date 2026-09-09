# AVANCE DE TESIS — REFERENCIA PARA EL REPOSITORIO

## Propósito
Este archivo sirve como referencia para interpretar el estado actual del proyecto de tesis. No se deben inventar actividades, etapas, metodologías o avances que no estén respaldados por el avance de tesis.

## 1. Título
**Desarrollo de un modelo multimodal basado en Deep Learning para la detección automática de violencia simbólica en memes en español.**

## 2. Estado general
El avance actual se concentra principalmente en:
- **A1 — Construcción del dataset**
- **A2 — Construcción/consolidación del protocolo de anotación**

La **A3 — Anotación del conjunto de datos** no está documentada como terminada.

## 3. A1 — Construcción del dataset

### EXIST 2024
EXIST 2024 se utiliza como fuente de datos de referencia/auxiliar.

Se construyó un subconjunto de:
- **1.712 memes en español**

Las etiquetas originales de EXIST 2024 corresponden a su tarea de detección de sexismo.

**Importante:** esas etiquetas NO deben interpretarse automáticamente como la variable principal de esta tesis:

`violencia_simbolica = YES / NO`

Por tanto, `dataset_exist2024_es_labeled.csv` representa actualmente un subconjunto etiquetado según la información original de EXIST y debe tratarse como **dataset auxiliar/de referencia**, no como dataset final de la tesis.

Para formar parte del dataset final deberá pasar por el proceso de anotación definido para esta investigación.

## 4. Exploración LGBTIQ+ dentro de EXIST
Se realizó una exploración léxica para identificar posibles memes relacionados con personas o temáticas LGBTIQ+.

Resultado:
- **74 candidatos**

Estos candidatos fueron obtenidos mediante un filtro exploratorio.

**Importante:** los 74 candidatos no representan automáticamente violencia simbólica, discurso de odio ni casos positivos. Requieren revisión según el protocolo de anotación.

La exploración de candidatos NO equivale a la anotación final.

## 5. Recolección propia
Está en desarrollo una **recolección propia de memes en español**, realizada manualmente a partir de fuentes de acceso público.

Durante esta etapa se registra:
- ID provisional;
- nombre del archivo;
- grupo objetivo de referencia;
- fuente;
- URL;
- fecha de recolección.

Existe una colección inicial de memes relacionados con la comunidad LGBTIQ+.

### Importante: recolección NO es anotación
La recolección consiste en recopilar candidatos y registrar su procedencia.

Durante la recolección **NO se asigna**:

`violencia_simbolica = YES / NO`

Esa decisión corresponde a la etapa posterior de anotación.

## 6. Organización conceptual del dataset
La investigación busca construir un **único dataset final** para la tarea principal.

Los grupos:
- MUJERES
- LGBTIQ+

sirven para organizar candidatos y facilitar la recolección. No implican dos datasets ni dos modelos independientes.

La variable principal del dataset final será:

`violencia_simbolica = YES / NO`

El grupo objetivo puede conservarse como metadato.

## 7. Definición operacional
Para efectos de la investigación, un meme presenta violencia simbólica cuando, mediante sus elementos textuales, visuales o mediante la interacción entre ambos, reproduce, legitima, naturaliza o refuerza representaciones, estereotipos, prejuicios, relaciones de desigualdad, subordinación, exclusión o estigmatización dirigidas hacia las mujeres o hacia personas pertenecientes a la comunidad LGBTIQ+.

## 8. A2 — Protocolo de anotación
Se desarrolló y probó preliminarmente un protocolo de clasificación binaria:

- **YES** — existe evidencia suficiente de violencia simbólica según la definición y criterios establecidos.
- **NO** — no existe evidencia suficiente de violencia simbólica según la definición y criterios establecidos.

La unidad de análisis es el **meme completo**, considerando texto, imagen e interacción entre ambos.

## 9. Criterios del protocolo
El protocolo contempla criterios relacionados con:
- estereotipos;
- desigualdad o subordinación;
- estigmatización;
- exclusión o invisibilización;
- naturalización de relaciones de dominación;
- representaciones degradantes.

También contempla reglas para situaciones ambiguas y casos donde es necesario interpretar el contenido multimodal.

El humor, la ironía y expresiones ofensivas no deben clasificarse automáticamente sin considerar el contexto completo.

## 10. Pruebas preliminares
Se realizaron pruebas preliminares del protocolo con casos reales relacionados con:
- comunidad LGBTIQ+;
- mujeres.

Estas pruebas sirvieron para revisar la aplicabilidad de los criterios y reglas.

**No equivalen a la anotación completa del dataset.**

## 11. A2.5 — Consolidación
A partir de las pruebas preliminares se consolidaron los criterios y reglas del protocolo.

La siguiente actividad indicada en el avance es:

**A3 — Anotación del conjunto de datos.**

Por tanto, no debe afirmarse que todo el dataset ya está anotado con `violencia_simbolica`.

## 12. Duplicados y organización técnica
El repositorio puede contener análisis técnicos relacionados con duplicados y organización de datos.

Los análisis de duplicados mediante hashes deben conservarse como evidencia del trabajo realizado cuando correspondan al avance.

Los duplicados no deben eliminarse automáticamente sin revisar su asociación con los registros y su impacto metodológico.

Cuando una misma imagen aparezca asociada a IDs diferentes, debe evitarse posteriormente que copias de la misma imagen queden en diferentes particiones de entrenamiento, validación y prueba.

## 13. No asumir como realizado
No se debe asumir que ya están completamente realizados:
- A3 — anotación completa;
- entrenamiento definitivo;
- evaluación definitiva;
- comparación final multimodal/unimodal;
- aplicación web final;
- OCR como pipeline final;
- procesamiento NLP final;
- entrenamiento definitivo de CNN;
- división definitiva train/validation/test.

Solo deben marcarse como realizados cuando exista evidencia correspondiente.

## 14. Reglas para trabajar con el repositorio
1. Usar este documento como referencia del estado de la tesis.
2. No inventar etapas ni actividades.
3. No presentar etiquetas originales de datasets externos como etiquetas de la tesis.
4. Diferenciar recolección, limpieza/preparación, anotación y dataset final.
5. No considerar la recolección propia como anotación.
6. No considerar la exploración léxica como anotación.
7. No considerar las etiquetas originales de EXIST 2024 como `violencia_simbolica`.
8. No afirmar que A3 está terminada.
9. Conservar la trazabilidad y procedencia de los datos.
10. Antes de eliminar archivos, generar un inventario y solicitar aprobación.

## 15. Flujo conceptual actual

**Fuentes de datos**
↓
**Recolección / selección de candidatos**
↓
**Limpieza y preparación**
↓
**Anotación mediante el protocolo propio**
↓
**Dataset final con `violencia_simbolica = YES / NO`**
↓
**Entrenamiento y evaluación del modelo**

El estado actual no debe adelantarse artificialmente a las etapas posteriores.

## Nota final
Este archivo es una referencia de trabajo para herramientas como GitHub Copilot. Ante cualquier duda sobre qué se ha realizado en la tesis, debe contrastarse con este documento. Si una actividad no está respaldada, debe indicarse que no existe evidencia suficiente en el avance actual.
