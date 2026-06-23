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

[Hier deine Zielnote eintragen, z.B. 1,0 - 1,3]

### Personal goals

[Hier persönliche Ziele eintragen, z.B.: Mein Ziel war es, tiefes Verständnis für Backend-Architekturen (SQLAlchemy) und sicheres Session-Management in Flask zu entwickeln, sowie einen sauberen, agilen Git-Workflow im Team zu etablieren.]

---

## Eidesstattliche Erklärung

**Nikita Pasichnyk, Matrikelnr.: [DEINE MATRIKELNUMMER HIER EINTRAGEN]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## 1. Meine Rolle & Git-Workflow

Nach der Definition unserer Value Proposition für "Thesis Match", ging es darum die festen technische Hürden zu benennen und sich Lösungen zu überlegen. Es war klar, dass eine Two-Sided Platform mit einer robusten Nutzerverwaltung und klaren Profilen steht und fällt. Ich habe daher die Verantwortung für den Einstieg in unsere App übernommen: **Die Registrierung, den Login und das dynamische Profil-Dashboard (Screens 1a, 1b, 7).**

Wie so vieles beim Programmieren, war der Weg dorthin kein gerader Strich, sondern ein iterativer Prozess, den ich in unserem Git-Repository über verschiedene Branches dokumentiert habe. Um "Unrelated Histories"-Konflikte durch lokale ZIP-Downloads zu vermeiden und die Teamgeschwindigkeit zu erhöhen, habe ich zudem für kleine bis mittlere Fixes einen agilen **"Trunk-Based Development"**-Ansatz im Team etabliert (`git clone` und direkte Pushes ins `main`-Branch nach vorherigem Pull).

---

## 2. Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | **Migration auf SQLAlchemy**<br>Refaktorierung der flachen SQLite-Tabelle in ein relationales, skalierbares ORM-Datenmodell. | Ich habe gelernt, komplexe 1:1-Beziehungen in Flask strikt objektorientiert und sicher gegen SQL-Injection zu modellieren. | Die zeitgleiche Erstellung von `User` und abhängigem `Profile` bei der Registrierung (gelöst durch den Einsatz von `db.session.flush()`). |
| 2 | **Dynamische UI & Route-Guarding**<br>Einheitliches Frontend für Studierende und Professoren bei strikter Backend-Trennung. | Das DRY-Prinzip (Don't Repeat Yourself) wurde konsequent angewendet. Eine Route steuert die Logik und hält das Template kompakt. | Das Backend musste gegen unautorisierte POST-Requests abgesichert werden, damit Studierende keine Professoren-Felder überschreiben können. |
| 3 | **Session-Management & Weiterleitung**<br>Intelligentes "Reverse Route-Guarding" und Erkennung von Erstanmeldungen. | Ich habe ein "Frictionless Onboarding" geschaffen. Die UX ist nahtlos und leitet Nutzer intelligent und ressourcenschonend zum richtigen Screen. | Das System musste sich den Zustand "frisch registriert" für den nächsten Request merken, ohne Datenbankeinträge zu hinterlassen (gelöst via `session.pop()`). |

---

## 3. Design Decisions that I led

*(Hinweis: Die detaillierten Erläuterungen wurden direkt in diesem Dokument festgehalten, um den Lesefluss zu gewährleisten.)*

### DD #01: Datenbank-Interaktion (ORM vs. Raw SQL)
* **Option A:** Direkte Ausführung von rohen SQL-Queries über das `sqlite3` Modul in der `app.py` (Mein initialer Ansatz in Version 1.0 zur simplen Darstellung und für Team-Tests).
* **Option B:** Nutzung des Object-Relational Mappers (ORM) SQLAlchemy.
* **Entscheidung:** Wir als Team haben uns für Option B entschieden. Rohe SQL-Befehle führten zu unübersichtlichem Code, als die Aufteilung in Professoren- und Studenten-Profile notwendig wurde. SQLAlchemy bot nativen Schutz gegen SQL-Injection durch parametrisierte Queries und erlaubte objektorientiertes Arbeiten.

### DD #02: Komplexitätsreduktion im Professoren-Profil
* **Option A:** Ein kombiniertes Auswahlfeld (Dropdown), das die maximale Anzahl der Plätze und den Status bündelt. Mein initialer Entwicklungsansatz zur Vermeidung inkonsistenter Datenbankzustände.
* **Option B:** Eine simple, binäre Checkbox ("Anfragen erhalten?"), während auf die exakte Zählung von Plätzen im MVP verzichtet wird.
* **Entscheidung:** Obwohl Option A technisch vollständig implementiert war, habe ich den Code nach Team-Feedback aktiv auf Option B refaktorisiert. Die Abfrage von exakten Kapazitäten verkompliziert das Profil unnötig. Diese Entscheidung beweist, dass agile Entwicklung und User Experience Vorrang vor bereits geschriebenem Code haben.

### DD #03: "Frictionless Onboarding" vs. Dynamisches JavaScript
* **Option A:** Abfrage der `Facheinheit` direkt im Registrierungsformular. Da dieses Feld nur für Professoren relevant ist, hätte es mittels Custom JavaScript dynamisch ein- und ausgeblendet werden müssen.
* **Option B:** Verschiebung der Abfrage in das spätere Profil-Dashboard und radikale Kürzung der Pflichtfelder im Anmeldeprozess (Frictionless Onboarding).
* **Entscheidung:** Ich habe mich für Option B entschieden. Option A hätte zwingend den Einsatz von JavaScript erfordert, was gegen die Projektrichtlinien ("Forbidden Technology") verstoßen hätte. Die technische Compliance hatte absolute Priorität. Spezifische Profil-Eigenschaften werden nun sicher erst nach dem initialen Login im rollenspezifischen Profil-Bereich erhoben.

---

## 4. Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| **Architektur-Upgrade (Version 1.1)**<br>Refaktorierung des Codes auf SQLAlchemy, WTForms Validatoren und Session-Logik. | Branch: `feature/screens-v1.1` (und final im `main`).<br>Commit: `feat: Vollständiges Update 1.1 - Neue Architektur, HTML-Profile & JS-Fix` | [SQLAlchemy Docs](https://docs.sqlalchemy.org/en/20/), [Flask-WTF Docs](https://flask-wtf.readthedocs.io/) |
| **Initiale Prototypen (Version 1.0)**<br>Erster Aufbau der Registrierungs- und Login-Screens mit nativer SQLite Datenbank. | Branch: `archive/screens-v1.0-initial` | Flask Official Documentation |
| **UX-Fixes & Route-Guarding**<br>Einbau von Redirects für eingeloggte User und Frontend-Validatoren (z.B. Semester Minimum). | Commits im `main`-Branch (Trunk-Based Development) | WTForms Documentation |

---

## 5. AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | Gemini | Sparringspartner für Code-Refactoring & Debugging | `app.py` (Route Guarding, SQLAlchemy Models), `forms.py` | Iteratives Prompting zur Fehlerbehebung (z.B. Lösung von HTTP 500 Errors bei fehlenden Formular-Choices) und Optimierung von Datenbank-Queries. |
| 02 | Gemini | Strategische UX- und Compliance-Beratung | `register.html`, Formulardesign | Prompting zur Findung von Alternativen für dynamisches UI-Rendering, um streng konform mit der "Forbidden Technology" (Verzicht auf JavaScript) zu bleiben. |
| 03 | Gemini | Strukturierung der Dokumentation | `nikita-pasichnyk.md` | Unterstützung bei der Formatierung der Markdown-Tabelle und Ausformulierung technischer Design-Entscheidungen für das Kolloquium. |
