from app.data_validade.models import DataValidade
from flask import request, jsonify
from flask.views import MethodView

class DataValidadeG(MethodView):#/data_validade
    def post(self):
        body = request.json

        quantidade = body.get('quantidade')
        data = body.get('data')
        produto_id = body.get('produto_id')
        estoque_id = body.get('estoque_id')


        if isinstance(quantidade,int) and isinstance(data,str):
            
            data_validade = DataValidade(quantidade=quantidade,data=data,\
                produto_id=produto_id,estoque_id=estoque_id)

            data_validade.save()
            return data_validade.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        data_validades = DataValidade.query.all()

        return jsonify([data_validade.json() for data_validade in data_validades]),200
        
class DataValidadeId(MethodView):#/data_validade/<int:id>
    def get(self,id):
        data_validade = DataValidade.query.get_or_404(id)
        return data_validade.json()

    def put(self,id):
        body = request.json

        quantidade = body.get('quantidade')
        data = body.get('data')
        produto_id = body.get('produto_id')
        estoque_id = body.get('estoque_id')

        if isinstance(quantidade,int) and isinstance(data,str):
            
            data_validade = DataValidade.query.get_or_404(id)
            
            data_validade.quantidade = quantidade
            data_validade.data = data
            data_validade.produto_id = produto_id
            data_validade.estoque_id = estoque_id


            data_validade.update()
            return data_validade.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        data_validade = DataValidade.query.get_or_404(id)

        quantidade = body.get('quantidade',data_validade.quantidade)
        data = body.get('data',data_validade.data)
        produto_id = body.get('produto_id',data_validade.produto_id)
        estoque_id = body.get('estoque_id',data_validade.estoque_id)

        if isinstance(quantidade,int) and isinstance(data,str):
            
            data_validade.quantidade = quantidade
            data_validade.data = data
            data_validade.produto_id = produto_id
            data_validade.estoque_id = estoque_id

            data_validade.update()
            return data_validade.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        data_validade = DataValidade.query.get_or_404(id)
        data_validade.delete(data_validade)

        return {"code_status":"deleted"}, 200
        
