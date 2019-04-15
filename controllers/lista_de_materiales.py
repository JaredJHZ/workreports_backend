from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.lista_de_materiales.lista_de_materiales import lista_de_materiales, eliminar_lista_de_materiales, get_lista_de_materiales, get_all, agregar_materiales_a_la_lista, get_precio_total
from middlewares.middlewares import authentication
import psycopg2

class Lista_de_material(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            lista_material = lista_de_materiales(id)
            try:
                lista_material.save()
                return {"mensaje": "exito al guardar la lista de materiales"},201
            except psycopg2.OperationalError as e:
                print('Unable to connect!\n{0}').format(e)
            except:
                return {"mensaje": "error al guardar la lista de materiales"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if data:
                return {"lista de materiales":data},200
            else:
                return {"mensaje":"error interno"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401

class ListaDeMaterialesParametro(Resource):

    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_lista_de_materiales(id)
            if data:
                return {"lista de materiales":data},201
            else:
                return {"mensaje": "lista de material no encontrado"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            if eliminar_lista_de_materiales(id):
                return {"mensaje":"lista de material eliminada"}
            else:
                return {"mensaje":"No se encontro la lista de material"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def post(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            materiales = info["materiales"]
            if agregar_materiales_a_la_lista(id,materiales):
                return {"mensaje":"agregados materiales a la lista"},201
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

class PrecioLista(Resource):

    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_precio_total(id)
            if data:
                return {"Precio de los materiales":data},201
            else:
                return {"mensaje": "lista de material no encontrado"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400
                