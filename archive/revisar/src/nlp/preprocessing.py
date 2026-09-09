"""Preprocesamiento del texto para modelos NLP."""


def normalize_text(text: str) -> str:
    """Normaliza texto sencillo."""
    if text is None:
        return ""
    return " ".join(text.strip().split())
