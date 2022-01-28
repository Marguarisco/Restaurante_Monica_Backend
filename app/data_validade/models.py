from app.models import BaseModel, db
from datetime import datetime


class DataValidade(BaseModel):
    __tablename__ = 'data_validade'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    quantidade = db.Column(db.Integer)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    data = db.Column(db.String(8))

    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), unique=True, nullable=False) #one to many
    estoque_id = db.Column(db.Integer, db.ForeignKey('estoque.id'), unique=True, nullable=False) #one to many

    def json(self):
        return {
            'id':self.id,
            'quantidade':self.quantidade,
            'data_criacao':self.data_criacao,
            'data':self.data
        }