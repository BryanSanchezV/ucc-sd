FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY etl_script.py .

CMD ["python", "etl_script.py"]
