from app.pedido.models import Pedido
from flask import request, jsonify
from flask.views import MethodView
from app.produto.models import Produto

class PedidoG(MethodView):#/pedido
    def post(self):
        body = request.json

        quantidade = body.get('quantidade')
        valor = body.get('valor')
        data_pagamento = body.get('data_pagamento')
        finalizado = body.get('finalizado')
        cliente_id = body.get('cliente_id')
        produtos = body.get('produtos')

        if isinstance(quantidade,int) and isinstance(valor,float) and isinstance(produtos,list):
            lista_produtos = []
            for i in produtos:
                produto = Produto.query.filter_by(nome=i).first()
                if not produto:
                    return {"code_status":f"produto named {i} not exist"},400
                lista_produtos += [produto]

            pedido = Pedido(quantidade=quantidade,valor=valor,data_pagamento=data_pagamento,\
                finalizado=finalizado,cliente_id=cliente_id,produtos=lista_produtos)

            pedido.save()
            return pedido.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        pedidos = Pedido.query.all()

        return jsonify([pedido.json() for pedido in pedidos]),200
        
class PedidoId(MethodView):#/pedido/<int:id>
    def get(self,id):
        pedido = Pedido.query.get_or_404(id)
        return pedido.json()

    def put(self,id):
        body = request.json

        quantidade = body.get('quantidade')
        valor = body.get('valor')
        data_pagamento = body.get('data_pagamento')
        finalizado = body.get('finalizado')
        produtos = body.get('produtos')


        if isinstance(quantidade,int) and isinstance(valor,float) and isinstance(produtos,list):

            lista_produtos = []
            for i in produtos:
                produto = Produto.query.filter_by(nome=i).first()
                if not produto:
                    return {"code_status":f"produto named {i} not exist"},400
                lista_produtos += [produto]

            pedido = Pedido.query.get_or_404(id)
            
            pedido.quantidade = quantidade 
            pedido.valor = valor
            pedido.data_pagamento = data_pagamento
            pedido.finalizado = finalizado
            pedido.produtos = lista_produtos

            pedido.update()
            return pedido.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        pedido = Pedido.query.get_or_404(id)

        quantidade = body.get('quantidade',pedido.quantidade)
        valor = body.get('valor',pedido.valor)
        data_pagamento = body.get('data_pagamento',pedido.data_pagamento)
        finalizado = body.get('finalizado',pedido.finalizado)


        if isinstance(quantidade,int) and isinstance(valor,float):
            
            pedido.quantidade = quantidade 
            pedido.valor = valor
            pedido.data_pagamento = data_pagamento
            pedido.finalizado = finalizado

            pedido.update()
            return pedido.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        pedido = Pedido.query.get_or_404(id)
        pedido.delete(pedido)

        return {"code_status":"deleted"}, 200
        
