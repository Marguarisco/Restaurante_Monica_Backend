from flask import Blueprint
from app.estoque.controller import EstoqueG, EstoqueId

estoque_api = Blueprint('estoque_api', __name__)

estoque_api.add_url_rule('/estoque',view_func= EstoqueG.as_view('estoque_geral'),methods = ['GET','POST'])

estoque_api.add_url_rule('/estoque/<int:id>',view_func= EstoqueId.as_view('estoque_id'),methods = ['GET','PUT','PATCH','DELETE'])
