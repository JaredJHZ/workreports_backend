from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import Usuario
from controllers.login import Login
from controllers.usuarios import Usuario, UsuarioGet, UsuarioDelete
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()



api.add_resource(Usuario, '/usuario/post')
api.add_resource(UsuarioGet,'/usuario/<id>')
api.add_resource(Login, '/login/<username>')
api.add_resource(UsuarioDelete, '/delete/user/<id>')

if __name__ == '__main__':
    app.run(debug=True)