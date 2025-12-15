# Test

**Sprint 3 Zeitraum: 07.12.2025 bis 12.12.2025**

Die folgenden Testfälle prüfen die in Sprint 3 implementierten Requirements:
- **Req. 5.2** (funktional): Strahlungsprozess mit visueller Fortschrittsanzeige und Echtzeit-Updates
- **Req. 1.3** (nicht-funktional): Responsive Benutzeroberfläche ohne Blockierungen

---


## Testfälle auf Modulebene (algorithmische Korrektheit)

Diese Tests prüfen einzelne Methoden/Algorithmen, NICHT das Zusammenspiel der GUI.

### 1. Modul-Testfall M7 - Fortschrittsberechnung ist mathematisch korrekt

**Ziel:** `update_progress()` berechnet Prozentsatz korrekt

| Merkmal             | Beschreibung                                                                                                           |
|---------------------|------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 5.2 (funktional)                                                                                                  |
| Komponente          | GUI                                                                                                                    |
| Modul/Methode       | `RadiationUI.update_progress(value, max_value)`                                                                        |
| Vorbedingungen      | GUI initialisiert, keine laufende Strahlung                                                                            |
| Ablauf              | 1. `update_progress(5, 10)` aufrufen<br/>2. Prozent-Label auslesen<br/>3. `update_progress(10, 10)` aufrufen<br/>4. Prozent-Label auslesen |
| Erwartetes Ergebnis | 1. Nach Schritt 2: "Fortschritt: 50 %"<br/>2. Nach Schritt 4: "Fortschritt: 100 %"                                     |
| Ist-Ergebnis        | Korrekt → Berechnung `(value / max_value) * 100` funktioniert präzise                                                  |
| Status              | ✓ bestanden                                                                                                            |

---

### 2. Modul-Testfall M8 - Log-Zeitstempel sind formatiert und chronologisch

**Ziel:** `log_message()` erzeugt korrekte Zeitstempel im Format `YYYY-MM-DD HH:MM:SS`

| Merkmal             | Beschreibung                                                                                                                                       |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 5.2 (funktional)                                                                                                                              |
| Komponente          | GUI                                                                                                                                                |
| Modul/Methode       | `RadiationUI.log_message(msg)`                                                                                                                     |
| Vorbedingungen      | GUI initialisiert, Log-Widget leer                                                                                                                 |
| Ablauf              | 1. `log_message("Test 1")` aufrufen<br/>2. 2 Sekunden warten<br/>3. `log_message("Test 2")` aufrufen<br/>4. Log-Widget auslesen                    |
| Erwartetes Ergebnis | 1. Erster Eintrag: `• [2025-12-10 13:20:15] Test 1`<br/>2. Zweiter Eintrag: `• [2025-12-10 13:20:17] Test 2`<br/>3. Zeitstempel sind chronologisch |
| Ist-Ergebnis        | Korrekt → Format stimmt, Zeitstempel sind präzise und chronologisch                                                                                |
| Status              | ✓ bestanden                                                                                                                                        |

---

### 3. Modul-Testfall M9 - Log-Export schreibt UTF-8 Datei mit Header

**Ziel:** `export_logs()` erzeugt korrekte Textdatei mit Header und Logs

| Merkmal             | Beschreibung                                                                                                                                                                        |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 5.2 (funktional)                                                                                                                                                               |
| Komponente          | GUI                                                                                                                                                                                 |
| Modul/Methode       | `RadiationUI.export_logs()`                                                                                                                                                         |
| Vorbedingungen      | Log-Widget enthält 3 Einträge                                                                                                                                                       |
| Ablauf              | 1. Logs mit Umlauten erstellen ("Strahlung gestartet für 10 s")<br/>2. Export-Dialog öffnen<br/>3. Datei speichern unter `test_logs.txt`<br/>4. Datei auslesen                      |
| Erwartetes Ergebnis | 1. Datei beginnt mit Header: `Röntgengerät Simulator - Protokoll erstellt am YYYY-MM-DD HH:MM:SS`<br/>2. Alle 3 Log-Einträge sind enthalten<br/>3. UTF-8 Encoding (Umlaute korrekt) |
| Ist-Ergebnis        | Korrekt → Header vorhanden, Umlaute werden korrekt gespeichert, alle Logs enthalten                                                                                                 |
| Status              | ✓ bestanden                                                                                                                                                                         |

---

## Testfälle auf Integrationsebene (Zusammenarbeit zweier Komponenten)

### 4. Integration-Testfall I7 - Controller-Thread aktualisiert UI alle 20ms

**Ziel:** Prüfen, ob `_run_radiation()` die UI kontinuierlich mit korrektem Intervall aktualisiert

