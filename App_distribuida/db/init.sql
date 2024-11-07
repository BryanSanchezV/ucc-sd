-- db/init.sql
CREATE TABLE IF NOT EXISTS mytable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    value INTEGER
);

INSERT INTO mytable (name, value) VALUES ('example', 100);
