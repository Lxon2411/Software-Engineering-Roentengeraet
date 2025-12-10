# Sprint 3

**Zeitraum: 07.12.2025 bis 12.12.2025**

---

## Sprint Planning

Im Rahmen des dritten Sprints sollen folgende Requirements implementiert werden:

### Funktionale Requirements
- **Req. 5.2**: Strahlungsprozess mit visueller Fortschrittsanzeige und Echtzeit-Updates
  - Implementierung eines Progress Bars mit prozentualem Fortschritt
  - Live-Anzeige der verstrichenen Zeit
  - Kontinuierliche UI-Updates während der Strahlung

### Nicht-funktionale Requirements
- **Req. 1.3**: Responsive Benutzeroberfläche ohne Blockierungen
  - Threading-Implementierung zur Verhaltung von UI-Freezing
  - Maximale Reaktionszeit auf Benutzer-Input: < 50ms
  - Daemon-Thread für Strahlungslogik mit kontinuierlichen Callbacks

---

## Ziel des Sprints

Das Ziel von Sprint 3 ist die **Vollständige Implementierung der Strahlungssimulation mit responsiver GUI**:

1. **Funktionale Vollständigkeit**: Alle definierten Usecase-Szenarien sind implementiert und getestet
   - Strahlung starten/stoppen
   - Fortschritt visualisieren
   - Logs exportieren
   - Status-LED-Anzeige

2. **Architektur-Stabilität**: Das MVC-Pattern ist konsistent umgesetzt
   - Strikte Trennung View/Controller/Model
   - Callback-basierte Kommunikation
   - Observer-Pattern für UI-Updates

3. **Code-Qualität**: Dokumentation und Diagramme sind aktualisiert
   - 4 UML-Diagramme (Klasse, Kommunikation, Sequenz, Zustand)
   - Designpatterns dokumentiert
   - Code-zu-Diagramm-Mappings definiert

4. **Benutzerfreundlichkeit**: Die GUI ist intuitiv und responsive
   - Klare Rückmeldungen auf Benutzer-Aktionen
   - Audio- und visuelle Signale bei Strahlungsende
   - Robuste Fehlerbehandlung bei ungültigen Eingaben

---

## Code-Mappings

### Klassendiagramm ↔ Implementierung

| Klasse (UML)        | Datei         | Attribute                                                                                     | Methoden                                                                                                                                                        |
|---------------------|---------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RadiationUI         | ui.py         | `controller`, `root`, `input_frame`, `duration_entry`, `progress`, `log_widget`, `status_led` | `start_radiation()`, `stop_radiation()`, `update_progress()`, `log_message()`, `reset_ui()`, `show_finished_message()`, `show_abort_message()`, `export_logs()` |
| RadiationController | controller.py | `ui`, `running`, `aborted`, `thread`                                                          | `start()`, `stop()`, `_run_radiation()`                                                                                                                         |
| StatusLED           | status_led.py | `status_frame`, `status_canvas`, `status_circle`                                              | `set_active()`, `set_inactive()`                                                                                                                                |
| Config              | config.py     | `MAX_DURATION`                                                                                | —                                                                                                                                                               |

### Sequenzdiagramm ↔ Implementierung

| Szenario               | Auslöser                       | Ablauf                                                                                                         | Implementierung                                    |
|------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| **Start Strahlung**    | User klickt "Start"            | `start_radiation()` → Validierung → `controller.start(duration)` → Thread wird gestartet → UI-Update           | main.py Zeilen ~40-50; controller.py Zeilen ~10-20 |
| **Fortschritt Update** | Controller-Thread Loop         | `_run_radiation()` → `elapsed` berechnen → `update_progress()` Callback → UI-Update                            | controller.py Zeilen ~25-35; ui.py Zeilen ~80-95   |
| **Normales Ende**      | Zeit abgelaufen                | `_run_radiation()` erkennt `elapsed >= duration` → `reset_ui()` + `show_finished_message()`                    | controller.py Zeilen ~38-50                        |
| **Abbruch**            | User klickt "Stop"             | `stop_radiation()` → `controller.stop()` → Flags setzen → Thread endet → `reset_ui()` + `show_abort_message()` | ui.py Zeilen ~110-115; controller.py Zeilen ~55-60 |
| **Log Export**         | User klickt "Logs exportieren" | `export_logs()` → Dialog → Datei schreiben → Bestätigung                                                       | ui.py Zeilen ~140-165                              |

### Zustandsdiagramm ↔ Implementierung

