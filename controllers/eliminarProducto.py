from db.connection import obtener_conexion

def eliminar_producto(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "DELETE FROM productos WHERE id = %s"

    cursor.execute(sql, (id,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas