import psycopg2
from psycopg2 import sql
import random
import time

# Configuración de conexión al maestro
DB_MASTER_CONFIG = {
    "dbname": "main_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",  # Conexión al contenedor maestro
    "port": 5432          # Puerto del maestro
}

# Configuración de conexión al esclavo
DB_SLAVE_CONFIG = {
    "dbname": "main_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",  # Conexión al contenedor esclavo
    "port": 5433          # Puerto del esclavo
}

# Función para generar datos aleatorios
def generar_datos():
    nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]
    edad = random.randint(18, 65)
    salario = round(random.uniform(1000, 5000), 2)
    return random.choice(nombres), edad, salario

# Función para insertar datos en el maestro
def insertar_datos():
    try:
        # Conexión al maestro
        conn = psycopg2.connect(**DB_MASTER_CONFIG)
        cursor = conn.cursor()

        # Generar datos
        nombre, edad, salario = generar_datos()

        # Insertar datos
        query = sql.SQL("INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s);")
        cursor.execute(query, (nombre, edad, salario))

        # Confirmar cambios
        conn.commit()
        print(f"\n➡️  Dato insertado en el maestro: {nombre}, {edad}, {salario}")

        # Cerrar conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error al insertar datos: {e}")

# Función para extraer y mostrar datos de una base de datos
def mostrar_datos(db_config, origen):
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Obtener todos los datos
        query = sql.SQL("SELECT * FROM empleados;")
        cursor.execute(query)
        rows = cursor.fetchall()

        # Mostrar los datos
        print(f"\n📋 Datos del {origen}:")
        for row in rows:
            print(f"  - ID: {row[0]}, Nombre: {row[1]}, Edad: {row[2]}, Salario: {row[3]}")

        # Cerrar conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error al mostrar datos del {origen}: {e}")

# Ejecución continua
if __name__ == "__main__":
    while True:
        # Insertar datos en el maestro
        insertar_datos()

        # Mostrar datos del maestro
        mostrar_datos(DB_MASTER_CONFIG, "maestro")

        # Mostrar datos del esclavo
        mostrar_datos(DB_SLAVE_CONFIG, "esclavo")

        # Esperar 5 segundos antes de la siguiente iteración
        time.sleep(5)
