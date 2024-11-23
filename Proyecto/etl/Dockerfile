# Usamos Python como base
FROM python:3.9-slim

# Instalar dependencias necesarias
RUN pip install psycopg2-binary cx_Oracle

# Copiar los archivos del ETL
COPY etl_script.py /app/etl_script.py

# Configurar el punto de entrada
WORKDIR /app
CMD ["python", "etl_script.py"]

