from flask import Blueprint
from app.satisfacao.controller import SatisfacaoG ,SatisfacaoId

satisfacao_api = Blueprint('satisfacao_api', __name__)

satisfacao_api.add_url_rule('/satisfacao',view_func= SatisfacaoG.as_view('satisfacao_geral'),methods = ['GET','POST'])

satisfacao_api.add_url_rule('/satisfacao/<int:id>',view_func= SatisfacaoId.as_view('satisfacao_id'),methods = ['GET','PUT','PATCH','DELETE'])