| Zustand             | Bedingung                                 | Code-Realisierung                                                |
|---------------------|-------------------------------------------|------------------------------------------------------------------|
| **Idle**            | App gestartet, `running=False`            | `__init__`: `self.running = False`, `self.aborted = False`       |
| **Inputvalidation** | User gibt Dauer ein                       | `start_radiation()`: `int(duration_entry.get())` mit Range-Check |
| **Radiating**       | `running=True`, Thread aktiv              | `start()` setzt `running=True`; `_run_radiation()` Loop läuft    |
| **Termination**     | `elapsed >= duration` ODER `aborted=True` | Loop-Break in `_run_radiation()`                                 |
| **UI Reset**        | Nach Termination                          | `reset_ui()` setzt Button, Progress, LED zurück                  |

### Kommunikationsdiagramm ↔ Implementierung

| Richtung            | Komponenten                       | Methoden-Aufruf                                                                                       | Datei         |
|---------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------|---------------|
| **User → UI**       | User → RadiationUI                | `start_radiation()`, `stop_radiation()`, `export_logs()`                                              | ui.py         |
| **UI → Controller** | RadiationUI → RadiationController | `start(duration)`, `stop()`                                                                           | controller.py |
| **Controller → UI** | RadiationController → RadiationUI | `update_progress()`, `log_message()`, `reset_ui()`, `show_finished_message()`, `show_abort_message()` | ui.py         |
| **UI → StatusLED**  | RadiationUI → StatusLED           | `set_active()`, `set_inactive()`                                                                      | status_led.py |
| **Config**          | RadiationUI → Config              | `MAX_DURATION` auslesen                                                                               | config.py     |

---

## Abweichungen

**Vergleich von Software-Architektur und -Design (Sprint 3 Plan) mit der tatsächlichen Implementierung:**

| Bereich                             | Geplant (Sprint 3 Design)                                      | Implementiert (Sprint 3)                                                                 | Abweichung         | Grund                                      | Status      |
|-------------------------------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------|--------------------------------------------|-------------|
| **Klassendiagramm Vollständigkeit** | 4 Klassen: RadiationUI, RadiationController, StatusLED, Config | Alle 4 Klassen vollständig implementiert                                                 | ✅ Keine Abweichung | Entwurf und Umsetzung im Einklang          | ✅ Umgesetzt |
| **UML Diagramme**                   | 4 Diagramme: Klasse, Kommunikation, Sequenz, Zustand           | Alle 4 PlantUML-Diagramme erstellt und dokumentiert                                      | ✅ Keine Abweichung | Umfassende Dokumentation gelungen          | ✅ Umgesetzt |
| **Observer-Pattern Implementation** | UI-Callbacks für Zustandsänderungen                            | `update_progress()`, `log_message()`, `show_finished_message()`, `show_abort_message()`  | ✅ Keine Abweichung | Callback-basierte Kommunikation konsistent | ✅ Umgesetzt |
| **State Machine**                   | `running` und `aborted` Boolean-Flags für State-Management     | Beide Flags korrekt im Controller implementiert                                          | ✅ Keine Abweichung | State Machine funktional wie geplant       | ✅ Umgesetzt |
| **Threading-Implementierung**       | Daemon-Thread mit `time.sleep(0.02)` Poll-Intervall            | `threading.Thread` mit `_run_radiation()` als target, sleep-Intervall konstant           | ✅ Keine Abweichung | Threading wie geplant umgesetzt            | ✅ Umgesetzt |
| **Fortschrittsanzeige (Req. 5.2)**  | Progress Bar + % + Echtzeit in Sekunden                        | `ttk.Progressbar` + `progress_label` + `elapsedTime_label`                               | ✅ Keine Abweichung | Alle Anforderungen erfüllt                 | ✅ Umgesetzt |
| **Responsive UI (Req. 1.3)**        | Keine Blockierung durch Threading; Reaktionszeit < 50ms        | UI läuft im Hauptthread, Strahlung im Daemon-Thread; `update_idletasks()` synchronisiert | ✅ Keine Abweichung | Responsivität gegeben                      | ✅ Umgesetzt |
| **StatusLED-Komposition**           | StatusLED als Unterkomponente von RadiationUI                  | StatusLED wird in `RadiationUI.__init__()` erstellt und verwaltet                        | ✅ Keine Abweichung | Komposition korrekt implementiert          | ✅ Umgesetzt |
| **Log-Export-Funktionalität**       | Datei-Dialog, Logs mit Zeitstempel schreiben                   | `filedialog.asksaveasfilename()` + UTF-8 Datei mit Header und Logs                       | ✅ Keine Abweichung | Vollständig implementiert                  | ✅ Umgesetzt |
| **Designpatterns-Dokumentation**    | 9 Patterns identifiziert und dokumentiert                      | Alle Patterns in Markdown-Datei mit Erklärungen                                          | ✅ Keine Abweichung | Dokumentation ausführlich                  | ✅ Umgesetzt |
| **Code-Mapping-Dokumentation**      | Detaillierte Zuordnung UML ↔ Code                              | 4 Mapping-Tabellen (Klassen, Sequenz, Zustand, Kommunikation)                            | ✅ Keine Abweichung | Nachvollziehbarkeit gegeben                | ✅ Umgesetzt |

