from app.models import BaseModel, db
from app.produto_pedido.models import ProdutoPedido



class Produto(BaseModel):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    tipo = db.Column(db.String(20)) #[COMIDA,BEBIDA]
    descricao = db.Column(db.String(2000))
    serve = db.Column(db.Integer)
    restricao = db.Column(db.String)
    valor = db.Column(db.Float)

    pedidos = db.relationship("Pedido", secondary=ProdutoPedido, backref="Produto")
    estoque = db.relationship("Estoque",backref='Produto',uselist=False)

    def json(self):
        return{
            'id':self.id,
            'nome':self.nome,
            'tipo':self.tipo,
            'descricao':self.descricao,
            'serve':self.serve,
            'restricao':self.restricao,
            'valor':self.valor
        }
