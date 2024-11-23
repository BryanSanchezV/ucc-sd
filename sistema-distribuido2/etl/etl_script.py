import psycopg2
import time

while True:
    try:
        conn_slave1 = psycopg2.connect(
            dbname="ppal_db", user="user", password="password", host="slave1", port="5432"
        )
        conn_slave2 = psycopg2.connect(
            dbname="slave2_db", user="user", password="password", host="slave2", port="5433"
        )

        with conn_slave1.cursor() as cur1, conn_slave2.cursor() as cur2:
            cur1.execute("SELECT * FROM tabla_x;")
            data = cur1.fetchall()
            for record in data:
                cur2.execute("INSERT INTO tabla_x_slave (usuario, cargo) VALUES (%s, %s);", record[1:])
            conn_slave2.commit()

        print("Datos replicados.")
        time.sleep(2)

    except Exception as e:
        print("Error:", e)
    finally:
        if 'conn_slave1' in locals():
            conn_slave1.close()
        if 'conn_slave2' in locals():
            conn_slave2.close()
