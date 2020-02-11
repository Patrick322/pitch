from . import db
from sglalchemy.sql import func
from . import login_Manager
from flask_login import UserMixin, current_user
from werzeug.security import generate_password_hash,check_password_hash



@login_manager.user_loader
def load_user(user_id)