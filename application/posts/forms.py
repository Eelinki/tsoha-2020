from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import Length, InputRequired

class PostForm(FlaskForm):
    message = TextAreaField("Message", [InputRequired(), Length(max=400)])

    class Meta:
        csrf = False