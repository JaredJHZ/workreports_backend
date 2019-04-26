from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.tareas.tareas import tareas, modificar_tarea, eliminar_tarea, get_tarea, get_all
from middlewares.middlewares import authentication
import psycopg2
from datetime import datetime

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
            try:
                tarea.save()
                return {"mensaje": "exito al guardar tarea"},201
            except:
                return {"mensaje": "error al guardar tarea"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if data:
                return {"tareas":data},200
            else:
                return {"mensaje":"Error interno"},501
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
            print(info)
            id = info["id"]
            nombre = info["nombre"]
            tarifa_hora = info["tarifa_hora"]
            estimado_horas = info["estimado_horas"]
            estado = info["estado"]
            real_horas = None
            try:
                print("entrando")
                modificar_tarea(id,nombre,tarifa_hora,estimado_horas,estado, fecha_termino = None, real_horas = real_horas)
                return {"mensaje":"Tarea modificada correctamente"}
            except:
                return {"mensaje": "Error al modificar tarea"},501
        else:
            return {"mensaje": "Error se necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_tarea(id)
            if data:
                return {"tarea":data},201
            else:
                return {"mensaje": "Tarea no encontrada"},404
        else:
            return {"mensaje": "Error se necesita estar autenticado"},400

    def delete(self,id):
        print("xd")
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            print(permission)
            if eliminar_tarea(id):
                return {"mensaje":"Tarea eliminada"}
            else:
                return {"mensaje":"No se encontro la tarea"},404
        else:
            return {"mensaje": "Error se necesita estar autenticado"},400
    
    def options(self):
        pass
                