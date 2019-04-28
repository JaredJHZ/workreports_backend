import psycopg2
from clases.ordenes.querys_orden import query_nombre_cliente_y_empleado, query_materiales, query_costo_de_materiales, query_tareas, query_costo_de_tareas, query_fecha_de_creacion
import time
from conexion import conection

def guardar_serie_de_tareas(id_serie_de_tareas,tareas):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"INSERT INTO tareas.serie_de_tareas (id) VALUES ('{id_serie_de_tareas}');"
        cursor.execute(query)
        con.commit()
        for tarea in tareas:
            query = f"INSERT INTO tareas.grupo_de_tareas VALUES('{id_serie_de_tareas}','{tarea}');"
            cursor.execute(query)
            con.commit()
        con.close()
        return True
    except:
        return False

def guardar_lista_de_materiales(id_lista_de_materiales, materiales):
    try:
        con = conection()
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

def generar_pdf(id_orden):
    info = query_nombre_cliente_y_empleado(id_orden)
    con = conection()
    cursor = con.cursor()
    cursor.execute(info)
    data = cursor.fetchone()
    #materiales
    materiales = query_materiales(id_orden)
    cursor.execute(materiales)
    todos_materiales = cursor.fetchall()
    lista_materiales = []
    for material in todos_materiales:
        item = {
            'nombre':material[0],
            'cantidad':material[1],
            'costo_unitario':material[2],
            'costo_total_material':material[3]
        }
        lista_materiales.append(item)

    #costo de materiales
    costo_de_materiales = query_costo_de_materiales(id_orden)
    cursor.execute(costo_de_materiales)
    costo_de_materiales = cursor.fetchone()
    print(costo_de_materiales)
    # tareas
    tareas = query_tareas(id_orden)
    cursor.execute(tareas)
    todas_tareas = cursor.fetchall()
    lista_tareas = []
    for tarea in todas_tareas:
        fecha = "No se ha completado"
        if tarea[3] != None:
            fecha = '{0:%d-%m-%Y}'.format(tarea[3])
        item = {
            'nombre':tarea[0],
            'tarifa_por_hora':tarea[1],
            'horas': tarea[2],
            'fecha': fecha,
            'total':tarea[4]
        }
        lista_tareas.append(item)
    # costo total de tareas
    costo_de_tareas = query_costo_de_tareas(id_orden)
    cursor.execute(costo_de_tareas)
    costo_de_tareas = cursor.fetchone()
    # fecha de creacion de la orden de trabajo
    fecha_de_creacion = query_fecha_de_creacion(id_orden)
    cursor.execute(fecha_de_creacion)
    fecha_de_creacion = cursor.fetchone()
    con.close()
    return {
        'empleado':data[1],
        'cliente':data[2],
        'materiales':lista_materiales,
        'costo_total_materiales':costo_de_materiales[0],
        'tareas':lista_tareas,
        'costo_total_tareas': costo_de_tareas[0],
        'fecha_de_creacion': '{0:%d-%m-%Y}'.format(fecha_de_creacion[0])
    }