CREATE TABLE tabla_2 (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT
);

INSERT INTO tabla_2 (descripcion, cantidad) VALUES 
('Descripción 1', 20),
('Descripción 2', 40),
('Descripción 3', 60);
