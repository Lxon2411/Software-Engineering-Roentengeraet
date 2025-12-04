# Sprint 2
**Zeitraum: 03.12.2025 bis 10.12.2025**

## Sprint Planning
Im Rahmen des zweiten Sprints sollen folgende Requirements implementiert werden:
- Req. 4.1 
- Req. 5.1 fertig implementieren
- Req. 

Der Fokus dabei liegt auf der Implementierung der Grundfunktionalitäten, die für die weitere Entwicklung des Projekts essenziell sind.

## Ziel des Sprints
1. Erstellung einer grundlegenden Projektstruktur in einer Implementierungsumgebung
2. Vollständige Umsetzung der grundlegenden Teilfunktionalitäten 
3. Implementierung einer grafischen Benutzeroberfläche 

## Abweichungen 

**Vergleich von Software-Architektur und -Design mit der tatsächlichen Implementierung:**

| Bereich                                     | Geplant (Architektur/Design)                                                                        | Implementiert                                                                 | Abweichung                                   | Grund                                                                               |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------|
| Schichtenmodell (GUI - Controller - System) | Strikte 3-Schichten-Struktur: GUI ↔ Controller ↔ Systemschicht (Timer, Sound, Hardware)             | Systemschicht existiert nicht → Sound & Timer direkt in UI/Controller         | Systemschicht fehlt vollständig              | Zeitersparnis, geringere Komplexität; Architektur wird in Sprint 2 korrigiert       |
| Timer-Mechanismus                           | ```SystemTimer``` als eigene Komponente, oder Nutzung von ```tkinter.after()```(ereignisorientiert) | Controller verwendet **eigenen Thread** + ```time.sleep()```                  | Architektur widerspricht UML-Sequenzdiagramm | Thread war einfacher zu implementieren, aber führt zu UI-Risiken; wird refaktoriert |
| UI-Interaktion                              | Controller steuert LED, Log, Button-Farben, Fortschritt                                             | UI übernimmt Großteil der Logik selbst (z.B. Button deaktivieren, Messagebox) | Verantwortlichkeiten verschoben              | UI war schneller handhabbar; wird evtl. in Sprint 2 korrigiert                      |
| Message-Handling                            | Logik über Controller → GUI                                                                         | GUI zeigt Messagebox selbst                                                   | Designabweichung                             | Vereinfachung für Sprint 1                                                          |
| Sound-Ausgabe                               | In Systemschicht gekapselt (Proxy Pattern)                                                          | Direkter Aufruf von ```winsound.Beep()```in ```show_finished_message()```     | Kein Proxy wie im Design vorgesehen          | Aufwand gering halten; einfache Lösung                                              |


## Gewonnene Erkenntnisse
**Erkenntnisse zur Entwicklung & Tools**:
- Zeit für die **Einrichtung der Entwicklungsumgebung und Tools** (IDE, Git, Python-Interpeter, Abhängigkeiten) muss früh eingeplant werden, da dies unerwartet zusätzlichen Aufwand verursacht hat
- Requirement **5.1** (funktional) wurde teilweise zusätzlich implementiert, da es technisch sinnvoll war und die vorhandenen Methoden es leicht ermöglichten
- Die Modulstruktur wird in Sprint 2 bereinigt und klarer getrennt, um spätere Erweiterungen zu erleichtern

**Erkenntnisse zu Architektur/Design**:
- Die UI-Integration war komplexer und zeitaufwändiger als erwartet → **Priorität in Sprint 2:** UI-Verbesserung & saubere Modultrennung
- Der **Timer-Thread** bringt potenzielle Nebenwirkungen (UI-Thread-Sicherheit). In Sprint 2 sollte ```after()``` oder ein SystemTimer-Modul verwendet werden.
- Die fehlende Systemschicht erzeugt eine starke Kopplung zwischen GUI und Logik → **Refactoring notwendig**.
- Die UI enthält mehr Business-Logik als geplant → GUI wird in Sprint 2 deutlich **verschlankt**.