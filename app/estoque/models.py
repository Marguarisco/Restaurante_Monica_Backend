from app.models import BaseModel, db

class Estoque(BaseModel):
    __tablename__ = 'estoque'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    quantidade = db.Column(db.Integer)
    em_estoque = db.Column(db.Integer)

    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), unique=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))

    def json(self):
        return{
            'id':self.id,
            'quantidade':self. quantidade,
            'em_estoque':self.em_estoque
        }
