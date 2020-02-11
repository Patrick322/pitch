from flask import flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemede import simpleMDE



# instances of flask extentions
# instances of Flask_loginManager
login_Manager = LoginManager()
login_Manager.session_protection = 'strong'
login_Manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
simple = simpleMDE

def create_app(config_name)
    '''
    Function that takes configeration setting key as an argument

    Args