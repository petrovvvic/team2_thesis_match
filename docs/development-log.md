# Entwicklungs-Log

## Alte rohe SQL-Datenbankdateien entfernt

Branch:
- remove-old-sql-database-folder

Was geändert wurde:
- `database/schema.sql` entfernt
- `database/seed.sql` entfernt

Warum:
- Die Anwendung nutzt die SQLAlchemy-Models in `db.py`.
- Die alten rohen SQL-Dateien waren nicht mehr die maßgebliche Quelle (Source of Truth) für das Datenbankmodell.
- Die App greift weiterhin über SQLAlchemy auf SQLite zu.

Wie ich es geprüft habe:
- Mit `git status` den aktuellen Branch und die geänderten Dateien geprüft.
- Mit `git diff --stat origin/main..HEAD` bestätigt, dass nur die alten SQL-Dateien entfernt wurden.

## 2026-06-18 — Rollenbasiertes Dashboard (Grundgerüst) hinzugefügt

Branch:
- feature/db-dashboard-basics

Was geändert wurde:
- Neue Route `/dashboard` in `app.py` hinzugefügt
- Dashboard-Navigationslink in `templates/base.html` ergänzt
- Neues Template `templates/dashboard.html` erstellt

Warum:
- Studierende und Professor:innen brauchen eine zentrale Übersicht ihrer Betreuungsanfragen.
- Das Dashboard zeigt je nach Rolle des eingeloggten Nutzers unterschiedliche Anfragedaten.
- Die Umsetzung nutzt das bestehende `SupervisionRequest`-Model und ändert das Datenbankschema nicht.

Wie ich es geprüft habe:
- Projekt-Abhängigkeiten in der virtuellen Umgebung installiert.
- App lokal mit `python -m flask --app app run --debug` gestartet.
- Als Studierende:r registriert und eingeloggt.
- Die Dashboard-Seite geöffnet und bestätigt, dass sie korrekt lädt.
- Danach die lokale SQLite-Datei mit `git restore instance/thesis_match.sqlite` zurückgesetzt, damit meine Test-Nutzerdaten nicht committet werden.

## 2026-06-18 — Erstellungs-Flow für Betreuungsanfragen hinzugefügt

Branch:
- feature/db-dashboard-basics

Was geändert wurde:
- Anfrage-Formular in `forms.py` hinzugefügt
- Route `/requests/new` in `app.py` hinzugefügt
- `templates/request_new.html` hinzugefügt
- Dashboard-Button für Studierende zum Erstellen einer neuen Anfrage ergänzt

Warum:
- Studierende brauchen einen Weg, Betreuungsanfragen direkt in der Web-App zu erstellen.
- Die Anfrage wird über das bestehende `SupervisionRequest`-SQLAlchemy-Model gespeichert.

Wie ich es geprüft habe:
- App lokal mit `python -m flask --app app run --debug` gestartet.
- Dashboard als Studierende:r geöffnet.
- Eine Test-Betreuungsanfrage erstellt.
- Die Anfrage erschien im Dashboard mit Status `submitted`.
- Danach `instance/thesis_match.sqlite` zurückgesetzt, damit lokale Testdaten nicht committet werden.

## 2026-07-18 — Passwort-Sicherheit: SECRET_KEY via .env + Passwort-Policy

Branch:
- main (trunk-based, nach vorherigem Pull)

Was geändert wurde:
- Den fest im Code stehenden `SECRET_KEY` aus `app.py` entfernt; er wird jetzt über eine lokale `.env`-Datei via `python-dotenv` geladen. Fehlt die Variable, bricht die App beim Start sofort mit einem `RuntimeError` und klarer Anweisung ab (statt still auf einen unsicheren Default zurückzufallen).
- Einen neuen Key generiert (Rotation — der alte war in der Git-Historie exponiert).
- `.env` zur `.gitignore` hinzugefügt, `.env.example` als Vorlage erstellt und den Konfigurationsschritt in die README aufgenommen.
- Eine Passwort-Policy in `forms.py` ergänzt: 8–24 Zeichen mit mindestens einem Groß-, einem Kleinbuchstaben, einer Ziffer und einem Sonderzeichen (eigener Validator `password_complexity`); die Anforderungen werden als Hilfetext unter dem Feld angezeigt.
- Session-Cookies gehärtet (`SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SAMESITE='Lax'`).

Warum:
- Der `SECRET_KEY` signiert die Session-Cookies; fest im Repo könnte jede:r mit Repo-Zugriff Sessions fälschen (siehe DD-11).
- Bisher war `123456` ein gültiges Passwort (siehe DD-12).

Wie ich es geprüft habe:
- App ohne `.env` gestartet → bricht mit klarer Fehlermeldung ab; mit `.env` → startet normal.
- Meine bestehende Session war nach der Key-Rotation ungültig (erwartet — Beleg, dass der neue Key aktiv ist).
- Registrierung mit schwachen Passwörtern getestet → je verletzter Regel eine spezifische Fehlermeldung; mit starkem Passwort → Registrierung und Login erfolgreich.
- Den Passwort-Hash in der Datenbank geprüft (`scrypt:…`, kein Klartext).
- Danach `instance/thesis_match.sqlite` mit `git restore` zurückgesetzt, damit keine Testdaten committet werden.
- Mit `git status` verifiziert, dass `.env` nicht auftaucht.

## 2026-07-18 — Upload-Limit für PDF-Anhänge auf 5 MB begrenzt

Branch:
- main

Was geändert wurde:
- PDF-Uploads im Chat auf max. 5 MB begrenzt: `FileSize`-Validator in `forms.py` (freundliche Meldung) plus `MAX_CONTENT_LENGTH = 5 MB` in `app.py` als harten Backstop.
- 413-Fehlerhandler ergänzt, der bei zu großen Dateien eine verständliche Meldung zeigt statt der rohen Fehlerseite.

Warum:
- Sehr große Uploads sollen Speicher und Server nicht unnötig belasten; PDFs für Nachrichten/Exposés sind klein.

Wie ich es geprüft habe:
- PDF > 5 MB hochgeladen → wird mit Hinweis „max. 5 MB" abgelehnt; kleinere PDF → Upload erfolgreich.
