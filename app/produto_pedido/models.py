from app.models import db

produto_pedido = db.Table(('produto_pedido'), db.Column('produto_id',db.Integer,db.ForeignKey('produto.id')), db.Column('pedido_id',db.Integer,db.ForeignKey('pedido.id')))