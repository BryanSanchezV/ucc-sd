FROM alpine:latest
WORKDIR /app
 
# Instalar dependencias necesarias
RUN apk update && \
    apk add --no-cache g++ make cmake postgresql-dev curl
 
# Descargar e instalar libpqxx
RUN curl -L https://github.com/jtv/libpqxx/archive/7.6.0.tar.gz | tar xz && \
    cd libpqxx-7.6.0 && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr . && \
    make && make install && \
    cd .. && rm -rf libpqxx-7.6.0
 
# Copiar el código fuente de la aplicación
COPY src/main.cpp /app
 
# Compilar la aplicación
RUN g++ -o application main.cpp -lpqxx -lpq
 
# Ejecutar la aplicación
CMD ["./application"]