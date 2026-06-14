from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, SelectField, SearchField
from wtforms.validators import InputRequired, Length

class ProfSearchForm(FlaskForm):
    search = SearchField(validators=[Optional()])
    submit = SubmitField('Suchen')

