# Datos y limitaciones

- Archivo: `coches_50000_completo.csv`, 50.000 filas, 14 columnas, tomado del subconjunto previamente preparado del archivo `vehicles_clean.csv` aportado en clase.
- Procedencia original declarada: anuncios de Craigslist Cars & Trucks (Estados Unidos). Referencia: https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data
- Precio: USD, en anuncios (no necesariamente precio final de venta).
- Kilometraje: **millas**, no kilómetros.
- Categorías de `condition` presentes: fair, good, excellent, like new.
- `condition` es una etiqueta del anuncio y no una inspección visual ni mecánica verificada.
- El modelo proporcionado es un Pipeline scikit-learn (`modelo_con_condition.joblib`) ya entrenado sobre el subconjunto de 50.000 registros, con partición de entrenamiento de 40.000 y prueba de 10.000, usando sklearn 1.8.0.
- Predictores utilizados por ese modelo: `year`, `odometer`, `manufacturer`, `fuel`, `type`, `transmission`, `condition`.
- Las otras columnas del CSV se conservan para practicar ingesta y exploración, aunque no entren en el modelo.
- Uso académico; comprobar los términos de redistribución de la fuente antes de publicar el dataset en repositorios públicos. Recomendación docente: repositorios privados con acceso compartido al profesor.
