from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, ProfileUpdateForm
from db import db, User

app = Flask(__name__)
# Ein Secret Key ist zwingend nötig, damit WTForms funktioniert (Sicherheits-Feature gegen CSRF-Attacken)
app.config['SECRET_KEY'] = 'ein-super-geheimes-passwort'

# NEU: Konfiguration für die SQLite-Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thesis_match.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Datenbank und Bootstrap mit der App verknüpfen
db.init_app(app)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

# Startseite leitet direkt zum Login weiter
@app.route('/')
def index():
    return redirect(url_for('login'))

# Screen 1b: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # 1. Nutzer anhand der E-Mail in der Datenbank suchen
        # SQLAlchemy Befehl, der absolut sicher gegen SQL-Injections ist
        user = db.session.execute(db.select(User).filter_by(email=form.email.data)).scalar_one_or_none()

        # 2. Prüfen: Existiert der Nutzer? UND Stimmt der Passwort-Hash überein?
        if user and check_password_hash(user.password_hash, form.password.data):

            # 3. Session starten (Der "Ausweis" für den Browser)
            session['user_id'] = user.id
            session['user_role'] = user.role

            flash('Erfolgreich eingeloggt!', 'success')  # Grüne Erfolgsmeldung
            return redirect(url_for('profile'))

        else:
            # Security: Keine genauen Infos geben, woran es lag!
            flash('Login fehlgeschlagen. Bitte überprüfe E-Mail und Passwort.', 'danger')

    return render_template('login.html', form=form)

# Screen 1a: Registrierung
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # 1. Passwort verschlüsseln (Security Best Practice!)
        hashed_pw = generate_password_hash(form.password.data)

        # 2. Einen neuen User aus den Formulareingaben erstellen
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password_hash=hashed_pw,
            role=form.role.data
        )

        # 3. In die Datenbank einfügen und speichern
        db.session.add(new_user)
        db.session.commit()

        print(f"Erfolgreich registriert: {new_user.email}")  # Kleiner Print für dein Terminal

        # 4. Nach erfolgreicher Registrierung zum Login schicken
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    # Session komplett leeren
    session.clear()
    flash('Du wurdest erfolgreich ausgeloggt.', 'info')
    return redirect(url_for('login'))

# Screen 7: Profil
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # --- TRICK 1: HÄRTUNG GEGEN UNBEFUGTEN ZUGRIFF ---
    # Wenn der Prof versucht, die Seite ohne Login aufzurufen: Sofort abweisen!
    if 'user_id' not in session:
        flash('Zugriff verweigert. Bitte logge dich zuerst ein.', 'danger')
        return redirect(url_for('login'))

    # Den aktuell eingeloggten Nutzer sicher aus der Datenbank abrufen
    # Parameterized Query über das ORM verhindert jegliche SQL-Injection
    user = db.session.execute(db.select(User).filter_by(id=session['user_id'])).scalar_one_or_none()

    # Sicherheitsnetz: Falls der Nutzer in der Zwischenzeit gelöscht wurde
    if not user:
        session.clear()
        return redirect(url_for('login'))

    form = ProfileUpdateForm()

    # --- 2. REGISTRIERUNG VON ÄNDERUNGEN (POST-REQUEST) ---
    if form.validate_on_submit():
        user.name = form.name.data

        # Wichtig für das Two-Sided-Konzept: Nur Profs dürfen diese Felder überschreiben
        if user.role == 'professor':
            user.themenfelder = form.themenfelder.data
            user.anforderungen = form.anforderungen.data
            user.freie_plaetze = form.freie_plaetze.data

        db.session.commit()  # Sicher in der SQLite-Datenbank speichern
        flash('Dein Profil wurde erfolgreich aktualisiert!', 'success')
        return redirect(url_for('profile'))

    # --- TRICK 2: DYNAMISCHES VORAUSFÜLLEN (GET-REQUEST) ---
    # Wenn die Seite das erste Mal geladen wird, befüllen wir die Formularfelder mit den echten DB-Daten
    elif request.method == 'GET':
        form.name.data = user.name
        if user.role == 'professor':
            form.themenfelder.data = user.themenfelder
            form.anforderungen.data = user.anforderungen
            form.freie_plaetze.data = user.freie_plaetze

    return render_template('profile.html', form=form, user=user)