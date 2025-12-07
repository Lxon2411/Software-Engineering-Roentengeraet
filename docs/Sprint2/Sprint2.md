# Sprint 2
**Zeitraum: 03.12.2025 bis 10.12.2025**

## Sprint Planning
Im Rahmen des zweiten Sprints sollen folgende Requirements implementiert werden:
- Req. 4.1 (funktional)
- Req. 5.1 (funktional) fertig implementieren
- Req. 1.2 (nicht-funktional)
- Req. 1.4 (nicht-funktional)


## Ziel des Sprints
1. **Architektur-Refactoring**: Implementierung der fehlenden Systemschicht zur Entkopplung von GUI und Logik
2. **Code-Qualität**: Strikte Umsetzung des 3-Schichten-Modells (GUI → Controller → System)
3. **UI-Verschlankung**: Verlagerung von Business-Logik aus der GUI in den Controller
4. **Thread-Sicherheit**: Evaluierung und Optimierung des Timer-Mechanismus (Thread vs. `tkinter.after()`)
5. **Vollständige Testabdeckung**: Unit-Tests für Controller und SystemLayer

## Architektur und Design

Die Systemarchitektur wurde im Sprint 2 vollständig überarbeitet und dokumentiert:

- **Klassendiagramm**: Zeigt die Beziehungen zwischen RadiationController, RadiationUI und StatusLED
- **Komponentendiagramm**: Definiert 5 Schnittstellen (IUserInteraction, ILogicControl, ISystemAccess, IUIUpdate, IStatusIndicator)
- **Sequenzdiagramm**: Visualisiert den zeitlichen Ablauf in 5 Phasen
- **Zustandsdiagramm**: Modelliert die Zustandsübergänge des Controllers
- **Kommunikationsdiagramm**: Zeigt die Abhängigkeiten und Interaktionen zwischen Komponenten

## Code-Mappings 

| **Requirement** | **Datei**       | **Klasse**            | **Methode(n)**                                    | **Zeilennummern (ca.)** |
|-----------------|-----------------|-----------------------|---------------------------------------------------|-------------------------|
| **4.1**         | `ui.py`         | `RadiationUI`         | `stop_radiation()`                                | ~80-82                  |
| **4.1**         | `controller.py` | `RadiationController` | `stop()`                                          | ~25-28                  |
| **5.1**         | `ui.py`         | `RadiationUI`         | `update_progress(value, max_value)`               | ~56-65                  |
| **5.1**         | `status_led.py` | `StatusLED`           | `set_active()`, `set_inactive()`                  | ~18-22                  |
| **5.1**         | `controller.py` | `RadiationController` | `_run_radiation()` (ruft `update_progress()` auf) | ~16-20                  |
| **1.2**         | `controller.py` | `RadiationController` | `stop()` (Flag-Verwaltung)                        | ~25-28                  |
| **1.4**         | `controller.py` | `RadiationController` | `_run_radiation()` (Timing-Logik)                 | ~13-24                  |

---

## Abweichungen 

**Vergleich von Software-Architektur und -Design mit der tatsächlichen Implementierung:**

