from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

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
        'Nachricht',
        validators=[DataRequired(), Length(min=1, max=2000)],
    )
    submit = SubmitField('Senden')