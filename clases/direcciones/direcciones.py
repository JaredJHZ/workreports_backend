import psycopg2
from conexion import conection

class direcciones:
    
    def __init__(self,id,calle,ciudad,estado,cp):
        self.id = id
        self.calle = calle
        self.ciudad = ciudad
        self.estado = estado
        self.cp = cp
        try:
            self.con = conection()
            print("conectado")
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
    
    def save(self):
        try:
            self.con = conection()
            self.cursor = self.con.cursor()
            query = f"INSERT INTO direcciones.direcciones(id, calle, ciudad, estado, cp) VALUES('{self.id}','{self.calle}','{self.ciudad}','{self.estado}','{self.cp}' ); "
            print(query)
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("Direccion guardada")
            return True
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            return False

def get_direccion(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM direcciones.direcciones WHERE id = '{id}' ;"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        id = data[0]
        calle = data[1]
        ciudad = data[2]
        estado = data[3]
        cp = data[4]
        direccion = {
            "id":id,
            "calle":calle,
            "ciudad":ciudad,
            "estado":estado,
            "cp":cp
        }
        return direccion
    except:
        print("error al obtener contraseña")
        return False
    

def modificar_direccion(id, calle, ciudad, estado, cp):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"UPDATE direcciones.direcciones SET calle = '{calle}', ciudad = '{ciudad}', estado = '{estado}', cp = '{cp}' WHERE id = '{id}'"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al modificar direccion")
        return False

def eliminar_direccion(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"DELETE FROM direcciones.direcciones WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al eliminar la direccion")
        return False

def get_all():
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM direcciones.direcciones;"
        cursor.execute(query)
        data = cursor.fetchall()
        directions = []
        for direccion in data:
            direction = {
                "id":direccion[0],
                "calle":direccion[1],
                "ciudad":direccion[2],
                "estado":direccion[3],
                "cp":direccion[4]
            }
            directions.append(direction)
        con.close()
        cursor.close()
        return directions
    except:
        print("error al obtener direcciones")
        return False