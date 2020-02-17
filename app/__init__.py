from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE



# instances of flask extentions
# instances of Flask_loginManagern ft michael jackson handhold my 
simple = SimpleMDE()
login_Manager = LoginManager()
login_Manager.session_protection = 'strong'
login_Manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    '''
    Function that takes configeration setting key as an argument

    Args:
        config_name : name of the configeration to be used
    '''

    # Initializing application
    app = Flask(__name__)

    

    # creating the appconfigeration
    app.config.from_object(config_options[config_name])


    #Initializing flask extensions
    
    db.init_app(app)
    simple.init_app(app)
    login_Manager.init_app(app)
    bootstrap.init_app(app)

    # Registering the main Blueprint
    from .first import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app