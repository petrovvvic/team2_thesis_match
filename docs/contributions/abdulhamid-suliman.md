---
title: Abdulhamid Suliman
parent: Individual Contributions
nav_order: 1
---


{: .no_toc }
# Abdulhamid Suliman

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

Meine angestrebte Note für dieses Modul liegt bei 1,0.



### Personal goals

Meine persönlichen Ziele in diesem Modul sind:



* den grundlegenden Aufbau einer vollständigen Flask-Webanwendung zu verstehen

* relationale Datenmodelle mit SQLAlchemy zu entwerfen und praktisch umzusetzen

* Primärschlüssel, Fremdschlüssel und Beziehungen zwischen Datenbankmodellen korrekt anzuwenden

* Formulare, Flask-Routen, SQLAlchemy-Abfragen und Jinja-Templates miteinander zu verbinden

* rollenabhängige Funktionen für Studierende sowie Professorinnen und Professoren zu implementieren

* den Anfrageprozess für die Betreuung einer Bachelorarbeit technisch abzubilden

* den Git- und GitHub-Workflow in einem Teamprojekt sicher anzuwenden

* Änderungen in kleinen und nachvollziehbaren Commits zu dokumentieren

* eigene Implementierungen durch Browser-Tests und Datenbankabfragen zu überprüfen

* technische Entscheidungen verständlich erklären und begründen zu können
---

## Eidesstattliche Erklärung

**Abdulhamid Suliman, Matrikelnr.: 77211817917**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :- | :----------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Bereinigung, Dokumentation und Erweiterung der SQLAlchemy-Datenbankgrundlage | Ich habe die bestehende Datenbankstruktur überprüft, nicht mehr benötigte SQL-Dateien entfernt und das tatsächlich implementierte relationale Datenmodell dokumentiert. Zusätzlich habe ich die Beziehung zwischen Studentenprofilen und Studiengängen erweitert. Dadurch wurde die Datenbasis des Projekts konsistenter und nachvollziehbarer. | Zu Beginn musste ich den Unterschied zwischen SQLite als Datenbanksystem und SQLAlchemy als Object-Relational Mapper verstehen. Anschließend musste ich nachvollziehen, wie Modelle, Fremdschlüssel, Beziehungen und Seed-Daten innerhalb der Flask-Anwendung zusammenarbeiten.                  |
| 2 | Implementierung des Anfrage-Flows für Betreuungsanfragen                     | Studierende können Betreuungsanfragen erstellen und Professorinnen beziehungsweise Professoren können die an sie gerichteten Anfragen annehmen oder ablehnen. Die Statusänderungen werden zusätzlich in einer eigenen Historientabelle protokolliert.                                                                                           | Die Herausforderung bestand darin, Flask-Routen, WTForms-Formulare, Rollen- und Berechtigungsprüfungen, SQLAlchemy-Transaktionen und Jinja-Templates korrekt miteinander zu verbinden. Außerdem musste verhindert werden, dass fremde oder bereits bearbeitete Anfragen erneut verändert werden. |
| 3 | Entwicklung und Überarbeitung des rollenabhängigen Dashboards                | Das Dashboard stellt abhängig von der Benutzerrolle unterschiedliche Anfragen, Statusinformationen und Aktionen dar. Zusätzlich habe ich die Bootstrap-Struktur korrigiert und die Oberfläche übersichtlicher und einheitlicher gestaltet.                                                                                                      | Ich musste rollenabhängige Datenbankabfragen, bedingte Darstellungen in Jinja und die Bootstrap-Grid-Struktur miteinander abstimmen. Außerdem musste sichergestellt werden, dass Aktionen wie „Anfrage stellen“ nur den dafür berechtigten Benutzern angezeigt werden.                           |

## Design Decisions that I led

