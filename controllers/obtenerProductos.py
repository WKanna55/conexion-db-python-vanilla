from db.connection import obtener_conexion


def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, categoria, precio, stock
        FROM productos
    """)

    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return [
        {
            "id": producto[0],
            "nombre": producto[1],
            "categoria": producto[2],
            "precio": float(producto[3]),
            "stock": producto[4]
        }
        for producto in productos
    ]