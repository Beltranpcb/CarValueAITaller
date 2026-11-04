# Contratos entre componentes (no cambiéis estos nombres)

## Flujo

1. `GET /` muestra el HTML `templates/index.html`.
2. `POST /tasar` recibe desde `request.form` los campos `year`, `odometer`, `manufacturer`, `fuel`, `type`, `transmission` y desde `request.files` el campo `foto`.
3. `validar_datos(form)` devuelve un diccionario de Python con los seis campos validados.
4. `validar_foto(archivo)` devuelve `(contenido_bytes, mimetype)`. Ya está implementado.
5. `clasificar_estado(contenido_bytes, mimetype)` devuelve `(condition, reason, source)`; `source` es `MOCK` o `COHERE`. `condition` pertenece a `{fair, good, excellent, like new, unknown}`.
6. `predecir_precio(datos, estado)` devuelve un `float` USD. No se llama si estado es `unknown`.
7. `guardar_tasacion(registro)` guarda el diccionario y devuelve el `id` entero. Campos del registro: los seis datos originales más `condition`, `justificacion`, `price_prediction`, `vision_source`.
8. `resultado.html` recibe variables `datos`, `estado`, `razon`, `precio`, `fuente`, `identificador`.
9. `GET /historial` llama a `obtener_ultimas_tasaciones(limite=10)` y recibe objetos ORM.

## Modelo de ML

| Tipo | Nombre | Ejemplo |
|---|---|---|
| numérico | `year` | `2016` |
| numérico | `odometer` | `80000` (millas) |
| categórico | `manufacturer` | `toyota` |
| categórico | `fuel` | `gas` |
| categórico | `type` | `sedan` |
| categórico | `transmission` | `automatic` |
| categórico | `condition` | `good` (procede solo de Cohere) |

El pipeline ya contiene su encoder de categorías. No aplicar un segundo encoding manual, no cambiar los nombres de columnas y no usar `car_age`.

## Persistencia

- Tabla `anuncios`: todos los **50.000** registros del CSV completo, creada con `pandas.DataFrame.to_sql()` desde Jupyter.
- Tabla `tasaciones`: registros creados por Flask y SQLAlchemy ORM. La foto no se almacena.

## Sin JavaScript

El formulario debe enviar sus datos por POST a `/tasar` e incluir la codificación correcta para enviar fotografías. El navegador manda los datos; Flask genera HTML desde el servidor. **La estructura del formulario la escribís vosotros.**

10. `GET /api/tasaciones` devuelve las últimas tasaciones en JSON: ejemplo de API Flask sin JavaScript.

## Bonus de analítica (opcional)

- `GET /estadisticas`: HTML con la pregunta de negocio, mensaje de error si `anuncios` todavía no existe y gráfica(s) cuando existan datos.
- `GET /estadisticas/grafico.png`: respuesta con MIME `image/png`, generada con Matplotlib desde consulta a **PostgreSQL `anuncios`**.
- `app/analytics.py` define contratos `obtener_resumen()` y `grafico_png(resumen)`; véase `BONUS_ESTADISTICAS.md`.
