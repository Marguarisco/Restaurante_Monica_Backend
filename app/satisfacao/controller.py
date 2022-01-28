from app.satisfacao.models import Satisfacao
from flask import request, jsonify, render_template
from flask.views import MethodView
from flask_mail import Message
from app.extensions import mail

class SatisfacaoG(MethodView):#/satisfacao
    def post(self):
        body = request.json

        email = body.get('email')
        atendimento = body.get('atendimento')
        sabor_comida = body.get('sabor_comida')   
        limpeza_organizacao = body.get('limpeza_organizacao')
        preco = body.get('preco')
        velocidade_servico = body.get('velocidade_servico')
        ambiente = body.get('ambiente')


        if isinstance(atendimento,int) and isinstance(sabor_comida,int) and isinstance(email,str) \
            and isinstance(limpeza_organizacao,int) and isinstance(preco,int) and isinstance(velocidade_servico,int) \
            and isinstance(ambiente,int):
            
            satisfacao = Satisfacao(atendimento=atendimento,sabor_comida=sabor_comida,email=email,\
                limpeza_organizacao=limpeza_organizacao,preco=preco,velocidade_servico=velocidade_servico,\
                ambiente=ambiente)

             

            msg = Message (
                sender= 'restaurantedamonicaweb@gmail.com',
                recipientes= [email],
                subject= 'Obrigado pela avaliação',
                html= render_template('email.html')
            )

            mail.send(msg)
            

            satisfacao.save()
            return satisfacao.json(),200
        return {"code_status":"invalid data in request"},400

    def get(self):

        satisfacaos = Satisfacao.query.all()

        return jsonify([satisfacao.json() for satisfacao in satisfacaos]),200


class SatisfacaoId(MethodView):#/satisfacao/<int:id>
    def get(self,id):
        satisfacao = Satisfacao.query.get_or_404(id)
        return satisfacao.json()

    def put(self,id):
        body = request.json

        email = body.get('email')
        atendimento = body.get('atendimento')
        sabor_comida = body.get('sabor_comida')   
        limpeza_organizacao = body.get('limpeza_organizacao')
        preco = body.get('preco')
        velocidade_servico = body.get('velocidade_servico')
        ambiente = body.get('ambiente')

        if isinstance(atendimento,int) and isinstance(sabor_comida,int) and isinstance(email,str) \
            and isinstance(limpeza_organizacao,int) and isinstance(preco,int) and isinstance(velocidade_servico,int) \
            and isinstance(ambiente,int):

            satisfacao = Satisfacao.query.get_or_404(id)
            
            satisfacao.atendimento = atendimento 
            satisfacao.sabor_comida = sabor_comida
            satisfacao.email = email
            satisfacao.limpeza_organizacao = limpeza_organizacao
            satisfacao.preco = preco
            satisfacao.velocidade_servico = velocidade_servico
            satisfacao.ambiente = ambiente


            satisfacao.update()
            return satisfacao.json(),200
        return {"code_status":"invalid data in request"},400

    def patch(self,id):
        body = request.json
        satisfacao = Satisfacao.query.get_or_404(id)

        atendimento = body.get('atendimento',satisfacao.atendimento)
        sabor_comida = body.get('sabor_comida',satisfacao.sabor_comida)
        email = body.get('email',satisfacao.email)
        limpeza_organizacao = body.get('limpeza_organizacao',satisfacao.limpeza_organizacao)
        preco = body.get('preco',satisfacao.preco)
        velocidade_servico = body.get('velocidade_servico',satisfacao.velocidade_servico)
        ambiente = body.get('ambiente',satisfacao.ambiente)

        if isinstance(atendimento,int) and isinstance(sabor_comida,int) and isinstance(email,str) \
            and isinstance(limpeza_organizacao,int) and isinstance(preco,int) and isinstance(velocidade_servico,int) \
            and isinstance(ambiente,int):
            
            satisfacao.atendimento = atendimento 
            satisfacao.sabor_comida = sabor_comida
            satisfacao.email = email
            satisfacao.limpeza_organizacao = limpeza_organizacao
            satisfacao.preco = preco
            satisfacao.velocidade_servico = velocidade_servico
            satisfacao.ambiente = ambiente


            satisfacao.update()
            return satisfacao.json(),200
        return {"code_status":"invalid data in request"},400

    def delete(self,id):
        satisfacao = Satisfacao.query.get_or_404(id)
        satisfacao.delete(satisfacao)

        return {"code_status":"deleted"}, 200
        
