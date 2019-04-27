def query_nombre_cliente_y_empleado(id_orden):
    query = f"select orden.id as id_de_la_orden, clientes.nombre as cliente, empleados.nombre as supervisor FROM orden_de_trabajo as orden\
            INNER JOIN clientes.clientes as clientes ON clientes.id = orden.id_cliente\
            INNER JOIN empleados.empleados as empleados ON empleados.id = orden.id_empleado_supervisor where orden.id = '{id_orden}';"
    return query

def query_materiales(id_orden):
        query = f"select materiales.nombre as nombre_material , grupo.numero as cantidad_del_material , materiales.costo_unitario as costo_unitario,\
                costo_unitario * grupo.numero as total  from orden_de_trabajo as orden\
                INNER JOIN materiales.lista_de_materiales as lista ON orden.id_lista_de_material = lista.id INNER JOIN\
                materiales.grupo_de_materiales as grupo ON grupo.id_lista_de_materiales = lista.id INNER JOIN\
                materiales.materiales as materiales ON materiales.id = grupo.id_material WHERE orden.id = '{id_orden}'; "

        return query

def query_costo_de_materiales(id_orden):
        query = f"select SUM(materiales.costo_unitario * grupo.numero) AS total from orden_de_trabajo as orden\
                INNER JOIN materiales.lista_de_materiales as lista ON orden.id_lista_de_material = lista.id INNER JOIN\
                materiales.grupo_de_materiales as grupo ON grupo.id_lista_de_materiales = lista.id INNER JOIN\
                materiales.materiales as materiales ON materiales.id = grupo.id_material WHERE orden.id = '{id_orden}'  GROUP BY orden.id ;"

        return query

def query_tareas(id_orden):
        query = f"SELECT tareas.nombre as nombre , tareas.tarifa_hora as tarifa , tareas.estimado_horas as horas, tareas.fecha_termino as fecha\
                ,tareas.estimado_horas * tareas.tarifa_hora as total from orden_de_trabajo as orden INNER JOIN tareas.grupo_de_tareas as grupo ON \
                grupo.id_serie_de_tareas = orden.id_serie_de_tareas INNER JOIN tareas.tareas as tareas ON tareas.id = grupo.id_tarea WHERE orden.id = '{id_orden}';"
        return query

def query_costo_de_tareas(id_orden):
        query = f"SELECT SUM(tareas.estimado_horas * tareas.tarifa_hora) as total from orden_de_trabajo as orden INNER JOIN tareas.grupo_de_tareas as grupo ON \
                grupo.id_serie_de_tareas = orden.id_serie_de_tareas INNER JOIN tareas.tareas as tareas ON tareas.id = grupo.id_tarea\
                WHERE orden.id = '{id_orden}' GROUP BY orden.id;"
        return query

def query_fecha_de_creacion(id_orden):
        query = f"SELECT orden_de_trabajo.fecha_de_creacion as fecha_de_creacion FROM orden_de_trabajo WHERE id = '{id_orden}';"
        return query