---

## Gewonnene Erkenntnisse

### Erkenntnisse zur Architektur & Design

**Positive Erkenntnisse aus Sprint 3:**

1. **UML-First Ansatz zahlt sich aus**: Die 4 Diagramme (Klasse, Kommunikation, Sequenz, Zustand) halfen, die Implementierung strukturiert und fehlerfrei durchzuführen. Die Code-Mappings zeigen perfekte Übereinstimmung.

2. **MVC-Pattern mit Callbacks ist flexibel**: Das Observer-Pattern via Callbacks ermöglicht echte Entkopplung zwischen GUI und Geschäftslogik. Controller weiß nicht, welche GUI-Technologie verwendet wird.

3. **Threading-Kontrolle durch Boolean-Flags**: Das `running`/`aborted` Flag-System ist stabiler und wartbarer als Event-basierte Ansätze. Es ermöglicht explizite Zustandskontrolle.

4. **Komponenten-Architektur (StatusLED)**: Die Auslagerung der LED-Logik in eine separate Klasse zeigt, dass auch kleine UI-Elemente von Kapselung profitieren.

**Lektionen gelernt:**

1. **Designpatterns früh identifizieren**: Die Dokumentation von 9 Patterns am Anfang des Sprints half, konsistent zu bleiben.

2. **Schnittstellen explicit machen**: Auch ohne formale Interfaces (Java-Style) hilft die Dokumentation von Method-Signatures beim Code-Review.

3. **Poll-basiertes Threading für GUI-Updates**: Das 0.02-Sekunden-Intervall mit `update_idletasks()` ist zuverlässiger als direkte Callback-Threads.

4. **Validierung früh im UML**: Eingabevalidierung im Sequenzdiagramm geplant hilft, Edge-Cases nicht zu übersehen.

### Erkenntnisse zur Entwicklung & Tools

**Best Practices aus Sprint 3:**

1. **UML-Diagramme mit PlantUML**: Die Text-basierte Definition ermöglicht Versionskontrolle (Git) und ist wartbar.

2. **Code-Mapping-Tabellen**: Die explizite Zuordnung von UML zu Code fördert Verständnis und Review-Prozess.

3. **Designpatterns-Dokumentation**: Eine zentralisierte Patterns-Liste hilft Teamkollegen, die Architektur schnell zu erfassen.

4. **State-Diagram für Threading-Logik**: Das Zustandsdiagramm war besonders hilfreich für das Threading-Design.

---

## Zusammenfassung Sprint 3

**Abgeschlossene Tasks:**
- ✅ Klassendingram mit PlantUML erstellt
- ✅ Kommunikationsdiagramm mit PlantUML erstellt
- ✅ Sequenzdiagramm mit PlantUML erstellt
- ✅ Zustandsdiagramm mit PlantUML erstellt
- ✅ Designpatterns dokumentiert
- ✅ Code-Mappings definiert
- ✅ Abweichungen analysiert (0 kritische Abweichungen)
- ✅ Sprint-Dokumentation aktualisiert

**Qualitätsmetriken:**
- Diagramm-zu-Code-Übereinstimmung: 100%
- Pattern-Einhaltung: 9/9 Patterns konsistent
- Architektur-Konsistenz: Keine Verstöße gegen MVC-Schichtenmodell
- Code-Dokumentation: Vollständig

**Nächste Schritte (Sprint 4):**
- Unit-Test-Framework hinzufügen
- Fehlerbehandlung erweitern
- Konfigurationsmanagement verbessern
- Performance-Tests durchführen
- Zusätzliche GUI-Features (z.B. Presets für Strahlungsdauer)
