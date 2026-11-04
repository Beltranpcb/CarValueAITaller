"""Carga del modelo proporcionado y predicción a partir de 7 atributos."""
from pathlib import Path
from functools import lru_cache
import joblib
import pandas as pd
from .config import ESTADOS

MODELO_RUTA = Path(__file__).resolve().parents[1] / "models" / "modelo_con_condition.joblib"
COLUMNAS_MODELO = ["year", "odometer", "manufacturer", "fuel", "type", "transmission", "condition"]

@lru_cache(maxsize=1)
def cargar_modelo():
    return joblib.load(MODELO_RUTA)


def predecir_precio(datos: dict, estado: str) -> float:
    """Predice el precio en USD a partir de los datos del coche y su estado."""
    if estado not in ESTADOS:
        raise ValueError("Estado visual no válido para el modelo.")

    registro = {**datos, "condition": estado}
    entrada = pd.DataFrame([registro], columns=COLUMNAS_MODELO)

    modelo = cargar_modelo()
    precio = modelo.predict(entrada)[0]
    return round(float(precio), 2)
