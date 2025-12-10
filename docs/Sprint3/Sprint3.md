# Sprint 2
**Zeitraum: 07.12.2025 bis 12.12.2025**

## Sprint Planning
Im Rahmen des zweiten Sprints sollen folgende Requirements implementiert werden:
- Req. 5.2 (funktional)
- Req. 1.3 (nicht-funktional)


## Ziel des Sprints


## Architektur und Design


## Code-Mappings 


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