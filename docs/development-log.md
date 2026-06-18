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