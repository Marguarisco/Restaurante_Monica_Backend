from app.produto_pedido.models import ProdutoPedido
from flask import request, jsonify
from flask.views import MethodView

class ProdutoPedidoG(MethodView):#/produto_pedido
    def get(self,):

        produto_pedidos = ProdutoPedido.query.all()

        return jsonify([produto_pedido.json() for produto_pedido in produto_pedidos]),200
        
class ProdutoPedidoId(MethodView):#/produto_pedido/<int:id>
    def get(self,id):
        produto_pedido = ProdutoPedido.query.get_or_404(id)
        return produto_pedido

