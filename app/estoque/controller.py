from app.estoque.models import Estoque
from flask import request, jsonify
from flask.views import MethodView

class EstoqueG(MethodView):#/estoque
    def post(self):
        body = request.json

        quantidade = body.get('quantidade')
        em_estoque = body.get('em_estoque')

        if isinstance(quantidade,int) and isinstance(em_estoque,str):
            estoque = Estoque(quantidade=quantidade,em_estoque=em_estoque)

            estoque.save()
            return estoque.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        estoques = Estoque.query.all()

        return jsonify([estoque.json() for estoque in estoques]),200
        
class EstoqueId(MethodView):#/estoque/<int:id>
    def get(self,id):
        estoque = Estoque.query.get_or_404(id)
        return estoque

    def put(self,id):
        body = request.json

        quantidade = body.get('quantidade')
        em_estoque = body.get('em_estoque')

        if isinstance(quantidade,int) and isinstance(em_estoque,str):

            estoque = Estoque.query.get_or_404(id)
            
            estoque.quantidade = quantidade 
            estoque.em_estoque = em_estoque

            estoque.update()
            return estoque.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        estoque = Estoque.query.get_or_404(id)

        quantidade = body.get('quantidade',estoque.quantidade)
        em_estoque = body.get('em_estoque',estoque.em_estoque)

        if isinstance(quantidade,int) and isinstance(em_estoque,str):
            
            estoque.quantidade = quantidade 
            estoque.em_estoque = em_estoque

            estoque.update()
            return estoque.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        estoque = Estoque.query.get_or_404(id)
        estoque.delete(estoque)

        return {"code_status":"deleted"}, 200
        
