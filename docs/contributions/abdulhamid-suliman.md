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
| 1 | Bereinigung, Dokumentation und gezielte Erweiterung der SQLAlchemy-Datenbankgrundlage | Ich habe die bestehende Datenbankstruktur überprüft, veraltete SQL-Dateien entfernt, das tatsächlich implementierte Datenmodell dokumentiert und die kontrollierte Zuordnung von Studiengängen zu Studentenprofilen erweitert. Damit habe ich zur Konsistenz und Nachvollziehbarkeit der zentralen Datenbasis beigetragen. | Zu Beginn musste ich den Unterschied zwischen SQLite als Datenbanksystem und SQLAlchemy als Object-Relational Mapper verstehen. Anschließend musste ich nachvollziehen, wie bestehende Modelle, Fremdschlüssel, Beziehungen, Seed-Daten und Formulare technisch zusammenwirken. |

| 2 | Implementierung und Dokumentation der Datenbankgrundlage mit SQLAlchemy | Das relationale Datenmodell bildet zentrale Bestandteile der Anwendung ab, beispielsweise Benutzer, Profile, Studiengänge und Betreuungsanfragen. Damit stellt es eine wesentliche technische Grundlage des Projekts dar. | Zu Beginn musste ich den Unterschied zwischen SQLite als Datenbanksystem und SQLAlchemy als Object-Relational Mapper verstehen. Anschließend musste ich das fachliche Datenmodell in Python-Klassen, Fremdschlüssel und Beziehungen übertragen. |

| 3 | Rollenabhängiges Dashboard und Anfrage-Flow für Betreuungsanfragen | Studierende können Anfragen erstellen und ihren Status verfolgen. Professorinnen und Professoren können die an sie gerichteten Anfragen einsehen, annehmen oder ablehnen. Statusänderungen werden zusätzlich protokolliert. | Die Herausforderung bestand darin, Benutzerrollen, Datenbankabfragen, Zugriffsprüfungen, Formulare, Jinja-Templates und Datenbanktransaktionen korrekt miteinander zu verbinden. |

| 4 | Integration der Bachelorstudiengänge des Fachbereichs 1 in das Studentenprofil | Studiengänge werden nicht als uneinheitlicher Freitext gespeichert, sondern aus kontrollierten Stammdaten ausgewählt. Dadurch werden unterschiedliche Schreibweisen und inkonsistente Daten vermieden. | Dafür mussten Seed-Daten, Fremdschlüssel, SQLAlchemy-Beziehungen und ein Dropdown-Feld konsistent umgesetzt werden. Zusätzlich wird der zugehörige Fachbereich automatisch aus dem ausgewählten Studiengang übernommen. |

## Design Decisions that I led

