from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.empleados.empleados import empleados, get_empleado, modificar_empleado, eliminar_empleado, get_all
from middlewares.middlewares import authentication
from errors import errorHandling
import psycopg2

class Empleados(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            nombre = info["nombre"]
            ap_paterno = info["ap_paterno"]
            ap_materno = info["ap_materno"]
            empleado = empleados(id,ap_paterno,ap_materno,nombre)
            empleado = empleado.save()
            if (isinstance(empleado, tuple)):
                return {"mensaje": errorHandling(empleado[1], empleado[2])},501   
            return {"mensaje": "exito al guardar empleado"},201
           
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if isinstance(data,tuple):
                return {"mensaje": errorHandling(data[1], data[2])},501   
            else:
                return {"empleados":data},200
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    def options(self):
        pass

class EmpleadosParametros(Resource):
    def put(self, id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force = True)
            nombre = info["nombre"]
            ap_paterno = info["ap_paterno"]
            ap_materno = info["ap_materno"]
            empleado = modificar_empleado(id,nombre,ap_paterno,ap_materno)
            if isinstance(empleado, tuple):
                return {"mensaje": errorHandling(empleado[1], empleado[2])},501   
            return {"mensaje":"empleado modificado correctamente"}
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            empleado = get_empleado(id)
            if isinstance(empleado, tuple):
                return {"mensaje": errorHandling(empleado[1], empleado[2])},501   
            else:
                return {"empleado":empleado},201
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            data = eliminar_empleado(id)
            if isinstance(data, tuple):
                    return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"mensaje":"empleado eliminado"}
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
    def options(self):
        pass
                