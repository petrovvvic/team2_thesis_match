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