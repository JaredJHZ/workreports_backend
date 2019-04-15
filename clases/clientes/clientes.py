import psycopg2

class clientes:

    def __init__(self,id,ap_paterno,ap_materno,nombres,id_direccion,email):
        self.id = id
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.nombres = nombres
        self.id_direccion = id_direccion
        self.email = email

    def save(self):
        try:
            self.con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
            self.cursor = self.con.cursor()
            query = f"INSERT INTO clientes.clientes(id, ap_paterno, ap_materno, nombre, id_direccion, email) VALUES('{self.id}','{self.ap_paterno}','{self.ap_materno}','{self.nombres}','{self.id_direccion}', '{self.email}' ); "
            print(query)
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("cliente guardados")
            return True
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            return False

def get_cliente(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"SELECT * FROM clientes.clientes WHERE id = '{id}' ;"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        id = data[0]
        nombre = data[1]
        ap_paterno = data[2]
        ap_materno = data[3]
        id_direccion = data[4]
        email = data[5]
        cliente = {
            "id":id,
            "nombre":nombre,
            "ap_paterno":ap_paterno,
            "ap_materno":ap_materno,
            "id_direccion":id_direccion,
            "email":email
        }
        return cliente
    except:
        print("error al obtener cliente")
        return False
    

def modificar_cliente(id, nombre, ap_paterno, ap_materno, id_direccion, email):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"UPDATE clientes.clientes SET nombre = '{nombre}', ap_paterno = '{ap_paterno}', ap_materno = '{ap_materno}', id_direccion = '{id_direccion}', email = '{email}' WHERE id = '{id}'"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al modificar cliente")
        return False

def eliminar_empleado(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"DELETE FROM clientes.clientes WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al eliminar al cliente")
        return False

def get_all():
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"SELECT * FROM clientes.clientes;"
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
    except:
        print("error al obtener clientes")
        return False