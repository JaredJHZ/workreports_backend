import psycopg2
from werkzeug.security import generate_password_hash, \
     check_password_hash
from querys import usuarios as user_querys
class Usuario:

    def __init__(self, usuario, password,id):
        self.usuario = usuario
        self.password = password
        self.id = id
        try:
            self.con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
            print("conectado")
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
        else:
            print("error")
    
    def save(self):
        try:
            self.con = psycopg2.connect("dbname='workreports' user='jaredhz' host='localhost' password='Atleti123@'")
            self.cursor = self.con.cursor()
            self.pw_hash = generate_password_hash(self.password)
            query = user_querys.usuarios['insertar']
            print(self.usuario)
            self.cursor.execute(query,(self.id,self.usuario,self.pw_hash))
            self.con.commit()
            self.con.close()
            print("guardado correcto")
            return True
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)

    
def get_data(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='localhost' password='Atleti123@'")
        cursor = con.cursor()
        query = user_querys.usuarios['consultar_usuario']
        cursor.execute(query, id)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        return data
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)

def check_password(username,password):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='localhost' password='Atleti123@'")
        cursor = con.cursor()
        query = f"SELECT password FROM usuarios WHERE usuario = '{username}' "
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        return check_password_hash(data[0], password)
    except psycopg2.OperationalError as e:
       print('Unable to connect!\n{0}').format(e)

def delete_user(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='localhost' password='Atleti123@'")
        cursor = con.cursor()
        query = f"DELETE FROM usuarios WHERE \"id\" LIKE '{id}' "
        cursor.execute(query)
        con.commit()
        print("eliminacion completada")
        cursor.close()
        con.close()
        return True
    except psycopg2.OperationalError as e:
       print('Unable to connect!\n{0}').format(e)
       return False