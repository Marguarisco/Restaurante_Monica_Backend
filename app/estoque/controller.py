from datetime import date

from app.estoque.models import Estoque
from flask import request, jsonify
from flask.views import MethodView

class EstoqueG(MethodView):#/estoque
    def post(self):
        body = request.json

        quantidade = body.get('quantidade')
        ultima_modificacao = body.get('ultima_modificacao')
        produto_id = body.get('produto_id')
        funcionario_id = body.get('funcionario_id')

        if quantidade >= 0:
            em_estoque = True
        else:
            em_estoque = False

        if isinstance(quantidade,int) and isinstance(produto_id,int):

            estoque = Estoque.query.filter_by(produto_id=produto_id).first()

            if estoque:
                return {"Code_status":"produto_id already linked to another estoque"},400

            estoque = Estoque(quantidade=quantidade,ultima_modificacao=ultima_modificacao,\
            produto_id=produto_id,funcionario_id=funcionario_id,em_estoque=em_estoque)

            estoque.save()
            return estoque.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        estoques = Estoque.query.all()

        return jsonify([estoque.json() for estoque in estoques]),200
        
class EstoqueId(MethodView):#/estoque/<int:id>
    def get(self,id):
        estoque = Estoque.query.get_or_404(id)
        return estoque.json()

    def put(self,id):
        body = request.json

        quantidade = body.get('quantidade')
        ultima_modificacao = body.get('ultima_modificacao')
        produto_id = body.get('produto_id')
        funcionario_id = body.get('funcionario_id')

        if quantidade >= 0:
            em_estoque = True
        else:
            em_estoque = False


        if isinstance(quantidade,int) and isinstance(produto_id,int):

            estoque = Estoque.query.get_or_404(id)
            
            estoque.quantidade = quantidade 
            estoque.ultima_modificacao = ultima_modificacao
            estoque.produto_id = produto_id
            estoque.funcionario_id = funcionario_id
            estoque.em_estoque = em_estoque

            estoque.update()
            return estoque.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        estoque = Estoque.query.get_or_404(id)

        quantidade = body.get('quantidade',estoque.quantidade)
        ultima_modificacao = body.get('ultima_modificacao',estoque.ultima_modificacao)
        produto_id = body.get('produto_id',estoque.produto_id)
        funcionario_id = body.get('funcionario_id',estoque.produto_id)

        if quantidade >= 0:
            em_estoque = True
        else:
            em_estoque = False


        if isinstance(quantidade,int) and isinstance(produto_id,int) :
            
            estoque.quantidade = quantidade 
            estoque.ultima_modificacao = ultima_modificacao
            estoque.quantidade = quantidade 
            estoque.produto_id = produto_id 
            estoque.funcionario_id = funcionario_id
            estoque.em_estoque = em_estoque

            estoque.update()
            return estoque.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        estoque = Estoque.query.get_or_404(id)
        estoque.delete(estoque)

        return {"code_status":"deleted"}, 200
        
