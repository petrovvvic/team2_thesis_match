import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField, IntegerField, BooleanField, SearchField
from wtforms.validators import (DataRequired, Email, Length, EqualTo, Optional, InputRequired, NumberRange, ValidationError)

MESSAGE_MAX_CHARS = 1000
ATTACHMENT_MAX_BYTES = 5 * 1024 * 1024  # 5 MB

def password_complexity(form, field):
    password = field.data or ''
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Das Passwort muss mindestens einen Großbuchstaben enthalten.')
    if not re.search(r'[a-z]', password):
        raise ValidationError('Das Passwort muss mindestens einen Kleinbuchstaben enthalten.')
    if not re.search(r'\d', password):
        raise ValidationError('Das Passwort muss mindestens eine Zahl enthalten.')
    if not re.search(r'[^A-Za-z0-9]', password):
        raise ValidationError('Das Passwort muss mindestens ein Sonderzeichen enthalten.')

# Screen 1a: Registrierung
class RegistrationForm(FlaskForm):
    first_name = StringField('Vorname*', validators=[DataRequired(message='Dieses Feld ist erforderlich.'), Length(min=2, max=50, message='Muss zwischen 2 und 50 Zeichen lang sein.')])
    last_name = StringField('Nachname*', validators=[DataRequired(message='Dieses Feld ist erforderlich.'), Length(min=2, max=50, message='Muss zwischen 2 und 50 Zeichen lang sein.')])
    email = StringField('HWR E-Mail Addresse*', validators=[DataRequired(message='Dieses Feld ist erforderlich.'), Email(message='Bitte eine gültige E-Mail-Adresse eingeben.')])
    password = PasswordField('Passwort*', validators=[
        DataRequired(message='Dieses Feld ist erforderlich.'),
        Length(min=8, max=24, message='Das Passwort muss 8 bis 24 Zeichen lang sein.'),
        password_complexity,
        ],
        description = 'Mindestens 8 Zeichen, mit Groß- und Kleinbuchstaben, einer Zahl und einem Sonderzeichen.'
    )
    confirm_password = PasswordField('Passwort Bestätigen*', validators=[DataRequired(message='Dieses Feld ist erforderlich.'), EqualTo('password', message='Die Passwörter müssen übereinstimmen.')])
    role = SelectField('An der HWR bin ich...*', choices=[('student', 'Student'), ('professor', 'Professor')], validators=[DataRequired(message='Bitte eine Rolle auswählen.')])
    submit = SubmitField('Register')


# Screen 1b: Login
class LoginForm(FlaskForm):
    email = StringField('HWR E-Mail Addresse*', validators=[DataRequired(message='Dieses Feld ist erforderlich.'), Email(message='Bitte eine gültige E-Mail-Adresse eingeben.')])
    password = PasswordField('Passwort*', validators=[DataRequired(message='Dieses Feld ist erforderlich.')])
    submit = SubmitField('Login')


# Screen 7: Profil Professor
class ProfessorProfileForm(FlaskForm):
    facheinheit_id = SelectField('Facheinheit', coerce=int, validators=[Optional()])
    title = StringField('Akademische(r) Titel', validators=[Optional()])
    research_areas = TextAreaField('Forschungsbereich(e)', validators=[Optional(), Length(max=500, message='Maximal 500 Zeichen erlaubt.')])
    requirements = TextAreaField('Voraussetzungen für Studierende', validators=[Optional(), Length(max=500, message='Maximal 500 Zeichen erlaubt.')])
    accepting_requests = BooleanField('Anfragen erhalten?')
    submit = SubmitField('Update Profile')

# Screen 7: Profil Student
class StudentProfileForm(FlaskForm):
    matriculation_number = StringField('Matrikelnummer', validators=[Optional(), Length(max=20, message='Maximal 20 Zeichen erlaubt.')])
    degree_program_id = SelectField('Studiengang', coerce=int, validators=[Optional()])
    semester = IntegerField('Aktuelles Semester',validators=[Optional(),NumberRange(min=1, message="Das Semester muss mindestens 1 sein.")],render_kw={'min': 1})
    study_focus = TextAreaField('Studienschwerpunkt / Interessen', validators=[Optional(), Length(max=200, message='Maximal 200 Zeichen erlaubt.')])
    submit = SubmitField('Update Profile')


