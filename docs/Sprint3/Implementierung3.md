# Implementierung
## Traceability-Matrix
[Traceability-Matrix](../Traceability-Matrix.md)
## Allgemeine Projektmetriken
| **Metrik**               | **Wert**                                        | **Beschreibung**                                |
|--------------------------|-------------------------------------------------|-------------------------------------------------|
| Programmiersprache       | Python 3.11                                     | Dynamisch typisiert, objektorientiert, modern   |
| IDE                      | PyCharm                                         | Standard Python-IDE, kompatibel für Doku in .md |
| Dateien (Module)         | 3 (GUI, Steuerung, System)                      | Nach Schichten getrennt                         |
| Klassen                  | 3 (StatusLED, RadiationController, RadiationUI) | Gute Modularität                                |
| Testabdeckung (Ziel)     | ≥ 80 %                                          | Empfehlung für Unit Tests                       |  
| Abhängigkeiten (Imports) | tkinter, time, platform, winsound               | Nur Standardbibliothek → portabel               |  
| Architekturprinzip       | MVC-ähnlich (GUI - Controller - System)         | Gute Trennung der Verantwortlichkeiten          |

