# Softwarearchitektur

Architekturtyp: **Schichten-/Komponentenarchitektur** mit Trennung von Logik, Steuerung und GUI

## Komponentendiagramm

![Architekturdiagramm](./../images/Architektur_Komponentendiagramm.png)

## Hauptkomponenten

1. **GUI-Schicht (Tkinter UI)**
   - Darstellung und Benutzerinteraktion
   - Eingabefeld: Strahlungsdauer (1-120 Sekunden)
   - Anzeigen: Fortschrittsbalken, Fortschritt in Prozent
   - Buttons: Start (aktivierbar/deaktivierbar), Stop

2. **Steuerungs-/Logik-Schicht (Controller)**
   - Überwacht Strahlungsdauer und Ablauf mittels Threading
   - Kommuniziert mit GUI und aktualisiert Fortschritt
   - Steuert Start/Stop und koordiniert Beendigung
   - Lädt Radiation in separatem Thread für UI-Responsivität

3. **Systemschicht**
   - Verwaltet Countdown und Zeitablauf (`time.time()`)
   - Steuert Signaltöne (`winsound.Beep()`)
   - Fehlerbehandlung und Validierung der Eingaben

## Traceability-Matrix

[Traceability-Matrix](./Traceability-Matrix.md)

## Verantwortlichkeiten der Komponenten

| **Komponente**     | **Rolle**                        | Verantwortlichkeiten                                                                                                                                                                                                                      |
|--------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUI (RadiationUI)  | Präsentationsschicht             | - Anzeige des Fortschrittsbalkens und Fortschritts in Prozent <br/> - Interaktion mit dem Benutzer (Eingabe Strahlungsdauer) <br/> - Übergabe von Benutzerbefehlen an Steuerungslogik <br/> - Reset der UI nach Beendigung               |
| Controller         | Anwendungsschicht/Business-Logik | - Steuerung des Strahlungsprozesses in separatem Thread <br/> - Überprüfung der Eingaben (Validierung: 1-MAX_DURATION) <br/> - Berechnung verstrichener Zeit und Fortschritt <br/> - Verwaltung des Running-Status                        |
| Systemschicht      | Technische Integrationsschicht   | - Simulation der Strahlung mittels `time.time()` <br/> - Zugriff auf OS-/Hardwarefunktionen (z.B. Tonwiedergabe via `winsound.Beep()`) <br/> - Threading für nebenläufige Ausführung <br/> - Ausgabe von Meldungsdialogen via `messagebox` |

## Schnittstellen zwischen den Komponenten

| **Von**    | **An**       | **Beschreibung**                                        | Schnittstelle                                        |
|------------|--------------|--------------------------------------------------------|------------------------------------------------------|
| GUI        | Controller   | Liefert die eingegebene Strahlungsdauer (int)          | `RadiationController.start(duration: int)`           |
| Controller | GUI          | Aktualisiert Fortschrittsbalken und Prozentanzeige    | `RadiationUI.update_progress(value, max_value)`     |
| Controller | GUI          | Setzt Button auf deaktiviert während Strahlung läuft  | `tk.Button.config(state=tk.DISABLED)`                |
| Controller | GUI          | Setzt Button auf aktiviert nach Beendigung            | `tk.Button.config(state=tk.NORMAL)`                  |
| Controller | GUI          | Zeigt Abschluss-Messagebox an                          | `RadiationUI.show_finished_message(duration)`        |
| Controller | GUI          | Setzt UI auf Initialzustand zurück                     | `RadiationUI.reset_ui()`                             |
| Controller | System       | Erzeugt akustischen Signalton (Frequenz, Dauer)       | `winsound.Beep(frequenz: int, dauer: int)`           |
| Controller | System       | Liest aktuelle Systemzeit für Zeitberechnung          | `time.time()`                                        |

## Technologiestack

| **Kategorie**            | **Technologie/Tool**                                                    | Begründung                                                                                                                                            |
|--------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sprache                  | Python 3.11                                                             | Modern & persönliche Erfahrung                                                                                                                       |
| Buildsystem              | -                                                                       | Kein Buildsystem notwendig                                                                                                                           |
| Versionskontrolle        | Git & GitHub                                                            | Standard                                                                                                                                              |
| IDE                      | PyCharm                                                                 | Standard Python-IDE, kompatibel für Doku in .md                                                                                                      |
| Ausgabe/GUI              | Tkinter (Standardbibliothek)                                            | Plattformunabhängiges GUI-Toolkit, bereits in Python integriert                                                                                      |
| Dokumentation            | Markdown                                                                | Standard, IDE-Integration                                                                                                                            |
| Codeanalyse              | flake8, pylint, mypy, SonarQube                                         | Statische Codeanalyse für Syntax- und Stilprüfungen sowie Typprüfung                                                                                 |
| Test-Framework           | pytest                                                                  | Python-Testframework für Unit- & Integrationstests                                                                                                   |
| Frameworks, Bibliotheken | Tkinter, `threading`, `time`, `winsound`, `tkinter.ttk`, `messagebox`   | Python-Standardbibliotheken zur Implementierung von UI, nebenläufiger Verarbeitung und Systeminteraktionen                                          |
| Paketverwaltung          | pip/venv                                                                | Verwalten externer Abhängigkeiten & virtuelle Entwicklungsumgebung                                                                                   |

## Implementierungsdetails Sprint v1

### Threading-Modell

Der Controller nutzt Python `threading` um die Strahlungssimulation in einem Daemon-Thread auszuführen:

```python
self.thread = threading.Thread(
    target=self._run_radiation, 
    args=(duration,), 
    daemon=True
)
self.thread.start()
```

**Vorteile:**
- UI bleibt responsiv während der Countdown läuft
- Ermöglicht zukünftige Stop-Funktionalität
- Nicht-blockierende Benutzerinteraktion

### Kommunikationsfluss

1. **Benutzer-Input:** Strahlungsdauer eingeben → Start-Button klicken
2. **Validierung:** Controller prüft `1 <= duration <= MAX_DURATION`
3. **Thread-Start:** `_run_radiation()` wird in separatem Thread gestartet
4. **Echtzeit-Updates:** Alle 20ms (`time.sleep(0.02)`) wird Fortschritt berechnet und UI aktualisiert
5. **Beendigung:** Nach Erreichen der Dauer wird Signalton abgespielt und Messagebox angezeigt
6. **Reset:** UI wird in Initialzustand zurückgesetzt

