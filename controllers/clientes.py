from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.clientes.clientes import clientes, get_cliente, modificar_cliente, eliminar_empleado, get_all
from middlewares.middlewares import authentication
import psycopg2
from errors import errorHandling
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
            email = info["email"]
            calle = info["calle"]
            ciudad = info["ciudad"]
            estado = info["estado"]
            cp = info["cp"]
            cliente = clientes(id,ap_paterno,ap_materno,nombre,calle,
            ciudad, estado , cp, email)
            cliente = cliente.save()
            if (cliente[0]) == False:
                return {"mensaje": errorHandling(cliente[1], cliente[2])},501    
            else:
                return {"mensaje": "exito al guardar cliente"},201
            return {"mensaje": "error al guardar cliente"},501
        else:
            return {"mensaje": "error, necesita autenticarse"},401

    def get(self):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            data = get_all()
            if (data[0]) == False:
                return {"mensaje": errorHandling(data[1], data[2])},501   
            else:
                return {"clientes":data},200
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
                cliente = modificar_cliente(id,nombre,ap_paterno,ap_materno,id_direccion,email)
                if (cliente[0]) == False:
                    return {"mensaje": errorHandling(cliente[1], cliente[2])},501   
                return {"mensaje":"cliente modificado correctamente"}
            except:
                return {"mensaje": "error al modificar cliente"},501
        else:
            return {"mensaje": "error se necesita estar autenticado"},401
    
    def get(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        if user:
            cliente = get_cliente(id)
            if (cliente[0]) == False:
                return {"mensaje": errorHandling(cliente[1], cliente[2])},501   
            else:
                return {"cliente":cliente},201
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def delete(self,id):
        token = request.headers.get("authentication")
        user = authentication(token)
        permission = user["permission"]
        if user and permission == 'ADMIN':
            cliente = eliminar_empleado(id)
            if (cliente[0]) == False:
                return {"mensaje": errorHandling(cliente[1], cliente[2])},501   
            return {"mensaje":"cliente eliminado"},201
        else:
            return {"mensaje": "error se necesita estar autenticado"},400

    def options(self):
        pass