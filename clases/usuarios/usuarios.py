import psycopg2
import jwt
from werkzeug.security import generate_password_hash, \
     check_password_hash
from configuration import get_key
from conexion import conection

class Usuario:

    def __init__(self, usuario, password,privilegios, id):
        self.usuario = usuario
        self.password = password
        self.id = id
        self.privilegios = privilegios
        try:
            self.con = conection()
            print("conectado")
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
        else:
            print("error")
    
    def save(self):
        try:
            self.con = conection()
            self.cursor = self.con.cursor()
            self.pw_hash = generate_password_hash(self.password)
            query = f"INSERT INTO usuarios (id, usuario, password,privilegios) VALUES('{self.id}',\
                     '{self.usuario}', '{self.pw_hash}', '{self.privilegios}');"
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("guardado correcto")
            return True
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)


def get_all_usuarios():
    try:
        con = conection()
        cursor = con.cursor()
        query = "SELECT * FROM usuarios;"
        cursor.execute(query)
        data = cursor.fetchall()
        usuarios = []
        for user in data:
            usuario = {
                'id': user[0],
                'usuario': user[1],
                'privilegios': user[3]
            }
            usuarios.append(usuario)
        cursor.close()
        con.close()
        return usuarios
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)


def get_data(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM usuarios WHERE id = '{id}';"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        return data
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)

def check_password(username,password):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT password, id FROM usuarios WHERE usuario = '{username}' "
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        if data == None:
            return False
        if check_password_hash(data[0], password):
            return data
    except psycopg2.OperationalError as e:
       print('Unable to connect!\n{0}').format(e)
       return False

def delete_user(id):
    try:
        con = conection()
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
        token = jwt.encode({"id":id, "user":username, "permission": permission}, get_key() )
        return token
    except psycopg2.OperationalError as e:
       print('Unable to connect!\n{0}').format(e)
       return False

def modificar_usuario(id, usuario, password, privilegios):
    try:
        con = conection()
        cursor = con.cursor()
        passW = generate_password_hash(password)
        print(passW)
        query = f"UPDATE usuarios SET usuario = '{usuario}', password = '{passW}', privilegios = '{privilegios}'  \
                    WHERE id = '{id}'"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except psycopg2.OperationalError as e:
        print(e)
        return False
