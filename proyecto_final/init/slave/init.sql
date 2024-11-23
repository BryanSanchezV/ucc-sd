CREATE TABLE tabla_y (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT
);

INSERT INTO tabla_y (descripcion, cantidad) VALUES 
('Descripción A', 10),
('Descripción B', 20),
('Descripción C', 30);
