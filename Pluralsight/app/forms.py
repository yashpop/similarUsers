from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserEntry(FlaskForm):
    user_handle = IntegerField('User Id',validators=[DataRequired()])
    submit = SubmitField('Get similar Users')
