1. Den neuesten Stand von Git holen
Navigiere in deinen Projektordner und hole dir den Branch Login/Reg+Profile-v1:


git fetch origin
git checkout Login/Reg+Profile-v1
#

2. Virtuelle Umgebung (venv) aktivieren
Auf dem Mac / Linux:

python3 -m venv venv
source venv/bin/activate
#

Auf Windows:

python -m venv venv
venv\\Scripts\\activate
#

3. Alle Abhängigkeiten mit einem Klick installieren

pip install -r requirements.txt
#

4. Den lokalen Server starten

flask run --port=5001
#