# Chat: Nachricht im Anfrage-Verlauf senden
class MessageForm(FlaskForm):
    message_text = TextAreaField(
        f'Nachricht (max. {MESSAGE_MAX_CHARS} Zeichen)',
        validators=[
            Optional(),
            Length(max=MESSAGE_MAX_CHARS,
                   message=f'Maximal {MESSAGE_MAX_CHARS} Zeichen erlaubt.'),
        ],
        render_kw={'maxlength': MESSAGE_MAX_CHARS, 'rows': 3},
    )
    attachment = FileField(
        'PDF anhängen (optional, max. 5 MB)',
        validators=[
            Optional(),
            FileAllowed(['pdf'], 'Nur PDF-Dateien sind erlaubt.'),
            FileSize(max_size=ATTACHMENT_MAX_BYTES, message='Datei zu groß (max. 5 MB).'),
        ],
    )
    submit = SubmitField('Senden')

    def validate(self, extra_validators=None):
        # Entweder Text oder PDF, nicht leer.
        if not super().validate(extra_validators):
            return False
        has_text = bool(self.message_text.data and self.message_text.data.strip())
        has_file = bool(self.attachment.data)
        if not has_text and not has_file:
            self.message_text.errors.append(
                'Bitte eine Nachricht schreiben oder eine PDF anhängen.'
            )
            return False
        return True

# Screen 4: Neue Betreuungsanfrage erstellen
class RequestForm(FlaskForm):
    professor_id = SelectField(
        'Professor/in auswählen*',
        coerce=int,
        validators=[DataRequired(message='Bitte eine:n Professor:in auswählen.')]
    )

    examiner_role = SelectField('Anfrage als*', choices=[('erst', 'Erstprüfer/in'), ('zweit', 'Zweitprüfer/in')], validators=[DataRequired(message='Bitte eine Prüfer-Rolle auswählen.')])

    proposed_title = StringField(
        'Arbeitstitel der Bachelorarbeit*',
        validators=[DataRequired(message='Dieses Feld ist erforderlich.'), Length(max=200, message='Maximal 200 Zeichen erlaubt.')]
    )
    short_description = TextAreaField(
        'Kurzbeschreibung*',
        validators=[DataRequired(message='Dieses Feld ist erforderlich.'), Length(max=1000, message='Maximal 1000 Zeichen erlaubt.')],
        render_kw={'rows': 5}
    )
    preferred_period = StringField(
        'Gewünschter Betreuungszeitraum*',
        validators=[DataRequired(message='Dieses Feld ist erforderlich.'), Length(max=100, message='Maximal 100 Zeichen erlaubt.')]
    )
    submit = SubmitField('Anfrage senden')


class RequestEditForm(FlaskForm):
    examiner_role = SelectField(
        'Anfrage als*',
        choices=[
            ('erst', 'Erstprüfer/in'),
            ('zweit', 'Zweitprüfer/in')
        ],
        validators=[DataRequired(message='Bitte eine Prüfer-Rolle auswählen.')]
    )

    proposed_title = StringField(
        'Arbeitstitel der Bachelorarbeit*',
        validators=[
            DataRequired(message='Dieses Feld ist erforderlich.'),
            Length(max=200, message='Maximal 200 Zeichen erlaubt.')
        ]
    )

    short_description = TextAreaField(
        'Kurzbeschreibung*',
        validators=[
            DataRequired(message='Dieses Feld ist erforderlich.'),
            Length(max=1000, message='Maximal 1000 Zeichen erlaubt.')
        ],
        render_kw={'rows': 5}
    )

    preferred_period = StringField(
        'Gewünschter Betreuungszeitraum*',
        validators=[
            DataRequired(message='Dieses Feld ist erforderlich.'),
            Length(max=100, message='Maximal 100 Zeichen erlaubt.')
        ]
    )

    submit = SubmitField('Änderungen speichern')
class RequestWithdrawForm(FlaskForm):
    submit = SubmitField('Anfrage zurückziehen')


class RequestStatusForm(FlaskForm):
    accept = SubmitField('Annehmen')
    reject = SubmitField('Ablehnen')

# Screen 2: Professor-Feed Suche/Filter
class ProfSearchForm(FlaskForm):
    search = SearchField(validators=[Optional()])
    facheinheit = SelectField(coerce=str, choices=[], validate_choice=False)
    availibilty = SelectField(coerce=str, choices=[('', 'Alle'), ('1', 'Verfügbar'), ('0', 'Nicht verfügbar')], validate_choice=False)
    submit = SubmitField('Suchen')
