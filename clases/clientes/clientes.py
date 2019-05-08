import psycopg2
from conexion import conection
class clientes:

    def __init__(self,id,ap_paterno,ap_materno,nombres,calle,ciudad,estado,cp,email):
        self.id = id
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.nombres = nombres
        self.calle = calle
        self.ciudad = ciudad
        self.estado = estado
        self.cp = cp
        self.email = email

    def save(self):
        try:
            self.con = conection()
            self.cursor = self.con.cursor()
            query = f"INSERT INTO workreports.clientes(id, ap_paterno, ap_materno, nombre, email, calle,ciudad,estado,cp)\
            VALUES('{self.id}','{self.ap_paterno}','{self.ap_materno}','{self.nombres}',\
            '{self.email}', '{self.calle}', '{self.ciudad}','{self.estado}','{self.cp}' ); "
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            return True
        except psycopg2.Error as e:
            return (False , e.pgcode, e)

def get_cliente(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM workreports.clientes WHERE id = '{id}' ;"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        id = data[0]
        nombre = data[1]
        ap_paterno = data[2]
        ap_materno = data[3]
        email = data[4]
        calle = data[5]
        ciudad = data[6]
        estado = data[7]
        cp = data[8]

        cliente = {
            "id":id,
            "nombre":nombre,
            "ap_paterno":ap_paterno,
            "ap_materno":ap_materno,
            "email":email,
            "calle":calle,
            "ciudad":ciudad,
            "estado":estado,
            "cp":cp
        }
        return cliente
    except psycopg2.Error as e:
        return (False , e.pgcode, e)
    

def modificar_cliente(id, nombre, ap_paterno, ap_materno, calle, ciudad, estado, cp ):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"UPDATE workreports.clientes SET nombre = '{nombre}', ap_paterno = '{ap_paterno}', \
            ap_materno = '{ap_materno}', calle = '{calle}', ciudad = '{ciudad}',\
            estado = '{estado}', cp = '{cp}' WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except psycopg2.Error as e:
        return (False , e.pgcode, e)

def eliminar_empleado(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"DELETE FROM workreports.clientes WHERE id = '{id}';"
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
        query = f"SELECT * FROM workreports.clientes;"
        cursor.execute(query)
        data = cursor.fetchall()
        clients = []
        for client in data:
            cliente = {
                "id":client[0],
                "nombre":client[1],
                "ap_paterno":client[2],
                "ap_materno":client[3],
                "id_direccion":client[4]
            }
            clients.append(cliente)
        con.close()
        cursor.close()
        return clients
    except psycopg2.Error as e:
        return (False , e.pgcode, e)