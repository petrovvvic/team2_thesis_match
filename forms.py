from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, SelectField, SearchField
from wtforms.validators import Optional

class ProfSearchForm(FlaskForm):
    search = SearchField(validators=[Optional()])
    submit = SubmitField('Suchen')

