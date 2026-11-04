"""Validaciones proporcionadas: NO son tarea del taller."""
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from .config import (MARCAS, COMBUSTIBLES, TIPOS, TRANSMISIONES,
                     ANIO_MIN, ANIO_MAX, MILLAS_MIN, MILLAS_MAX)

MAX_FOTO_BYTES = 5 * 1024 * 1024
MIMES = {"image/jpeg": "JPEG", "image/png": "PNG", "image/webp": "WEBP"}


def validar_datos(form):
    try:
        anio = int(form.get("year", ""))
        millas = int(form.get("odometer", ""))
    except (TypeError, ValueError):
        raise ValueError("El año y el kilometraje deben ser números enteros.")
    marca = str(form.get("manufacturer", "")).strip()
    combustible = str(form.get("fuel", "")).strip()
    tipo = str(form.get("type", "")).strip()
    transmision = str(form.get("transmission", "")).strip()
    if not ANIO_MIN <= anio <= ANIO_MAX:
        raise ValueError(f"El año debe estar entre {ANIO_MIN} y {ANIO_MAX}.")
    if not MILLAS_MIN <= millas <= MILLAS_MAX:
        raise ValueError(f"El kilometraje debe estar entre {MILLAS_MIN} y {MILLAS_MAX} millas.")
    for etiqueta, valor, permitidos in [
        ("Marca", marca, MARCAS), ("Combustible", combustible, COMBUSTIBLES),
        ("Tipo", tipo, TIPOS), ("Transmisión", transmision, TRANSMISIONES),
    ]:
        if valor not in permitidos:
            raise ValueError(f"{etiqueta}: valor no válido ({valor}).")
    return dict(year=anio, odometer=millas, manufacturer=marca,
                fuel=combustible, type=tipo, transmission=transmision)


def validar_foto(archivo):
    if not archivo or not archivo.filename:
        raise ValueError("Selecciona una fotografía del vehículo.")
    mimetype = archivo.mimetype
    if mimetype not in MIMES:
        raise ValueError("La fotografía debe ser JPG, PNG o WEBP.")
    contenido = archivo.read(MAX_FOTO_BYTES + 1)
    if len(contenido) > MAX_FOTO_BYTES:
        raise ValueError("La fotografía no puede superar los 5 MB.")
    if not contenido:
        raise ValueError("La fotografía está vacía.")
    try:
        img = Image.open(BytesIO(contenido))
        if img.format != MIMES[mimetype]:
            raise ValueError("El formato de la imagen no coincide con el archivo.")
        img.verify()
    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("La imagen está dañada o no es válida.") from exc
    return contenido, mimetype
