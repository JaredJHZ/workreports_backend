--Consulta de los nombres del cliente y empleado de una orden--

select orden.id as id_de_la_orden, clientes.nombre as cliente, empleados.nombre as supervisor FROM orden_de_trabajo as orden
INNER JOIN clientes.clientes as clientes ON clientes.id = orden.id_cliente
INNER JOIN empleados.empleados as empleados ON empleados.id = orden.id_empleado_supervisor where orden.id = '1';

--Consulta de los materiales de una orden--



SELECT materiales.nombre as nombre_material, lista.cantidad_utilizada as cantidad_del_material, materiales.costo as costo_unitario,
costo * lista.cantidad_utilizada as total FROM orden_de_trabajo as orden INNER JOIN materiales.lista_de_materiales as
lista ON orden.id = lista.id_orden_de_trabajo INNER JOIN materiales.materiales as materiales ON materiales.id = lista.id_material WHERE orden.id = '1';

--Costo total de materiales --



select SUM(materiales.costo * lista.cantidad_utilizada) AS total from orden_de_trabajo as orden
INNER JOIN materiales.lista_de_materiales as lista ON lista.id_orden_de_trabajo = orden.id INNER JOIN
materiales.materiales as materiales on lista.id_material = materiales.id WHERE orden.id = '1' GROUP BY orden.id;

--Consulta de todos las tareas de una orden--

SELECT tareas.nombre as nombre, tareas.tarifa_hora as tarifa, tareas.estimado_horas as horas, tareas.fecha_termino as fecha,
tareas.estimado_horas * tareas.tarifa_hora as total from orden_de_trabajo as orden INNER JOIN tareas.serie_de_tareas as serie ON
serie.id_ordenes_de_trabajo = orden.id INNER JOIN tareas.tareas as tareas ON tareas.id = serie.id_tarea WHERE orden.id = '1';


--Costo total de tareas --

SELECT SUM(tareas.tarifa_hora * tareas.estimado_horas) as total from orden_de_trabajo as orden INNER JOIN tareas.serie_de_tareas as serie ON
serie.id_ordenes_de_trabajo = orden.id INNER JOIN tareas.tareas ON tareas.id = serie.id_tarea WHERE orden.id = '1';

-- Fecha de creacion de orden --
SELECT orden_de_trabajo.fecha_de_creacion as fecha_de_creacion FROM orden_de_trabajo WHERE id = '1';

--Consulta de todoslas ordendes--

SELECT cliente.nombre, orden.fecha_de_creacion, orden.calle, orden.ciudad, orden.estado FROM
orden_de_trabajo as orden INNER JOIN clientes.clientes as cliente ON cliente.id = orden.id_cliente
WHERE orden.id = '1';

