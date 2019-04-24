from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.clientes.clientes import clientes, get_cliente, modificar_cliente, eliminar_empleado, get_all
from middlewares.middlewares import authentication
import psycopg2

class Clientes(Resource):
    def post(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force=True)
            id = info["id"]
            nombre = info["nombre"]
            ap_paterno = info["ap_paterno"]
            ap_materno = info["ap_materno"]
            id_direccion = info["direcccion"]
            email = info["email"]
            cliente = clientes(id,ap_paterno,ap_materno,nombre,id_direccion,email)
            try:
                cliente.save()
                return {"mensaje": "exito al guardar cliente"},201
            except psycopg2.OperationalError as e:
                print('Unable to connect!\n{0}').format(e)
            except:
                return {"mensaje": "error al guardar cliente"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401

    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if data:
                return {"clientes":data},200
            else:
                return {"mensaje":"error interno"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401
    
    def options(self):
        pass

class ClientesParametros(Resource):
    def put(self, id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            info = request.get_json(force = True)
            print(info)
            nombre = info["nombre"]
            ap_paterno = info["ap_paterno"]
            ap_materno = info["ap_materno"]
            id_direccion = info["direccion"]
            email = info["email"]
            try:
                modificar_cliente(id,nombre,ap_paterno,ap_materno,id_direccion,email)
                return {"mensaje":"cliente modificado correctamente"}
            except:
                return {"mensaje": "error al modificar cliente"},501
        else:
            return {"mensaje": "error se necesita estar autenticado"},401
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_cliente(id)
            if data:
                return {"cliente":data},201
            else:
                return {"mensaje": "cliente no encontrado"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        print(user)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            if eliminar_empleado(id):
                return {"mensaje":"cliente eliminado"}
            else:
                return {"mensaje":"No se encontro al cliente"},404
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def options(self):
        pass
                