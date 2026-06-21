import os
import uuid

from flask import (Flask, render_template, redirect, url_for, request, session,
                   flash, jsonify, send_from_directory, abort)
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy import func
from forms import RegistrationForm, LoginForm, ProfessorProfileForm, StudentProfileForm, MessageForm, RequestForm, ProfSearchForm
from db import (db, User, StudentProfile, ProfessorProfile, SupervisionRequest,
                RequestMessage, Attachment)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ein-super-geheimes-passwort'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thesis_match.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# PDF uploads: files live in instance/uploads, only metadata goes in the DB.
app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # hard backstop (10 MB)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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

## CHAT
def _current_user():
    """Return the logged-in User or None."""
    if 'user_id' not in session:
        return None
    return db.session.get(User, session['user_id'])

@app.route('/dashboard')
def dashboard():
    """Role-based dashboard for students and professors."""
    user = _current_user()
    if not user:
        flash('Access denied. Please log in first.', 'danger')
        return redirect(url_for('login'))

    if user.role == 'student':
        requests_q = db.select(SupervisionRequest).where(
            SupervisionRequest.student_id == user.id
        ).order_by(SupervisionRequest.updated_at.desc())
    elif user.role == 'professor':
        requests_q = db.select(SupervisionRequest).where(
            SupervisionRequest.professor_id == user.id
        ).order_by(SupervisionRequest.updated_at.desc())
    else:
        requests_q = db.select(SupervisionRequest).where(False)

    dashboard_requests = db.session.execute(requests_q).scalars().all()

    status_counts = {}
    for sup_request in dashboard_requests:
        status_counts[sup_request.status] = status_counts.get(sup_request.status, 0) + 1

    return render_template(
        'dashboard.html',
        user=user,
        dashboard_requests=dashboard_requests,
        status_counts=status_counts,
    )
@app.route('/requests/new', methods=['GET', 'POST'])
def create_request():
    """Create a new supervision request as a student."""
    user = _current_user()
    if not user:
        flash('Access denied. Please log in first.', 'danger')
        return redirect(url_for('login'))

    if user.role != 'student':
        flash('Nur Studierende können Betreuungsanfragen erstellen.', 'danger')
        return redirect(url_for('dashboard'))

    form = RequestForm()

    professors = db.session.execute(
        db.select(User)
        .join(ProfessorProfile, ProfessorProfile.user_id == User.id)
        .where(
            User.role == 'professor',
            ProfessorProfile.accepting_requests == 1
        )
        .order_by(User.last_name.asc(), User.first_name.asc())
    ).scalars().all()

    form.professor_id.choices = [
        (
            professor.id,
            f"{(professor.professor_profile.title + ' ') if professor.professor_profile and professor.professor_profile.title else ''}{professor.first_name} {professor.last_name}"
        )
        for professor in professors
    ]

    if not professors:
        flash('Aktuell sind keine Professor/innen für Anfragen verfügbar.', 'info')

    if form.validate_on_submit():
        selected_professor = db.session.get(User, form.professor_id.data)

        if not selected_professor or selected_professor.role != 'professor':
            flash('Ausgewählte/r Professor/in wurde nicht gefunden.', 'danger')
            return redirect(url_for('create_request'))

        new_request = SupervisionRequest(
            student_id=user.id,
            professor_id=selected_professor.id,
            proposed_title=form.proposed_title.data.strip(),
            short_description=form.short_description.data.strip(),
            preferred_period=form.preferred_period.data.strip(),
            status='submitted'
        )

        db.session.add(new_request)
        db.session.commit()

        flash('Betreuungsanfrage wurde erfolgreich erstellt.', 'success')
        return redirect(url_for('dashboard'))

    return render_template('request_new.html', form=form, user=user)

@app.route('/chats')
def chats():
    """Übersicht aller Anfragen, an denen der Nutzer beteiligt ist (Chat-Einstieg)."""
    user = _current_user()
    if not user:
        flash('Access denied. Please log in first.', 'danger')
        return redirect(url_for('login'))

    requests_q = db.select(SupervisionRequest).where(
        (SupervisionRequest.student_id == user.id)
        | (SupervisionRequest.professor_id == user.id)
    ).order_by(SupervisionRequest.updated_at.desc())
    conversations = db.session.execute(requests_q).scalars().all()

    return render_template('chats.html', conversations=conversations, user=user)


