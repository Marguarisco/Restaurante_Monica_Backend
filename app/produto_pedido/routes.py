from flask import Blueprint
from app.produto_pedido.controller import ProdutoPedidoG, ProdutoPedidoId

produto_pedido_api = Blueprint('produto_pedido_api', __name__)

produto_pedido_api.add_url_rule('/produto_pedido',view_func= ProdutoPedidoG.as_view('produto_pedido_geral'),methods = ['GET'])

produto_pedido_api.add_url_rule('/produto_pedido/<int:id>',view_func= ProdutoPedidoId.as_view('produto_pedido_id'),methods = ['GET'])
