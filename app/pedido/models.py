from app.models import BaseModel, db
from datetime import datetime

class Pedido(BaseModel):
    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    def json(self):
        return{
            'id':self.id,
            'quantidade':self.quantidade,
            'valor':self.valor
        }