@app.route('/chats/<int:request_id>', methods=['GET', 'POST'])
def chat(request_id):
    """Nachrichtenverlauf einer Anfrage anzeigen und neue Nachricht senden."""
    user = _current_user()
    if not user:
        flash('Access denied. Please log in first.', 'danger')
        return redirect(url_for('login'))

    sup_request = db.session.get(SupervisionRequest, request_id)
    if not sup_request:
        flash('Anfrage nicht gefunden.', 'danger')
        return redirect(url_for('chats'))

    # Nur Student oder Professor dieser Anfrage dürfen den Verlauf sehen.
    if user.id not in (sup_request.student_id, sup_request.professor_id):
        flash('Kein Zugriff auf diesen Nachrichtenverlauf.', 'danger')
        return redirect(url_for('chats'))

    form = MessageForm()
    if form.validate_on_submit():
        message = RequestMessage(
            request_id=sup_request.id,
            sender_id=user.id,
            message_text=(form.message_text.data or '').strip(),
        )
        db.session.add(message)
        db.session.flush()  # assign message.id before linking the attachment

        upload = form.attachment.data
        if upload:
            stored_name = f"{uuid.uuid4().hex}.pdf"
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], stored_name)
            upload.save(full_path)
            db.session.add(Attachment(
                request_id=sup_request.id,
                message_id=message.id,
                uploaded_by=user.id,
                attachment_context='message',
                original_filename=secure_filename(upload.filename) or 'datei.pdf',
                storage_path=stored_name,
                mime_type='application/pdf',
                file_size=os.path.getsize(full_path),
            ))

        db.session.commit()
        return redirect(url_for('chat', request_id=sup_request.id))

    return render_template('chat.html', sup_request=sup_request, form=form, user=user)


@app.route('/attachments/<int:attachment_id>')
def download_attachment(attachment_id):
    """PDF-Anhang herunterladen — nur für Beteiligte der zugehörigen Anfrage."""
    user = _current_user()
    if not user:
        flash('Access denied. Please log in first.', 'danger')
        return redirect(url_for('login'))

    attachment = db.session.get(Attachment, attachment_id)
    if not attachment:
        abort(404)

    sup_request = db.session.get(SupervisionRequest, attachment.request_id)
    if not sup_request or user.id not in (sup_request.student_id, sup_request.professor_id):
        abort(403)

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        attachment.storage_path,
        as_attachment=True,
        download_name=attachment.original_filename,
    )


## API ANFRAGE BESTE PROFS TODO: MEISTGEFRAGTE THEMEB

@app.route('/api/top-supervisors')
def api_top_supervisors():
    """JSON-Rangliste der meistgefragten Professoren nach Anzahl der Anfragen."""
    limit = request.args.get('limit', default=10, type=int)
    limit = max(1, min(limit, 100))

    rows = db.session.execute(
        db.select(
            User.id,
            User.first_name,
            User.last_name,
            ProfessorProfile.title,
            ProfessorProfile.research_areas,
            func.count(SupervisionRequest.id).label('request_count'),
        )
        .join(ProfessorProfile, ProfessorProfile.user_id == User.id)
        .outerjoin(SupervisionRequest, SupervisionRequest.professor_id == User.id)
        .where(User.role == 'professor')
        .group_by(User.id)
        .order_by(func.count(SupervisionRequest.id).desc(), User.last_name.asc())
        .limit(limit)
    ).all()

    ranking = [
        {
            'rank': index,
            'professor_id': row.id,
            'name': f"{row.title + ' ' if row.title else ''}{row.first_name} {row.last_name}",
            'research_areas': row.research_areas,
            'request_count': row.request_count,
        }
        for index, row in enumerate(rows, start=1)
    ]

    return jsonify({'count': len(ranking), 'ranking': ranking})

@app.route('/feed/', methods=['GET', 'POST'])
def feed():
    form = forms.ProfSearchForm()
    faculties = db.session.execute(db.select(Faculty)).scalars().all()
    form.faculty.choices = [('', 'Alle Fachbereiche')] + [(str(f.id),f.name) for f in faculties]

    facheinheiten = db.session.execute(db.select(Facheinheit)).scalars().all()
    form.facheinheit.choices = [('', 'Alle Facheinheiten')] + [(str(e.id),e.name) for e in facheinheiten]

    professors = db.session.execute(db.select(ProfessorProfile)).scalars().all()

    if request.method == 'POST' and form.validate():
        suchbegriff = (form.search.data or "").lower()
        faculty = form.faculty.data
        facheinheit = form.facheinheit.data
        availabilty = form.availibilty.data

        filtered = []
        for prof in professors:
            match_search = (
                suchbegriff == "" or
                suchbegriff in f"{prof.user.first_name} {prof.user.last_name}".lower() or
                (prof.research_areas and suchbegriff in prof.research_areas.lower())
            )

            match_faculty = (not faculty or str(prof.facheinheit.faculty_id)== str(faculty))
            match_facheinheit = (not facheinheit or str(prof.facheinheit_id)== str(facheinheit))
            match_availibilty = (not availabilty or str(prof.accepting_requests) == str(availabilty))

            if match_search and match_faculty and match_availibilty and match_facheinheit: 
                filtered.append(prof)
        professors = filtered      
                       
    
    return render_template('feed.html', form=form, professoren=professors)
    

@app.route('/profile/<int:id>', methods=['GET', 'POST'])
def profile(id):
    prof = db.session.get(ProfessorProfile, id)
    return render_template('profile-detail.html', prof=prof)