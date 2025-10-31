# Software-Engineering-Roentengeraet
Software Engineering Projekt (WS25)
von Leon Wühr

## Repository
[Github Repository](https://github.com/Lxon2411/Software-Engineering-Roentengeraet)

### Teilfunktionalitäten
1. **Benutzerdefinierte Eingabe der Strahlungsdauer**
2. **Starten der Strahlung**
3. **Automatisches Abschalten nach Ablauf der eingestellten Dauer**
4. **Manuelles Stoppen (z.B. im Falle eines Notfalls)**
5. **Status- und Fortschrittsanzeige**

## Gesamtdokumentation

## Benutzerhandbuch

## Installation & Ausführung
Es gibt zwei verschiedene Möglichkeiten, das Projekt zum Laufen zu bringen:

1. Schnelle & einfache Variante: Herunterladen und Ausführen der **.exe-Datei** aus dem ```dist-Ordner```
    [main.exe](./dist/main.exe)  
    **Voraussetzungen:**
      - Kein Python erforderlich
      - Keine zusätzlichen Abhängigkeiten nötig
      - Funktioniert nur unter **Windows**!  
      **Hinweis:** Je nach Windows-Systemeinstellung muss beim ersten Start der Hinweis *Die App wurde aus Sicherheitsgründen blockiert* mit *"Trotzdem ausführen"* bestätigt werden.
2. Alternative: Ausführung des Quellcodes
    ```cmd
    git clone https://github.com/Lxon2411/Software-Engineering-Roentengeraet.git
    cd Software-Engineering-Roentgengerät
    git checkout v1     # Wechsel zu lauffähiger Version nach Sprint 1 (Ausführen in src/Program)
    git checkout v2     # Wechsel zu lauffähiger Version nach Sprint 2 (Ausführen in src/Program)
    git checkout v3     # Wechsel zu lauffähiger Version nach Sprint 3 (Ausführen in src/Program)
    cd src
    python main.py
    ```
    **Voraussetzungen:**
    - **Python 3.11 oder höher** muss installiert sein
    - Folgende Bibliotheken werden benötigt: 
   ```cmd
   pip install -r requirements.txt
   ```
   - In der Python IDE (z.B. **PyCharm**) muss ein **Python-Interpreter** konfiguriert sein (*z.B. unter "File → Settings → Project → Python Interpreter")

