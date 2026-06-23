# team2_thesis_match
Dieses App verbindet Studierende und Dozenten, damit die besten Bachelorarbeiten geschrieben werden. Entwickelt von **Team 2.**


# Installation & lokales Starten

Voraussetzung: **Python 3** muss installiert sein. Komplette Einrichtung in unter 10 Minuten:

1. Repository klonen:
   ```
   git clone https://github.com/petrovvvic/team2_thesis_match.git
   ```
2. In den Projektordner wechseln:
   ```
   cd team2_thesis_match
   ```
3. Virtuelle Umgebung erstellen und aktivieren:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   (Windows: `venv\Scripts\activate`)
4. Abhängigkeiten installieren:
   ```
   pip install -r requirements.txt
   ```
5. App starten:
   ```
   flask --app app run
   ```
   Danach im Browser `http://127.0.0.1:5000` öffnen.
   (macOS: Port 5000 ist oft durch AirPlay belegt — dann `flask --app app run --port 5050` und `http://127.0.0.1:5050`.)

Die mitgelieferte Datenbank (`instance/thesis_match.sqlite`) enthält bereits Demo-Daten (u. a. 17 Professor:innen, Fachbereich, Facheinheiten, Studiengänge), sodass der Feed direkt befüllt ist.

**Optional – Referenzdaten neu befüllen** (falls die DB leer ist):
```
python seed_data.py        # Studiengänge (FB1)
```
Die Facheinheiten werden über `insert_sample()` in `db.py` gesetzt.

# Demo-Zugang

- **Professor:innen-Accounts:** Passwort `demo1234` (z. B. `anna.schneider@hwr-berlin.de`, `thomas.becker@hwr-berlin.de`).
- **Studierende:r:** am einfachsten selbst registrieren (ist Teil des Happy Path, s. u.).

# Happy Path (zum Durchklicken)

Reihenfolge, um den Kernprozess zu reproduzieren:

**A) Studierende:r sucht Betreuung**
1. **Registrieren** als „Studierende/r" → einloggen
2. **Professoren-Feed** öffnen, per Suche / Facheinheit / Verfügbarkeit filtern
3. **Profil-Detailseite** einer/eines Professor:in öffnen
4. **„Anfrage stellen"** → Formular ausfüllen (Thema, Zeitraum, Kurzbeschreibung) → absenden
5. **Dashboard / „Meine Anfragen"** → Status der Anfrage sehen

**B) Professor:in bearbeitet die Anfrage**
6. Als die/den angefragte:n **Professor:in einloggen** (Demo-Account, Passwort `demo1234`) → **Dashboard**
7. Anfrage **annehmen oder ablehnen** (Status ändert sich)
8. **Chat** zur Anfrage öffnen → Nachricht senden + optional **PDF anhängen**

# API — Top-Betreuer-Rangliste

JSON-API, die Professor:innen nach Anzahl der erhaltenen Betreuungsanfragen rankt.

- **Endpoint:** `GET /api/top-supervisors`
- **Optionaler Parameter:** `limit` (Standard `10`, max `100`)

Beispiele (im Browser oder via `curl`):
```
http://127.0.0.1:5050/api/top-supervisors
http://127.0.0.1:5050/api/top-supervisors?limit=5
```
