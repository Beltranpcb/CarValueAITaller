"""Cohere Vision: una foto -> estado exterior + justificación breve."""
import base64
import json
import os
import re
from .config import ESTADOS

MODELO_VISION = "command-a-vision-07-2025"
# TODO C1-A (autoría propia): diseñad y escribid el prompt del modelo visual.
# El texto NO se proporciona. Revisad GUIA_ALUMNADO.md, etapa 5.
# Debe describir tarea, reglas, 4 estados, unknown y formato de respuesta.
PROMPT = ""  # RELLENAR. No vale copiar el prompt de otro equipo.


class VisionError(Exception):
    """Error de proveedor o de respuesta no interpretable."""


def parsear_respuesta(texto: str) -> tuple[str, str]:
    """Helper ya implementado: valida el JSON que responde la IA."""
    limpio = re.sub(r"^```(?:json)?\s*|\s*```$", "", texto.strip(), flags=re.I)
    if not limpio.startswith("{"):
        a, b = limpio.find("{"), limpio.rfind("}")
        if a >= 0 and b > a:
            limpio = limpio[a:b+1]
    try:
        obj = json.loads(limpio)
    except (ValueError, TypeError) as exc:
        raise VisionError("Cohere no devolvió un JSON interpretable.") from exc
    estado = str(obj.get("condition", "")).strip().lower()
    razon = str(obj.get("reason", "")).strip()[:350]
    if estado not in (*ESTADOS, "unknown"):
        raise VisionError(f"Cohere devolvió una categoría inesperada: {estado!r}")
    return estado, razon or "Sin justificación visible."


def clasificar_estado(contenido: bytes, mimetype: str) -> tuple[str, str, str]:
    """TODO C1: devuelve (condition, reason, fuente)."""
    if os.getenv("VISION_MOCK", "0") == "1":
        return "good", "Modo demostración: estado fijo, sin analizar la fotografía.", "MOCK"
    token = os.getenv("COHERE_API_KEY", "").strip()
    if not token:
        raise VisionError("Falta COHERE_API_KEY en el archivo .env")
    if not PROMPT.strip():
        raise VisionError("Falta redactar el prompt visual: tarea C1-A.")
    # TODO C1-B: convierte contenido en data URL base64 (mimetype dinamico).
    # TODO C1-B: cliente = cohere.ClientV2(api_key=token); cliente.chat(...).
    # TODO C1-B: recoge texto; parsear_respuesta(texto); devuelve estado, razon, "COHERE".
    raise NotImplementedError("Completa la llamada real a Cohere Vision")
