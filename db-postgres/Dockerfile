FROM postgres:latest
WORKDIR /app
COPY requirements.txt /app
COPY app.py /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]