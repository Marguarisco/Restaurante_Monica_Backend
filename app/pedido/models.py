from app.models import BaseModel, db
from datetime import datetime
from app.produto_pedido.models import produto_pedido

class Pedido(BaseModel):
    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    data_pagamento = db.Column(db.DateTime)
    finalizado = db.Column(db.Boolean, default=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'),nullable=False) #one to many

    produtos = db.relationship("Produto", secondary=produto_pedido, backref="pedidos") #many to many
    
    def json(self):
        return{
            'id':self.id,
            'quantidade':self.quantidade,
            'valor':self.valor,
            'data_criacao':self.data_criacao,
            'finalizado':self.finalizado,
            'data_pagamento':self.data_pagamento,
            'cliente_id':self.cliente_id
        }
