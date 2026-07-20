# Datenmodell

![erm](https://github.com/petrovvvic/team2_thesis_match/raw/main/docs/assets/images/Screenshot%202026-06-21%20205638.png)

Die Anwendung nutzt **SQLite** als Datenbanktechnologie und **Flask-SQLAlchemy** als ORM-Schicht.
Die Datenbankdatei liegt unter `instance/thesis_match.sqlite`.

Die SQLAlchemy-Model-Klassen sind in `db.py` definiert. Diese Klassen sind die maßgebliche Quelle (Source of Truth) für die aktuelle Datenbankstruktur.

## Zentrale Entitäten

### User

Das `User`-Model speichert Login- und Account-Daten für Studierende und Professor:innen.

Wichtige Felder:
- `id`
- `email`
- `password_hash`
- `first_name`
- `last_name`
- `role`
- `account_status`
- `created_at`

Das Feld `role` unterscheidet Studierende und Professor:innen.

Beziehungen:
- Ein User hat ein `StudentProfile`
- Ein User hat ein `ProfessorProfile`
- Ein User kann als Studierende:r oder Professor:in mit vielen Betreuungsanfragen verbunden sein

### StudentProfile

Das `StudentProfile`-Model speichert studierendenspezifische Profildaten.

Wichtige Felder:
- `user_id`
- `matriculation_number`
- `faculty_id`
- `degree_program_id`
- `semester`
- `study_focus`

Beziehungen:
- Gehört zu einem `User`
- Kann eine `Faculty` referenzieren
- Kann einen `DegreeProgram` referenzieren

### ProfessorProfile

Das `ProfessorProfile`-Model speichert professorspezifische Profildaten.

Wichtige Felder:
- `user_id`
- `facheinheit_id`
- `title`
- `research_areas`
- `requirements`
- `max_supervisions`
- `accepting_requests`

Beziehungen:
- Gehört zu einem `User`
- Kann eine `Facheinheit` referenzieren

### Faculty

Das `Faculty`-Model speichert die Fachbereiche, damit Nutzer keine Fachbereichsnamen manuell eingeben müssen.

Wichtige Felder:
- `id`
- `code`
- `name`
- `created_at`

Beziehungen:
- Ein Fachbereich hat viele Studiengänge
- Ein Fachbereich hat viele Facheinheiten
- Studierendenprofile referenzieren einen Fachbereich direkt; Professorenprofile indirekt über ihre Facheinheit

### DegreeProgram

Das `DegreeProgram`-Model speichert Studiengänge, die zu einem Fachbereich gehören.

Wichtige Felder:
- `id`
- `faculty_id`
- `name`
- `degree`

Beziehungen:
- Gehört zu einem `Faculty`
- Kann von Studierendenprofilen referenziert werden

### Facheinheit

Das `Facheinheit`-Model speichert die akademischen Einheiten (Untereinheiten) innerhalb eines Fachbereichs. Professor:innen sind einer Facheinheit zugeordnet, und der Professor-Feed lässt sich danach filtern.

Wichtige Felder:
- `id`
- `faculty_id`
- `name`

Beziehungen:
- Gehört zu einem `Faculty`
- Kann von vielen Professorenprofilen referenziert werden

### SupervisionRequest

Das `SupervisionRequest`-Model repräsentiert die Anfrage einer/eines Studierenden an eine:n Professor:in zur Betreuung der Bachelorarbeit.

Wichtige Felder:
- `id`
- `student_id`
- `professor_id`
- `examiner_role`
- `proposed_title`
- `short_description`
- `preferred_period`
- `status`
- `created_at`
- `updated_at`

Beziehungen:
- Gehört zu einem Studierenden-User
- Gehört zu einem Professor-User
- Kann viele Nachrichten (`RequestMessage`) haben
- Kann viele Anhänge (`Attachment`) haben
- Kann Einträge in der Status-Historie haben

### RequestMessage

Das `RequestMessage`-Model speichert die Nachrichten im anfragebezogenen Chat.

Wichtige Felder:
- `id`
- `request_id`
- `sender_id`
- `message_text`
- `created_at`

Beziehungen:
- Gehört zu einer `SupervisionRequest`
- Gehört zu einem sendenden User
- Kann Anhänge haben

### Attachment

Das `Attachment`-Model speichert die Metadaten zu hochgeladenen PDF-Dateien.

Wichtige Felder:
- `id`
- `request_id`
- `message_id`
- `uploaded_by`
- `attachment_context`
- `original_filename`
- `storage_path`
- `mime_type`
- `file_size`
- `created_at`

Es werden nur die **Metadaten** in der Datenbank gespeichert. Die eigentlichen PDF-Dateien liegen im Upload-Ordner der Anwendung.

### RequestStatusHistory

Das `RequestStatusHistory`-Model speichert die Statusänderungen von Betreuungsanfragen.

Wichtige Felder:
- `id`
- `request_id`
- `old_status`
- `new_status`
- `changed_by`
- `comment`
- `created_at`

Beziehungen:
- Gehört zu einer `SupervisionRequest`
- Speichert, welcher User den Status geändert hat

