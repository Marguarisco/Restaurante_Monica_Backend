from app.produto.models import Produto
from flask import request, jsonify
from flask.views import MethodView

class ProdutoG(MethodView):#/produto
    def post(self):
        body = request.json

        nome = body.get('nome')
        tipo = body.get('tipo')
        descricao = body.get('descricao')
        serve = body.get('serve')
        restricao = body.get('restricao')
        valor = body.get('valor')


        if isinstance(nome,str) and isinstance(tipo,str) and isinstance(descricao,str) \
            and isinstance(serve,int) and isinstance(restricao,str) and isinstance(valor,float):
            
            produto = Produto(nome=nome,tipo=tipo,descricao=descricao,\
                serve=serve,restricao=restricao,valor=valor)

            produto.save()
            return produto.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        produtos = Produto.query.all()

        return jsonify([produto.json() for produto in produtos]),200
        
class ProdutoId(MethodView):#/produto/<int:id>
    def get(self,id):
        produto = Produto.query.get_or_404(id)
        return produto.json()

    def put(self,id):
        body = request.json

        nome = body.get('nome')
        tipo = body.get('tipo')
        descricao = body.get('descricao')
        serve = body.get('serve')
        restricao = body.get('restricao')
        valor = body.get('valor')

        if isinstance(nome,str) and isinstance(tipo,str) and isinstance(descricao,str) \
            and isinstance(serve,int) and isinstance(restricao,str) and isinstance(valor,float):
            
            produto = Produto.query.get_or_404(id)
            
            produto.nome = nome 
            produto.tipo = tipo
            produto.descricao = descricao
            produto.serve = serve
            produto.restricao = restricao
            produto.valor = valor


            produto.update()
            return produto.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        produto = Produto.query.get_or_404(id)

        nome = body.get('nome',produto.nome)
        tipo = body.get('tipo',produto.tipo)
        descricao = body.get('descricao',produto.descricao)
        serve = body.get('serve',produto.serve)
        restricao = body.get('restricao',produto.restricao)
        valor = body.get('valor',produto.valor)

        if isinstance(nome,str) and isinstance(tipo,str) and isinstance(descricao,str) \
            and isinstance(serve,int) and isinstance(restricao,str) and isinstance(valor,float):
            
            
            produto.nome = nome 
            produto.tipo = tipo
            produto.descricao = descricao
            produto.serve = serve
            produto.restricao = restricao
            produto.valor = valor


            produto.update()
            return produto.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        produto = Produto.query.get_or_404(id)
        produto.delete(produto)

        return {"code_status":"deleted"}, 200
        
