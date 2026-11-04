FROM python:3.12-slim
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
# TODO A3: instala las dependencias Python durante la build
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
COPY templates/ ./templates/
COPY models/ ./models/
COPY tests/ ./tests/
COPY pytest.ini ./
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "app.main", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
