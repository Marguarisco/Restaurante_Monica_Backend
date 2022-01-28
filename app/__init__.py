from flask import Flask
from app.config import Config
from app.extensions import db, migrate, mail, jwt
from app.cliente.routes import cliente_api
from app.pedido.routes import pedido_api
from app.produto.routes import produto_api
from app.funcionario.routes import funcionario_api
from app.estoque.routes import estoque_api
from app.data_validade.routes import data_validade_api
from app.satisfacao.routes import satisfacao_api


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(cliente_api)
    app.register_blueprint(pedido_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(estoque_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(data_validade_api)
    app.register_blueprint(satisfacao_api)




    return app

app = create_app
