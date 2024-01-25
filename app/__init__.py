from flask import Flask
from flask_pymongo import PyMongo
from .routes import bp as main_bp
from .auth import auth_bp as auth_bp
from flask_jwt_extended import JWTManager
from config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
