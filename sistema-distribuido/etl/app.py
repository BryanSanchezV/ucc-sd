from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_data_from_table(table_name):
    conn = psycopg2.connect(
        dbname="ppal_db",
        user="user",
        password="password",
        host="slave1"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/tabla_x")
def tabla_x():
    data = get_data_from_table("tabla_x")
    return jsonify(data)

@app.route("/tabla_y")
def tabla_y():
    data = get_data_from_table("tabla_y")
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
