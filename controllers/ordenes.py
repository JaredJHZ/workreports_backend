from flask import Flask, request, jsonify, render_template , make_response
from flask_restful import Resource, Api, reqparse
import pdfkit 
from middlewares.middlewares import authentication
from clases.ordenes.ordenes import ordenes
from clases.ordenes.funciones_ordenes import guardar_serie_de_tareas, guardar_lista_de_materiales, generar_pdf, get_orden, get_all_ordenes, eliminar_orden, update_orden, add_material, add_tarea, delete_material_orden, delete_tarea_orden
import psycopg2
import pathlib
import datetime
import time
from errors import errorHandling

class Ordenes(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:

            info = request.get_json(force=True)
            # materiales
            id = info['id']
            id_del_cliente = info['cliente']
            id_empleado_supervisor = info['empleado']
            fecha_termino = info['fecha_termino']
            fecha_requerida = info['fecha_requerida']
            calle = info['calle']
            ciudad = info['ciudad']
            estado = info['estado']
            cp = info['cp']

            materiales = info['materiales']
            tareas = info['tareas']
            orden = ordenes(id,id_del_cliente,id_empleado_supervisor,fecha_termino,fecha_requerida, calle, ciudad,estado,cp)

            data = orden.save()

            guardar_lista_de_materiales(materiales, id)

            guardar_serie_de_tareas(tareas, id)

            if isinstance(data,tuple):
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"mensaje":"Exito al guardar orden"},201
        else:
            return {"mensaje": "Permiso denegado"},401

    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = lista_ordenes = get_all_ordenes()
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"ordenes":lista_ordenes},201
        else:
            return {"mensaje": "Error al autenticarse"},501

    def options(self):
        pass

class OrdenesPDF(Resource):

    def get(self,id):
        token = request.headers.get('authentication')
        user = authentication(token)
        if user:
            info = generar_pdf(id)

            image = pathlib.Path('/Users/jaredhernandez/WorkReports/backend/static/css/images/icons/logo.png').as_uri()
            
            costo_total = float(info['costo_total_materiales']) + float(info['costo_total_tareas'])


            rendered = render_template('pdf_template.html', cliente = info['empleado'], empleado = info['cliente'], 
            orden = id, image = image, materiales = info['materiales'], costo_total_materiales = info['costo_total_materiales'], tareas = info['tareas'] ,
            costo_total_tareas = info['costo_total_tareas'], costo_total = costo_total, fecha_de_creacion = info['fecha_de_creacion'], calle = info['calle'], ciudad
            = info['ciudad'], estado = info['estado'], cp = info['cp'])

            pdf = pdfkit.from_string(rendered, False)
            response = make_response(pdf)
            response.headers['Content-Type'] = 'application/pdf'
            fecha = '{0:%d-%m-%Y %h:%m:%s}'.format(datetime.datetime.now())
            
            response.headers['Content-Disposition'] = f"inline; filename={'orden-'+id+'-fecha-'+fecha}.pdf"
            return response
        else:
            return {"mensaje":"Error al autenticarse"}
    def options(self):
        pass


class OrdenesConParametro(Resource):

    def get(self,id):
        token = request.headers.get('authentication')
        user = authentication(token)
        if user:
            data = get_orden(id)
            if isinstance(data,tuple):
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"orden":data},201
        else:
            return {"mensaje":'Erro al autenticarse'},401

    def delete(self,id):
        token = request.headers.get('authentication')
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            data = eliminar_orden(id)
            if isinstance(data,tuple):
                return {"mensaje":errorHandling(data[1], data[2])},501
            return {"mensaje":"Orden eliminada correctamente"},201
        else:
            return {"mensaje":'Erro al autenticarse'},401

    def put(self,id):
        token = request.headers.get('authentication')
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id_del_cliente = info['cliente']
            id_empleado_supervisor = info['empleado']
            calle = info['calle']
            ciudad = info['ciudad']
            estado = info['estado']
            cp = info['cp']
            data = update_orden(id,id_empleado_supervisor, id_del_cliente,calle, ciudad, estado, cp)
            if isinstance(data,tuple):
                return {"mensaje":errorHandling(data[1], data[2])},501
            return {"mensaje":"Orden modificada correctamente"},201
        else:
            return {"mensaje":'Error al autenticarse'},401

    
    def options(self):
        pass

class OrdenesMateriales(Resource):
    
    def post(self,id,material):
        token = request.headers.get('authentication')
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            cantidad_estimada = info['cantidad_estimada']
            cantidad_utilizada = info['cantidad_utilizada']
            data = add_material(id,material,cantidad_estimada,cantidad_utilizada)
            if isinstance(data,tuple):
                return {"mensaje":errorHandling(data[1], data[2])},501
            return {"mensaje":"Orden modificada correctamente"},201
        else:
            return {"mensaje":'Error al autenticarse'},401
    
    def delete(self,id,material):
        token = request.headers.get('authentication')
        user = authentication(token)
        if user:
            data = delete_material_orden(id,material)
            if isinstance(data,tuple):
                return {"mensaje":errorHandling(data[1], data[2])},501
            return {"mensaje":"Orden modificada correctamente"},201
        else:
            return {"mensaje":'Error al autenticarse'},401    

    def options(self):
        pass

class OrdenesTareas(Resource):
    def options(self):
        pass
    
    def post(self,id,tarea):
        token = request.headers.get('authentication')
        user = authentication(token)
        if user:
            data = add_tarea(id,tarea)
            if isinstance(data,tuple):
                return {"mensaje":errorHandling(data[1], data[2])},501
            return {"mensaje":"Orden modificada correctamente"},201
        else:
            return {"mensaje":'Error al autenticarse'},401

    def delete(self,id,tarea):
        token = request.headers.get('authentication')
        user = authentication(token)
        if user:
            data = delete_tarea_orden(id,tarea)
            if isinstance(data,tuple):
                return {"mensaje":errorHandling(data[1], data[2])},501
            return {"mensaje":"Orden modificada correctamente"},201
        else:
            return {"mensaje":'Error al autenticarse'},401