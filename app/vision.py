"""Cohere Vision: una foto -> estado exterior + justificación breve."""
import base64
import json
import os
import re
import cohere
from .config import ESTADOS

MODELO_VISION = "command-a-vision-07-2025"
# TODO C1-A (autoría propia): diseñad y escribid el prompt del modelo visual.
# El texto NO se proporciona. Revisad GUIA_ALUMNADO.md, etapa 5.
# Debe describir tarea, reglas, 4 estados, unknown y formato de respuesta.
PROMPT = """Eres un tasador de coches de segunda mano, analiza la fotografía adjunta y evalúa solo el aspecto exterior visible del coche (carrocería, pintura, abolladuras, arañazos, óxido, cristales, llantas y neumáticos).

Elige UNA sola etiqueta de esta lista, escrita exactamente así:
- "like new": aspecto de coche nuevo, sin marcas ni desgaste visibles.
- "excellent": muy buen estado, con desgaste mínimo apenas perceptible.
- "good": buen estado general, con marcas pequeñas de uso (arañazos leves, pequeños roces).
- "fair": estado aceptable, con daños o desgaste claramente visibles (abolladuras, óxido, pintura deteriorada).

Si en la imagen no se aprecia claramente un coche, o no se ve suficientemente bien como para valorar su exterior (por ejemplo, solo se ve una rueda o una imagen borrosa u oscura), responde "unknown", no trates de adivinar.

Reglas que debes de seguir:
1. No deduzcas nada que no se vea: no puedes opinar sobre el motor, el kilometraje, el historial de accidentes, averías o el funcionamiento mecánico. No puedes dar ideas vagas que no se puedan confirmar visualmente.
2. Basa la justificación solo en detalles visibles en la foto.

Formato de respuesta: devuelve solo un objeto JSON válido, sin texto antes ni después y sin bloques de Markdown, con exactamente estas dos claves:
{"condition": "<una de: like new, excellent, good, fair, unknown>", "reason": "<explicación breve en español, máximo dos frases>"}
No añadas más campos ni puntuaciones de confianza."""


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
    """Devuelve (condition, reason, fuente)."""
    if os.getenv("VISION_MOCK", "0") == "1":
        return "good", "Modo demostración: estado fijo, sin analizar la fotografía.", "MOCK"
    token = os.getenv("COHERE_API_KEY", "").strip()
    if not token:
        raise VisionError("Falta COHERE_API_KEY en el archivo .env")
    if not PROMPT.strip():
        raise VisionError("Falta redactar el prompt visual: tarea C1-A.")

    # Foto -> data URL en base64, usando el MIME real de la imagen
    data_url = f"data:{mimetype};base64," + base64.b64encode(contenido).decode("utf-8")

    # Llamada a Cohere: cualquier fallo de red, clave o límite se convierte en VisionError
    try:
        cliente = cohere.ClientV2(api_key=token)
        respuesta = cliente.chat(
            model=MODELO_VISION,
            temperature=0,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            }],
        )
    except Exception as exc:
        raise VisionError(f"No se pudo consultar Cohere: {exc}") from exc

    # Recoger el texto de la respuesta
    texto = "".join(
        getattr(bloque, "text", "") or "" for bloque in (respuesta.message.content or [])
    )
    if not texto.strip():
        raise VisionError("Cohere devolvió una respuesta vacía.")

    # parsear_respuesta queda fuera del try para no tapar su propio VisionError
    estado, razon = parsear_respuesta(texto)
    return estado, razon, "COHERE"