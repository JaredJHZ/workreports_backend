import psycopg2

class lista_de_materiales:

    def __init__(self,id):
        self.id = id

    def save(self):
        try:
            self.con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
            self.cursor = self.con.cursor()
            query = f"INSERT INTO materiales.lista_de_materiales(id) VALUES('{self.id}' ); "
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            print("lista de materiales guardada")
            return True
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            return False

def get_lista_de_materiales(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"SELECT * FROM materiales.lista_de_materiales WHERE id = '{id}' ;"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        id = data[0]
        lista = {
            "id":id
        }
        return lista
    except:
        print("error al obtener la lista de materiales")
        return False
    

def eliminar_lista_de_materiales(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"DELETE FROM materiales.lista_de_materiales WHERE id = '{id}';"
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al eliminar la lista de materiales")
        return False

def get_all():
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"SELECT * FROM materiales.lista_de_materiales;"
        cursor.execute(query)
        data = cursor.fetchall()
        lists = []
        for material in data:
            mater = {
                "id":material[0],
            }
            listas.append(mater)
        con.close()
        cursor.close()
        return lists
    except:
        print("error al obtener listas de materiales")
        return False

def agregar_materiales_a_la_lista(id,materiales):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        for material in materiales:
            id_m = material["id"]
            numero = material["numero"]
            query = f"INSERT INTO materiales.grupo_de_materiales (id_lista_de_materiales, id_material, numero) VALUES ('{id}', '{id_m}', '{numero}') "
            cursor.execute(query)
            con.commit()
        con.close()
        cursor.close()
        return True
    except:
        print("error al agregar materiales")
        return False

def get_precio_total(id):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        total = 0
        query = f"SELECT materiales.materiales.costo_unitario, materiales.grupo_de_materiales.numero FROM materiales.materiales INNER JOIN materiales.grupo_de_materiales ON materiales.materiales.id = materiales.grupo_de_materiales.id_material WHERE materiales.grupo_de_materiales.id_lista_de_materiales = '{id}'; "
        cursor.execute(query)
        data = cursor.fetchall()
        for precions in data:
            total += precions[0] * precions[1]
        print(total)
        con.close()
        cursor.close()
        return total
    except:
        print("error al recuperar precios de materiales")
        return False