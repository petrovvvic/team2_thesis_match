from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


db = SQLAlchemy()

class Faculty(db.Model):
    __tablename__ = 'faculties'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    facheinheiten = db.relationship('Facheinheit', back_populates='faculty')
    students = db.relationship('StudentProfile', back_populates='faculty')
    degree_programs = db.relationship('DegreeProgram', back_populates='faculty') 

class Facheinheit(db.Model):
    __tablename__ = 'facheinheiten'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    faculty = db.relationship('Faculty', back_populates='facheinheiten')
    professors = db.relationship('ProfessorProfile', back_populates='facheinheit')
    thesis_topics = db.relationship('ThesisTopic', back_populates='facheinheit')
    

class DegreeProgram(db.Model):
    __tablename__ = 'degree_programs'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(20), nullable=False)

    faculty = db.relationship('Faculty', back_populates='degree_programs')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    account_status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    student_profile = db.relationship('StudentProfile', back_populates='user', uselist=False)
    professor_profile = db.relationship('ProfessorProfile', back_populates='user', uselist=False)

class StudentProfile(db.Model):
    __tablename__ = 'student_profiles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    matriculation_number = db.Column(db.String(20), unique=True, nullable=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=True)
    degree_program_id = db.Column(db.Integer, db.ForeignKey('degree_programs.id'), nullable=True)
    semester = db.Column(db.Integer, nullable=True)
    study_focus = db.Column(db.String(200), nullable=True)

    user = db.relationship('User', back_populates='student_profile')
    faculty = db.relationship('Faculty', back_populates='students')

class ProfessorProfile(db.Model):
    __tablename__ = 'professor_profiles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    facheinheit_id = db.Column(db.Integer, db.ForeignKey('facheinheiten.id'), nullable=True)
    title = db.Column(db.String(50), nullable=True)
    research_areas = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.Text, nullable=True)
    max_supervisions = db.Column(db.Integer, default=0)
    accepting_requests = db.Column(db.Integer, default=1)

    user = db.relationship('User', back_populates='professor_profile')
    facheinheit = db.relationship('Facheinheit', back_populates='professors')

class SupervisionRequest(db.Model):
    __tablename__ = 'supervision_requests'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    proposed_title = db.Column(db.String(200), nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    preferred_period = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='submitted')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    student = db.relationship('User', foreign_keys=[student_id])
    professor = db.relationship('User', foreign_keys=[professor_id])
    messages = db.relationship(
        'RequestMessage',
        backref='request',
        order_by='RequestMessage.created_at',
        cascade='all, delete-orphan',
    )

class RequestMessage(db.Model):
    __tablename__ = 'request_messages'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('supervision_requests.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    sender = db.relationship('User', foreign_keys=[sender_id])
    attachments = db.relationship(
        'Attachment',
        backref='message',
        cascade='all, delete-orphan',
    )

class Attachment(db.Model):
    __tablename__ = 'attachments'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('supervision_requests.id'), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('request_messages.id'), nullable=True)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    attachment_context = db.Column(db.String(10), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    storage_path = db.Column(db.String(255), nullable=False, unique=True)
    mime_type = db.Column(db.String(50), nullable=False, default='application/pdf')
    file_size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    uploader = db.relationship('User', foreign_keys=[uploaded_by])

# Themen für Thesissschreiben
class ThesisTopic(db.Model):
    __tablename__ = 'thesis_topics'
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    facheinheit_id = db.Column(db.Integer, db.ForeignKey('facheinheiten.id'), nullable=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=True)
    topic_area = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='open')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    professor = db.relationship('User', foreign_keys=[professor_id])
    facheinheit = db.relationship('Facheinheit', back_populates='thesis_topics')
  

class RequestStatusHistory(db.Model):
    __tablename__ = 'request_status_history'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('supervision_requests.id'), nullable=False)
    old_status = db.Column(db.String(20), nullable=True)
    new_status = db.Column(db.String(20), nullable=False)
    changed_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    request = db.relationship('SupervisionRequest', foreign_keys=[request_id])
    editor = db.relationship('User', foreign_keys=[changed_by])

def insert_sample():

        db.session.execute(db.delete(Facheinheit))
        db.session.execute(db.delete(Faculty))
        db.session.commit():
        
        fb1 =Faculty(code='FB1', name='Wirtschaftswissenschaften')
        db.session.add(fb1)
        db.session.commit()

    facheinheiten = [
        Facheinheit(faculty_id=fb1.id, name='Unternehmensführung / Personal / Organisation'),
        Facheinheit(faculty_id=fb1.id, name='Marketing'),
        Facheinheit(faculty_id=fb1.id, name='Finanzwirtschaft'),
        Facheinheit(faculty_id=fb1.id, name='Steuern'),
        Facheinheit(faculty_id=fb1.id, name='Rechnungswesen'),
        Facheinheit(faculty_id=fb1.id, name='Supply Chain und Operations Management'),
        Facheinheit(faculty_id=fb1.id, name='Quantitative Methoden'),
        Facheinheit(faculty_id=fb1.id, name='Wirtschaftsinformatik'),
        Facheinheit(faculty_id=fb1.id, name='Volkswirtschaftslehre'),
        Facheinheit(faculty_id=fb1.id, name='Gesellschaftswissenschaften'),
        Facheinheit(faculty_id=fb1.id, name='Wirtschaftsrecht'),
    ]
    db.session.add_all(facheinheiten)
    db.session.commit()
    

