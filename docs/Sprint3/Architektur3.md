# Softwarearchitektur Sprint 3

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
   - **Neue:** Logs-Widget mit ScrolledText und Export-Button

2. **Steuerungs-/Logik-Schicht (Controller)**
   - Überwacht Strahlungsdauer und Ablauf mittels Threading
   - Verwaltet Abbruch-Status (Abort-Flag)
   - Kommuniziert mit GUI und aktualisiert Fortschritt
   - **Neue:** Logging von Start-, Stop- und Abbruchereignissen
   - Koordiniert Start/Stop und Beendigung
   - Lädt Radiation in separatem Thread für UI-Responsivität

3. **System-/Hardware-Abstraktions-Schicht**
   - **StatusLED-Komponente:** Visuelles Status-Widget (grün=aktiv, rot=inaktiv)
   - **Logging-System:** Strukturiertes Event-Logging mit Timestamps
   - **File-Export:** Persistierung von Logs in UTF-8 Textdateien
   - **Systemschicht:** Verwaltung von Countdown, Zeitablauf und Signaltönen

## Traceability-Matrix

[Traceability-Matrix](./Traceability-Matrix.md)

## Verantwortlichkeiten der Komponenten

| **Komponente**     | **Rolle**                        | Verantwortlichkeiten                                                                                                                                                                                                                      |
|--------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUI (RadiationUI)  | Präsentationsschicht             | - Anzeige des Fortschrittsbalkens, Fortschritt in Prozent und vergangener Zeit <br/> - Interaktion mit dem Benutzer (Eingabe Strahlungsdauer, Start/Stop) <br/> - Übergabe von Benutzerbefehlen an Steuerungslogik <br/> - Reset der UI nach Beendigung <br/> - Button-State Management (Start/Stop) <br/> - **Neu:** Logging und Log-Verwaltung |
| Controller         | Anwendungsschicht/Business-Logik | - Steuerung des Strahlungsprozesses in separatem Thread <br/> - Verwaltung des Abort-Status (Abbruch-Flag) <br/> - Überprüfung der Eingaben (Validierung: 1-MAX_DURATION) <br/> - Berechnung verstrichener Zeit und Fortschritt <br/> - Unterscheidung zwischen normaler Beendigung und Abbruch <br/> - **Neu:** Event-Logging bei Start/Stop/Abort |
| StatusLED          | UI-Komponente/Status-Widget     | - Visuelle Darstellung des Strahlungs-Status <br/> - Farbwechsel grün (aktiv) ↔ rot (inaktiv) <br/> - Canvas-basierte Implementierung                                                                                                    |
| Logging-System     | Daten-Persistierungs-Layer       | - **Neu:** Erfassung von Strahlungsereignissen mit Timestamp <br/> - Formatierung von Log-Meldungen (Timestamp + Nachricht) <br/> - Speicherung im ScrolledText-Widget <br/> - Bereitstellung von Logs für Export                          |
| Systemschicht      | Technische Integrationsschicht   | - Simulation der Strahlung mittels `time.time()` <br/> - Zugriff auf OS-/Hardwarefunktionen (z.B. Tonwiedergabe via `winsound.Beep()`) <br/> - **Neu:** Datei-I/O für Log-Export (`filedialog`, `open()`) <br/> - Threading für nebenläufige Ausführung <br/> - Ausgabe von Meldungsdialogen via `messagebox` |

## Schnittstellen zwischen den Komponenten

