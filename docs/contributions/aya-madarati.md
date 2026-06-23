---
title: Aya Madarati
parent: Individual Contributions
nav_order: 1
---

{: .attention }
> Create a separate, individual file for every team member, proposed naming scheme: `📄firstname-lastname.md`.
>
> *Find and replace* (VS Code: <kbd>Ctrl</kbd>+<kbd>H</kbd> / <kbd>⌘</kbd>+<kbd>H</kbd>) `Jane Dane` with the student's name. On this template page, you will find this name 4 times (including in this `attention` box). 
>
> You may delete this `attention` box.

{: .no_toc }
# Jane Dane

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

Meine Zielnote für dieses Modul ist 1,0.

### Personal goals

Ich möchte verstehen wie eine Web-Applikation von der Idee bis zur Umsetzung entsteht. Konkret will ich Python, Flask, SQLite und Jinja2 praktisch anwenden und lernen wie man ein Nutzerproblem analysiert und daraus eine sinnvolle App-Lösung entwickelt.

---

## Eidesstattliche Erklärung: 

**[Aya Madarati, Matrikelnr.: 77204158016]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Implementierung des Professor-Feeds: Suche, Filterlogik (Facheinheit, Verfügbarkeit) und Anbindung an die Datenbank | Der Feed funktioniert vollständig dynamisch mit Live-Daten aus der Datenbank statt Platzhaltern | Verstehen wie man mehrere Filterkriterien gleichzeitig korrekt kombiniert |
| 2 | Implementierung der Profil-Detailseite inkl. bedingter Darstellung (ausgegraut, deaktivierter Button) je nach Verfügbarkeitsstatus | Die Seite verknüpft mehrere zusammenhängende Datenbanktabellen korrekt in einer übersichtlichen Ansicht und gibt Studierenden sofort sichtbares Feedback zur Verfügbarkeit | Verstehen wie verknüpfte Datenbank-Beziehungen korrekt in Jinja2-Templates dargestellt werden |
| 3 | An der Value Proposition und den UI-Screens gearbeitet und in GitHub Pages dokumentiert | Jeder Screen ist nachvollziehbar aus einem konkreten Problem der Value Proposition abgeleitet | Die Inhalte mehrfach an neues Feedback angepasst, ohne den roten Faden zu verlieren |


## Design Decisions that I led

