from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from middlewares.middlewares import authentication
from clases.ordenes.ordenes import ordenes
from clases.ordenes.funciones_ordenes import guardar_serie_de_tareas, guardar_lista_de_materiales
import psycopg2
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
            orden.save()
            return {"mensaje":"Exito al guardar orden"},201
        else:
            return {"mensaje": "Error"},401

    def options(self):
        pass