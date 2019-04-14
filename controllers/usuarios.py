from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import get_data,delete_user
class Usuario(Resource):
	def post(self):
		requestJson = request.get_json(force=True)
		username = requestJson['usuario']
		id = requestJson['id']
		passw = requestJson['password']
		usuario = Usuario(username,passw,id)
		usuario.save()
		return {"ok": "Usuario registrado"}, 201

class UsuarioGet(Resource):
	def get(self,id):
		data = get_data(id)
		return {"id":data[0] , "usuario":data[1] }

class UsuarioDelete(Resource):
	def delete(self,id):
		ok = delete_user(id)
		if ok:
			return {"borrado": True}
		else:
			return {"borrado": False}