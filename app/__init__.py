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

    Args:
        config_name : name of the configeration to be used
    '''

    # Initializing application
    app = Flask(__name__)

simple.init__app(name)

# creating the appconfigeration
app.config.from_object(config_options[config_name])


#Initializing flask extensions
bootstrap.init__app()
db.init_app(app)
login_Manager.init__app(app)

# Registering the main Blueprint
from.main import main as main_blueprint
app.register_blueprint(main_blueprint)

# registering the auth blueprint
from.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# setting config when using API
#from.request import configure_request
#config_request(app)

    return app