FROM gcc:latest

WORKDIR /app

COPY main.cpp .

# Instalar dependencias necesarias
RUN apt-get update && \
    apt-get install -y libpq-dev libpqxx-dev && \
    g++ -o cliente main.cpp -lpqxx

CMD ["./cliente"]
