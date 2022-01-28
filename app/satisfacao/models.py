from app.models import BaseModel, db
from datetime import datetime


class Satisfacao(BaseModel):
    __tablename__ = 'satisfacao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    email = db.Column(db.String(200), nullable=False)
    atendimento = db.Column(db.Integer)
    sabor_comida = db.Column(db.Integer)
    limpeza_organizacao = db.Column(db.Integer)
    preco = db.Column(db.Integer, nullable=False)
    velocidade_servico = db.Column(db.Integer)
    ambiente = db.Column(db.Integer)
    data_criacao = db.Column(db.DateTime, default=datetime.now)

    

    def json(self):
        return {
            'id':self.id,
            'email':self.email,
            'atendimento':self.atendimento,
            'sabor_comida':self.sabor_comida,
            'limpeza_organizacao':self.limpeza_organizacao,
            'preco':self.preco,
            'velocidade_servico':self.velocidade_servico,
            'ambiente':self.ambiente,
            'data_criacao':self.data_criacao
        }