from flask import Blueprint
from app.pedido.controller import PedidoG, PedidoId

pedido_api = Blueprint('pedido_api', __name__)

pedido_api.add_url_rule('/pedido',view_func= PedidoG.as_view('pedido_geral'),methods = ['GET','POST'])

pedido_api.add_url_rule('/pedido/<int:id>',view_func= PedidoId.as_view('pedido_id'),methods = ['GET','PUT','PATCH','DELETE'])
