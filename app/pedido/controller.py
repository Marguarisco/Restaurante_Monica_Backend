from app.pedido.models import Pedido
from flask import request, jsonify
from flask.views import MethodView

class PedidoG(MethodView):#/pedido
    def post(self,):
        body = request.json

        quantidade = body.get('quantidade')
        valor = body.get('valor')


        if isinstance(quantidade,int) and isinstance(valor,float):
            
            pedido = Pedido(quantidade=quantidade,valor=valor)

            pedido.save()
            return pedido.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self,):

        pedidos = Pedido.query.all()

        return jsonify([pedido.json() for pedido in pedidos]),200
        
class PedidoId(MethodView):#/pedido/<int:id>
    def get(self,id):
        pedido = Pedido.query.get_or_404(id)
        return pedido

    def put(self,id):
        body = request.json

        quantidade = body.get('quantidade')
        valor = body.get('valor')

        if isinstance(quantidade,int) and isinstance(valor,float):

            pedido = Pedido.query.get_or_404(id)
            
            pedido.quantidade = quantidade 
            pedido.valor = valor

            pedido.update()
            return pedido.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        pedido = Pedido.query.get_or_404(id)

        quantidade = body.get('quantidade',pedido.quantidade)
        valor = body.get('valor',pedido.valor)


        if isinstance(quantidade,int) and isinstance(valor,float):
            
            pedido.quantidade = quantidade 
            pedido.valor = valor

            pedido.update()
            return pedido.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        pedido = Pedido.query.get_or_404(id)
        pedido.delete(pedido)

        return {"code_status":"deleted"}, 200
        
