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

    def verify_password(self, password):
        return check_password_hash(password)

        def __repr__(self)
            return f'{self.username}'



class pitch(db.model):
    '''
    '''
    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.column(db.Integer,db,ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable = False)
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    upvotes = db.relationship('upvote', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relation('Downvotes', backref = 'pitch', lazy = 'dynamic')


    @classmethod
    def get pitches(cls, id)
        pitches = Pitch.query.order_by(pitch_id=id).desc().all()
        return pitches

    def __repr__(self):
        return f'pitch {self.description}'



class Comment(db.Model):
    __tablename__='comments'

    id = db.column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.column(db.Text)


    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"


class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.column(db.Integer,primary_key = True)
    upvote = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_upvotes(self):
        upvote_pitch = Upvote(user = current, pitch)
        upvote_pitch.save_upvotes()


    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote

        @classmethod
        def get_all_upvotes(cls,pitch_id):
            upvotes = Upvote.query.order_by('id').all()
            return upvotes

        def __repr__(self):
            return f'{self.user_id}:{self.pitch_id}'



class Downvote(db.Model):
    __tablename__= 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(Integer,default = 1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_downvotes(cls,id)
        downvote_pitch = Downvote(user = current_user, pitch_id=id)
        downvote_pitch.save_downvotes()


    @classmethod
    def get_downvotes(cls,id):
        downvote_pitch = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls,pitch_id):
        downvote = Downvote.query.ordee_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
        