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

    if app.app_context():
        from . import routes
        from . import auth

        db.create_all()

        return app