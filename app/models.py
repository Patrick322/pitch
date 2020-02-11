from . import db
from sglalchemy.sql import func
from . import login_Manager
from flask_login import UserMixin, current_user
from werzeug.security import generate_password_hash,check_password_hash



@login_manager.user_loader
def load_user(user_id)
    return user.query.get(init(user_id))



class User(UserMixin,db.model)

    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.column(db.String(unique = True,index = True))
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref= 'user', lazy='dynamic')
    upvotes = db.relationship('upvote', backref = 'user', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')


    @property
    def pasword(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)