CREATE TABLE tabla_x (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    valor NUMERIC
);

INSERT INTO tabla_x (nombre, valor) VALUES 
('Producto A', 100),
('Producto B', 200),
('Producto C', 300);
