--Consulta de los nombres del cliente y empleado de una orden--

select orden.id as id_de_la_orden, clientes.nombre as cliente, empleados.nombre as supervisor FROM orden_de_trabajo as orden
INNER JOIN clientes.clientes as clientes ON clientes.id = orden.id_cliente
INNER JOIN empleados.empleados as empleados ON empleados.id = orden.id_empleado_supervisor where orden.id = '1';

--Consulta de los materiales de una orden--

select materiales.nombre as nombre_material , grupo.numero as cantidad_del_material , materiales.costo_unitario as costo_unitario, 
costo_unitario * grupo.numero as total  from orden_de_trabajo as orden 
INNER JOIN materiales.lista_de_materiales as lista ON orden.id_lista_de_material = lista.id INNER JOIN
materiales.grupo_de_materiales as grupo ON grupo.id_lista_de_materiales = lista.id INNER JOIN
materiales.materiales as materiales ON materiales.id = grupo.id_material WHERE orden.id = '1'; 

--Costo total de materiales --

select SUM(materiales.costo_unitario * grupo.numero) AS total from orden_de_trabajo as orden 
INNER JOIN materiales.lista_de_materiales as lista ON orden.id_lista_de_material = lista.id INNER JOIN
materiales.grupo_de_materiales as grupo ON grupo.id_lista_de_materiales = lista.id INNER JOIN
materiales.materiales as materiales ON materiales.id = grupo.id_material GROUP BY orden.id; 

--Consulta de todos las tareas de una orden--
SELECT tareas.nombre as nombre , tareas.tarifa_hora as tarifa , tareas.estimado_horas as horas, tareas.fecha_termino as fecha
,tareas.estimado_horas * tareas.tarifa_hora as total from orden_de_trabajo as orden INNER JOIN tareas.grupo_de_tareas as grupo ON 
grupo.id_serie_de_tareas = orden.id_serie_de_tareas INNER JOIN tareas.tareas as tareas ON tareas.id = grupo.id_tarea WHERE orden.id = '1';

--Costo total de materiales --

SELECT SUM(tareas.estimado_horas * tareas.tarifa_hora) as total from orden_de_trabajo as orden INNER JOIN tareas.grupo_de_tareas as grupo ON
grupo.id_serie_de_tareas = orden.id_serie_de_tareas INNER JOIN tareas.tareas as tareas ON tareas.id = grupo.id_tarea GROUP BY orden.id;

-- Fecha de creacion de orden --
SELECT orden_de_trabajo.fecha_de_creacion as fecha_de_creacion FROM orden_de_trabajo WHERE id = '1';

--Consulta de todoslas ordendes--

SELECT cliente.nombre, orden.fecha_de_creacion, direccion.calle, direccion.ciudad, direccion.estado FROM
orden_de_trabajo as orden INNER JOIN clientes.clientes as cliente ON cliente.id = orden.id_cliente
INNER JOIN direcciones.direcciones as direccion ON direccion.id = orden.id_direccion_de_trabajo 
WHERE orden.id = '1';
-- english -
SELECT clients.name, work_order.date, direction.street, direction.city, direction.zip FROM
work_orders as work_order INNER JOIN clients.clients as clients ON client.id = work_order.id_client
INNER JOIN directions.directions as direction ON direction.id = work_order.id_work_direction 
WHERE work_order.id = '1';