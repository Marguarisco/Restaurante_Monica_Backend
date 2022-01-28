from app.models import BaseModel, db
from datetime import datetime

class Estoque(BaseModel):
    __tablename__ = 'estoque'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    quantidade = db.Column(db.Integer, nullable=False)
    em_estoque = db.Column(db.Boolean)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    ultima_modificacao = db.Column(db.String(8))

    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), unique=True, nullable=False) #one to one
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id')) #one to many

    data_validade = db.relationship("DataValidade", backref="estoque") #one to many

    def json(self):
        return{
            'id':self.id,
            'quantidade':self. quantidade,
            'em_estoque':self.em_estoque,
            'data_criacao':self.data_criacao,
            'ultima_modificacao':self.ultima_modificacao,
            'produto_id':self.produto_id,
            'funcionario_id':self.funcionario_id
        }
