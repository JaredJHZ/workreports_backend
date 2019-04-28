import psycopg2
from conexion import conection

class materiales:

    def __init__(self,id,nombre, costo_unitario):
        self.id = id
        self.nombre = nombre
        self.costo_unitario = costo_unitario

    def save(self):
        try:
            self.con = conection()
            self.cursor = self.con.cursor()
            query = f"INSERT INTO materiales.materiales(id, nombre, costo_unitario) VALUES('{self.id}',\
                '{self.nombre}','{self.costo_unitario}' ); "
            print(query)
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("material guardado")
            return True
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            return False

def get_material(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM materiales.materiales WHERE id = '{id}' ;"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        id = data[0]
        nombre = data[1]
        costo_unitario = data[2]
        material = {
            "id":id,
            "nombre":nombre,
            "costo_unitario":costo_unitario
        }
        return material
    except:
        print("error al obtener material")
        return False
    

def modificar_material(id, nombre, costo_unitario):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"UPDATE materiales.materiales SET nombre = '{nombre}', costo_unitario = '{costo_unitario}' WHERE id = '{id}'"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al modificar material")
        return False

def eliminar_material(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"DELETE FROM materiales.materiales WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al eliminar el material")
        return False

def get_all():
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM materiales.materiales;"
        cursor.execute(query)
        data = cursor.fetchall()
        materiales = []
        for mat in data:
            material = {
                "id":mat[0],
                "nombre":mat[1],
                "costo_unitario":mat[2]
            }
            materiales.append(material)
        con.close()
        cursor.close()
        return materiales
    except:
        print("error al obtener materiales")
        return False