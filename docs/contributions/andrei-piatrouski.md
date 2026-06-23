---
title: Andrei Piatrouski
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Andrei Piatrouski

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1,0

### Personal goals

Besseres Verständnis von Full-Stack-Architekturen bzw. -Technologien und Verfeinerung der Project-Management-Skills.

---

## Eidesstattliche Erklärung

**Andrei Piatrouski, Matrikelnr.: 77206441960**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Chat zwischen Studierenden und Professor/innen inkl. PDF-Anhängen. | Ein im MVP voll nutzbarer Chat (zugrunde liegende Entscheidungen siehe DD #00 und #01). | Eine gute Chat-UX ohne JavaScript zu erreichen (Details in DD #00). |
| 2 | JSON-API für die Top-Betreuer-Rangliste (nach Anfragevolumen). | Liefert sauberes, sortiertes JSON mit konfigurierbarem Limit. | Korrekte Aggregation über SQLAlchemy (zählen, gruppieren, auch Professor/innen mit 0 Anfragen einbeziehen). |
| 3 | Versionskontroll-Workflow & Integration: PR-Management, Branch-Merges und Konfliktlösung. | Team-Beiträge sauber zusammengeführt und das Repository zusammengehalten. | Divergierende Branches und Merge-Konflikte (u. a. in `forms.py`) lösen, ohne Arbeit zu verlieren. |

## Design Decisions that I led

1. [DD #00 — Chat ohne JavaScript (server-rendered statt JS-Framework)](../design-decisions/dd-00.md)
2. [DD #01 — PDF-Anhänge: Datei im Upload-Ordner, Metadaten in der Datenbank](../design-decisions/dd-01.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Value Proposition, Target Scope, Happy Path & Wireframes (Produkt-Discovery) | [eea6080](https://github.com/petrovvvic/team2_thesis_match/commit/eea6080), [d5bb230](https://github.com/petrovvvic/team2_thesis_match/commit/d5bb230), [b51d6c4](https://github.com/petrovvvic/team2_thesis_match/commit/b51d6c4) | Nutzer Befragungen, Mom Test methodiken |
| Projekt-Setup: Umbau von Submodule auf reguläre Ordnerstruktur | [72613f0](https://github.com/petrovvvic/team2_thesis_match/commit/72613f0) | Git-Dokumentation |
| Chat / Nachrichtenverlauf zwischen Studi und Prof (server-rendered, ohne JS, Scroll-Box + Zeichenlimit) | [f066bcb](https://github.com/petrovvvic/team2_thesis_match/commit/f066bcb), [2eece0a](https://github.com/petrovvvic/team2_thesis_match/commit/2eece0a) | Flask-, Flask-WTF-, SQLAlchemy-Doku |
| PDF-Anhänge an Chat-Nachrichten (Datei im Upload-Ordner, Metadaten in DB) | [fb43b10](https://github.com/petrovvvic/team2_thesis_match/commit/fb43b10) | Flask-Doku (File Uploads, secure_filename) |
| Top-Betreuer JSON-API (Ranking nach Anfragevolumen) | [fb43b10](https://github.com/petrovvvic/team2_thesis_match/commit/fb43b10) | Flask-, SQLAlchemy-Doku |
| Facheinheit-Auswahl im Profil + DB-/Forms-/App-Fixes | [48ec18d](https://github.com/petrovvvic/team2_thesis_match/commit/48ec18d) | Flask-WTF-Doku |
| Versionskontroll-Workflow & Integration: Pull-Request-Management, Branch-Merging und Merge-Konfliktlösung | [PR #2](https://github.com/petrovvvic/team2_thesis_match/commit/880a274), [PR #3](https://github.com/petrovvvic/team2_thesis_match/commit/130f059), [PR #4](https://github.com/petrovvvic/team2_thesis_match/commit/f4c09a4), [PR #8](https://github.com/petrovvvic/team2_thesis_match/commit/9dff4cf), [PR #9](https://github.com/petrovvvic/team2_thesis_match/commit/95e3f7e), [47d9445](https://github.com/petrovvvic/team2_thesis_match/commit/47d9445) | Git-Doku |

---

## AI Directory

| #   | AI Tool | Verwendungszweck | Betroffene Bereiche (Code + Docs) | Anmerkungen, Vorgehen, Prompts |
| :-- | :--     | :--              | :--                               | :--                            |
| 01  | Claude (Anthropic) | Auflösung von Git-Merge-Konflikten in Pull Requests | `app.py`, `db.py`, `forms.py`, `.gitignore` | Schrittweise Begleitung durch VS Code's Merge-Editor zur Konfliktlösung auf `feature/prof-feed+profile-detail` → `main`. Zusätzlich wurde der versehentlich committete `venv/`-Ordner via `git rm -r --cached venv/` aus dem Git-Tracking entfernt. Vorgehen: sequentielles Prompting mit schrittweiser Ausführung und Screenshot-basierter Klärung. |
| 02  | Claude (Anthropic) | Formatierung und Korrektur fehlerhafter Markdown-Dateien | `README.md`, Dokumentations-`.md`-Dateien | Diagnose einer fehlerhaften Markdown-Tabelle (alles in einer Zeile, fehlende Trennzeile) und Bereitstellung der korrigierten Struktur. Prompt: Einfügen des kaputten Rohtexts mit Aufforderung zur Korrektur. |
| 03  | Claude (Anthropic) | HTML-Template-Boilerplates und UI-Container-Struktur | `templates/` (Jinja2 `.html`-Dateien) | Generierung von Lo-Fi-HTML-Wireframe-Gerüsten für zentrale Screens (Professor-Feed, Profil-Detailseite, Registrierungsflow) als strukturellen Ausgangspunkt für das Jinja2-Templating. Vorgehen: Beschreibung des Screen-Zwecks + Flask/kein-JS-Constraint → Boilerplate-Container-Struktur. |
| 04  | Claude (Anthropic) | Sparringspartner & Brainstorming für Chat-Logik und Backend-Architektur | `app.py`, `forms.py`, `templates/chat.html` | Iteratives Durchdenken der Chat-Implementierung: Datenbankmodellierung von Nachrichten, Routing-Logik, Session-Handling und Persistenz ohne WebSockets (Flask-konform). Vorgehen: Beschreibung des gewünschten Verhaltens → Diskussion von Architekturentscheidungen → Ableitung konkreter Implementierungsansätze. |
