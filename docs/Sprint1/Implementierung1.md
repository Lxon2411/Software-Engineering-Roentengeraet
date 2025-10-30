# Implementierung
## Traceability-Matrix
| **Requirement-ID** | **Komponente**                 | **Klasse(n)**                                                  | **Schnittstelle(n)**                                                                      |
|--------------------|--------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1.1                | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController```                  | ```toggle_radiation()```, ```start_radiation()```, ```stop_radiation()```                 |
| 2.1                | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController```                  | ```duration_entry.get()```, ```start_radiation()```                                       |
| 3.1                | Steuerungslogik, Systemschicht | ```RadiationController```                                      | ```update_timer()```, ```time.time()```, ```winsound.Beep()```                            |

## Allgemeine Projektmetriken
| **Metrik**               | **Wert**                                        | **Beschreibung**                              |
|--------------------------|-------------------------------------------------|-----------------------------------------------|
| Programmiersprache       | Python 3.11                                     | Dynamisch typisiert, objektorientiert, modern |
| Dateien (Module)         | 3 (GUI, Steuerung, System)                      | Nach Schichten getrennt                       |
| Klassen                  | 3 (StatusLED, RadiationController, RadiationUI) | Gute Modularität                              |
| Testabdeckung (Ziel)     | ≥ 80 %                                          | Empfehlung für Unit Tests                     |  
| Abhängigkeiten (Imports) | tkinter, time, platform, winsound               | Nur Standardbibliothek → portabel             |  
| Architekturprinzip       | MVC-ähnlich (GUI - Controller - System)         | Gute Trennung der Verantwortlichkeiten        |

