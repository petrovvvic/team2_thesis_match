---
title: TL;DR
nav_order: 1
---

# TL;DR — Thesis Match

**Was:** Webplattform, die Bachelor-Studierende und Professor:innen der HWR (Fachbereich 1) für die Betreuung von Abschlussarbeiten zusammenbringt.

**Problem (belegt durch 2 Umfragen: Studierende n=10, Professor:innen n=5):** Studierende finden nur schwer eine fachlich passende, verfügbare Betreuung; Professor:innen erhalten unstrukturierte und unpassende Anfragen per E-Mail.

**Lösung:** Professor:innen machen ihr Betreuungsangebot sichtbar (Themenfelder, Verfügbarkeit); Studierende suchen gezielt, sehen die Verfügbarkeit vorab und stellen strukturierte Anfragen — inklusive Chat und PDF-Anhängen.

**Zielgruppe:** Studierende (primär) und Professor:innen (sekundär), HWR FB1.

## Kernablauf (Happy Path)

Registrierung/Login → Professor-Feed (Suche & Filter) → Profil-Detailseite → strukturierte Anfrage → „Meine Anfragen" bzw. Betreuer-Dashboard (annehmen/ablehnen) → Chat. Dazu: Top-Betreuer-Rangliste über eine JSON-API.

## Technik

Flask + Flask-SQLAlchemy + Bootstrap, SQLite. Bewusst **server-rendered, ohne JavaScript-Framework**.

## Schnellstart

```
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
flask --app app run
```
Browser: `http://127.0.0.1:5000` (macOS: `--port 5050`, da Port 5000 von AirPlay belegt ist).

## Wichtige Design-Entscheidungen

- **Chat ohne JavaScript** (server-rendered) — siehe [DD #00](design-decisions/dd-00.md)
- **PDF-Anhänge** als Datei im Upload-Ordner + Metadaten in der DB (kein BLOB) — siehe [DD #01](design-decisions/dd-01.md)
- **Kein Bewertungssystem für Professor:innen** — nach Feedback von Prof. Eck verworfen; die Rangliste wertet nur das Anfragevolumen aus.

## Wo stehen die Details?

- Value Proposition (inkl. Value Proposition Canvas): [Value Proposition](01-value-proposition.md)
- Product Discovery (Umfragen, Probleme, Lösungen, Tests): [Product Discovery](product-discovery/)
- Individuelle Beiträge & Eidesstattliche Erklärung: [Individual Contributions](contributions/)
