from app.models import BaseModel, db

class ProdutoPedido(BaseModel):
    __tablename__ = 'produto_pedido'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))

    def json(self):
        return{
            'id':self.id,
            'produto_id':self.produto_id,
            'pedido_id':self.pedido_id
        }
