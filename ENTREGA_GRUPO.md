# Entrega · CarValue AI

**Grupo:** ...

**Repositorio GitHub (privado, con acceso al profesor):** https://github.com/...

| Integrante | Parte implementada | Rama | 2 commits propios | URL del PR | ¿Quién revisó? |
|---|---|---|---|---|---|
| ... | ... | ... | Sí/No | ... | ... |
| ... | ... | ... | Sí/No | ... | ... |
| ... (si hay 3) | ... | ... | Sí/No | ... | ... |

## Pruebas de funcionamiento

- [ ] Docker Compose: 3 servicios activos.
- [ ] `SELECT COUNT(*) FROM anuncios` devuelve 50000.
- [ ] `GET /health` OK.
- [ ] Formulario POST sin JavaScript; fotografía recibida en Flask.
- [ ] Modo `MOCK` integra modelo ML + SQLAlchemy y guarda tasación.
- [ ] `/historial` muestra tasación.
- [ ] Modo real Cohere (`VISION_MOCK=0`): probado / no probado por falta de clave o límite de uso (explicar).
- [ ] `docker compose exec app pytest -q`: ___ tests superados.
- [ ] `.env` no está versionado.
- [ ] Prompt propio escrito en `app/vision.py` (sin usar uno prefabricado).
- [ ] Formulario HTML y página de resultado programados por el equipo.

## Reflexión breve (4 preguntas)

**1. HTTP frente a SQL:** ...

**2. Host `db` frente a `localhost`:** ...

**3. Valor del PR respecto a commits directos en `main`:** ...

**4. Qué hacemos si Cohere devuelve `unknown`:** ...

## Incidencias que no pudimos resolver (si las hay)

...

## BONUS (solo si se ha hecho)

- [ ] `/estadisticas` muestra gráfica(s) basadas en consultas a PostgreSQL `anuncios`.
- [ ] `/estadisticas/grafico.png` responde `image/png`.
- [ ] PR `feature/dashboard` revisado: URL ___

## Decisiones de implementación

**Criterio del prompt (cómo definimos las categorías y el caso `unknown`):** ...

**Decisión del HTML (atributos de formulario y envío de foto):** ...
