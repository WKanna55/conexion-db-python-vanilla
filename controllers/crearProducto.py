from db.connection import obtener_conexion

def crear_producto(nombre, categoria, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO productos (nombre, categoria, precio, stock)
        VALUES (%s, %s, %s, %s)
    """

    valores = (nombre, categoria, precio, stock)

    cursor.execute(sql, valores)

    conexion.commit()

    id_producto = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_producto