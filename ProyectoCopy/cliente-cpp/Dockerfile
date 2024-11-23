FROM gcc:latest

# Instalar dependencias de PostgreSQL
RUN apt-get update && apt-get install -y libpqxx-dev

# Copiar los archivos del cliente
WORKDIR /app
COPY main.cpp Makefile ./

# Compilar el programa
RUN make

# Ejecutar el programa
CMD ["./client"]
