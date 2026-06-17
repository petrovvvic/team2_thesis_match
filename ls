from flask_sqlalchemy import SQLAlchemy

# Das ist unsere Datenbank-Instanz
db = SQLAlchemy()


# Die User-Klasse repräsentiert eine Tabelle in unserer SQLite-Datenbank
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)  # Niemals Passwörter in Klartext speichern!
    role = db.Column(db.String(20), nullable=False)  # 'student' oder 'professor'

    # Diese Felder sind später nur für Professoren wichtig
    themenfelder = db.Column(db.String(500), nullable=True)
    anforderungen = db.Column(db.String(500), nullable=True)
    freie_plaetze = db.Column(db.String(10), nullable=True)