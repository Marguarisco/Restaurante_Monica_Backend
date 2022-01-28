from app.cliente.models import Cliente
from flask import jsonify, request
from flask.views import MethodView

class ClienteG(MethodView):#/cliente
    def get(self):
        clientes = Cliente.query.all()

        return jsonify([cliente.json() for cliente in clientes]),200

    def post(self):
        body = request.json

        nome = body.get('nome')

        if isinstance(nome,str):
            
            cliente = Cliente(nome=nome)

            cliente.save()
            return cliente.json(),200

        return {"code_status":"invalid data in request"},400

class ClienteId(MethodView):#/cliente/<int:id>
    def get(self,id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.json()

    def put(self,id):
        body = request.json

        nome = body.get('nome')

        if isinstance(nome,str):
            
            cliente = Cliente.query.get_or_404(id)
            
            cliente.nome = nome 

            cliente.update()
            return cliente.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        cliente = Cliente.query.get_or_404(id)

        nome = body.get('nome',cliente.nome)

        if isinstance(nome,str):
            
            
            cliente.nome = nome 

            cliente.update()
            return cliente.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)

        return {"code_status":"deleted"}, 200