from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.empleados.empleados import empleados, get_empleado, modificar_empleado, eliminar_empleado, get_all
from middlewares.middlewares import authentication
import psycopg2

class Empleados(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            print(info)
            nombre = info["nombre"]
            ap_paterno = info["ap_paterno"]
            ap_materno = info["ap_materno"]
            id_direccion = info["direcccion"]
            emplado = empleados(id,ap_paterno,ap_materno,nombre,id_direccion)
            try:
                emplado.save()
                return {"mensaje": "exito al guardar empleado"},201
            except psycopg2.OperationalError as e:
                print('Unable to connect!\n{0}').format(e)
            except:
                return {"mensaje": "error al guardar empleado"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if data:
                return {"empleados":data},200
            else:
                return {"mensaje":"error interno"},501
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
            id_direccion = info["direccion"]
            try:
                modificar_empleado(id,nombre,ap_paterno,ap_materno,id_direccion)
                return {"mensaje":"empleado modificado correctamente"}
            except:
                return {"mensaje": "error al modificar empleado"},501
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_empleado(id)
            if data:
                return {"empleado":data},201
            else:
                return {"mensaje": "empleado no encontrado"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            if eliminar_empleado(id):
                return {"mensaje":"empleado eliminado"}
            else:
                return {"mensaje":"No se encontro el empleado"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
    def options(self):
        pass
                