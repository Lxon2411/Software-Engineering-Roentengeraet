# Softwarearchitektur Sprint 2

Architekturtyp: **Schichten-/Komponentenarchitektur** mit Trennung von Logik, Steuerung und GUI

## Komponentendiagramm

![Architekturdiagramm](./../images/Architektur_Komponentendiagramm.png)

## Hauptkomponenten

1. **GUI-Schicht (Tkinter UI)**
   - Darstellung und Benutzerinteraktion
   - Eingabefeld: Strahlungsdauer (1-120 Sekunden)
   - Anzeigen: Fortschrittsbalken, Fortschritt in Prozent, vergangene Strahlungsdauer
   - Buttons: Start/Stop (dynamisch wechselnd)
   - Status-LED-Widget: Visuelles Feedback (grün/rot)

2. **Steuerungs-/Logik-Schicht (Controller)**
   - Überwacht Strahlungsdauer und Ablauf mittels Threading
   - Verwaltet Abbruch-Status (Abort-Flag)
   - Kommuniziert mit GUI und aktualisiert Fortschritt
   - Koordiniert Start/Stop und Beendigung
   - Lädt Radiation in separatem Thread für UI-Responsivität

3. **System-/Hardware-Abstraktions-Schicht**
   - **StatusLED-Komponente:** Visuelles Status-Widget (grün=aktiv, rot=inaktiv)
   - **Systemschicht:** Verwaltung von Countdown, Zeitablauf und Signaltönen

## Traceability-Matrix

[Traceability-Matrix](./Traceability-Matrix.md)

## Verantwortlichkeiten der Komponenten

| **Komponente**     | **Rolle**                        | Verantwortlichkeiten                                                                                                                                                                                                                      |
|--------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUI (RadiationUI)  | Präsentationsschicht             | - Anzeige des Fortschrittsbalkens, Fortschritt in Prozent und vergangener Zeit <br/> - Interaktion mit dem Benutzer (Eingabe Strahlungsdauer, Start/Stop) <br/> - Übergabe von Benutzerbefehlen an Steuerungslogik <br/> - Reset der UI nach Beendigung <br/> - Button-State Management (Start/Stop) |
| Controller         | Anwendungsschicht/Business-Logik | - Steuerung des Strahlungsprozesses in separatem Thread <br/> - Verwaltung des Abort-Status (Abbruch-Flag) <br/> - Überprüfung der Eingaben (Validierung: 1-MAX_DURATION) <br/> - Berechnung verstrichener Zeit und Fortschritt <br/> - Unterscheidung zwischen normaler Beendigung und Abbruch |
| StatusLED          | UI-Komponente/Status-Widget     | - Visuelle Darstellung des Strahlungs-Status <br/> - Farbwechsel grün (aktiv) ↔ rot (inaktiv) <br/> - Canvas-basierte Implementierung                                                                                                    |
| Systemschicht      | Technische Integrationsschicht   | - Simulation der Strahlung mittels `time.time()` <br/> - Zugriff auf OS-/Hardwarefunktionen (z.B. Tonwiedergabe via `winsound.Beep()`) <br/> - Threading für nebenläufige Ausführung <br/> - Ausgabe von Meldungsdialogen via `messagebox` |

## Schnittstellen zwischen den Komponenten

| **Von**    | **An**       | **Beschreibung**                                              | Schnittstelle                                        |
|------------|--------------|---------------------------------------------------------------|------------------------------------------------------|
| GUI        | Controller   | Liefert die eingegebene Strahlungsdauer (int)                 | `RadiationController.start(duration: int)`           |
| GUI        | Controller   | Triggert Abbruch der Strahlung                                | `RadiationController.stop()`                         |
| Controller | GUI          | Aktualisiert Fortschrittsbalken, Prozent und vergangene Zeit  | `RadiationUI.update_progress(value, max_value)`     |
| Controller | GUI          | Zeigt Abschluss-Messagebox an (erfolgreiche Beendigung)       | `RadiationUI.show_finished_message(duration)`        |
| Controller | GUI          | Zeigt Abbruch-Messagebox an (Benutzer-Abort)                  | `RadiationUI.show_abort_message(elapsed)`            |
| Controller | GUI          | Setzt UI auf Initialzustand zurück                            | `RadiationUI.reset_ui()`                             |
| GUI        | StatusLED    | Setzt LED auf aktiv (grün)                                    | `StatusLED.set_active()`                             |
| GUI        | StatusLED    | Setzt LED auf inaktiv (rot)                                   | `StatusLED.set_inactive()`                           |
| Controller | System       | Erzeugt akustischen Signalton (Frequenz, Dauer)               | `winsound.Beep(frequenz: int, dauer: int)`           |
| Controller | System       | Liest aktuelle Systemzeit für Zeitberechnung                  | `time.time()`                                        |

## Technologiestack

| **Kategorie**            | **Technologie/Tool**                                                            | Begründung                                                                                                                                            |
|--------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sprache                  | Python 3.11                                                                    | Modern & persönliche Erfahrung                                                                                                                       |
| Buildsystem              | -                                                                              | Kein Buildsystem notwendig                                                                                                                           |
| Versionskontrolle        | Git & GitHub                                                                   | Standard                                                                                                                                              |
| IDE                      | PyCharm                                                                        | Standard Python-IDE, kompatibel für Doku in .md                                                                                                      |
| Ausgabe/GUI              | Tkinter (Standardbibliothek)                                                   | Plattformunabhängiges GUI-Toolkit, bereits in Python integriert                                                                                      |
| Dokumentation            | Markdown                                                                       | Standard, IDE-Integration                                                                                                                            |
| Codeanalyse              | flake8, pylint, mypy, SonarQube                                                | Statische Codeanalyse für Syntax- und Stilprüfungen sowie Typprüfung                                                                                 |
| Test-Framework           | pytest                                                                         | Python-Testframework für Unit- & Integrationstests                                                                                                   |
| Frameworks, Bibliotheken | Tkinter, `threading`, `time`, `winsound`, `tkinter.ttk`, `tkinter.Canvas`, `messagebox` | Python-Standardbibliotheken zur Implementierung von UI, nebenläufiger Verarbeitung, Status-Visualisierung und Systeminteraktionen                  |
| Paketverwaltung          | pip/venv                                                                       | Verwalten externer Abhängigkeiten & virtuelle Entwicklungsumgebung                                                                                   |

