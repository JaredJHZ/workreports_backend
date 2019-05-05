from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.tareas.tareas import tareas, modificar_tarea, eliminar_tarea, get_tarea, get_all
from middlewares.middlewares import authentication
import psycopg2
from datetime import datetime
from errors import errorHandling

class Tareas(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            nombre = info["nombre"]
            tarifa_hora = info["tarifa_hora"]
            estimado_horas = info["estimado_horas"]
            estado = info["estado"]
            tarea = tareas(id,nombre,tarifa_hora,estimado_horas,estado)
            data = tarea.save()
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"mensaje": "exito al guardar tarea"},201
        else:
            return {"mensaje": "error, necesita autenticarse"},401

    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"tareas":data},200
        else:
            return {"mensaje": "Error, necesita autenticarse"},401
    
    def options(self):
        pass

class TareasParametro(Resource):
    def put(self, id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force = True)
            id = info["id"]
            nombre = info["nombre"]
            tarifa_hora = info["tarifa_hora"]
            estimado_horas = info["estimado_horas"]
            estado = info["estado"]
            real_horas = None
            data = modificar_tarea(id,nombre,tarifa_hora,estimado_horas,estado, fecha_termino = None, real_horas = real_horas)
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"mensaje":"Tarea modificada correctamente"}
        else:
            return {"mensaje": "Error se necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_tarea(id)
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"tarea":data},201
        else:
            return {"mensaje": "Error se necesita estar autenticado"},400

    def delete(self,id):
        print("xd")
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            data = eliminar_tarea(id)
            if (data[0]) == False:
                    return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"mensaje":"Tarea eliminada"}
        else:
            return {"mensaje": "Error se necesita estar autenticado"},400
    def options(self):
        pass
                