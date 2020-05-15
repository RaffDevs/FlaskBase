from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from Routes.routes import init_app
config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='Templates', static_folder='Static')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    return app