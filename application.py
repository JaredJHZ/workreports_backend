from flask import Flask, request, jsonify, render_template , make_response
from flask_restful import Resource, Api, reqparse
import pdfkit
from clases.usuarios.usuarios import Usuario
from controllers.login import Login
from controllers.usuarios import Usuario, UsuarioGet, UsuarioDelete, UsuariosPut
from controllers.empleados import Empleados,EmpleadosParametros
from controllers.clientes import Clientes,ClientesParametros
from controllers.materiales import MaterialesParametro, Materiales
from controllers.lista_de_materiales import Lista_de_material, ListaDeMaterialesParametro,PrecioLista
from controllers.tareas import Tareas, TareasParametro
from controllers.ordenes import Ordenes, OrdenesPDF, OrdenesConParametro
from flask_restful.utils import cors

application = app = Flask(__name__)
api = Api(app)

api.decorators = [cors.crossdomain(origin='*', headers=['accept', 'Content-Type','authentication'])]

parser = reqparse.RequestParser()


# Rutas de usuario
api.add_resource(Usuario, '/usuarios/')
api.add_resource(UsuarioGet,'/usuarios/<id>')
api.add_resource(UsuariosPut,'/usuarios/update/<id>')
api.add_resource(UsuarioDelete, '/usuarios/delete/<id>')

# Rutas de login
api.add_resource(Login, '/login/<username>')

# Rutas de direcciones

#api.add_resource(Direcciones, '/direcciones/')
#api.add_resource(DireccionesParametro, '/direcciones/<id>')

# Rutas de empleados
api.add_resource(Empleados, '/empleados/')
api.add_resource(EmpleadosParametros, '/empleados/<id>')

# Rutas de clientes
api.add_resource(Clientes, '/clientes/')
api.add_resource(ClientesParametros, '/clientes/<id>')

# Rutas de materiales

api.add_resource(Materiales, '/materiales/')
api.add_resource(MaterialesParametro, '/materiales/<id>')

# Rutas de lista de materiales

api.add_resource(Lista_de_material, '/lista_material/')
api.add_resource(PrecioLista,'/lista_material/precio/<id>')
api.add_resource(ListaDeMaterialesParametro, '/lista_material/<id>')

# Rutas de tareas

api.add_resource(Tareas, '/tareas/')
api.add_resource(TareasParametro, '/tareas/<id>')

# Rutas de ordenes

api.add_resource(Ordenes, '/ordenes/')
api.add_resource(OrdenesConParametro, '/ordenes/<id>')
api.add_resource(OrdenesPDF,'/pdf/<id>')



#main
class HelloWorld(Resource):
    def get(self):
        return {"message":"Hello to workreports"}
api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True)
