import psycopg2
import datetime
import time
from conexion import conection
class tareas:

    def __init__(self,id,nombre, tarifa_hora, estimado_horas, estado, real_horas = None, fecha_termino = None):
        self.id = id
        self.nombre = nombre
        self.tarifa_hora = tarifa_hora
        self.estimado_horas = estimado_horas
        self.estado = estado
        self.real_horas = real_horas
        self.fecha_termino = fecha_termino

    def save(self):
        try:
            fecha = 'NULL'
            self.con = conection()
            self.cursor = self.con.cursor()
            if self.real_horas == None:
                self.real_horas = "Null"
            if self.fecha_termino == None:
                self.fecha_termino = "Null"
            if self.estado == 'completa':
                self.fecha_termino = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                fecha = f"TIMESTAMP '{self.fecha_termino}'"

            query = f"INSERT INTO tareas.tareas(id, nombre, tarifa_hora, estimado_horas, estado, horas_reales,\
                 fecha_termino) VALUES('{self.id}','{self.nombre}',{self.tarifa_hora}, {self.estimado_horas}, \
                     '{self.estado}', {self.real_horas}, {fecha} ); "
                     
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            return True
        except psycopg2.Error as e:
            return (False , e.pgcode, e)

def get_tarea(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"SELECT * FROM tareas.tareas WHERE id = '{id}' ;"
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        id = data[0]
        nombre = data[1]
        tarifa_hora = data[2]
        estimado_horas = data[3]
        estado = data[4]
        real_horas = data[5]
        fecha = data[6]
        if fecha != None:
            fecha = fecha.strftime("%B %d, %Y")
        tarea = {
            "id":id,
            "nombre":nombre,
            "tarifa":tarifa_hora,
            "estimado":estimado_horas,
            "estado":estado,
            "real_horas":real_horas,
            "fecha_termino":fecha
        }
        return tarea
    except psycopg2.Error as e:
        return (False , e.pgcode, e)
    

def modificar_tarea(id,nombre, tarifa_hora, estimado_horas, estado, real_horas, fecha_termino):
    try:
        con = conection()
        cursor = con.cursor()
        if estado == 'completa':
            fecha_termino = "TIMESTAMP '{0:%Y-%m-%d %H:%M:%S}'".format(datetime.datetime.now())
        else:
            fecha_termino = 'null'

        if real_horas == None:
            real_horas = 'null'
        
        query = (f"UPDATE tareas.tareas SET nombre = '{nombre}', tarifa_hora = '{tarifa_hora}', \
            estimado_horas = {estimado_horas}, estado = '{estado}', horas_reales = {real_horas}, \
                fecha_termino = {fecha_termino} WHERE id = '{id}';")
      
        cursor.execute(query)
        con.commit()
        con.close()
        cursor.close()
        return True
    except psycopg2.Error as e:
        return (False , e.pgcode, e)

def eliminar_tarea(id):
    try:
        con = conection()
        cursor = con.cursor()
        query = f"DELETE FROM tareas.tareas WHERE id = '{id}';"
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
        query = f"SELECT * FROM tareas.tareas;"
        cursor.execute(query)
        data = cursor.fetchall()
        tasks = []
        for tarea in data:
            fecha = 'null'
            if tarea[6] != None:
                fecha = tarea[6].strftime("%B %d, %Y")
            
            task = {
                "id":tarea[0],
                "nombre":tarea[1],
                "tarifa_hora":tarea[2],
                "estimado_horas":tarea[3],
                "estado":tarea[4],
                "real_horas":tarea[5],
                "fecha_termino":fecha
            }
            tasks.append(task)
        con.close()
        cursor.close()
        return tasks
    except psycopg2.Error as e:
        return (False , e.pgcode, e)