from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from .authentication import auth

        app.register_blueprint(auth.auth_blueprint)
        app.register_blueprint(routes.main_blueprint)

        db.create_all()

        return app