| **Von**    | **An**       | **Beschreibung**                                              | Schnittstelle                                        |
|------------|--------------|---------------------------------------------------------------|------------------------------------------------------|
| GUI        | Controller   | Liefert die eingegebene Strahlungsdauer (int)                 | `RadiationController.start(duration: int)`           |
| GUI        | Controller   | Triggert Abbruch der Strahlung                                | `RadiationController.stop()`                         |
| Controller | GUI          | Aktualisiert Fortschrittsbalken, Prozent und vergangene Zeit  | `RadiationUI.update_progress(value, max_value)`     |
| Controller | GUI          | Zeigt Abschluss-Messagebox an (erfolgreiche Beendigung)       | `RadiationUI.show_finished_message(duration)`        |
| Controller | GUI          | Zeigt Abbruch-Messagebox an (Benutzer-Abort)                  | `RadiationUI.show_abort_message(elapsed)`            |
| Controller | GUI          | Setzt UI auf Initialzustand zurück                            | `RadiationUI.reset_ui()`                             |
| **Neu** Controller | **Neu** GUI | Erzeugt Log-Eintrag mit Timestamp                             | `RadiationUI.log_message(msg: str)`                  |
| GUI        | StatusLED    | Setzt LED auf aktiv (grün)                                    | `StatusLED.set_active()`                             |
| GUI        | StatusLED    | Setzt LED auf inaktiv (rot)                                   | `StatusLED.set_inactive()`                           |
| **Neu** GUI | **Neu** File-I/O | Öffnet Save-Dialog und exportiert Logs                      | `filedialog.asksaveasfilename()`, `open(file, 'w')`  |
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
| Frameworks, Bibliotheken | Tkinter, `threading`, `time`, `winsound`, `tkinter.ttk`, `tkinter.Canvas`, `scrolledtext`, `filedialog`, `datetime`, `messagebox` | Python-Standardbibliotheken zur Implementierung von UI, nebenläufiger Verarbeitung, Status-Visualisierung, Logging und Datei-Export |
| Paketverwaltung          | pip/venv                                                                       | Verwalten externer Abhängigkeiten & virtuelle Entwicklungsumgebung                                                                                   |

## Implementierungsdetails Sprint 3

### Neue Features

#### 1. Logging-System

**Log-Message-Format:**
```python
def log_message(self, msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"• [{timestamp}] {msg}"
    self.log_widget.config(state="normal")
    self.log_widget.insert("end", line + "\n")
    self.log_widget.see("end")
    self.log_widget.config(state="disabled")
```

**Format:** `• [YYYY-MM-DD HH:MM:SS] Meldung`

**Logged Events (Controller):**
- `"Strahlung gestartet für X s"` - Start-Event mit Dauer
- `"Strahlung automatisch beendet nach X.X s"` - Normale Beendigung
- `"Strahlung abgebrochen nach X.X s"` - Benutzer-Abort

**Vorteile:**
- Strukturierte Event-Erfassung mit ISO-8601 Timestamps
- Persistente Aufzeichnung aller Strahlungsvorgänge
- Basis für Audit-Trail und Fehlerdiagnose
- ScrolledText-Widget mit Auto-Scroll (`.see("end")`)
- Read-only Widget schützt vor Benutzereingaben

#### 2. Log-Export-Funktion

**Export-Dialog mit Zeitstempel:**
```python
def export_logs(self):
    logs = self.log_widget.get("1.0", "end").strip()
    if not logs:
        messagebox.showinfo("Logs exportieren", "Keine Log-Einträge vorhanden.")
        return

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    default_name = f"RGS-Logs-{ts}.txt"
    file_path = filedialog.asksaveasfilename(
        title="Logs exportieren",
        initialfile=default_name,
        defaultextension=".txt",
        filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")]
    )
```

**Export-Header:**
```
Röntgengerät Simulator - Protokoll erstellt am YYYY-MM-DD HH:MM:SS

• [YYYY-MM-DD HH:MM:SS] Log-Eintrag 1
• [YYYY-MM-DD HH:MM:SS] Log-Eintrag 2
...
```

**Fehlerbehandlung:**
```python
try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Röntgengerät Simulator - Protokoll erstellt am {timestamp}\n\n")
        f.write(logs + "\n")
    messagebox.showinfo("Logs exportieren", f"Logs wurden erfolgreich nach\n{file_path}\nexportiert.")
except OSError as e:
    messagebox.showerror("Fehler beim Exportieren", f"Die Logs konnten nicht gespeichert werden:\n[{e}")
```

**Vorteile:**
- UTF-8 Encoding für internationale Zeichensätze
- Automatische Dateinamenvergabe mit Zeitstempel (RGS-Logs-20260107-150730.txt)
- Flexible Datei-Dialog-Integration mit Filter
- Benutzerfreundliche Fehlerbehandlung mit Fehlerdialog
- Bestätigung bei erfolgreichem Export

#### 3. ScrolledText Logging Widget

**Widget-Konfiguration:**
```python
self.log_widget = scrolledtext.ScrolledText(
    log_frame,
    height=8,
    state="disabled",
    wrap="word"
)
self.log_widget.pack(fill="both", expand=True, padx=5, pady=5)
```

**Eigenschaften:**
- **height=8:** 8 Zeilen Höhe (angepassbar)
- **state="disabled":** Schreibschutz für Benutzer
- **wrap="word":** Zeilenumbruch bei Wortgrenzen
- **Scrollbar:** Automatisch integriert
- **Expandierbar:** Füllt verfügbaren Platz

