FROM openjdk:latest

# Copiar los archivos del cliente
WORKDIR /app
COPY cliente-java/Main.java ./

# Compilar el programa
RUN javac Main.java

# Ejecutar el programa
CMD ["java", "main"]
