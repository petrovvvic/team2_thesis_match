---
title: Nikita Pasichnyk
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Nikita Pasichnyk

<details open markdown="block">
<summary>Table of contents</summary>
{: .text-delta }
- TOC
{:toc}
</details>

## Meta-Goals

### Target grade

1,0

### Personal goals

Verbesserung der eigenen Python-Skills im Bereich Backend-Architektur, der sichere Umgang mit ORM-Modellen (SQLAlchemy) sowie die Etablierung einer agilen und störungsfreien Kollaboration im Team.

---

## Eidesstattliche Erklärung

**Nikita Pasichnyk, Matrikelnr.: 77202191909**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## 1. Meine Rolle & Git-Workflow

Nach der Definition unserer Value Proposition für "Thesis Match" ging es darum, die festen technischen Hürden zu benennen und sich Lösungen zu überlegen. Es war klar, dass eine Two-Sided Platform mit einer robusten Nutzerverwaltung und klaren Profilen steht und fällt. Ich habe daher die Verantwortung für den Einstieg in unsere App übernommen: **Die Registrierung, den Login und das dynamische Profil-Dashboard (Screens 1a, 1b, 7).**

Wie so vieles beim Programmieren, war der Weg dorthin kein gerader Strich, sondern ein iterativer Prozess, den ich in unserem Git-Repository über verschiedene Branches dokumentiert habe. Um "Unrelated Histories"-Konflikte durch lokale ZIP-Downloads zu vermeiden und die Teamgeschwindigkeit zu erhöhen, habe ich zudem für kleine bis mittlere Fixes einen agilen **"Trunk-Based Development"**-Ansatz im Team etabliert (`git clone` und direkte Pushes in den `main`-Branch nach vorherigem Pull).

---

## 2. Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | **Migration auf SQLAlchemy**<br>Refaktorierung der flachen SQLite-Tabelle in ein relationales, skalierbares ORM-Datenmodell. | Ich habe gelernt, komplexe 1:1-Beziehungen in Flask strikt objektorientiert und sicher gegen SQL-Injection zu modellieren. | Die zeitgleiche Erstellung von `User` und abhängigem `Profile` bei der Registrierung (gelöst durch den Einsatz von `db.session.flush()`). |
| 2 | **Dynamische UI & Route-Guarding**<br>Einheitliches Frontend für Studierende und Professoren bei strikter Backend-Trennung. | Das DRY-Prinzip (Don't Repeat Yourself) wurde konsequent angewendet. Eine Route steuert die Logik und hält das Template kompakt. | Das Backend musste gegen unautorisierte POST-Requests abgesichert werden, damit Studierende keine Professoren-Felder überschreiben können. |
| 3 | **Session-Management & Weiterleitung**<br>Intelligentes "Reverse Route-Guarding" und Erkennung von Erstanmeldungen. | Ich habe ein "Frictionless Onboarding" geschaffen. Die UX ist nahtlos und leitet Nutzer intelligent und ressourcenschonend zum richtigen Screen. | Das System musste sich den Zustand "frisch registriert" für den nächsten Request merken, ohne Datenbankeinträge zu hinterlassen (gelöst via `session.pop()`). |

---

## 3. Design Decisions that I led

1. [DD #06 — Datenbank-Interaktion (ORM vs. Raw SQL)](https://github.com/petrovvvic/team2_thesis_match/blob/main/docs/design-decisions/dd-06.md)
2. [DD #07 — Komplexitätsreduktion im Professoren-Profil](https://github.com/petrovvvic/team2_thesis_match/blob/main/docs/design-decisions/dd-07.md)
3. [DD #08 — "Frictionless Onboarding" vs. Dynamisches JavaScript](https://github.com/petrovvvic/team2_thesis_match/blob/main/docs/design-decisions/dd-08.md)
4. [DD #09 — Wahrung der referenziellen Integrität (Foreign Keys)](https://github.com/petrovvvic/team2_thesis_match/blob/main/docs/design-decisions/dd-09.md)
5. [DD #10 — Sicherheitskonzept der Authentifizierung](https://github.com/petrovvvic/team2_thesis_match/blob/main/docs/design-decisions/dd-10.md)

---

## 4. Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| **Architektur-Upgrade (Version 1.1)**<br>Refaktorierung des Codes auf SQLAlchemy, WTForms Validatoren und Session-Logik. | [Branch: feature/screens-v1.1](https://github.com/petrovvvic/team2_thesis_match/tree/feature/screens-v1.1)<br>Commit: `feat: Vollständiges Update 1.1 - Neue Architektur, HTML-Profile & JS-Fix` | [SQLAlchemy 2.0 Docs](https://docs.sqlalchemy.org/en/20/),<br>[Flask-WTF Docs](https://flask-wtf.readthedocs.io/) |
| **Initiale Prototypen (Version 1.0)**<br>Erster Aufbau der Registrierungs- und Login-Screens mit nativer SQLite Datenbank. | [Branch: archive/screens-v1.0-initial](https://github.com/petrovvvic/team2_thesis_match/tree/archive/screens-v1.0-initial)<br>Commit: `feat: Version 1.0 - Screens 1a, 1b und 7 voll funktionsfähig...` | [Flask Official Documentation](https://flask.palletsprojects.com/) |
| **UX-Fixes & Route-Guarding**<br>Einbau von Redirects für eingeloggte User und Frontend-Validatoren (z.B. Semester Minimum). | Commits im `main`-Branch:<br>`fix: Routing issues`<br>`Semester fix (negative integers)`<br>`fix: Fachbereich anpassung -> Prof Profile` | [WTForms Validators](https://wtforms.readthedocs.io/en/3.0.x/validators/) |
| **Security & Form Validation**<br>Implementierung von `werkzeug.security` (Password Hashing) und Formular-Validierung. | Siehe Hash-Generierung in der `/register` Route (`app.py`). | [Werkzeug Security API](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security) |
| **Relationales Datenbank-Design**<br>Aufbau der komplexen 1:1 und 1:n Beziehungen zwischen `User` und Profilen. | Siehe Model-Definitionen in der `db.py` | [SQLAlchemy Relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html) |

---

## 5. AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | Gemini | Sparringspartner für Code-Refactoring & Debugging | `app.py` (Route Guarding, SQLAlchemy Models), `forms.py` | Iteratives Prompting zur Fehlerbehebung (z.B. Lösung von HTTP 500 Errors bei fehlenden Formular-Choices) und Optimierung von Datenbank-Queries. |
| 02 | Gemini | Strategische UX- und Compliance-Beratung | `register.html`, Formulardesign | Prompting zur Findung von Alternativen für dynamisches UI-Rendering, um streng konform mit der "Forbidden Technology" (Verzicht auf JavaScript) zu bleiben. |
| 03 | Gemini | Strukturierung der Dokumentation | `nikita-pasichnyk.md` | Unterstützung bei der Formatierung der Markdown-Tabelle und Ausformulierung technischer Design-Entscheidungen für das Kolloquium. |
| 04 | DeepSeek | Logik-Optimierung und Query-Design | `app.py` (Filterlogik im `/feed` und API-Abfragen) | Einsatz zur Optimierung der Python-Suchlogik (`suchbegriff in f"{prof.user.first_name}..."`) und Evaluierung von SQLAlchemy-Listenabfragen. |
| 05 | DeepSeek | Security Best-Practices & Architektur | `app.py`, `db.py` | Recherche-Prompts bezüglich Best-Practices für die Handhabung von `werkzeug.security` Hashes beim Registrierungsprozess und strukturelle Trennung von DB-Models. |
