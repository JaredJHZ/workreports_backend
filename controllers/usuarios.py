from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import get_data,delete_user, modificar_usuario, get_all_usuarios
from clases.usuarios.usuarios import Usuario as User
from middlewares.middlewares import authentication

class Usuario(Resource):
	def options(self):
		pass
    	
	def post(self):
		token = request.headers.get("Authentication")
		if token:
			user = authentication(token)
			if user:
				permission = user["permission"]
				if permission == 'ADMIN':
					requestJson = request.get_json(force=True)
					username = requestJson['usuario']
					id = requestJson['id']
					passw = requestJson['password']
					privilegios = requestJson['privilegios']
					usuario = User(username,passw,privilegios,id)
					usuario.save()
					return {"mensaje": "Usuario registrado"}, 201
				else:
					return {"mensaje": "No es el permiso adecuado"}
			else:
				return {"mensaje": "permiso denegado"}, 401

	def get(self):
		token = request.headers.get("authentication")
		if token:
			user = authentication(token)
			if user:
				permission = user["permission"]
				if permission == 'ADMIN':
					usuarios = get_all_usuarios()
					return {"usuarios":usuarios}, 200
				else:
					return {"mensaje": "No es el permiso adecuado"}
			else:
				return {"mensaje": "permiso denegado"}
		else:
			return {"mensaje": "permiso denegado"}
class UsuarioGet(Resource):
	def options(self):
		pass
        
	def get(self,id):
		token = request.headers.get("authentication")
		if token:
			user = authentication(token)
			try:
				if user:
					data = get_data(id)
					return {"id":data[0] , "usuario":data[1], "permission":data[3] },200
				else:
					return {"mensaje":"Error al cargar usuario"}, 400
			except:
				return {"mensaje":"Error al cargar usuario"}, 404


class UsuarioDelete(Resource):
	def options(self):
		pass
        
	def delete(self,id):
		token = request.headers.get("Authentication")
		user = authentication(token)
		permission = user["permission"]
		try:
			if user and permission == 'ADMIN':
				ok = delete_user(id)
				if ok:
					return {"mensaje": "Usuario eliminado!"},201
				else:
					return {"mensaje": "No se pudo eliminar el usuario"},401
			else:
				return {"mensaje": "permiso denegado"},404
		except:
			return {"mensaje":"permiso denegado"},401

class UsuariosPut(Resource):
	def options(self):
		pass
	
	def put(self,id):
		token = request.headers.get("Authentication")
		user = authentication(token)
		permission = user["permission"]
		try:
			if user and permission == 'ADMIN':
				requestJson = request.get_json(force=True)
				username = requestJson['usuario']
				passw = requestJson['password']
				privilegios = requestJson['privilegios']
				ok = modificar_usuario(id,username,passw,privilegios)
				if ok:
					return {"mensaje": "Usuario modificado"},201
				else:
					return {"mensaje": "No se pudo modificar"},401
			else:
				return {"mensaje": "permiso denegado"},404
		except:
			return {"mensaje":"permiso denegado"},401