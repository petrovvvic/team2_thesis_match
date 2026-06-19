from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thesis_match.sqlite' 

db = SQLAlchemy()
db.init_app(app)

class Faculty(db.Model):
    __tablename__ = 'faculties'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    professors = db.relationship('ProfessorProfile', back_populates='faculty')
    
    students = db.relationship('StudentProfile', back_populates='faculty')

class DegreeProgram(db.Model):
    __tablename__ = 'degree_programs'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(20), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    account_status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
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
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=True)
    title = db.Column(db.String(50), nullable=True)
    research_areas = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.Text, nullable=True)
    max_supervisions = db.Column(db.Integer, default=0)
    accepting_requests = db.Column(db.Integer, default=1)

    user = db.relationship( 'User', back_populates='professor_profile')
    faculty = db.relationship('Faculty', back_populates='professors')

# ------------------------------------------------------------------
# Supervision requests + chat (owner: Andrei – chat feature)
#
# NOTE: This is a MINIMAL version of supervision_requests, added only so the
# chat (request_messages) has something to attach to. The full request flow
# (Screen 4 Anfrage-Flow, Screen 5 Meine Anfragen, Screen 6 Dashboard) is a
# separate task; columns here follow schema.sql so they stay compatible.
# ------------------------------------------------------------------

class SupervisionRequest(db.Model):
    __tablename__ = 'supervision_requests'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    proposed_title = db.Column(db.String(200), nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    preferred_period = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='submitted')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
    # 'initial' = attached to the request itself (Anfrage-Flow);
    # 'message' = attached to a chat message (chat feature).
    attachment_context = db.Column(db.String(10), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    storage_path = db.Column(db.String(255), nullable=False, unique=True)
    mime_type = db.Column(db.String(50), nullable=False, default='application/pdf')
    file_size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    uploader = db.relationship('User', foreign_keys=[uploaded_by])

# ------------------------------------------------------------------
# Thesis topics + status history (added to complete the data model;
# owned by the request-flow / topic-management tasks).
# ------------------------------------------------------------------

class ThesisTopic(db.Model):
    __tablename__ = 'thesis_topics'
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=True)
    topic_area = db.Column(db.String(100), nullable=False)
    # allowed values: 'open', 'archived'
    status = db.Column(db.String(20), nullable=False, default='open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    professor = db.relationship('User', foreign_keys=[professor_id])

class RequestStatusHistory(db.Model):
    __tablename__ = 'request_status_history'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('supervision_requests.id'), nullable=False)
    # status values: 'submitted', 'in_review', 'needs_info', 'accepted', 'rejected', 'withdrawn'
    old_status = db.Column(db.String(20), nullable=True)
    new_status = db.Column(db.String(20), nullable=False)
    changed_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    request = db.relationship('SupervisionRequest', foreign_keys=[request_id])
    editor = db.relationship('User', foreign_keys=[changed_by])

    