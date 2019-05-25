import psycopg2
import datetime
import time
from conexion import conection
class ordenes:

    def __init__(self, id , cliente, empleado, fecha_de_termino, fecha_requerida, calle, ciudad, estado, cp ):

        self.fecha_de_creacion = "TIMESTAMP '{0:%Y-%m-%d %H:%M:%S}'".format(datetime.datetime.now())
        self.id = id
        self.fecha_requerida = fecha_requerida
        self.fecha_de_termino = fecha_de_termino
        self.empleado = empleado
        self.cliente = cliente
        self.calle = calle
        self.ciudad = ciudad
        self.estado = estado
        self.cp = cp

    def save(self):
        try:
            self.con = conection()
            self.cursor = self.con.cursor()
            query = f"INSERT INTO workreports.orden_de_trabajo(id,calle,ciudad,estado,cp,fecha_de_creacion, fecha_requerida, fecha_termino, id_empleado_supervisor,\
            id_cliente) VALUES ('{self.id}','{self.calle}','{self.ciudad}','{self.estado}','{self.cp}',{self.fecha_de_creacion},TIMESTAMP '{self.fecha_requerida}',\
            TIMESTAMP  '{self.fecha_de_termino}','{self.empleado}','{self.cliente}');"
            if self.empleado == 'null':
                    query = f"INSERT INTO workreports.orden_de_trabajo(id,calle,ciudad,estado,cp,fecha_de_creacion, fecha_requerida, fecha_termino, id_empleado_supervisor,\
                    id_cliente) VALUES ('{self.id}','{self.calle}','{self.ciudad}','{self.estado}','{self.cp}',{self.fecha_de_creacion},TIMESTAMP '{self.fecha_requerida}',\
                    TIMESTAMP  '{self.fecha_de_termino}',{self.empleado},'{self.cliente}');"
            self.cursor.execute(query)
            self.con.commit()
            self.con.close()
            return True
        except psycopg2.Error as e:
            return (False , e.pgcode, e)