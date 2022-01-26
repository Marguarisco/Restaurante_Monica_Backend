from app.models import BaseModel, db


class Funcionario(BaseModel):
    __tablename__ = 'funcionario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(70), unique=True, index=True)
    telefone = db.Column(db.String(13))
    posicao = db.Column(db.String(20))
    data_nascimento = db.Column(db.String(10))

    estoque = db.relationship("Estoque",backref="Empregado")

    def json(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'cpf':self.cpf,
            'email':self.email,
            'telefone':self.telefone,
            'posicao':self.posicao,
            'data_nascimento':self.data_nascimento
        }