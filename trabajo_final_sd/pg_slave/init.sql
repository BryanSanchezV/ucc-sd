-- En el contenedor esclavo (pg_slave/init.sql)
-- Conexión al servidor maestro
SELECT pg_start_backup('replica_backup', true);

-- Conectar el esclavo al maestro
-- Asegúrate de que estos valores coincidan con la configuración del maestro
-- y la dirección del maestro
SELECT pg_stop_backup();
