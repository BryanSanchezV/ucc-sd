CREATE TABLE tabla_1 (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    valor NUMERIC
);

INSERT INTO tabla_1 (nombre, valor) VALUES 
('Producto 1', 200),
('Producto 2', 400),
('Producto 3', 600);
