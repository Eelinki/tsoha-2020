from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, InputRequired

class GroupForm(FlaskForm):
    groupname = StringField("Group name", [InputRequired(), Length(max=30)])

    class Meta:
        csrf = False