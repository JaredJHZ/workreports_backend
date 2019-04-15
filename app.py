from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from clases.usuarios.usuarios import Usuario
from controllers.login import Login
from controllers.usuarios import Usuario, UsuarioGet, UsuarioDelete
from controllers.direcciones import Direcciones,DireccionesParametro
from controllers.empleados import Empleados,EmpleadosParametros
from controllers.clientes import Clientes,ClientesParametros
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


# Rutas de usuario
api.add_resource(Usuario, '/usuario/')
api.add_resource(UsuarioGet,'/usuario/<id>')
api.add_resource(UsuarioDelete, '/delete/user/<id>')

# Rutas de login
api.add_resource(Login, '/login/<username>')

# Rutas de direcciones

api.add_resource(Direcciones, '/direcciones/')
api.add_resource(DireccionesParametro, '/direcciones/<id>')

# Rutas de empleados
api.add_resource(Empleados, '/empleados/')
api.add_resource(EmpleadosParametros, '/empleados/<id>')

# Rutas de clientes
api.add_resource(Clientes, '/clientes/')
api.add_resource(ClientesParametros, '/clientes/<id>')

if __name__ == '__main__':
    app.run(debug=True)