1. [DD #02: Studiengänge als relationale Stammdaten statt Freitext](../design-decisions/dd-02.md)
2. [DD #03: Gemeinsames rollenabhängiges Dashboard statt getrennter Dashboards](../design-decisions/dd-03.md)

---


## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Bereinigung der bisherigen Datenbankstruktur und Dokumentation des tatsächlich implementierten SQLAlchemy-Datenmodells                                             | [Commit `a76b52f`](https://github.com/petrovvvic/team2_thesis_match/commit/a76b52f), [Commit `01ae16b`](https://github.com/petrovvvic/team2_thesis_match/commit/01ae16b), [Commit `0edf879`](https://github.com/petrovvvic/team2_thesis_match/commit/0edf879), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4) | [HWR-Kursmaterial: SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html), [Projektdatei `db.py`](https://github.com/petrovvvic/team2_thesis_match/blob/main/db.py)                                                                                   |
| Implementierung und Dokumentation eines gemeinsamen rollenabhängigen Dashboards für Studierende sowie Professorinnen und Professoren                               | [Commit `c02b1fb`](https://github.com/petrovvvic/team2_thesis_match/commit/c02b1fb), [Commit `554b28f`](https://github.com/petrovvvic/team2_thesis_match/commit/554b28f), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4)                                                                                      | [HWR-Kursmaterial: Flask](https://hwrberlin.github.io/fswd/flask.html), [HWR-Kursmaterial: SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html), [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html)         |
| Implementierung und Dokumentation des Erstellens und Speicherns einer Betreuungsanfrage                                                                            | [Commit `462a2f1`](https://github.com/petrovvvic/team2_thesis_match/commit/462a2f1), [Commit `fb7df66`](https://github.com/petrovvvic/team2_thesis_match/commit/fb7df66), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4)                                                                                      | [HWR-Kursmaterial: Flask](https://hwrberlin.github.io/fswd/flask.html), [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html), [HWR-Kursmaterial: SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html)         |
| Erstellung kontrollierter Seed-Daten für Bachelorstudiengänge sowie Ergänzung der Beziehung zwischen `StudentProfile` und `DegreeProgram`                          | [Commit `a48f701`](https://github.com/petrovvvic/team2_thesis_match/commit/a48f701), [Commit `bc17ced`](https://github.com/petrovvvic/team2_thesis_match/commit/bc17ced), [Pull Request #8](https://github.com/petrovvvic/team2_thesis_match/pull/8)                                                                                      | [HWR-Kursmaterial: SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html), [HWR Berlin: Studiengänge](https://www.hwr-berlin.de/studium/studiengaenge), [Projektdatei `db.py`](https://github.com/petrovvvic/team2_thesis_match/blob/main/db.py)      |
| Integration der Studiengangsauswahl in das Studentenprofil und automatische Übernahme des zugehörigen Fachbereichs                                                 | [Commit `03dd8bd`](https://github.com/petrovvvic/team2_thesis_match/commit/03dd8bd), [Pull Request #8](https://github.com/petrovvvic/team2_thesis_match/pull/8)                                                                                                                                                                           | [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html), [HWR-Kursmaterial: SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html), [HWR Berlin: Studiengänge](https://www.hwr-berlin.de/studium/studiengaenge)    |
| Implementierung des Annehmens und Ablehnens von Betreuungsanfragen einschließlich Rollenprüfung, Zuordnungsprüfung, CSRF-geschützten Formularen und Statushistorie | [Commit `558efac`](https://github.com/petrovvvic/team2_thesis_match/commit/558efac)                                                                                                                                                                                                                                                       | [HWR-Kursmaterial: Flask](https://hwrberlin.github.io/fswd/flask.html), [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html), [HWR-Kursmaterial: SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html)         |
| Rollenabhängige Anzeige des Buttons „Anfrage stellen“ im Professorenprofil                                                                                         | [Commit `4860a76`](https://github.com/petrovvvic/team2_thesis_match/commit/4860a76), [Pull Request #11](https://github.com/petrovvvic/team2_thesis_match/pull/11)                                                                                                                                                                         | [HWR-Kursmaterial: Flask](https://hwrberlin.github.io/fswd/flask.html), [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html)                                                                                           |
| Überarbeitung des Dashboard-Layouts durch Korrektur der Bootstrap-Grid-Struktur, gleichmäßige Statistik-Kacheln und optische Hervorhebung der Gesamtübersicht      | [Commit `1d327b2`](https://github.com/petrovvvic/team2_thesis_match/commit/1d327b2), [Pull Request #11](https://github.com/petrovvvic/team2_thesis_match/pull/11)                                                                                                                                                                         | [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html), [Projektdatei `dashboard.html`](https://github.com/petrovvvic/team2_thesis_match/blob/main/templates/dashboard.html)                                             |
| Aktualisierung meiner persönlichen Contribution-Seite und Dokumentation der technischen Design Decisions DD-02 und DD-03                                           | [Commit `c1226c7`](https://github.com/petrovvvic/team2_thesis_match/commit/c1226c7), [Pull Request #10](https://github.com/petrovvvic/team2_thesis_match/pull/10)                                                                                                                                                                         | [HWR-Kursmaterial: Design Decisions](https://hwrberlin.github.io/fswd/design-decisions.html), [HWR-Bewertungsanforderungen](https://hwrberlin.github.io/fswd/assessment.html), [HWR-Kursmaterial: Git und GitHub](https://hwrberlin.github.io/fswd/git.html) |
| Implementierung des Bearbeitens und Zurückziehens eigener offener Betreuungsanfragen einschließlich Berechtigungs- und Statusprüfungen | [Commit `5f3867a`](https://github.com/petrovvvic/team2_thesis_match/commit/5f3867a) | [HWR-Kursmaterial: Flask](https://hwrberlin.github.io/fswd/flask.html), [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html), [HWR-Kursmaterial: SQLAlchemy](https://hwrberlin.github.io/fswd/sqlalchemy.html) |
| Rollenabhängige Anzeige der ausgewählten Prüferrolle im gemeinsamen Dashboard für Studierende sowie Professorinnen und Professoren | [Commit `6788ce7`](https://github.com/petrovvvic/team2_thesis_match/commit/6788ce7) | [HWR-Kursmaterial: User Interfaces](https://hwrberlin.github.io/fswd/user-interfaces.html), [Projektdatei `dashboard.html`](https://github.com/petrovvvic/team2_thesis_match/blob/main/templates/dashboard.html) |

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | ChatGPT (OpenAI) | Erklärung des Git- und GitHub-Workflows | Branches, Commits, Pull-, Push- und Merge-Vorgänge | Terminalausgaben und Git-Befehle eingefügt und erklären lassen; alle Befehle selbst ausgeführt |
| 02 | ChatGPT (OpenAI) | Erklärung und Unterstützung bei der SQLAlchemy-Datenstruktur | `db.py`, `seed_data.py`, Datenmodelldokumentation | Gefragt, wie Modelle, Primär- und Fremdschlüssel, Beziehungen und Seed-Daten zusammenarbeiten |
| 03 | ChatGPT (OpenAI) | Unterstützung beim Anfrage-Flow | `app.py`, `forms.py`, `request_new.html`, `request_edit.html`, `request_withdraw.html` | Unterstützung beim Erstellen, Bearbeiten, Zurückziehen, Annehmen und Ablehnen von Betreuungsanfragen |
| 04 | ChatGPT (OpenAI) | Erklärung von Flask-, WTForms- und Jinja-Konzepten | Flask-Routen, Formulare und Templates | Gefragt, wie Routen, Formulare, Datenbankabfragen und Templates miteinander verbunden werden |
| 05 | ChatGPT (OpenAI) | Unterstützung bei Dashboard- und UI-Anpassungen | `dashboard.html`, `profile-detail.html` | Unterstützung bei rollenabhängiger Darstellung, Bootstrap-Struktur und Anzeige der Prüferrolle |
| 06 | ChatGPT (OpenAI) | Debugging und Testunterstützung | App-Start, Browser-Tests, Datenbank- und Git-Prüfungen | Fehlermeldungen und Testergebnisse eingefügt, mögliche Ursachen und Prüfschritte erklären lassen |
| 07 | ChatGPT (OpenAI) | Formulierungshilfe und Strukturierung der Projektdokumentation | Development Log, Contributions und Design Decisions | Unterstützung bei Grammatik, Struktur und verständlicher Beschreibung meiner eigenen Beiträge |
