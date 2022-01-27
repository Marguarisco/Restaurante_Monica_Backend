from app.models import BaseModel, db



class Produto(BaseModel):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(20)) #[COMIDA,BEBIDA,etc]
    descricao = db.Column(db.String(2000))
    serve = db.Column(db.Integer)
    restricao = db.Column(db.String) #[VEGETARIANO,VEGANO,GLUTEN FREE,etc]
    valor = db.Column(db.Float, nullable=False)

    estoque = db.relationship("Estoque",backref='produtos',uselist=False) #one to one

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