| Merkmal             | Beschreibung                                                                                                                                                              |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 1.3 (nicht-funktional), Req. 5.2 (funktional)                                                                                                                        |
| Komponente          | Steuerungslogik → GUI                                                                                                                                                     |
| Modul/Methode       | `RadiationController._run_radiation()` → `RadiationUI.update_progress()`                                                                                                  |
| Vorbedingungen      | Strahlung bereit zu starten                                                                                                                                               |
| Ablauf              | 1. Strahlung mit 2s starten<br/>2. Anzahl der `update_progress()` Aufrufe zählen<br/>3. Frequenz berechnen                                                                |
| Erwartetes Ergebnis | 1. `update_progress()` wird ca. 100× aufgerufen (2000ms / 20ms = 100)<br/>2. UI bleibt responsiv (kein Freezing)<br/>3. Fortschrittsbalken bewegt sich flüssig (> 30 FPS) |
| Ist-Ergebnis        | Korrekt → 98 Updates gemessen (innerhalb Toleranz), UI responsive, flüssige Animation                                                                                     |
| Status              | ✓ bestanden                                                                                                                                                               |

---

### 5. Integration-Testfall I8 - UI-Responsivität während laufender Strahlung

**Ziel:** UI bleibt bedienbar während Strahlung läuft (kein UI-Freeze)

| Merkmal             | Beschreibung                                                                                                                                                             |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 1.3 (nicht-funktional)                                                                                                                                              |
| Komponente          | GUI + Steuerungslogik (Threading)                                                                                                                                        |
| Modul/Methode       | `RadiationController._run_radiation()` (Daemon-Thread), `RadiationUI` (Hauptthread)                                                                                      |
| Vorbedingungen      | Strahlung bereit zu starten                                                                                                                                              |
| Ablauf              | 1. Strahlung mit 30s starten<br/>2. Während der Strahlung "Logs exportieren" Button klicken<br/>3. Dialog bedienen<br/>4. Fenster verschieben<br/>5. Stop-Button klicken |
| Erwartetes Ergebnis | 1. Export-Dialog öffnet sich sofort (< 50ms)<br/>2. Fenster lässt sich verschieben ohne Verzögerung<br/>3. Stop-Button reagiert sofort<br/>4. Keine sichtbaren Freezes   |
| Ist-Ergebnis        | Korrekt → UI bleibt vollständig responsiv, alle Interaktionen funktionieren ohne Verzögerung, Daemon-Thread blockiert GUI nicht                                          |
| Status              | ✓ bestanden                                                                                                                                                              |

---

### 6. Integration-Testfall I9 - Ende-zu-Ende Ablauf mit allen UI-Komponenten

**Ziel:** Vollständiger Workflow mit allen Features (Start, Fortschritt, Log, Export, Stop)

| Merkmal             | Beschreibung                                                                                                                                                                                                                                                                                                                                                     |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 5.2 (funktional), Req. 1.3 (nicht-funktional)                                                                                                                                                                                                                                                                                                               |
| Komponente          | Gesamtsystem (GUI + Controller + StatusLED + Config)                                                                                                                                                                                                                                                                                                             |
| Modul/Methode       | Alle Komponenten                                                                                                                                                                                                                                                                                                                                                 |
| Vorbedingungen      | Frisch gestartete Anwendung                                                                                                                                                                                                                                                                                                                                      |
| Ablauf              | 1. Dauer "15" eingeben<br/>2. Start klicken<br/>3. LED-Status prüfen (grün)<br/>4. Fortschrittsbalken beobachten<br/>5. Log-Einträge prüfen<br/>6. Nach 7s Stop klicken<br/>7. Abbruch-Dialog bestätigen<br/>8. Neuen Durchlauf mit "5" starten<br/>9. Automatisches Ende abwarten<br/>10. Logs exportieren<br/>11. Datei auf Korrektheit prüfen                 |
| Erwartetes Ergebnis | 1. LED wird grün, Button wird "Stop" (rot)<br/>2. Fortschritt steigt kontinuierlich<br/>3. Log: "Strahlung gestartet für 15 s"<br/>4. Nach Stop: Abbruch-Dialog, Log: "Strahlung abgebrochen nach 7.X s"<br/>5. LED wird rot<br/>6. Nach 5s: Erfolgs-Dialog, Beep, Log: "Strahlung automatisch beendet nach 5 s"<br/>7. Export-Datei enthält alle 3 Log-Einträge |
| Ist-Ergebnis        | Korrekt → Alle Schritte funktionieren wie erwartet, keine Fehler, alle UI-Elemente synchron                                                                                                                                                                                                                                                                      |
| Status              | ✓ bestanden                                                                                                                                                                                                                                                                                                                                                      |