1. [DD #04](../design-decisions/dd-04.md)
2. [DD #05](../design-decisions/dd-05.md)
---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Professor-Feed: Grundstruktur, Suchfeld, Filterlogik (Facheinheit/Verfügbarkeit) implementiert | [Suchformular für Proffeed](https://github.com/petrovvvic/team2_thesis_match/commit/a6a96a313bd4ed9502efe4c521a95ffaeb69458c), [Selectfield in forms.py](https://github.com/petrovvvic/team2_thesis_match/commit/2e29d392d032c9f31fcefeed2eda3fda48f7c15c), [faculty + availibilty filter](https://github.com/petrovvvic/team2_thesis_match/commit/85e8db39e93c4b639e4eeb78d3144738da2979d3), [Filter Logik](https://github.com/petrovvvic/team2_thesis_match/commit/9384393720fde2cbddf21c357e5defb1de20853d), [nicht verfügbare Profs deaktivieren](https://github.com/petrovvvic/team2_thesis_match/commit/a32db9a0c51cd73e80d7d3281552dd44a673039d) | [WTForms Fields](https://wtforms.readthedocs.io/en/3.1.x/fields/), [user-interfaces.html](https://hwrberlin.github.io/fswd/user-interfaces.html) |
| Profil-Detailseite implementiert | [prof-profile.html](https://github.com/petrovvvic/team2_thesis_match/commit/b8a9d930fcf149e90f42f54bee6644f85c8624ee), [profile-detail.html](https://github.com/petrovvvic/team2_thesis_match/commit/b246742155de498b109d784a738f3f6b4ef90b4c), [profiledetail.html Update](https://github.com/petrovvvic/team2_thesis_match/commit/fc885cc55ae258d2288a1ef6f4b07e8e481c3086) |  |
| Datenbank-Anbindung von Feed und Profil-Detail (SQLAlchemy) | [DB Integration für Feed und profile-detail.html](https://github.com/petrovvvic/team2_thesis_match/commit/49d936a3644f4d42c86fa2b3eb886d199864776c), [DB Verbindung + Suchlogik](https://github.com/petrovvvic/team2_thesis_match/commit/4d3f8664af4db011114b48769419a7647febdec1), [db.py ziehen und aktualisieren](https://github.com/petrovvvic/team2_thesis_match/commit/49b65d622cd350ae1494069af861b83213bb0e2f), [db.py Update](https://github.com/petrovvvic/team2_thesis_match/commit/60c8ff386cc9c349f143dbe562403692f9b1cddb), [Korrekturen](https://github.com/petrovvvic/team2_thesis_match/commit/2110bfd6ad2745495d2849799eca1f9b61b00052) | [sqlalchemy.html](https://hwrberlin.github.io/fswd/sqlalchemy.html) |
| Datenmodell-Anpassung: Facheinheit-Ebene eingeführt (statt direkter Fachbereichs-Zuordnung), basierend auf Recherche zur echten HWR-Struktur und Feedback von Prof. Eck | [DB-Update (Facheinheiten)](https://github.com/petrovvvic/team2_thesis_match/commit/1aa711781106f1cd2707d7d7d1ab5d13be87c346), [DB-Update (Facheinheiten)](https://github.com/petrovvvic/team2_thesis_match/commit/ce879ce157d24e3bf3d303fac879b864527f6e7b), [DB-Relationsfixe (Facheinheit)](https://github.com/petrovvvic/team2_thesis_match/commit/8407c8a79c2227871fbdafd3ce098338aaf1b2c5), [Facheinheit forms.py + app.py](https://github.com/petrovvvic/team2_thesis_match/commit/022ac9a27269e4ad78672524261e093e369edb46), [db.py, app.py Fixes + Facheinheiten in HTMLs](https://github.com/petrovvvic/team2_thesis_match/commit/f7b029537e8f17eb942af6721a2861ca0074de5f) | [HWR Facheinheiten](https://www.hwr-berlin.de/hwr-berlin/fachbereiche-und-bps/fb-1-wirtschaftswissenschaften/organisation-und-verwaltung/professuren-lehrende-und-facheinheiten/) |
Stammdaten-Seed für Facheinheiten implementiert| [fix seed facheinheiten and UI](https://github.com/petrovvvic/team2_thesis_match/commit/25c5722) | [sqlalchemy.html, Abschnitt 6+8](https://hwrberlin.github.io/fswd/sqlalchemy.html) |
| Grundstruktur: Routen, Basis-Template, Navigation | [App Routen](https://github.com/petrovvvic/team2_thesis_match/commit/05f71ab04fcea20f0701c1ed9d855cee22035262), [Basis-HTML-Struktur](https://github.com/petrovvvic/team2_thesis_match/commit/26abbd9491fb1d9317042cf34eee9e63fb99a7e3), [Navigation in base.html](https://github.com/petrovvvic/team2_thesis_match/commit/0ab696d031dc93f43e4829937a35e45f820b0bcd) | [flask.html](https://hwrberlin.github.io/fswd/flask.html) |
| Value Proposition und UI-components erstellt und mehrfach überarbeitet | [Update 01-value-proposition.md](https://github.com/petrovvvic/team2_thesis_match/commit/b1ae67c4a0b8e5f271b723b4062dff1e552c76b3) (+ mehrere weitere Commits gleichen Namens) |   |
---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

## AI Directory

[You must maintain a comprehensive AI Directory, as per FB1 regulations on generative AI use. Any use of AI is documented precisely per task.]

## AI Directory

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | Perplexity AI  | Erklärung von Flask-Konzepten: Routen, `render_template`, GET vs. POST, `url_for` | `app.py` |  [Flask-Framework](https://hwrberlin.github.io/fswd/flask.html) als Grundlage genannt, Claude hat Konzepte erklärt.Gefragt, wie man in Python eine App-Route erstellt und zwischen den Seiten navigiert. |
| 02  | Claude (Anthropic, claude.ai) | Erklärung von WTForms-Feldern: `SearchField`, `SelectField`, `Optional` | `forms.py` | Gefragt: "Was macht SearchField und woher kommt es?" — Antwort auf Ecks Tutorial-Tabelle zurückgeführt. |
| 03  | Claude (Anthropic, claude.ai) | Erklärung von Jinja2-Konzepten: `{% for %}`, `{% if %}`, `{% extends %}`, `{% block %}` | `feed.html`, `profile-detail.html`, `base.html` | Gefragt wie Jinja2-Schleifen und Blöcke funktionieren. |
| 04  | Claude (Anthropic, claude.ai) | Debugging: Fehlermeldungen erklärt (`IndentationError`, `backref`-Konflikt, `NoForeignKeysError`) | `app.py`, `db.py` | Fehlermeldung eingefügt, Ursache erklärt bekommen. |
| 05  | Claude (Anthropic, claude.ai) | Erklärung von SQLAlchemy-Konzepten: `back_populates`, `db.session.execute`, `db.select` | `db.py`, `app.py` | Gefragt wie Datenbankbeziehungen in SQLAlchemy funktionieren — Grundlage für eigene Implementierung. |
| 06  | ChatGPT (OpenAI) | Unterstützung bei der Erklärung der HWR-Datenbankstruktur | `db.py` | Hilfe beim Verständnis der Struktur von HWR (Fachbereiche, Facheinheiten, Professoren, Studierende und Studiengänge) und deren Beziehungen im Datenbankmodell.|
| 07 | ChatGPT (OpenAI) | Formulierungshilfe und sprachliche Überarbeitung | Dokumentation | Unterstützung bei Grammatik, Rechtschreibung und besserer Formulierung.
| 08  | Claude (Anthropic, claude.ai) |Brainstorming und Ideenfindung für die App-Konzeption |  | Unterstützung beim Entwickeln und Bewerten von Ideen.
