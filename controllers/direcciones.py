from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.direcciones.direcciones import direcciones, get_direccion, modificar_direccion, eliminar_direccion, get_all
from middlewares.middlewares import authentication
import psycopg2

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
                direccion.save()
                return {"mensaje": "exito al guardar direccion"},201
            except psycopg2.OperationalError as e:
                print('Unable to connect!\n{0}').format(e)
            except:
                return {"mensaje": "error al guardar direccion"},501
        else:
            return {"mensaje": "error, necesita autenticarsecc"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if data:
                return {"direcciones":data},200
            else:
                return {"mensaje":"error interno"},501
        else:
            return {"mensaje": "error, necesita autenticarsecc"},401

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
                modificar_direccion(id,calle,ciudad,estado,cp)
                return {"mensaje":"direccion modificada correctamente"}
            except:
                return {"mensaje": "error al modificar direccion"},501
        else:
            return {"mensaje": "error necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_direccion(id)
            if data:
                return {"direccion":data},201
            else:
                return {"mensaje": "direccion no encontrada"},404
        else:
            return {"mensaje": "error necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            if eliminar_direccion(id):
                return {"mensaje":"direccion eliminada"}
            else:
                return {"mensaje":"No se encontro la direccion"},404
        else:
            return {"mensaje": "error necesita estar autenticado"},400
                