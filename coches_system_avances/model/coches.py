
from conexionBD import conexion, cursor
class Autos:
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def eliminar(id_coche):
        try:
            cursor.execute("DELETE FROM coches WHERE id_coche=%s", (id_coche,))
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def insertar(color, marca, modelo, velocidad, caballaje, plazas):
        try:
            sql = "INSERT INTO coches VALUES(null,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (color, marca, modelo, velocidad, caballaje, plazas))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    @staticmethod
    def actualizar(id_coche, color, marca, modelo, velocidad, caballaje, plazas):
        try:
            sql = "UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id_coche=%s"
            cursor.execute(sql, (color, marca, modelo, velocidad, caballaje, plazas, id_coche))
            conexion.commit()
            return True
        except:
            return False