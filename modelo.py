from database_config import obtener_conexion

class ProductoModelo:
    @staticmethod
    def obtener_todos():
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos ORDER BY id DESC")
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return productos

    @staticmethod
    def guardar(nombre, categoria, precio, stock):
        conn = obtener_conexion()
        cursor = conn.cursor()
        sql = "INSERT INTO productos (nombre, categoria, precio, stock) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, categoria, precio, stock))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar(id_producto):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def restar_stock(id_producto):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET stock = stock - 1 WHERE id = %s AND stock > 0", (id_producto,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def sumar_stock(id_producto):
        conn = obtener_conexion()
        cursor = conn.cursor()
        # Suma una unidad al stock actual
        cursor.execute("UPDATE productos SET stock = stock + 1 WHERE id = %s", (id_producto,))
        conn.commit()
        cursor.close()
        conn.close()