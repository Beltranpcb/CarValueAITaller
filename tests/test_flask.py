"""Prueba de extremo a extremo SIN consumir créditos de Cohere."""
import io
import os
from PIL import Image
os.environ["VISION_MOCK"]="1"
from app.main import app

def mini_png():
    b=io.BytesIO()
    Image.new("RGB", (100,100), "white").save(b, format="PNG")
    b.seek(0)
    return b

def test_formulario_y_salud():
    client=app.test_client()
    assert client.get("/health").status_code == 200
    html=client.get("/")
    assert html.status_code == 200
    assert b"CarValue AI" in html.data

def test_post_y_persistencia():
    client=app.test_client()
    respuesta=client.post("/tasar",data={
      "manufacturer":"toyota", "year":"2016", "odometer":"80000",
      "fuel":"gas", "type":"sedan", "transmission":"automatic",
      "foto":(mini_png(),"coche.png","image/png")
    }, content_type="multipart/form-data")
    assert respuesta.status_code == 200, respuesta.data[:900]
    assert b"MOCK" in respuesta.data
    historial=client.get("/historial")
    assert historial.status_code == 200
    assert b"toyota" in historial.data.lower()
    api=client.get("/api/tasaciones")
    assert api.status_code == 200 and isinstance(api.json,list) and len(api.json)>0
