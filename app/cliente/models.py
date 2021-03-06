from app.models import BaseModel, db

class Cliente(BaseModel):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)

    pedido = db.relationship("Pedido", backref='comprador') #one to many

    def json(self):
        return{
            'id':self.id,
            'nome':self.nome
        }
