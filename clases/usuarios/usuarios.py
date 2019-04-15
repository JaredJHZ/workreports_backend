import psycopg2
import jwt
from werkzeug.security import generate_password_hash, \
     check_password_hash
from querys import usuarios as user_querys
from configuration import key
class Usuario:

    def __init__(self, usuario, password,privilegios, id):
        self.usuario = usuario
        self.password = password
        self.id = id
        self.privilegios = privilegios
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
            self.cursor.execute(query,(self.id,self.usuario,self.pw_hash,self.privilegios))
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
        query = f"SELECT password, id FROM usuarios WHERE usuario = '{username}' "
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        if check_password_hash(data[0], password):
            return data
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

def set_token(id):
    try:
        user = get_data(id)
        id = user[0]
        username = user[1]
        permission = user[3]
        token = jwt.encode({"id":id, "user":username, "permission": permission}, key)
        return token
    except psycopg2.OperationalError as e:
       print('Unable to connect!\n{0}').format(e)
       return False
