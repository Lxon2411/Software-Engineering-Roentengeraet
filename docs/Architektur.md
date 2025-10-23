# Softwarearchitektur
Architekturtyp: **Schichten-/Komponentenarchitektur mit Trennung von Logik, Steuerung und GUI**

## Komponentendiagramm
![Architekturdiagramm](./images/Architektur_Komponentendiagramm.png)

## Hauptkomponenten
1. GUI-Schicht (Tkinter UI)
- Darstellung und Benutzerinteraktion
- Buttons: Start/Stop
- Anzeigen: Status, Fortschrittsbalken, Reststrahlungszeit, Protokoll

2. Steuerungs- /Logik-Schicht (Controller)
- Überwacht Strahlungsdauer und Ablauf
- Kommuniziert mit GUI
- Steuert Start/Stop und Fortschritt

3. Systemschicht
- Verwaltet Countdown und Zeitablauf
- Steuern der Signaltöne
- Systemprüfungen


| **Komponente**      | **Requirements**                       
|---------------------|--------------------------------------------------------------
| GUI                 | Req. 1.1, Req. 2.1, Req. 4.1, Req. 5.1, Req 5.2
| Steuerungslogik     | Req. 1.1, Req. 2.1, Req. 3.1, Req. 4.1, Req. 5.1, Req. 5.2                       
| Systemschicht       | Req. 3.1              

## Schnittstellen zwischen den Komponenten
| **von**             | **an**               |      **Beschreibung**                      
|---------------------|----------------------|-----------------------------------------------------------------
| GUI                 | Steuerungslogik      | Liefert die eingegebene Strahlungsdauer (int)
| Steuerungslogik     | GUI                  | Ändert Text und Hintergrundfarbe des Start/Stop-Buttons
| Steuerungslogik     | GUI                  | Aktualisiert die Anzeige der Strahlungsdauer
| Steuerungslogik     | GUI                  | Setzt den Wert des Fortschrittbalkens (0-100%)
| Steuerungslogik     | GUI                  | Setzt die Status-LED auf grün oder rot
| Steuerungslogik     | GUI                  | Fügt eine Meldung dem Logfeld hinzu
| Steuerungslogik     | GUI                  | Zeigt eine Messagebox (error/info/warning) an
| Steuerungslogik     | System               | Erzeugt einen akustischen Signalton (plattformabhängig, z.B. ```winsound.Beep()```)
| Steuerungslogik     | System               | Liefert die aktuelle Zeit (z.B. ```time.time()```)

## Technologien
- Python
- Tkinter für UI
