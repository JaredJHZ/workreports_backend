def query_nombre_cliente_y_empleado(id_orden):
    query = f"select orden.id as id_de_la_orden, clientes.nombre as cliente, empleados.nombre, clientes.id, empleados.id, clientes.ap_paterno,\
             clientes.ap_materno, empleados.ap_paterno, empleados.ap_materno as supervisor FROM workreports.orden_de_trabajo as orden\
                INNER JOIN workreports.clientes as clientes ON clientes.id = orden.id_cliente\
                INNER JOIN workreports.empleados as empleados ON empleados.id = orden.id_empleado_supervisor where orden.id = '{id_orden}';"
    return query

def query_materiales(id_orden):
        query = f"SELECT materiales.nombre as nombre_material, lista.cantidad_utilizada as cantidad_del_material, materiales.costo as costo_unitario,\
                costo * lista.cantidad_utilizada as total, materiales.id FROM workreports.orden_de_trabajo as orden INNER JOIN workreports.lista_de_materiales as\
                lista ON orden.id = lista.id_orden_de_trabajo INNER JOIN workreports.materiales as materiales ON materiales.id = lista.id_material WHERE orden.id = '{id_orden}'; "

        return query

def query_costo_de_materiales(id_orden):
        query = f"select SUM(materiales.costo * lista.cantidad_utilizada) AS total from workreports.orden_de_trabajo as orden\
                INNER JOIN workreports.lista_de_materiales as lista ON lista.id_orden_de_trabajo = orden.id INNER JOIN\
                workreports.materiales as materiales on lista.id_material = materiales.id WHERE orden.id = '{id_orden}' GROUP BY orden.id;"

        return query

def query_tareas(id_orden):
        query = f"SELECT tareas.nombre as nombre, tareas.tarifa_hora as tarifa, tareas.estimado_horas as horas, tareas.fecha_termino as fecha,\
                tareas.estimado_horas * tareas.tarifa_hora as total, tareas.id FROM workreports.orden_de_trabajo as orden INNER JOIN workreports.serie_de_tareas as serie ON\
                serie.id_orden_de_trabajo = orden.id INNER JOIN workreports.tareas as tareas ON tareas.id = serie.id_tarea WHERE orden.id = '{id_orden}';"
        return query

def query_costo_de_tareas(id_orden):
        query = f"SELECT SUM(tareas.tarifa_hora * tareas.estimado_horas) as total from workreports.orden_de_trabajo as orden INNER JOIN workreports.serie_de_tareas as serie ON\
                serie.id_orden_de_trabajo = orden.id INNER JOIN workreports.tareas ON tareas.id = serie.id_tarea WHERE orden.id = '{id_orden}';"
        return query

def query_fecha_de_creacion(id_orden):
        query = f"SELECT orden_de_trabajo.fecha_de_creacion as fecha_de_creacion FROM workreports.orden_de_trabajo WHERE id = '{id_orden}';"
        return query

def query_get_todas_las_ordenes():
        query = "SELECT orden.id,cliente.nombre, orden.fecha_de_creacion, orden.calle, orden.ciudad, orden.estado FROM workreports.orden_de_trabajo as orden INNER JOIN workreports.clientes as cliente ON cliente.id = orden.id_cliente;"
        return query

def query_get_direccion(id_orden):
        query = f"SELECT orden_de_trabajo.calle, orden_de_trabajo.ciudad, orden_de_trabajo.estado, orden_de_trabajo.cp FROM workreports.orden_de_trabajo WHERE orden_de_trabajo.id = '{id_orden}';"
        return query

def query_delete_orden(id_orden):
        query = f"DELETE FROM workreports.orden_de_trabajo as orden WHERE orden.id = '{id_orden}' ;"
        return query

def query_update_orden(id_orden,empleado,cliente, calle,ciudad,estado,cp):
        query = f"UPDATE workreports.orden_de_trabajo SET id_empleado_supervisor = '{empleado}', id_cliente = '{cliente}', calle = '{calle}', ciudad = '{ciudad}', estado = '{estado}', cp = '{cp}';"
        return query

def query_add_tarea(id_orden,id_tarea):
        query = f"INSERT INTO workreports.serie_de_tareas(id_tarea,id_orden_de_trabajo) VALUES('{id_tarea}','{id_orden}')"
        return query

def query_add_material(id_orden,id_material,cantidad_estimada, cantidad_utilizada):
        query = f"INSERT INTO workreports.lista_de_materiales(id_orden_de_trabajo, id_material,cantidad_estimada,cantidad_utilizada) VALUES ('{id_orden}','{id_material}','{cantidad_estimada}','{cantidad_utilizada}');"
        return query

def delete_tarea(id_orden,id_tarea):
        query = f"DELETE FROM workreports.serie_de_tareas WHERE id_orden_de_trabajo = '{id_orden}' AND id_tarea = '{id_tarea}' ;"
        return query

def delete_material(id_orden,id_material):
        query = f"DELETE FROM workreports.lista_de_materiales WHERE id_orden_de_trabajo = '{id_orden}' AND id_material = '{id_material}';   "
        return query