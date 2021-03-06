from flask import Blueprint
from app.cliente.controller import ClienteG, ClienteId

cliente_api = Blueprint('cliente_api', __name__)

cliente_api.add_url_rule('/cliente',view_func= ClienteG.as_view('cliente_geral'),methods = ['GET','POST'])

cliente_api.add_url_rule('/cliente/<int:id>',view_func= ClienteId.as_view('cliente_id'),methods = ['GET','PUT','PATCH','DELETE'])

