import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)


print("Conexión exitosa")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM productos")

productos = cursor.fetchall()

for producto in productos:
    print(producto)

cursor.close()
conexion.close()