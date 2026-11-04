# CarValue AI · Proyecto inicial para alumnado

**Comienza por [`GUIA_ALUMNADO.md`](GUIA_ALUMNADO.md)** (también en PDF dentro de `docs/`). Está diseñada para una sesión de **150 minutos** en equipos de 2-3, con PRs de GitHub obligatorios.

## Tres comandos para orientarte

```bash
cp .env.example .env                 # PowerShell: Copy-Item .env.example .env
docker compose config                # Tras completar las tareas A1-A4
docker compose up --build -d
```

**Importante:** el prompt de Cohere y los formularios de HTML están **vacíos a propósito**; debéis diseñarlos y escribirlos siguiendo las instrucciones. Además el repositorio contiene errores `TODO` intencionales. No es un programa completo: debes integrarlo por ramas. La versión resuelta **NO** se entrega a los estudiantes.

**Modo pruebas** `VISION_MOCK=1`: no usa Cohere ni analiza fotos; siempre devuelve `good`. **Modo real** `VISION_MOCK=0`: necesita clave en `.env` y el ejercicio C1.

- Frontend: http://localhost:5000
- Salud: http://localhost:5000/health
- Historial: http://localhost:5000/historial
- API JSON: http://localhost:5000/api/tasaciones
- Jupyter: http://localhost:8888/lab?token=carvalue123

**Bonus opcional:** `/estadisticas` y `/estadisticas/grafico.png`, con gráficos de anuncios almacenados en PostgreSQL (no se entrega resuelto): [`docs/BONUS_ESTADISTICAS.md`](docs/BONUS_ESTADISTICAS.md).
