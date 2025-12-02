from conexionBD import *

class Operaciones:
    @staticmethod
    def insertar(n1, n2, signo, resultado):
        try:
            cursor.execute("INSERT INTO operaciones VALUES (null, NOW(), %s, %s, %s, %s)", (n1, n2, signo, resultado))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM operaciones")
            operacion = cursor.fetchall()
            return operacion
        except:
            return []

    @staticmethod
    def actualizar(n1, n2, signo, resultado, id):
        try:
            cursor.execute("UPDATE operaciones SET fecha=NOW(), n1=%s, n2=%s, signo=%s, resultado=%s where id=%s", (n1, n2, signo, resultado, id))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM operaciones WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False
