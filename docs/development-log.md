# Development Log

## Removed old raw SQL database files

Branch:
- remove-old-sql-database-folder

What changed:
- Removed database/schema.sql
- Removed database/seed.sql

the reason why:
- The application uses SQLAlchemy models in db.py.
- The old raw SQL files were no longer the source of truth for the database model.
- The app still uses SQLite through SQLAlchemy.

How I checked it:
- I used git status to check the current branch and see which files changed.
- I used git diff --stat origin/main..HEAD to confirm that only the old SQL files were removed.

## 2026-06-18 — Added basic role-based dashboard

Branch:

* feature/db-dashboard-basics

What changed:

* I added a new `/dashboard` route in `app.py`
* Then added a dashboard navigation link in `templates/base.html`
* CAfter that i created the new template `templates/dashboard.html`

Why:

* Students and professors need a central overview of their supervision requests.
* The dashboard shows different request data depending on the logged-in user's role.
* The implementation uses the existing `SupervisionRequest` model and does not change the database schema.

How I checked it:

* I installed the project requirements in the virtual environment.
* I ran the app locally with `python -m flask --app app run --debug`.
* I registered and logged in as a student.
* I opened the dashboard page and confirmed that it loaded correctly.
* I restored the local SQLite database file afterward using `git restore instance/thesis_match.sqlite`so that my test user data was not committed.

## 2026-06-18 — Added supervision request creation flow

Branch:
- feature/db-dashboard-basics

What changed:
- Added a request form in `forms.py`
- Added the `/requests/new` route in `app.py`
- Added `templates/request_new.html`
- Added a dashboard button for students to create a new request

Why:
- Students need a way to create supervision requests from the web app.
- The request is saved through the existing `SupervisionRequest` SQLAlchemy model.

How I checked it:
- I ran the app locally with `python -m flask --app app run --debug`.
- I opened the dashboard as a student.
- I created a test supervision request.
- The request appeared on the dashboard with status `submitted`.
- I restored `instance/thesis_match.sqlite` afterward so local test data was not committed.

## 2026-07-18 — Password security: SECRET_KEY via .env + password policy

Branch:
- main (trunk-based, after pulling first)

What changed:
- Removed the hardcoded `SECRET_KEY` from `app.py`; it is now loaded from a local `.env` file via `python-dotenv`. If the variable is missing, the app fails fast on startup with a `RuntimeError` and a clear instruction (instead of silently falling back to an insecure default).
- Generated a new key (rotation — the old one was exposed in the git history).
- Added `.env` to `.gitignore`, created `.env.example` as a template, and added the configuration step to the README.
- Added a password policy in `forms.py`: 8–24 characters with at least one uppercase letter, one lowercase letter, one digit and one special character (custom validator `password_complexity`); the requirements are shown as help text below the field.
- Hardened session cookies (`SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SAMESITE='Lax'`).

Why:
- The `SECRET_KEY` signs session cookies; hardcoded in the repo, anyone with repo access could forge sessions (see DD-11).
- Until now, `123456` was a valid password (see DD-12).

How I checked it:
- Started the app without a `.env` → it aborts with a clear error message; with `.env` → starts normally.
- My existing session was invalidated after the key rotation (expected — proof that the new key is active).
- Tested registration with weak passwords → one specific error message per violated rule; with a strong password → registration and login succeed.
- Checked the password hash in the database (`scrypt:…`, no plaintext).
- Restored `instance/thesis_match.sqlite` afterward with `git restore` so that no test data gets committed.
- Verified with `git status` that `.env` does not show up.
