from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField, IntegerField, BooleanField, SearchField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

MESSAGE_MAX_CHARS = 1000
ATTACHMENT_MAX_BYTES = 5 * 1024 * 1024  # 5 MB

# Screen 1a: Registrierung
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('HWR E-Mail Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('I am a...', choices=[('student', 'Student'), ('professor', 'Professor')], validators=[DataRequired()])
    submit = SubmitField('Register')


# Screen 1b: Login
class LoginForm(FlaskForm):
    email = StringField('HWR E-Mail Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# Screen 7: Profil Professor
class ProfessorProfileForm(FlaskForm):
    title = StringField('Academic Title', validators=[Optional()])
    research_areas = TextAreaField('Research Areas', validators=[Optional(), Length(max=500)])
    requirements = TextAreaField('Requirements for Students', validators=[Optional(), Length(max=500)])
    max_supervisions = IntegerField('Max. Active Supervisions', validators=[DataRequired()])
    accepting_requests = BooleanField('Currently Accepting Requests')
    submit = SubmitField('Update Profile')

# Screen 7: Profil Student
class StudentProfileForm(FlaskForm):
    matriculation_number = StringField('Matriculation Number', validators=[Optional(), Length(max=20)])
    semester = IntegerField('Current Semester', validators=[Optional()])
    study_focus = TextAreaField('Study Focus / Interests', validators=[Optional(), Length(max=200)])
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
        # A message must carry at least text or a PDF — never both empty.
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
        'Professor/in auswählen',
        coerce=int,
        validators=[DataRequired()]
    )
    proposed_title = StringField(
        'Arbeitstitel der Bachelorarbeit',
        validators=[DataRequired(), Length(max=200)]
    )
    short_description = TextAreaField(
        'Kurzbeschreibung',
        validators=[DataRequired(), Length(max=1000)],
        render_kw={'rows': 5}
    )
    preferred_period = StringField(
        'Gewünschter Betreuungszeitraum',
        validators=[DataRequired(), Length(max=100)]
    )
    submit = SubmitField('Anfrage senden')


# Screen 2: Professor-Feed Suche/Filter
class ProfSearchForm(FlaskForm):
    search = SearchField(validators=[Optional()])
    faculty = SelectField(coerce=str, choices=[], validate_choice=False)
    facheinheit = SelectField(coerce=str, choices=[], validate_choice=False)
    availibilty = SelectField(coerce=str, choices=[('', 'Alle'), ('1', 'Verfügbar'), ('0', 'Nicht verfügbar')], validate_choice=False)
    submit = SubmitField('Suchen')
