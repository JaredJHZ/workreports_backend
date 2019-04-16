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
            except psycopg2.OperationalError as e:
                print('Unable to connect!\n{0}').format(e)
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
                return {"mensaje":"error interno"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401

class TareasParametro(Resource):
    def put(self, id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force = True)
            nombre = info["nombre"]
            tarifa_hora = info["tarifa_horas"]
            estimado_horas = info["estimado_horas"]
            estado = info["estado"]
            real_horas = info["real_horas"]
            if estado == "COMPLETADO":
                now = datetime.now()
                try:
                    modificar_tarea(id,nombre,tarifa_hora,estimado_horas,estado, fecha_termino = now, real_horas = real_horas)
                    return {"mensaje":"tarea modificada correctamente"}
                except:
                    return {"mensaje": "error al modificar tarea"},501
            else:
                try:
                    modificar_tarea(id,nombre,tarifa_hora,estimado_horas,estado, fecha_termino = None, real_horas = None)
                    return {"mensaje":"tarea modificada correctamente"}
                except:
                    return {"mensaje": "error al modificar tarea"},501
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_tarea(id)
            if data:
                return {"tarea":data},201
            else:
                return {"mensaje": "tarea no encontrada"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            if eliminar_tarea(id):
                return {"mensaje":"tarea eliminada"}
            else:
                return {"mensaje":"No se encontro la tarea"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
                