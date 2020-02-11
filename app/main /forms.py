from flask_wft import Flaskform
from wtforms import StringFields,PasswordField,Submitted,BooleanField,TextAreaField,RadioField
from wtforms.validators import Required ,Email,EqualTo
from Wtforms import ValidationError



class PitchForm(FlaskForm):
        title = StringField('Title', Validators=[Required()])
        description = TextAreaField("Choose your pitch",[Required()])
        category = RadioField('Label', choices=[ ('promotionpitch','promopitch'), ('interviewpitch','interviewpitch'),('pickuppitch','pickuplines')]validator=[Required()])
        submit = submitField('submit')

class CommentForm(Flaskform):
    description = TextAreaField('Leave comment',validators=[Required()])
    submit = submitField()

class UpvoteForm(FlaskForm);
        submit = SubmitField()


class Downvote(FlaskForm):
        submit = SubmitField()