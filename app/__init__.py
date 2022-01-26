from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.cliente.routes import cliente_api
from app.pedido.routes import pedido_api
from app.produto.routes import produto_api
from app.funcionario.routes import funcionario_api
from app.estoque.routes import estoque_api


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(cliente_api)
    app.register_blueprint(pedido_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(estoque_api)
    app.register_blueprint(funcionario_api)


    return app

app = create_app
