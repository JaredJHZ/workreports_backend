import psycopg2
import datetime
import time
from conexion import conection
class ordenes:

    def __init__(self, id ,fecha_de_creacion = None, fecha_requerida = None, fecha_de_termino = None, 
    empleado = None, direccion = None, serie_de_tareas = None, lista_de_materiales = None, cliente=None, calle = None,
    ciudad = None , estado = None, cp = None ):

        self.fecha_de_creacion = "TIMESTAMP '{0:%Y-%m-%d %H:%M:%S}'".format(datetime.datetime.now())
        self.id = id
        self.fecha_requerida = "TIMESTAMP '{0:%Y-%m-%d %H:%M:%S}'".format(datetime.datetime.now())
        self.fecha_de_termino = "TIMESTAMP '{0:%Y-%m-%d %H:%M:%S}'".format(datetime.datetime.now())
        self.empleado = empleado
        self.direccion = direccion
        self.serie_de_tareas = serie_de_tareas
        self.lista_de_materiales = lista_de_materiales
        self.cliente = cliente
        self.calle = calle
        self.ciudad = ciudad
        self.estado = estado
        self.cp = cp

    def save(self):
        try:
            self.con = conection()
            self.cursor = self.con.cursor()
            query = f"INSERT INTO ordenes_de_trabajo (id,fecha_de_creacion,fecha_requerida,\
                     fecha_termino,id_empleado_supervisor,id_direccion_de_trabajo, id_serie_de_tareas, \
                         id_lista_de_material, id_cliente, calle, ciudad, estado, cp)\
                        VALUES ('{self.id}',{self.fecha_de_creacion},{self.fecha_requerida}, \
                        {self.fecha_de_termino},'{self.empleado}','{self.direccion}', \
                        '{self.serie_de_tareas}','{self.lista_de_materiales}','{self.cliente}', '{self.calle}',\
                        '{self.ciudad}', '{self.estado}', '{self.cp}');"
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            return True
        except psycopg2.Error as e:
            return (False , e.pgcode, e)