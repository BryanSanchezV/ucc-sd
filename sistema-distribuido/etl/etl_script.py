import psycopg2
import cx_Oracle

pg_conn = psycopg2.connect(
    dbname="ppal_db", user="user", password="password", host="slave1", port="5432"
)
pg_cursor = pg_conn.cursor()

oracle_conn = cx_Oracle.connect("user/password@oracleGvenz:1521/ORCL")
oracle_cursor = oracle_conn.cursor()

pg_cursor.execute("SELECT * FROM data_warehouse;")
rows = pg_cursor.fetchall()

for row in rows:
    oracle_cursor.execute(
        "INSERT INTO data_warehouse_oracle (id, data) VALUES (:1, :2)",
        (row[0], row[1]),
    )

oracle_conn.commit()
pg_cursor.close()
pg_conn.close()
oracle_cursor.close()
oracle_conn.close()
