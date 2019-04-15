from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import get_data,delete_user
from clases.usuarios.usuarios import Usuario as User
from middlewares.middlewares import authentication
import jwt
from configuration import key
class Usuario(Resource):
	def post(self):
		token = request.headers.get("Authentication")
		if token:
			user = authentication(token)
			if user:
				permission = user["permission"]
				print(permission)
				if permission == 'ADMIN':
					requestJson = request.get_json(force=True)
					username = requestJson['usuario']
					id = requestJson['id']
					passw = requestJson['password']
					privilegios = requestJson['privilegios']
					usuario = User(username,passw,privilegios,id)
					usuario.save()
					return {"ok": "Usuario registrado"}, 201
				else:
					return {"errr": "No es el permiso adecuado"}
			else:
				return {"error": "permiso denegado"}, 401

class UsuarioGet(Resource):
	def get(self,id):
		try:
			if user:
				data = get_data(id)
				return {"id":data[0] , "usuario":data[1] },200
			else:
				return {"autenticacion":"fallada"}, 400
		except:
			return {"autenticacion":"fallada"}, 400

class UsuarioDelete(Resource):
	def delete(self,id):
		token = request.headers.get("Authentication")
		user = authentication(token)
		permission = user["permission"]
		try:
			if user and permission == 'ADMIN':
				ok = delete_user(id)
				if ok:
					return {"borrado": True},201
				else:
					return {"borrado": False},401
			else:
				return {"error": "permiso denegado"},404
		except:
			return {"error":"permiso denegado"},401