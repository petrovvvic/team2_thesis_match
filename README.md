# team2_thesis_match
Dieses App verbindet Studierende und Dozenten, damit die besten Bachelorarbeiten geschrieben werden. Entwickelt von **Team 2.**

# Team Composition
Team: Andrei Piatrouski, Nikita Pasichnyk, Aya Madarati, Abdulhamid Suliman

| Student | Personal Goals | Target Grade |
|---------|---------------|--------------|
|Andrei   | Besseres Verständnis von Full Stack Architekturen bzw. Technologien und Verfeinerung der Project Management Skills | 1,0 |
|Nikita   | Verbesserung der eigenen Python-Skills sowie das Erstellen einer robusten und voll funktionsfähigen Web-Applikation  | 1,0 |
|Aya      | Verbesserung der Python Skills + Projekt Management Skills | 1,0 |
|Abdulhamid | Verbesserung der Python Skills + Projekt Management Skills | 1,0 |

# Instruktion

Voraussetzung: **Python 3** muss installiert sein.

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





# TODO
- api dokus am ende:   
- http://127.0.0.1:5050/api/top-supervisors
- http://127.0.0.1:5050/api/top-supervisors?limit=5
