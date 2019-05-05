from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.direcciones.direcciones import direcciones, get_direccion, modificar_direccion, eliminar_direccion, get_all
from middlewares.middlewares import authentication
import psycopg2
from errors import errorHandling

class Direcciones(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            calle = info["calle"]
            ciudad = info["ciudad"]
            estado = info["estado"]
            cp = info["cp"]
            direccion = direcciones(id,calle,ciudad,estado,cp)
            try:
                direccion = direccion.save()
                if (direccion[0]) == False:
                    return {"mensaje": errorHandling(direccion[1], direccion[2])},501   
                return {"mensaje": "exito al guardar direccion"},201
            except:
                return {"mensaje": "error al guardar direccion"},501
        else:
            return {"mensaje": "error, necesita autenticarsecc"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            else:
                return {"direcciones":data},200
        else:
            return {"mensaje": "error, necesita autenticarsecc"},401
    def options(self):
        pass

class DireccionesParametro(Resource):
    def put(self, id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force = True)
            calle = info["calle"]
            ciudad = info["ciudad"]
            estado = info["estado"]
            cp = info["cp"]
            try:
                direccion = modificar_direccion(id,calle,ciudad,estado,cp)
                if (direccion[0]) == False:
                    return {"mensaje": errorHandling(direccion[1], direccion[2])},501   
                return {"mensaje":"direccion modificada correctamente"},201
            except:
                return {"mensaje": "error al modificar direccion"},501
        else:
            return {"mensaje": "error necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_direccion(id)
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            else:
                return {"direccion":data},201
        else:
            return {"mensaje": "error necesita estar autenticado"},400

    def delete(self,id):
        pass
                
    def options(self):
        pass