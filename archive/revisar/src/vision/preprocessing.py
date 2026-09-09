"""Preprocesamiento de imágenes para visión por computadora."""


def resize_image(image, target_size=(224, 224)):
    """Redimensiona una imagen a tamaño objetivo."""
    return image.resize(target_size)
