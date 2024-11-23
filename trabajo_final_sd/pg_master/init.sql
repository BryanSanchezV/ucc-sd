-- Crear una tabla para datos
CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    salario NUMERIC(10, 2)
);

-- Configurar la publicación de datos
CREATE PUBLICATION replicacion_empleados FOR ALL TABLES;
