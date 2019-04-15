from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.materiales.materiales import materiales, get_material, eliminar_material, modificar_material, get_all
from middlewares.middlewares import authentication
import psycopg2

class Materiales(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            nombre = info["nombre"]
            costo_unitario = info["costo_unitario"]
            material = materiales(id,nombre,costo_unitario)
            try:
                material.save()
                return {"mensaje": "exito al guardar material"},201
            except psycopg2.OperationalError as e:
                print('Unable to connect!\n{0}').format(e)
            except:
                return {"mensaje": "error al guardar material"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if data:
                return {"materiales":data},200
            else:
                return {"mensaje":"error interno"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401

class MaterialesParametro(Resource):
    def put(self, id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force = True)
            nombre = info["nombre"]
            costo_unitario = info["costo_unitario"]
            try:
                modificar_material(id,nombre,costo_unitario)
                return {"mensaje":"material modificado correctamente"}
            except:
                return {"mensaje": "error al modificar material"},501
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_material(id)
            if data:
                return {"cliente":data},201
            else:
                return {"mensaje": "material no encontrado"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            if eliminar_material(id):
                return {"mensaje":"cliente eliminado"}
            else:
                return {"mensaje":"No se encontro al cliente"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
                