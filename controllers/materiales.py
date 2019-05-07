from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.materiales.materiales import materiales, get_material, eliminar_material, modificar_material, get_all
from middlewares.middlewares import authentication
import psycopg2
from errors import errorHandling

class Materiales(Resource):
    def options(self):
        pass
    def post(self):
        print(request.headers)
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            nombre = info["nombre"]
            costo_unitario = info["costo"]
            material = materiales(id,nombre,costo_unitario)
            material = material.save()
            if isinstance(material, tuple):
                return {"mensaje": errorHandling(material[1], material[2])},501   
            return {"mensaje": "exito al guardar material"},201
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"materiales":data},200
        else:
            return {"mensaje": "error, necesita autenticarse"},401

class MaterialesParametro(Resource):
    def options(self):
        pass
    def put(self, id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force = True)
            nombre = info["nombre"]
            costo_unitario = info["costo"]
            material = modificar_material(id,nombre,costo_unitario)
            if isinstance(material, tuple):
                return {"mensaje": errorHandling(material[1], material[2])},501   
            return {"mensaje":"material modificado correctamente"}
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_material(id)
            if isinstance(data,tuple):
                return {"mensaje": errorHandling(data[1], data[2])},501   
            else:
                return {"cliente":data},201
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'admin':
            data = eliminar_material(id)
            if isinstance(data,tuple):
                return {"mensaje": errorHandling(data[1], data[2])},501   
            return {"mensaje":"material eliminado"}
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
                