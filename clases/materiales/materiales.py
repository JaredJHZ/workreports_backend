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
            query = f"INSERT INTO workreports.materiales(id, nombre, costo) VALUES('{self.id}',\
                '{self.nombre}','{self.costo_unitario}' ); "
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("material guardado")
            return True
        except psycopg2.Error as e:
            return (False , e.pgcode, e)

def get_material(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM workreports.materiales WHERE id = '{id}' ;"
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
    except psycopg2.Error as e:
        return (False , e.pgcode, e)

def modificar_material(id, nombre, costo_unitario):
    try:
        con = conection()
        cursor = con.cursor()
        print("xd")
        query = f"UPDATE workreports.materiales SET nombre = '{nombre}', costo = '{costo_unitario}' WHERE id = '{id}'"
        print(query)
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except psycopg2.Error as e:
        return (False , e.pgcode, e)

def eliminar_material(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"DELETE FROM workreports.materiales WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except psycopg2.Error as e:
        return (False , e.pgcode, e)

def get_all():
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM workreports.materiales;"
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
    except psycopg2.Error as e:
        return (False , e.pgcode, e)