| Bereich                                         | Geplant (Sprint 2 Design)                                                                                                             | Implementiert (Sprint 2)                                                                              | Abweichung                     | Grund                                                           | Status        |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------|---------------|
| **Schichtenmodell** (GUI - Controller - System) | Strikte 3-Schichten-Struktur: GUI ↔ Controller ↔ SystemLayer mit definierten Schnittstellen (ILogicControl, ISystemAccess, IUIUpdate) | GUI ↔ Controller ↔ SystemLayer korrekt implementiert; Schnittstellen als Callbacks realisiert         | ✅ Keine Abweichung             | Sprint 2 Fokus auf Refactoring war erfolgreich                  | ✅ Umgesetzt   |
| **SystemLayer-Implementierung**                 | Dedizierte Klasse `SystemLayer` mit Methoden: `getCurrentTime()`, `sleep()`, `playBeep()`                                             | SystemLayer abstrahiert alle OS-Zugriffe; Proxy-Pattern korrekt umgesetzt                             | ✅ Keine Abweichung             | Vollständige Entkopplung erreicht                               | ✅ Umgesetzt   |
| **Timer-Mechanismus**                           | Bewertung von Thread vs. `tkinter.after()`; Entscheidung für Daemon-Thread mit `time.sleep(0.02)`                                     | Controller nutzt separaten Daemon-Thread für `_run_radiation()`; `update_progress()` via Callback     | ✅ Keine Abweichung             | Thread bietet bessere Kontrolle über Timing und Abort-Verhalten | ✅ Umgesetzt   |
| **Controller-Verantwortlichkeiten**             | - Strahlung starten/stoppen - Thread-Verwaltung - State Management (running, aborted) - UI-Callbacks aufrufen                         | Controller implementiert alle geplanten Verantwortlichkeiten; vollständige Entkopplung von UI-Details | ✅ Keine Abweichung             | Klare Separation of Concerns erreicht                           | ✅ Umgesetzt   |
| **UI-Verantwortlichkeiten**                     | - Nur Eingabevalidierung - Button/LED-Rendering - Nachrichten anzeigen - Controller-Methoden aufrufen                                 | UI implementiert korrekt nur Präsentation; Business-Logik vollständig in Controller verlagert         | ✅ Keine Abweichung             | Verschlankung erfolgreich; UI ist jetzt reine View-Schicht      | ✅ Umgesetzt   |
| **StatusLED-Komponente**                        | Separate Klasse mit `set_active()` und `set_inactive()` Methoden; von UI aufgerufen                                                   | StatusLED korrekt als Unter-Komponente von RadiationUI implementiert                                  | ✅ Keine Abweichung             | Gute Kapselung der LED-Logik                                    | ✅ Umgesetzt   |
| **Sound-Ausgabe**                               | In SystemLayer gekapselt; Proxy-Pattern für `winsound.Beep()`                                                                         | Alle Sound-Aufrufe erfolgen via SystemLayer; zentrale Kontrolle                                       | ✅ Keine Abweichung             | Konsistente Systemschicht-Nutzung                               | ✅ Umgesetzt   |
| **Schnittstellen-Definitionen**                 | Explizite Schnittstellen: ILogicControl, ISystemAccess, IUIUpdate, IStatusIndicator als abstrakte Klassen oder Protokolle             | Schnittstellen als implizite Protokolle in Python realisiert; funktional äquivalent                   | ⚠️ Umsetzung statt Deklaration | Python-Konvention; äquivalent zu Java-Interfaces                | ✅ Ausreichend |                                                        | Direkter Aufruf von ```winsound.Beep()```in ```show_finished_message()```     | Kein Proxy wie im Design vorgesehen          | Aufwand gering halten; einfache Lösung                                              |


## Gewonnene Erkenntnisse

### Erkenntnisse zur Architektur & Design

**Positive Erkenntnisse:**
- Die **strikte Schichtenarchitektur** führt zu wartbarerem und testbarerem Code
- Die **SystemLayer-Abstraktion** macht das System plattformunabhängig (könnte auf Linux portiert werden)
- Das **Callback-Pattern** ermöglicht echte Entkopplung zwischen GUI und Logik
- Die **expliziten Schnittstellen** im Komponentendiagramm halfen bei der korrekten Implementierung

**Lektionen gelernt:**
- **Frühe UML-Diagramme zahlen sich aus**: Die detaillierten Diagramme (Klasse, Komponenten, Sequenz, Zustand, Kommunikation) halfen, die Implementierung sauberer zu gestalten als in Sprint 1
- **Thread-Management ist kritisch**: Der Daemon-Thread mit explizitem `running` Flag ist stabiler als Event-basierte Ansätze
- **Explizite Schnittstellendefinition** (auch in Python durch Dokumentation) hilft, unerwartete Abhängigkeiten zu vermeiden
- **`update_idletasks()` ist essentiell** für GUI-Updates aus Nicht-Main-Threads

### Erkenntnisse zur Entwicklung & Tools

**Verbesserungen für zukünftige Sprints:**
- UML-Design **vor der Implementierung** erstellen (erfolgreich in Sprint 2 umgesetzt)
- **Schnittstellendefinitionen** dokumentieren, bevor Code geschrieben wird
- **Code Reviews** nach jedem Feature zur Einhaltung von Architektur-Regeln
- **Unit-Tests** für Controller und SystemLayer hinzufügen (Sprint 3 Ziel)

**Best Practices identifiziert:**
- Systemschicht früh abstrahieren, um Platform-Abhängigkeiten zu isolieren
- Threading-Logik zentral halten (im Controller, nicht verteilt)
- Callbacks statt direkter Methodenaufrufe für loose Coupling
- State-Flags explizit dokumentieren (running, aborted)