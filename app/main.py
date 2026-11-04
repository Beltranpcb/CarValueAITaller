"""Flask sin JavaScript: GET formulario, POST tasación, GET historial."""
from flask import Flask, render_template, request
from .config import MARCAS, COMBUSTIBLES, TIPOS, TRANSMISIONES, ESTADOS
from .validators import validar_datos, validar_foto
from .predictor import predecir_precio
from .vision import clasificar_estado, VisionError
from .db import crear_tablas, guardar_tasacion, obtener_ultimas_tasaciones

app = Flask(__name__, template_folder="../templates")
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024 + 8192
OPCIONES = dict(marcas=MARCAS, combustibles=COMBUSTIBLES,
                tipos=TIPOS, transmisiones=TRANSMISIONES)

with app.app_context():
    crear_tablas()

@app.get("/")
def inicio():
    return render_template("index.html", opciones=OPCIONES)

@app.post("/tasar")
def tasar():
    try:
        datos = validar_datos(request.form)
        foto, mimetype = validar_foto(request.files.get("foto"))
        # TODO B2: unir vision -> modelo -> base de datos; ver CONTRATO_COMPONENTES.md
        # TODO B2: llama a clasificar_estado; comprueba que NO sea unknown.
        # TODO B2: llama a predecir_precio y construye registro para guardar_tasacion.
        # TODO B2: devuelve resultado.html con datos, estado, razon, precio, fuente e identificador.
        raise NotImplementedError("Completa la ruta POST /tasar")
    except (ValueError, VisionError, NotImplementedError) as exc:
        return render_template("index.html", opciones=OPCIONES, error=str(exc)), 400

@app.get("/historial")
def historial():
    filas = obtener_ultimas_tasaciones(limite=10)
    return render_template("historial.html", filas=filas)

@app.get("/api/tasaciones")
def api_tasaciones():
    """API JSON mínima: consultar las últimas tasaciones sin JavaScript."""
    filas = obtener_ultimas_tasaciones(limite=10)
    return [dict(id=f.id, manufacturer=f.manufacturer, year=f.year,
                 condition=f.condition, price_prediction=f.price_prediction)
            for f in filas]

@app.get("/health")
def health():
    return {"status": "ok", "service": "carvalue"}


# BONUS D3: cuando el núcleo funcione, incorporar (sin cambiar otras rutas):
#   GET /estadisticas              -> renderizar pagina de visualización
#   GET /estadisticas/grafico.png  -> responder image/png desde PostgreSQL
# Ver docs/BONUS_ESTADISTICAS.md. NO usar JavaScript ni leer el CSV aquí.
