import psycopg2

def guardar_serie_de_tareas(id_serie_de_tareas,tareas):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"INSERT INTO tareas.serie_de_tareas (id) VALUES ('{id_serie_de_tareas}');"
        cursor.execute(query)
        con.commit()
        for tarea in tareas:
            query = f"INSERT INTO tareas.grupo_de_tareas (id_serie_de_tareas, id_tarea) VALUES('{id_serie_de_tareas}',\
            '{tarea}');"
            cursor.execute(query)
            con.commit()
        con.close()
        return True
    except:
        return False

def guardar_lista_de_materiales(id_lista_de_materiales, materiales):
    try:
        con = psycopg2.connect("dbname='workreports' user='jaredhz' host='127.0.0.1' password='Atleti123@'")
        cursor = con.cursor()
        query = f"INSERT INTO materiales.lista_de_materiales (id) VALUES ('{id_lista_de_materiales}');"
        cursor.execute(query)
        con.commit()
        for material in materiales:
            mid = material['id']
            num = material['numero']
            query = f"INSERT INTO materiales.grupo_de_materiales (id_lista_de_materiales,id_material, numero) \
                VALUES ('{id_lista_de_materiales}','{mid}','{num}');"
            cursor.execute(query)
            con.commit()
        con.close()
        return True
    except:
        return False