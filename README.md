# team2_thesis_match
Dieses App verbindet Studierende und Dozenten, damit die besten Bachelorarbeiten geschrieben werden. Entwickelt von **Team 2.**
# Installation & lokales Starten


# Installation & lokales Starten

Voraussetzung: **Python 3** muss installiert sein. Komplette Einrichtung in unter 10 Minuten.

1. Repository klonen:
```
   git clone https://github.com/petrovvvic/team2_thesis_match.git
```

2. In den Projektordner wechseln:
```
   cd team2_thesis_match
```

3. Virtuelle Umgebung erstellen und aktivieren:

   **macOS / Linux:**
```
   python3 -m venv venv
   source venv/bin/activate
```

   **Windows (PowerShell):**
```
   python -m venv venv
   venv\Scripts\Activate.ps1
```
   > Falls PowerShell die Aktivierung mit einer Fehlermeldung zur „Execution Policy" blockiert, einmalig ausführen:
   > ```
   > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   > ```

   **Windows (CMD / Eingabeaufforderung):**
```
   python -m venv venv
   venv\Scripts\activate.bat
```

4. Abhängigkeiten installieren (gilt für alle Systeme, venv muss aktiv sein):
```
   pip install -r requirements.txt
```

5. Konfiguration anlegen — `.env.example` zu `.env` kopieren und eigenen `SECRET_KEY` generieren:

   **macOS / Linux:**
```
   cp .env.example .env
   python -c "import secrets; print(secrets.token_hex(32))"
```

   **Windows (PowerShell & CMD):**
```
   copy .env.example .env
   python -c "import secrets; print(secrets.token_hex(32))"
```
   Den ausgegebenen Wert als `SECRET_KEY` in die `.env` eintragen.

6. **WICHTIG!!! – Datenbank befüllen** (vor dem Erststart ausführen, um die Demodaten zu bekommen; falls die DB leer ist, nach dem `.env`-Schritt):
```
   flask --app app seed
```
   Legt **Fachbereich, Facheinheiten, Studiengänge** und Demo-Accounts an. Mehrfaches Ausführen erzeugt keine Duplikate.

7. App starten:
```
   flask --app app run
```
   Danach im Browser `http://127.0.0.1:5000` öffnen.
   - **macOS:** Port 5000 ist oft durch AirPlay belegt — dann `flask --app app run --port 5050` und `http://127.0.0.1:5050` verwenden.
   - **Windows:** Port 5000 ist normalerweise frei, kein Extra-Schritt nötig.

# Demo-Zugang

- **Professor:innen-Accounts:** Passwort `demo1234` (z. B. `anna.schneider@hwr-berlin.de`, `thomas.becker@hwr-berlin.de`).
- **Studierende:r:** am einfachsten selbst registrieren (ist Teil des Happy Path, s. u. Sonst: max.mustermann@stud.hwr-berlin.de, Passwort `demo1234`).

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
