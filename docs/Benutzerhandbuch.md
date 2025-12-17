# Benutzerhandbuch

## 1. Einleitung

Der Röntgengerät-Simulator ist eine Desktop-Anwendung zur Simulation eines einfachen Röntgensystems. Dieses Handbuch beschreibt Installation, Bedienung und typische Anwendungsfälle.

---

## 2. Installation

### 2.1 Systemvoraussetzungen

- Windows 10 oder neuer.
- Keine separate Python-Installation erforderlich, wenn die EXE genutzt wird.
- Für die Entwicklung:
  - Python 3.11.x
  - Tkinter (in Python enthalten)

### 2.2 Installation über EXE

1. Downloade die Datei `RadiationSimulator_vX.exe`.
2. Optional: Verschiebe die Datei in einen eigenen Ordner (z. B. `C:\Programme\RadiationSimulator`).
3. Doppelklicke die EXE, um die Anwendung zu starten.

**Hinweis:** Beim ersten Start kann Windows SmartScreen eine Warnung anzeigen („Windows hat Ihren PC geschützt“).  
In diesem Fall:
- Auf **„Weitere Informationen“** klicken.
- Dann **„Trotzdem ausführen“** wählen.

---

## 3. Überblick Benutzeroberfläche

Nach dem Start erscheint das Hauptfenster „Röntgengerät Simulation“ mit folgenden Bereichen:

- **Eingabebereich „Einstellungen“**
  - Textfeld zur Eingabe der Strahlungsdauer (in Sekunden).
  - Hinweistext: „Strahlungsdauer (1–120 Sekunden) eingeben“.

- **Anzeigebereich**
  - Label „Vergangene Strahlungsdauer: …“.
  - Horizontaler Fortschrittsbalken.
  - Label „Fortschritt: … %“.

- **Bedienelemente**
  - Button „Start“ / „Stop“.
  - Status-LED mit Beschriftung „Strahlung:“.
  - Button „Logs exportieren“.

- **Log-Bereich**
  - Scrollbare Textbox mit protokollierten Ereignissen.

---

## 4. Bedienung

### 4.1 Strahlung starten

1. Gib im Eingabefeld eine **Ganzzahl zwischen 1 und 120** ein.
2. Klicke auf den **„Start“-Button**.
3. Die GUI reagiert wie folgt:
   - Der Button wechselt zu **„Stop“** und wird rot.
   - Die Status-LED wird grün.
   - Der Fortschrittsbalken beginnt, sich zu füllen.
   - Die verstrichene Strahlungsdauer wird in Sekunden angezeigt.
   - Im Log erscheint ein Eintrag mit Zeitstempel, z. B.:  
     `• [2025-12-10 13:20:15] Strahlung gestartet für 10 s`.

Wenn die eingegebene Dauer ungültig ist (z. B. leer, 0, >120, Buchstaben), erscheint ein Fehlerdialog, und die Strahlung wird **nicht** gestartet.

### 4.2 Strahlung automatisch beenden

- Läuft die Strahlung bis zur eingestellten Zeit ab, passiert folgendes:
  - Fortschrittsbalken steht auf 100 %.
  - LED wird rot.
  - Der Button geht zurück auf „Start“ (grün).
  - Eine Info-MessageBox informiert:  
    „Die Strahlung wurde erfolgreich nach X Sekunden beendet.“
  - Im Log erscheint ein Eintrag:  
    `• [Zeitstempel] Strahlung automatisch beendet nach X.X s`.

### 4.3 Strahlung manuell abbrechen

1. Während die Strahlung läuft, klicke auf den **„Stop“-Button** (rot).
2. Die GUI reagiert wie folgt:
   - Strahlung wird sofort abgebrochen.
   - LED wird rot.
   - Fortschrittsbalken bleibt stehen und wird anschließend zurückgesetzt.
   - Der Button wechselt wieder auf „Start“ (grün).
   - Eine Warn-MessageBox informiert:  
     „Die Strahlung wurde nach X.X Sekunden abgebrochen!“
   - Im Log erscheint ein Eintrag:  
     `• [Zeitstempel] Strahlung abgebrochen nach X.X s`.

### 4.4 Logs ansehen und exportieren

- Der Log-Bereich zeigt alle relevanten Ereignisse:
  - Start der Strahlung.
  - Automatisches Ende.
  - Manuelle Abbrüche.

**Export:**

1. Klicke auf **„Logs exportieren“**.
2. Es öffnet sich ein Datei-Speichern-Dialog.
3. Wähle Speicherort und Dateiname (Standard: `RS-Logs-YYYYMMDD-HHMMSS.txt`).
4. Klicke auf „Speichern“.
5. Eine Bestätigungsmeldung informiert über den erfolgreichen Export.

*Hinweis:* Ist der Log-Bereich leer, erscheint eine Info-MessageBox:  
„Keine Log-Einträge vorhanden.“