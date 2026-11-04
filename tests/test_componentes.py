"""Autocomprobaciones. Ejecutar: docker compose exec app pytest -q"""
from app.validators import validar_datos
from app.predictor import predecir_precio
from app.vision import parsear_respuesta, clasificar_estado

DATOS = dict(year="2016",odometer="80000",manufacturer="toyota",
             fuel="gas",type="sedan",transmission="automatic")

def test_datos_validos():
    out=validar_datos(DATOS)
    assert out["year"] == 2016 and out["odometer"] == 80000

def test_modelo_joblib():
    precio=predecir_precio(validar_datos(DATOS), "good")
    assert 0 < precio < 500_000

def test_parser_cohere():
    estado, razon=parsear_respuesta('{"condition":"excellent","reason":"Pintura cuidada"}')
    assert estado == "excellent" and razon

def test_mock_de_vision(monkeypatch):
    monkeypatch.setenv("VISION_MOCK","1")
    estado,razon,fuente=clasificar_estado(b"foto", "image/jpeg")
    assert estado == "good" and fuente == "MOCK"
