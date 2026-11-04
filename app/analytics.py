"""BONUS (opcional): dashboard HTTP con estadísticas calculadas sobre PostgreSQL.

No es una tarea obligatoria del núcleo. Revisar docs/BONUS_ESTADISTICAS.md.
NO leer data/coches_50000_completo.csv desde esta ruta: la fuente debe ser SQL.
"""
from io import BytesIO
import matplotlib
matplotlib.use("Agg")  # backend sin pantalla para Docker/servidor web
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import text
from .db import engine

ORDEN_ESTADOS = ["fair", "good", "excellent", "like new"]


def obtener_resumen():
    """TODO D1: leer la tabla anuncios vía SQLAlchemy y calcular conteo y mediana por estado.

    Devolver un DataFrame con columnas: condition, cantidad, precio_mediano.
    Debe respetar ORDEN_ESTADOS. No utilizar el CSV local como origen.
    """
    raise NotImplementedError("BONUS D1: consulta y resumen de anuncios")


def grafico_png(resumen: pd.DataFrame) -> bytes:
    """TODO D2: representar una o dos gráficas usando matplotlib y devolver PNG en bytes.

    No usar plt.show() en un servidor. Guardar en BytesIO y cerrar la figura.
    """
    raise NotImplementedError("BONUS D2: representar PNG con matplotlib")
