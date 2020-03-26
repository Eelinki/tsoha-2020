from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, InputRequired

class UserForm(FlaskForm):
    username = StringField("Username", [InputRequired(), Length(max=16)])
    password = PasswordField("Password", [InputRequired(), Length(min=8)])

    class Meta:
        csrf = False