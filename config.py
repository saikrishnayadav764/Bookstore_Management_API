import os

class Config:
    MONGO_URI = 'mongodb+srv://naruto:naruto@cluster0.be644zi.mongodb.net/db' #Connection String
    JWT_SECRET_KEY = 'super-secret'  # Secret Key

    @staticmethod
    def init_app(app):
        pass
