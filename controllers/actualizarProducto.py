from db.connection import obtener_conexion

def actualizar_producto(id, nombre, categoria, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        UPDATE productos
        SET nombre = %s,
            categoria = %s,
            precio = %s,
            stock = %s
        WHERE id = %s
    """

    valores = (nombre, categoria, precio, stock, id)

    cursor.execute(sql, valores)

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas