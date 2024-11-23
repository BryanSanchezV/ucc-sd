# Usamos Python como base
FROM python:3.9-slim

# Instalar dependencias necesarias
RUN pip install psycopg2-binary cx_Oracle

# Copiar los archivos del ETL
COPY etl/etl_script.py /etl/etl_script.py

# Configurar el punto de entrada
WORKDIR /etl
CMD ["python", "etl_script.py"]