**Vorteile:**
- Lesbare Log-Anzeige mit automatischem Scrollen
- Compact Widget-Design
- Benutzerfreundlich (Kopieren möglich, Editieren nicht)

#### 4. Enhanced Resource Loading

**Robuste Ressourcen-Pfad-Handling:**
```python
def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS  # PyInstaller Bundle
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# Verwendung:
icon_path = resource_path("icon.png")
try:
    icon = PhotoImage(file=icon_path)
    root.iconphoto(False, icon)
except Exception as e:
    print(f"Icon konnte nicht geladen werden: {e}")
```

**Verbesserungen:**
- **PyInstaller-Kompatibilität:** Unterstützt Bundle-Pfade (`_MEIPASS`)
- **Fallback-Logik:** Nutzt Skript-Verzeichnis als Fallback
- **Fehlertoleranz:** Exception-Handling verhindert App-Crash bei fehlender Icon-Datei
- **Logging:** Benutzer wird informiert, wenn Icon nicht geladen werden kann

#### 5. Project Root Path Management

**Dynamisches Sys-Path-Handling:**
```python
def main():
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
```

**Zweck:**
- **Flexibles Import-System:** Module aus beliebigem Verzeichnis importierbar
- **IDE & CLI Kompatibilität:** Funktioniert in PyCharm und via Terminal
- **Relative Imports:** `from src.gui.ui import RadiationUI` funktioniert überall

### Threading-Modell (Erweitert mit Logging)

```python
def start(self, duration):
    self.running = True
    self.aborted = False
    self.thread = threading.Thread(target=self._run_radiation, args=(duration,), daemon=True)
    self.thread.start()
    self.ui.log_message(f"Strahlung gestartet für {duration} s")  # NEW

def _run_radiation(self, duration):
    # ... Laufzeitlogik ...
    if not self.aborted:
        self.ui.log_message(f"Strahlung automatisch beendet nach {elapsed:.1f} s")  # NEW
    else:
        self.ui.log_message(f"Strahlung abgebrochen nach {elapsed:.1f} s")  # NEW
```

### Kommunikationsfluss (Erweitert mit Logging)

**Normales Szenario mit Logging:**
1. **Benutzer-Input:** Strahlungsdauer eingeben → Start-Button klicken
2. **Validierung:** Controller prüft `1 <= duration <= MAX_DURATION`
3. **Log-Eintrag:** `log_message("Strahlung gestartet für X s")`
4. **UI-Update:** Button wechselt zu "Stop" (rot), LED wird grün
5. **Thread-Start:** `_run_radiation()` wird in separatem Thread gestartet
6. **Echtzeit-Updates:** Alle 20ms wird Fortschritt berechnet und UI aktualisiert
7. **Beendigung:** Nach Erreichen der Dauer:
   - Log-Eintrag: `log_message("Strahlung automatisch beendet nach X.X s")`
   - Signalton (400Hz) abgespielt
   - Erfolgs-Messagebox angezeigt
8. **Reset:** UI wird in Initialzustand zurückgesetzt

**Abbruch-Szenario mit Logging:**
1. **Benutzer-Action:** Während der Strahlung "Stop"-Button klicken
2. **Abort-Flag:** `controller.stop()` setzt `self.aborted = True`
3. **Thread-Exit:** While-Schleife bricht ab
4. **Log-Eintrag:** `log_message("Strahlung abgebrochen nach X.X s")`
5. **Abbruch-Message:** Warnsignalton (250Hz) + Abbruch-Messagebox
6. **Reset:** UI wird in Initialzustand zurückgesetzt

**Export-Szenario (neu):**
1. **Benutzer-Action:** "Logs exportieren"-Button klicken
2. **Dialog:** Save-Dialog mit Default-Dateinamen (`RGS-Logs-YYYYMMDD-HHMMSS.txt`)
3. **Datei-I/O:** Logs werden in UTF-8 Textdatei geschrieben
4. **Bestätigung:** Success-Messagebox mit Dateipfad oder Error-Dialog


## Log-Beispiel (Sprint 3)

```
Röntgengerät Simulator - Protokoll erstellt am 2026-01-07 15:07:30

• [2026-01-07 15:07:32] Strahlung gestartet für 10 s
• [2026-01-07 15:07:42] Strahlung automatisch beendet nach 10.0 s
• [2026-01-07 15:07:50] Strahlung gestartet für 5 s
• [2026-01-07 15:07:53] Strahlung abgebrochen nach 3.1 s
```

