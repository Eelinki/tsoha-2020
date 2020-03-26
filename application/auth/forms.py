from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, InputRequired

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(max=16)])
    username = StringField("Username", [InputRequired(), Length(max=16)])
    password = PasswordField("Password", [InputRequired(), Length(min=8)])

    class Meta:
        csrf = False