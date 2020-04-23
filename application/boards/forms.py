from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, InputRequired

class BoardForm(FlaskForm):
    boardname = StringField("Board name", [InputRequired(), Length(max=64)])

    class Meta:
        csrf = False

class ThreadForm(FlaskForm):
    title = StringField("Title", [InputRequired(), Length(max=64)])

    class Meta:
        csrf = False