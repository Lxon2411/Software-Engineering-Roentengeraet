# Softwarearchitektur
Architekturtyp: **Schichten-/Komponentenarchitektur mit Trennung von Logik, Steuerung und GUI**

## Hauptkomponenten:
1. GUI-Schicht (Tkinter UI)
- Darstellung und Benutzerinteraktion
- Buttons: Start/Stop
- Anzeigen: Fortschrittsbalken, Reststrahlungszeit

2. Steuerungs- /Logik-Schicht (Controller)
- Überwacht Strahlungsdauer und Ablauf
- Kommuniziert mit GUI
- Steuert Start/Stop und Fortschritt

3. Simulations- / Timer-Komponente
- Verwaltet countdown und Zeitablauf
- Liefert Zustandsänderungen an GUI

## Technologien:
- Python
- Tkinter für UI

