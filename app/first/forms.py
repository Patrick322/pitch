from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import Required ,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
        title = StringField('Title', validators=[Required()])
        description = TextAreaField("Choose your pitch",[Required()])
        category = SelectField('Category', choices=[('promotion','Promotion Pitch'), ('project','Project Pitch'), ('pickup','Pick Up lines')], validators=[Required()])
        submit = SubmitField('submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Leave comment',validators=[Required()])
    submit = SubmitField()

class UpvoteForm(FlaskForm):
        submit = SubmitField()


class Downvote(FlaskForm):
        submit = SubmitField()