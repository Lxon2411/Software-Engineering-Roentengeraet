# Softwarearchitektur
Architekturtyp: **Schichten-/Komponentenarchitektur** mit Trennung von Logik, Steuerung und GUI

## Komponentendiagramm
![Architekturdiagramm](./images/Architektur_Komponentendiagramm.png)

## Hauptkomponenten
1. **GUI-Schicht (Tkinter UI)**
- Darstellung und Benutzerinteraktion
- Buttons: Start/Stop
- Anzeigen: Status, Fortschrittsbalken, Reststrahlungszeit, Protokoll

2. **Steuerungs- /Logik-Schicht (Controller)**
- Überwacht Strahlungsdauer und Ablauf
- Kommuniziert mit GUI
- Steuert Start/Stop und Fortschritt

3. **Systemschicht**
- Verwaltet Countdown und Zeitablauf
- Steuern der Signaltöne
- Systemprüfungen

## Traceability-Matrix 
| **Komponente**  | **Requirements**                                           |
|-----------------|------------------------------------------------------------|
| GUI             | Req. 1.1, Req. 2.1, Req. 4.1, Req. 5.1, Req 5.2            |
| Steuerungslogik | Req. 1.1, Req. 2.1, Req. 3.1, Req. 4.1, Req. 5.1, Req. 5.2 |
| Systemschicht   | Req. 3.1                                                   |

## Verantwortlichkeiten der Komponenten
| **Komponente**  | **Rolle**                        | Verantwortlichkeiten                                                                                                                                                                                    |
|-----------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUI             | Präsentationsschicht             | - Anzeige von Zuständen <br/> - Interaktion mit dem Benutzer <br/> - Übergibt Benutzerbefehle an Steuerungslogik                                                                                        |
| Steuerungslogik | Anwendungsschicht/Business-Logik | - Steuerung des Strahlungsprozesses <br/> - Überprüfung der Eingaben (Validierung der Strahlungsdauer)<br/> - Kommunikation zwischen GUI und Systemschicht                                              |
| Systemschicht   | technische Integrationsschicht   | -Simulation der Hardware<br/> - Zugriff auf OS-/Hardwarefunktionen (z.B. Tonwiedergabe via ``winsound``, Zeitsteuerung via ``after()``)<br/> - Ausgabe von Systemdialogen (z.B. ``messagebox.showinfo`` |

## Schnittstellen zwischen den Komponenten
| **von**         | **an**          | **Beschreibung**                                                                    | Schnittstellen |
|-----------------|-----------------|-------------------------------------------------------------------------------------|----------------|
| GUI             | Steuerungslogik | Liefert die eingegebene Strahlungsdauer (int)                                       |                |
| Steuerungslogik | GUI             | Ändert Text und Hintergrundfarbe des Start/Stop-Buttons                             |                |
| Steuerungslogik | GUI             | Aktualisiert die Anzeige der Strahlungsdauer                                        |                |
| Steuerungslogik | GUI             | Setzt den Wert des Fortschrittbalkens (0-100%)                                      |                |
| Steuerungslogik | GUI             | Setzt die Status-LED auf grün oder rot                                              |                |
| Steuerungslogik | GUI             | Fügt eine Meldung dem Logfeld hinzu                                                 |                |
| Steuerungslogik | GUI             | Zeigt eine Messagebox (error/info/warning) an                                       |                |
| Steuerungslogik | System          | Erzeugt einen akustischen Signalton (plattformabhängig, z.B. ```winsound.Beep()```) |                |
| Steuerungslogik | System          | Liefert die aktuelle Zeit (z.B. ```time.time()```)                                  |                |

## Technologiestack
| **Kategorie**            | **Technologie/Tool**                                                         | Begründung                                                                                               |
|--------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Sprache                  | Python 3.11.4                                                                | Modern & persönliche Erfahrung                                                                           | 
| Buildsystem              | -                                                                            | kein Buildsystem notwendig                                                                               |
| Versionskontrolle        | Git & GitHub                                                                 | Standard                                                                                                 |
| IDE                      | PyCharm                                                                      | Standard Python-IDE, kompatibel für Doku in .md                                                          |
| Ausgabe/GUI              | Tkinter (Standardbibliothek)                                                 | Plattformunabhängiges GUI-Toolkit, bereits in Python integriert                                          |
| Dokumentation            | Markdown                                                                     | Standard, IDE-Integration                                                                                |
| Codeanalyse              | flake8, pylint, mypy, Sonarqube                                              | Statische Codeanalyse für Syntax- und Stilprüfungen (``flake8``, ``pylint``) sowie Typprüfung (``mypy``) |
| Test-Framework           | pytest                                                                       | Python-Testframework für Unit- & Integrationstests                                                       |
| Frameworks, Bibliotheken | Tkinter für UI, ``winsound``, ``time``, ``patform``, ``ttk``, ``messagebox`` | Python-Standardbibliotheken zur Implementierung von UI & Systeminteraktionen                             |
| Paketverwaltung          | pip/venv                                                                     | Verwalten externer Abhängigkeiten & virtuelle Entwicklungsumgebung                                       |
