from flask import Flask
from Infrastructure.Context.SQLContext import SQLContext

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    return app


class Config:
    SECRET_KEY = 'dES344FByb2R1Y3Rvcw=='
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 3600, 'pool_timeout': 100, 'pool_pre_ping': True}
    PORT = 8080
    
class LocalConfig(Config):
    
    CONTEXT_FACTORY = SQLContext
    DEBUG = True
    VERIFY_SSL = False
    WEAPI_CHUCKNORRIS = 'https://api.chucknorris.io/jokes'
    WEAPI_JOKE ='https://icanhazdadjoke.com/'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/configurador_chistes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    
    CONTEXT_FACTORY = SQLContext
    DEBUG = False
    VERIFY_SSL = False
    WEAPI_CHUCKNORRIS = 'https://api.chucknorris.io/jokes'
    WEAPI_JOKE ='https://icanhazdadjoke.com/'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/configurador_chistes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class QualityConfig(Config):
    CONTEXT_FACTORY = SQLContext
    DEBUG = False
    VERIFY_SSL = False
    WEAPI_CHUCKNORRIS = 'https://api.chucknorris.io/jokes'
    WEAPI_JOKE ='https://icanhazdadjoke.com/'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/configurador_chistes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    CONTEXT_FACTORY = SQLContext
    DEBUG = False
    VERIFY_SSL = False
    WEAPI_CHUCKNORRIS = 'https://api.chucknorris.io/jokes'
    WEAPI_JOKE ='https://icanhazdadjoke.com/'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/configurador_chistes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    loc=LocalConfig,
    dev=DevelopmentConfig,
    quality=QualityConfig,
    prod=ProductionConfig
)

ENVIRONMENT_NAME = 'loc'
