from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import check_password, set_token

class Login(Resource):
    def post(self,username):
        requestJson = request.get_json(force=True)
        passw = requestJson['password']
        logged = check_password( username,  passw)
        if logged:
            token = set_token(logged[1])
            return {"sesion":str(token)},200,{"authentications":token}
        else:
            return {"sesion":False},400
    def options(self):
        pass