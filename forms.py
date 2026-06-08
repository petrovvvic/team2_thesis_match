from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


# Screen 1a: Registrierung
class RegistrationForm(FlaskForm):
    # DataRequired stellt sicher, dass das Feld nicht leer abgesendet werden kann
    name = StringField('Vollständiger Name', validators=[DataRequired(), Length(min=2, max=50)])

    # Email-Validator prüft, ob ein @-Zeichen etc. vorhanden ist
    email = StringField('HWR E-Mail Adresse', validators=[DataRequired(), Email()])

    password = PasswordField('Passwort', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Passwort bestätigen', validators=[DataRequired(), EqualTo('password')])

    # Hier wählen die Nutzer ihre Rolle (Two-Sided Platform!)
    role = SelectField('Ich bin...', choices=[('student', 'Studierende/r'), ('professor', 'Professor/in')],
                       validators=[DataRequired()])

    submit = SubmitField('Registrieren')


# Screen 1b: Login
class LoginForm(FlaskForm):
    email = StringField('HWR E-Mail Adresse', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Einloggen')


# Screen 7: Profil bearbeiten (Besonders wichtig für Professoren)
class ProfileUpdateForm(FlaskForm):
    # Name und E-Mail können hier optional auch geändert werden
    name = StringField('Vollständiger Name', validators=[DataRequired()])

    # Diese Felder sind z.B. nur für Professoren relevant
    themenfelder = TextAreaField('Meine Themenfelder', validators=[Length(max=500)])
    anforderungen = TextAreaField('Anforderungen an Studierende', validators=[Length(max=500)])

    # Kapazitäten (z.B. wie viele Plätze noch frei sind)
    freie_plaetze = SelectField('Verfügbare Betreuungsplätze',
                                choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3+', '3 oder mehr')])

    submit = SubmitField('Profil aktualisieren')