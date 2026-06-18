from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField, SearchField
from wtforms.validators import Optional

class ProfSearchForm(FlaskForm):
    search = SearchField(validators=[Optional()])

    faculty = SelectField(coerce=str, choices=[], validate_choice=False)

    availibilty = SelectField(coerce=str,choices=[('', 'Alle'), ('1', 'Verfügbar'), ('0', 'Nicht verfügbar')], validate_choice=False)
    
    submit = SubmitField('Suchen')

