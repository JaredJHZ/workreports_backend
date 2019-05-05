from flask import Flask, request, jsonify, render_template , make_response
from flask_restful import Resource, Api, reqparse
import pdfkit 
from middlewares.middlewares import authentication
from clases.ordenes.ordenes import ordenes
from clases.ordenes.funciones_ordenes import guardar_serie_de_tareas, guardar_lista_de_materiales, generar_pdf, get_orden, get_all_ordenes
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
            id_serie_de_tareas = info["serie_de_tareas"]
            tareas = info["tareas"]
            #se guardan las tareas de la orden de trabajo y se hace un enlace
            guardar_serie_de_tareas(id_serie_de_tareas, tareas)
            lista_de_materiales = info["lista_de_materiales"]
            materiales = info["materiales"]
            #se guardan los materiales de la orden de trabajo y se hace un enlace
            guardar_lista_de_materiales(lista_de_materiales, materiales)
            #se crea la orden de trabajo con las tareas y enlaces realizados
            id = info['id']
            empleado = info['empleado']
            direccion = info['direccion']
            cliente = info['cliente']
            orden = ordenes(id, empleado= empleado, direccion=direccion,serie_de_tareas= id_serie_de_tareas,
            lista_de_materiales=lista_de_materiales, cliente= cliente )
            data = orden.save()
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"mensaje":"Exito al guardar orden"},201
        else:
            return {"mensaje": "Error"},401

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
            costo_total_tareas = info['costo_total_tareas'], costo_total = costo_total, fecha_de_creacion = info['fecha_de_creacion'])

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
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"orden":data},201
        else:
            return {"mensaje":'Erro al autenticarse'},401
    
    def options(self):
        pass