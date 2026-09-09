"""Métricas de evaluación."""


def accuracy_score(y_true, y_pred):
    """Calcula precisión simple."""
    if len(y_true) != len(y_pred):
        raise ValueError("Las listas deben tener la misma longitud")
    correct = sum(int(t == p) for t, p in zip(y_true, y_pred))
    return correct / len(y_true) if y_true else 0.0
