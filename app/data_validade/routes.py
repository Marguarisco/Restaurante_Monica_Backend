from flask import Blueprint
from app.data_validade.controller import DataValidadeG, DataValidadeId

data_validade_api = Blueprint('data_validade_api', __name__)

data_validade_api.add_url_rule('/data_validade',view_func= DataValidadeG.as_view('data_validade_geral'),methods = ['GET','POST'])

data_validade_api.add_url_rule('/data_validade/<int:id>',view_func= DataValidadeId.as_view('data_validade_id'),methods = ['GET','PUT','PATCH','DELETE'])