## Implementierungsdetails Sprint 2

### Neue Features

#### 1. Stop/Abort-Funktionalität

**Abort-Flag-Pattern:**
```python
def start(self, duration):
    self.running = True
    self.aborted = False  # Reset abort flag
    # Thread starten...

def stop(self):
    if self.running:
        self.aborted = True  # Abort-Flag setzen
    self.running = False
```

**Unterscheidung zwischen Normal- und Abbruch-Beendigung:**
```python
if not self.aborted:
    self.ui.show_finished_message(duration)  # Normales Ende
else:
    self.ui.show_abort_message(elapsed)       # Benutzer-Abort
```

**Vorteile:**
- Gaubfrei Unterscheidung zwischen Beendigung und Abbruch
- Unterschiedliche Fehlertöne (400Hz vs. 250Hz)
- Unterschiedliche Meldungen für Benutzer

#### 2. Start/Stop Button Toggle

**Dynamischer Button-Zustand:**
```python
def start_radiation(self):
    # ... Validierung ...
    self.controller.start(duration)
    self.startButton.config(
        text="Stop",
        bg="red",
        command=self.stop_radiation
    )
    self.status_led.set_active()

def stop_radiation(self):
    self.controller.stop()
```

**Reset auf Start-Button:**
```python
def reset_ui(self):
    self.startButton.config(
        text="Start",
        bg="green",
        command=self.start_radiation
    )
```

**Vorteile:**
- Intuitive UI (Nutzer sieht aktuellen Zustand)
- Verhindert parallele Ausführungen
- Visuelles Feedback für aktiven Prozess

#### 3. Status-LED Component

**Separate StatusLED-Klasse:**
```python
class StatusLED:
    def __init__(self, root):
        self.status_canvas = tk.Canvas(self.inner_frame, width=20, height=20, highlightthickness=0)
        self.status_circle = self.status_canvas.create_oval(2, 2, 18, 18, fill="red")

    def set_active(self):
        self.status_canvas.itemconfig(self.status_circle, fill="green")

    def set_inactive(self):
        self.status_canvas.itemconfig(self.status_circle, fill="red")
```

**Vorteile:**
- Modulares Widget-Design (wiederverwendbar)
- Klare visuelle Indikation des Status
- Canvas-basiert für einfache Skalierbarkeit

#### 4. Vergangene Strahlungsdauer Anzeige

**Echtzeit-Zeitupdates:**
```python
self.elapsedTime_label = tk.Label(root, font=("Arial", 10), 
                                   text=f"Vergangene Strahlungsdauer: ")
self.elapsedTime_label.pack(pady=(2, 0))

# In update_progress:
self.elapsedTime_label.config(text=f"Vergangene Strahlungsdauer: {value:.1f} s")
```

**Vorteile:**
- Besseres User Experience
- Echtzeit-Feedback über verstrichene Zeit
- Hilft bei Abbruchdaten-Tracking

### Threading-Modell (Erweitert)

Der Controller nutzt Python `threading` um die Strahlungssimulation in einem Daemon-Thread auszuführen:

```python
self.thread = threading.Thread(
    target=self._run_radiation, 
    args=(duration,), 
    daemon=True
)
self.thread.start()
```

**Abort-Handling in Thread:**
```python
while self.running:
    elapsed = time.time() - start_time
    if elapsed >= duration:
        break
    self.ui.update_progress(elapsed, duration)
    time.sleep(0.02)

if not self.aborted:  # Normales Ende
    # ...
else:  # Benutzer hat Stop gedrückt
    # ...
```

### Kommunikationsfluss (Erweitert)

**Normales Szenario:**
1. **Benutzer-Input:** Strahlungsdauer eingeben → Start-Button klicken
2. **Validierung:** Controller prüft `1 <= duration <= MAX_DURATION`
3. **UI-Update:** Button wechselt zu "Stop" (rot), LED wird grün
4. **Thread-Start:** `_run_radiation()` wird in separatem Thread gestartet
5. **Echtzeit-Updates:** Alle 20ms wird Fortschritt berechnet und UI aktualisiert
6. **Beendigung:** Nach Erreichen der Dauer wird Signalton (400Hz) abgespielt und Erfolgs-Messagebox angezeigt
7. **Reset:** UI wird in Initialzustand zurückgesetzt (Button "Start" grün, LED rot)

**Abbruch-Szenario:**
1. **Benutzer-Action:** Während der Strahlung "Stop"-Button klicken
2. **Abort-Flag:** `controller.stop()` setzt `self.aborted = True` und `self.running = False`
3. **Thread-Exit:** While-Schleife bricht ab
4. **Differenzierung:** `if not self.aborted` evaluiert zu False
5. **Abbruch-Message:** Warnsignalton (250Hz, 300ms) + Abbruch-Messagebox mit verstrichener Zeit
6. **Reset:** UI wird in Initialzustand zurückgesetzt

