import psycopg2
import cx_Oracle

# Conexión a PostgreSQL (Principal y Slave)
pg_ppal_conn = psycopg2.connect(
    host="ppal-db",
    database="ppal_db",
    user="user",
    password="password"
)

pg_slave_conn = psycopg2.connect(
    host="slave-db",
    database="slave_db",
    user="user",
    password="password"
)

# Conexión a Oracle
oracle_conn = cx_Oracle.connect(
    user="system",
    password="password",
    dsn="oracle-dwh:1521/dwh"
)

# ETL: Extraer datos de PostgreSQL y cargarlos en Oracle
def etl_process():
    try:
        # Extraer datos de PostgreSQL Principal
        with pg_ppal_conn.cursor() as ppal_cursor:
            ppal_cursor.execute("SELECT * FROM tabla_x")
            ppal_data = ppal_cursor.fetchall()

        # Extraer datos de PostgreSQL Slave
        with pg_slave_conn.cursor() as slave_cursor:
            slave_cursor.execute("SELECT * FROM tabla_y")
            slave_data = slave_cursor.fetchall()

        # Cargar datos en Oracle
        with oracle_conn.cursor() as oracle_cursor:
            for row in ppal_data:
                oracle_cursor.execute(
                    "INSERT INTO data_warehouse (id, nombre, valor) VALUES (:1, :2, :3)",
                    row
                )
            for row in slave_data:
                oracle_cursor.execute(
                    "INSERT INTO data_warehouse_slave (id, descripcion, cantidad) VALUES (:1, :2, :3)",
                    row
                )
            oracle_conn.commit()

        print("ETL completado con éxito.")
    except Exception as e:
        print(f"Error en el ETL: {e}")

if __name__ == "__main__":
    etl_process()
