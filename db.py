from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Faculty(db.Model):
    __tablename__ = 'faculties'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
    student_profile = db.relationship('StudentProfile', backref='user', uselist=False)
    professor_profile = db.relationship('ProfessorProfile', backref='user', uselist=False)

class StudentProfile(db.Model):
    __tablename__ = 'student_profiles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    matriculation_number = db.Column(db.String(20), unique=True, nullable=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=True)
    degree_program_id = db.Column(db.Integer, db.ForeignKey('degree_programs.id'), nullable=True)
    semester = db.Column(db.Integer, nullable=True)
    study_focus = db.Column(db.String(200), nullable=True)

class ProfessorProfile(db.Model):
    __tablename__ = 'professor_profiles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=True)
    title = db.Column(db.String(50), nullable=True)
    research_areas = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.Text, nullable=True)
    max_supervisions = db.Column(db.Integer, default=0)
    accepting_requests = db.Column(db.Integer, default=1)