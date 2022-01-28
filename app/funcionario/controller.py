from click import decorators
from app.funcionario.models import Funcionario
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import jwt
from flask_jwt_extended import create_access_token, jwt_required

import bcrypt

class FuncionarioG(MethodView):#/funcionario
    def post(self):
        body = request.json

        nome = body.get('nome')
        cpf = body.get('cpf')
        email = body.get('email')
        telefone = body.get('telefone')
        posicao = body.get('posicao')
        data_nascimento = body.get('data_nascimento')
        senha = body.get('senha')


        if isinstance(nome,str) and isinstance(cpf,str) and isinstance(email,str) \
            and isinstance(telefone,str) and isinstance(posicao,str) and isinstance(data_nascimento,str):
            
            funcionario = Funcionario.query.filter_by(email=email).first()

            if funcionario:
                return {"code_status":"funcionario already exist"},400

            funcionario = Funcionario.query.filter_by(cpf=cpf).first()

            if funcionario:
                return {"code_status":"funcionario already exist"},400

            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            
            funcionario = Funcionario(nome=nome,cpf=cpf,email=email,\
                telefone=telefone,posicao=posicao,data_nascimento=data_nascimento,senha_hash=senha_hash)

            funcionario.save()
            return funcionario.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        funcionarios = Funcionario.query.all()

        return jsonify([funcionario.json() for funcionario in funcionarios]),200
        
class FuncionarioId(MethodView):#/funcionario/<int:id>
    decorators = [jwt_required()]
    def get(self,id):
        funcionario = Funcionario.query.get_or_404(id)
        print(funcionario)
        return funcionario.json(),200

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
        
class FuncionarioLogin(MethodView):#/login
    def post(self):
        body = request.json

        id = body.get('id')
        senha = body.get('senha')

        funcionario = Funcionario.query.get_or_404(id)

        if not funcionario or bcrypt.hashpw(senha.encode(), funcionario.senha_hash) != funcionario.senha_hash: 
            return {"code_status":"id or senha do not exist"},400
        
        token = create_access_token(identity = funcionario.id)

        return {"token": token},200