1. [DD #02]
2. [DD #03]
---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Entfernung veralteter SQL-Dateien aus dem Projekt | [Commit `a76b52f`](https://github.com/petrovvvic/team2_thesis_match/commit/a76b52f) | https://hwrberlin.github.io/fswd/git.html: SQLAlchemy; bestehende Projektmodelle in db.py |
| Dokumentation der Bereinigung der bisherigen Datenbankdateien | [Commit `01ae16b`](https://github.com/petrovvvic/team2_thesis_match/commit/01ae16b), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4) | https://hwrberlin.github.io/fswd/sqlalchemy.html#5-create-the-data-model: SQLAlchemy; bestehende Projektstruktur |

| Dokumentation des implementierten relationalen Datenmodells | [Commit `0edf879`](https://github.com/petrovvvic/team2_thesis_match/commit/0edf879), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4) | https://hwrberlin.github.io/fswd/sqlalchemy.html: SQLAlchemy|

| Implementierung eines rollenabhängigen Dashboards für Studierende und Professorinnen beziehungsweise Professoren | [Commit `c02b1fb`](https://github.com/petrovvvic/team2_thesis_match/commit/c02b1fb), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4) | https://hwrberlin.github.io/fswd/: Flask Routing; SQLAlchemy; User Interfaces |

| Dokumentation der Dashboard-Implementierung | [Commit `554b28f`](https://github.com/petrovvvic/team2_thesis_match/commit/554b28f), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4) | https://hwrberlin.github.io/fswd/: Flask documentation, Jinja documentation |

| Implementierung des Erstellens und Speicherns einer Betreuungsanfrage | [Commit `462a2f1`](https://github.com/petrovvvic/team2_thesis_match/commit/462a2f1), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4) | https://hwrberlin.github.io/fswd/: Flask Routing; SQLAlchemy; User Interfaces |

| Dokumentation des Anfrage-Flows | [Commit `fb7df66`](https://github.com/petrovvvic/team2_thesis_match/commit/fb7df66), [Pull Request #4](https://github.com/petrovvvic/team2_thesis_match/pull/4) |https://hwrberlin.github.io/fswd/: Flask documentation, SQLAlchemy documentation |

| Erstellung von Seed-Daten für ausgewählte Bachelorstudiengänge des Fachbereichs 1 | [Commit `a48f701`](https://github.com/petrovvvic/team2_thesis_match/commit/a48f701), [Pull Request #8](https://github.com/petrovvvic/team2_thesis_match/pull/8) | https://hwrberlin.github.io/fswd/- : SQLAlchemy; offizielle Studiengangsübersicht der HWR Berlin |

| Ergänzung der SQLAlchemy-Beziehung zwischen `StudentProfile` und `DegreeProgram` | [Commit `bc17ced`](https://github.com/petrovvvic/team2_thesis_match/commit/bc17ced), [Pull Request #8](https://github.com/petrovvvic/team2_thesis_match/pull/8) | https://hwrberlin.github.io/fswd/: SQLAlchemy|

| Integration der Studiengangsauswahl in das Studentenprofil | [Commit `03dd8bd`](https://github.com/petrovvvic/team2_thesis_match/commit/03dd8bd), [Pull Request #8](https://github.com/petrovvvic/team2_thesis_match/pull/8) | Flask-WTF SelectField documentation, SQLAlchemy documentation |

| Automatische Übernahme des Fachbereichs aus dem ausgewählten Studiengang | [Commit `03dd8bd`](https://github.com/petrovvvic/team2_thesis_match/commit/03dd8bd), [Pull Request #8](https://github.com/petrovvvic/team2_thesis_match/pull/8) | SQLAlchemy documentation |
| Implementierung des Annehmens und Ablehnens von Betreuungsanfragen | [Commit `558efac`](https://github.com/petrovvvic/team2_thesis_match/commit/558efac) | https://hwrberlin.github.io/fswd/: SQLAlchemy |

| Prüfung, dass nur der tatsächlich angefragte Professor bzw. Professorin eine Anfrage bearbeiten darf | [Commit `558efac`](https://github.com/petrovvvic/team2_thesis_match/commit/558efac) | Flask documentation |

| Protokollierung der Statusänderungen in `RequestStatusHistory` | [Commit `558efac`](https://github.com/petrovvvic/team2_thesis_match/commit/558efac) | SQLAlchemy session documentation |

| Anpassung des Dashboards um Chat-, Annehmen- und Ablehnen-Schaltflächen | [Commit `558efac`](https://github.com/petrovvvic/team2_thesis_match/commit/558efac) | Jinja documentation, Bootstrap documentation, Flask-WTF documentation |

| Manuelle Prüfung des Anfrage-Flows und der Statusänderungen | Lokale Browser-Tests und Datenbankabfragen während der Entwicklung | Python documentation, Flask documentation, SQLAlchemy documentation |


---

## AI Directory


| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01 | ChatGPT | Erklärung des Git- und GitHub-Workflows | Lokaler Git-Workflow, Branches, Commits, Push-, Pull- und Merge-Vorgänge sowie Pull Requests | Ich bat um Erklärungen zu Befehlen wie `git status`, `git add`, `git commit`, `git push`, `git pull`, `git switch`, `git restore` und `git merge`. Alle Befehle wurden von mir manuell ausgeführt. |
| 02 | ChatGPT | Unterstützung bei der Datenbankbereinigung | Entfernung veralteter SQL-Dateien und zugehörige Dokumentation | ChatGPT half mir zu verstehen, welche alten SQL-Dateien nach der Umstellung des Projekts auf SQLAlchemy nicht mehr benötigt wurden. Ich prüfte und entfernte die Dateien manuell. |
| 03 | ChatGPT | Unterstützung beim Verständnis von SQLite und SQLAlchemy | Datenbankarchitektur und Datenmodelldokumentation | ChatGPT erklärte den Unterschied zwischen SQLite als Datenbanksystem und SQLAlchemy als Object-Relational Mapper. Außerdem half es bei der Strukturierung der Dokumentation von Tabellen und Beziehungen. |
| 04 | ChatGPT | Implementierungs- und Lernunterstützung für das rollenabhängige Dashboard | `app.py`, `templates/dashboard.html` und Dashboard-Dokumentation | ChatGPT erklärte rollenabhängige Abfragen, die Routenlogik, Jinja-Bedingungen und die Übergabe von Daten aus einer Flask-Route an ein Template. Ich implementierte und testete die Änderungen manuell. |
| 05 | ChatGPT | Implementierungs- und Lernunterstützung für den Erstellungsprozess von Betreuungsanfragen | `app.py`, `forms.py`, Anfrage-Template und Dokumentation des Anfrage-Flows | ChatGPT half bei der Strukturierung des Ablaufs aus Anzeige des Formulars, Validierung der Eingaben, Erstellung eines SQLAlchemy-Objekts und Speicherung über die Datenbank-Session. |
| 06 | ChatGPT | Unterstützung bei den Seed-Daten für Studiengänge | `seed_data.py` | ChatGPT erklärte, wie Seed-Daten eingefügt werden können, ohne unnötige doppelte Einträge zu erzeugen. Die ausgewählten Studiengänge und die endgültigen Daten wurden von mir manuell geprüft. |
| 07 | ChatGPT | Unterstützung bei SQLAlchemy-Beziehungen | `db.py`, Beziehung zwischen `StudentProfile` und `DegreeProgram` | ChatGPT erklärte Fremdschlüssel, Beziehungen und den Zugriff auf verknüpfte Daten über SQLAlchemy-Modelle. |
| 08 | ChatGPT | Unterstützung beim Studiengang-Dropdown | Formular, Route und Template des Studentenprofils | ChatGPT half bei der Erklärung eines WTForms-`SelectField`, der Umwandlung in Integer-Werte mit `coerce=int` und der Übertragung von Datenbankeinträgen in die Dropdown-Auswahl. |
| 09 | ChatGPT | Unterstützung beim Annehmen und Ablehnen von Anfragen | `app.py`, `forms.py`, `templates/dashboard.html` | ChatGPT half bei der Strukturierung der POST-Route, der Rollenprüfung, der Prüfung der Zuordnung zur angefragten Person und der Validierung, dass nur Anfragen mit dem Status `submitted` bearbeitet werden können. |
| 10 | ChatGPT | Unterstützung bei CSRF-geschützten Statusformularen | `RequestStatusForm` und `templates/dashboard.html` | ChatGPT erklärte, warum jede Statusänderung über ein POST-Formular mit `hidden_tag()` und `validate_on_submit()` erfolgen sollte. |
| 11 | ChatGPT | Unterstützung bei der Statushistorie | `RequestStatusHistory` und Route zur Statusänderung | ChatGPT half bei der Erklärung, wie der alte Status, der neue Status und der bearbeitende Benutzer als eigener Historieneintrag innerhalb derselben Datenbanktransaktion gespeichert werden können. |
| 12 | ChatGPT | Debugging-Unterstützung | Python-Importtests, Syntaxfehler, Fehler beim Formularimport und Git-Diff-Prüfungen | ChatGPT half bei der Interpretation von Fehlermeldungen und schlug einzelne Diagnosebefehle vor. Ich führte jeden Befehl manuell aus und korrigierte die betroffenen Dateien selbst. |
| 13 | ChatGPT | Unterstützung beim Testen | Browser-Tests, Statustests und direkte Datenbankabfragen | ChatGPT schlug Testabläufe für das Erstellen, Annehmen und Ablehnen von Anfragen sowie für die Prüfung der daraus resultierenden Datenbankeinträge vor. |
| 14 | ChatGPT | Unterstützung bei der Dokumentation | Persönliche Contribution-Seite, Contribution-Tabelle, Quellenliste und AI Directory | ChatGPT half bei der Strukturierung dieses Dokuments auf Grundlage meiner tatsächlichen Git-Commits und implementierten Projektfunktionen. Ich prüfte und überarbeitete den Text manuell vor dem Commit. |



### Details of the AI-supported workflow

Für KI-unterstützte Aufgaben bin ich grundsätzlich nach folgendem Vorgehen vorgegangen:

Ich beschrieb den aktuellen Projektstand, das Implementierungsziel oder eine konkrete Fehlermeldung.
ChatGPT erklärte das relevante technische Konzept oder schlug einzelne Umsetzungsschritte vor.
Ich öffnete und bearbeitete die betroffenen Dateien manuell.
Ich überprüfte die Änderungen mit Git-Befehlen wie git diff, git diff --check und git status.
Ich importierte oder startete die Flask-Anwendung lokal.
Ich testete die betroffenen Funktionen im Browser.
Falls erforderlich, fragte ich die SQLite-Datenbank mithilfe von SQLAlchemy direkt ab.
Ich überprüfte die endgültigen Änderungen, bevor ich einen Commit erstellte.
Ich pushte den Branch und erstellte den Pull Request manuell.

ChatGPT führte keine Änderungen am Repository, Terminalbefehle, Commits, Push-Vorgänge oder Merge-Vorgänge selbstständig aus. Ich blieb für die Prüfung, das Testen und die Dokumentation sämtlicher endgültiger Projektinhalte verantwortlich.