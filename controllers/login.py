from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import check_password, set_token
import os

class Login(Resource):
    def post(self,username):
        info = request.get_json(force=True)
        passw = info['password']
        logged = check_password( username,  passw)
        if logged == "error":
            return {"mensaje":"error en base de datos"},400
        if logged:
            token = set_token(logged[1])
            if token:
                return {"sesion":str(token)},200,{"authentications":token}
            else:
                return {"mensaje":"Usuario no registrado"},404
        else:
            return {"mensaje":"Usuario no registrado"},400
    def options(self):
        pass
