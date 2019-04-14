from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import check_password

class Login(Resource):
    def post(self,username):
        requestJson = request.get_json(force=True)
        passw = requestJson['password']
        logged = check_password( username,  passw)
        if logged:
            return {"sesion":True},200
        else:
            return {"sesion":False},400