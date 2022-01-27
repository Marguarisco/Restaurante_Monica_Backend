from app.funcionario.models import Funcionario
from flask import request, jsonify
from flask.views import MethodView

class FuncionarioG(MethodView):#/funcionario
    def post(self):
        body = request.json

        nome = body.get('nome')
        cpf = body.get('cpf')
        email = body.get('email')
        telefone = body.get('telefone')
        posicao = body.get('posicao')
        data_nascimento = body.get('data_nascimento')


        if isinstance(nome,str) and isinstance(cpf,str) and isinstance(email,str) \
            and isinstance(telefone,str) and isinstance(posicao,str) and isinstance(data_nascimento,str):
            
            funcionario = Funcionario.query.filter_by(email=email).first()

            if funcionario:
                return {"code_status":"funcionario already exist"},400

            funcionario = Funcionario.query.filter_by(cpf=cpf).first()

            if funcionario:
                return {"code_status":"funcionario already exist"},400
            
            funcionario = Funcionario(nome=nome,cpf=cpf,email=email,\
                telefone=telefone,posicao=posicao,data_nascimento=data_nascimento)

            funcionario.save()
            return funcionario.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        funcionarios = Funcionario.query.all()

        return jsonify([funcionario.json() for funcionario in funcionarios]),200
        
class FuncionarioId(MethodView):#/funcionario/<int:id>
    def get(self,id):
        funcionario = Funcionario.query.get_or_404(id)
        return funcionario

    def put(self,id):
        body = request.json

        nome = body.get('nome')
        cpf = body.get('cpf')
        email = body.get('email')
        telefone = body.get('telefone')
        posicao = body.get('posicao')
        data_nascimento = body.get('data_nascimento')

        if isinstance(nome,str) and isinstance(cpf,str) and isinstance(email,str) \
            and isinstance(telefone,str) and isinstance(posicao,str) and isinstance(data_nascimento,str):
            
            funcionario = Funcionario.query.get_or_404(id)
            
            funcionario.nome = nome 
            funcionario.cpf = cpf
            funcionario.email = email
            funcionario.telefone = telefone
            funcionario.posicao = posicao
            funcionario.data_nascimento = data_nascimento


            funcionario.update()
            return funcionario.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        funcionario = Funcionario.query.get_or_404(id)

        nome = body.get('nome',funcionario.nome)
        cpf = body.get('cpf',funcionario.cpf)
        email = body.get('email',funcionario.email)
        telefone = body.get('telefone',funcionario.telefone)
        posicao = body.get('posicao',funcionario.posicao)
        data_nascimento = body.get('data_nascimento',funcionario.data_nascimento)

        if isinstance(nome,str) and isinstance(cpf,str) and isinstance(email,str) \
            and isinstance(telefone,str) and isinstance(posicao,str) and isinstance(data_nascimento,str):
            
            
            funcionario.nome = nome 
            funcionario.cpf = cpf
            funcionario.email = email
            funcionario.telefone = telefone
            funcionario.posicao = posicao
            funcionario.data_nascimento = data_nascimento


            funcionario.update()
            return funcionario.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)

        return {"code_status":"deleted"}, 200
        
