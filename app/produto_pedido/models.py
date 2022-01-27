from app.models import db

#Tabela auxiliar para criar a relação many to many entre produto e pedido

produto_pedido = db.Table(('produto_pedido'), \
    db.Column('produto_id', db.Integer, db.ForeignKey('produto.id'), primary_key=True), \
    db.Column('pedido_id', db.Integer, db.ForeignKey('pedido.id'), primary_key=True))