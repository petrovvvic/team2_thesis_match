from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, ProfessorProfileForm, StudentProfileForm
from db import db, User, StudentProfile, ProfessorProfile

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ein-super-geheimes-passwort'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thesis_match.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(email=form.email.data)).scalar_one_or_none()
        if user and check_password_hash(user.password_hash, form.password.data):
            session['user_id'] = user.id
            session['user_role'] = user.role
            flash('Erfolgreich eingeloggt!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login fehlgeschlagen. Bitte überprüfe E-Mail und Passwort.', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password_hash=hashed_pw,
            role=form.role.data,
            account_status='active'
        )
        db.session.add(new_user)
        db.session.flush()

        if new_user.role == 'student':
            new_profile = StudentProfile(user_id=new_user.id)
            db.session.add(new_profile)
        elif new_user.role == 'professor':
            new_profile = ProfessorProfile(user_id=new_user.id)
            db.session.add(new_profile)

        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash('Du wurdest erfolgreich ausgeloggt.', 'info')
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash('Access denied. Please log in first.', 'danger')
        return redirect(url_for('login'))

    user = db.session.execute(db.select(User).filter_by(id=session['user_id'])).scalar_one_or_none()
    if not user:
        session.clear()
        return redirect(url_for('login'))

    if user.role == 'professor':
        form = ProfessorProfileForm()
        profile_data = user.professor_profile
        if form.validate_on_submit():
            profile_data.title = form.title.data
            profile_data.research_areas = form.research_areas.data
            profile_data.requirements = form.requirements.data
            profile_data.max_supervisions = form.max_supervisions.data
            profile_data.accepting_requests = form.accepting_requests.data
            db.session.commit()
            flash('Professor profile successfully updated!', 'success')
            return redirect(url_for('profile'))
        elif request.method == 'GET':
            form.title.data = profile_data.title
            form.research_areas.data = profile_data.research_areas
            form.requirements.data = profile_data.requirements
            form.max_supervisions.data = profile_data.max_supervisions
            form.accepting_requests.data = profile_data.accepting_requests

    elif user.role == 'student':
        form = StudentProfileForm()
        profile_data = user.student_profile
        if form.validate_on_submit():
            profile_data.matriculation_number = form.matriculation_number.data
            profile_data.semester = form.semester.data
            profile_data.study_focus = form.study_focus.data
            db.session.commit()
            flash('Student profile successfully updated!', 'success')
            return redirect(url_for('profile'))
        elif request.method == 'GET':
            form.matriculation_number.data = profile_data.matriculation_number
            form.semester.data = profile_data.semester
            form.study_focus.data = profile_data.study_focus

    return render_template('profile.html', form=form, user=user)