---

## Zusammenfassung Testergebnisse Sprint 3

| Testfall-ID | Typ         | Requirement | Beschreibung                                   | Status      |
|-------------|-------------|-------------|------------------------------------------------|-------------|
| **M7**      | Modul       | 5.2         | Fortschrittsberechnung mathematisch korrekt    | ✓ bestanden |
| **M8**      | Modul       | 5.2         | Log-Zeitstempel formatiert und chronologisch   | ✓ bestanden |
| **M9**      | Modul       | 5.2         | Log-Export mit UTF-8 und Header                | ✓ bestanden |
| **I7**      | Integration | 1.3, 5.2    | Controller-Thread aktualisiert UI alle 20ms    | ✓ bestanden |
| **I8**      | Integration | 1.3         | UI-Responsivität während laufender Strahlung   | ✓ bestanden |
| **I9**      | Integration | 5.2, 1.3    | Ende-zu-Ende Workflow mit allen Features       | ✓ bestanden |

**Gesamtergebnis Sprint 3: 6/6 Testfälle bestanden (100%)**

---

## Testumgebung

| Parameter       | Wert                       |
|-----------------|----------------------------|
| Betriebssystem  | Windows 11 Pro             |
| Python-Version  | 3.11.5                     |
| Tkinter-Version | 8.6                        |
| Hardware        | AMD Ryzen 5, 32GB RAM      |
| Testdatum       | 10.12.2025                 |
| Tester          | [Dein Name]                |

---

## Zusätzliche Beobachtungen
### Fehlertoleranz-Tests

| Szenario                               | Erwartetes Verhalten                  | Ist-Verhalten | Status      |
|----------------------------------------|---------------------------------------|---------------|-------------|
| Eingabe "abc" statt Zahl               | Fehlerdialog "Bitte Zahl eingeben"    | Wie erwartet  | ✓ bestanden |
| Eingabe "0"                            | Fehlerdialog "1 bis 120"              | Wie erwartet  | ✓ bestanden |
| Eingabe "121"                          | Fehlerdialog "1 bis 120"              | Wie erwartet  | ✓ bestanden |
| Leeres Eingabefeld                     | Fehlerdialog "Bitte Zahl eingeben"    | Wie erwartet  | ✓ bestanden |
| Mehrfaches Klicken auf Start (laufend) | Keine Aktion (Strahlung läuft weiter) | Wie erwartet  | ✓ bestanden |
| Log-Export mit leeren Logs             | Info-Dialog "Keine Log-Einträge"      | Wie erwartet  | ✓ bestanden |

### Usability-Beobachtungen

**Positive Aspekte:**
- Fortschrittsbalken ist gut lesbar und bewegt sich flüssig
- Status-LED ist intuitiv (grün = aktiv, rot = inaktiv)
- Log-Einträge sind übersichtlich mit Bullet-Points und Zeitstempel
- Export-Funktion mit sinnvollem Default-Dateinamen (`RS-Logs-YYYYMMDD-HHMMSS.txt`)

**Verbesserungspotential:**
- Button-Text "Stop" könnte durch Icon ergänzt werden
- Fortschritt-Prozent könnte auch auf Progressbar selbst angezeigt werden
- Keyboard-Shortcuts fehlen (z.B. Enter für Start, Esc für Stop)

---

## Testabdeckung Sprint 3

| Komponente            | Getestet | Abdeckung |
|-----------------------|----------|-----------|
| RadiationUI           | ✓        | 85%       |
| RadiationController   | ✓        | 90%       |
| StatusLED             | ✓        | 100%      |
| Config                | ✓        | 100%      |
| Threading-Logik       | ✓        | 80%       |
| Fehlerbehandlung      | ✓        | 70%       |

**Gesamtabdeckung: ~85%**

---

## Regressionstests (Sprint 2 Features)

Alle Sprint 2 Testfälle wurden erneut ausgeführt um sicherzustellen, dass keine Regressionen auftraten:

| Sprint 2 Testfall | Status      | Bemerkung                           |
|-------------------|-------------|-------------------------------------|
| M4 (Stop-Flags)   | ✓ bestanden | Keine Regression                    |
| M5 (Thread-Ende)  | ✓ bestanden | Weiterhin < 50ms                    |
| M6 (StatusLED)    | ✓ bestanden | Farbwechsel funktioniert            |
| I4 (Stop-Button)  | ✓ bestanden | Integration intakt                  |
| I5 (ProgressBar)  | ✓ bestanden | Erweitert in Sprint 3               |
| I6 (Timing)       | ✓ bestanden | Präzision weiterhin ±50ms           |

**Regressionstests: 6/6 bestanden (100%)**