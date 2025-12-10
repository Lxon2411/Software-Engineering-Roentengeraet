# Test

**Sprint 2 Zeitraum: 07.12.2025 bis 12.12.2025**

Die folgenden Testfälle prüfen die in Sprint 2 implementierten Requirements:
- **Req. 5.2** (funktional): Ereignis-Logging
- **Req. 1.3** (nicht-funktional): 
---

## Offene Testfälle für Sprint 3

1. **Unit-Tests (automatisiert)**: Pytest-basierte Tests für alle Controller-Methoden
2. **Edge-Case-Tests**:
   - Mehrfaches schnelles Start/Stop
   - Stop während Abschalt-Phase
   - Sehr kurze Strahlungszeiten (< 1s)
   - Sehr lange Strahlungszeiten (> 60s)
3. **Stress-Tests**: 100× Start/Stop-Zyklen ohne Memory-Leaks
4. **Barrierefreiheit-Tests** (Req. 1.3): Screenreader-Kompatibilität, Farbkontrast
5. **Plattform-Tests**: SystemLayer auf Linux/macOS testen


## Testfälle auf Modulebene (algorithmische Korrektheit)

Diese Tests prüfen einzelne Methoden/Algorithmen, NICHT das Zusammenspiel der GUI.

### 1. Modul-Testfall M4 - Manuelles Stoppen setzt Flags korrekt

**Ziel:** `stop()` setzt `running = False` und `aborted = True` korrekt

| Merkmal             | Beschreibung                                                                      |
|---------------------|-----------------------------------------------------------------------------------|
| Requirement         | Req. 4.1 (funktional), Req. 1.2 (nicht-funktional)                                |
| Komponente          | Steuerungslogik                                                                   |
| Modul/Methode       | `RadiationController.stop()`                                                      |
| Vorbedingungen      | Strahlung läuft (`running = True`, `aborted = False`)                             |
| Ablauf              | 1. Strahlung mit 10s starten<br/>2. Nach 3s `stop()` aufrufen<br/>3. Flags prüfen |
| Erwartetes Ergebnis | `running = False`, `aborted = True`                                               |
| Ist-Ergebnis        | Korrekt → Flags werden sofort gesetzt                                             |
| Status              | ✓ bestanden                                                                       |

---

### 2. Modul-Testfall M5 - Thread beendet sich nach Stop innerhalb 50ms

**Ziel:** Thread reagiert schnell auf `running = False`

| Merkmal             | Beschreibung                                                                                     |
|---------------------|--------------------------------------------------------------------------------------------------|
| Requirement         | Req. 1.2 (nicht-funktional)                                                                      |
| Komponente          | Steuerungslogik                                                                                  |
| Modul/Methode       | `RadiationController._run_radiation()`                                                           |
| Vorbedingungen      | Strahlung läuft in separatem Thread                                                              |
| Ablauf              | 1. Strahlung mit 20s starten<br/>2. Nach 2s `stop()` aufrufen<br/>3. Zeit bis Thread-Ende messen |
| Erwartetes Ergebnis | Thread beendet sich innerhalb von 50ms (max. 1 Polling-Zyklus à 20ms + Overhead)                 |
| Ist-Ergebnis        | Korrekt → Thread endet nach ~30ms (1× sleep-Zyklus)                                              |
| Status              | ✓ bestanden                                                                                      |

---

### 3. Modul-Testfall M6 - StatusLED wechselt korrekt zwischen Zuständen

**Ziel:** `set_active()` und `set_inactive()` ändern LED-Farbe

| Merkmal             | Beschreibung                                                                                        |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Requirement         | Req. 5.1 (funktional)                                                                               |
| Komponente          | GUI                                                                                                 |
| Modul/Methode       | `StatusLED.set_active()`, `StatusLED.set_inactive()`                                                |
| Vorbedingungen      | StatusLED initialisiert (rot)                                                                       |
| Ablauf              | 1. `set_active()` aufrufen<br/>2. Farbe prüfen<br/>3. `set_inactive()` aufrufen<br/>4. Farbe prüfen |
| Erwartetes Ergebnis | 1. LED wird grün (`fill="green"`)<br/>2. LED wird rot (`fill="red"`)                                |
| Ist-Ergebnis        | Korrekt → Canvas-Item ändert Farbe korrekt                                                          |
| Status              | ✓ bestanden                                                                                         |

---

## Testfälle auf Integrationsebene (Zusammenarbeit zweier Komponenten)

### 4. Integration-Testfall I4 - GUI Stop-Button triggert Controller korrekt

**Ziel:** Prüfen, ob der Stop-Button den Controller korrekt aufruft

| Merkmal             | Beschreibung                                                                                                                                                                                             |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 4.1 (funktional)                                                                                                                                                                                    |
| Komponente          | GUI → Steuerungslogik                                                                                                                                                                                    |
| Modul/Methode       | `RadiationUI.stop_radiation()`, `RadiationController.stop()`                                                                                                                                             |
| Vorbedingungen      | Strahlung läuft (Button = "Stop", BG = Rot)                                                                                                                                                              |
| Ablauf              | 1. Strahlung mit 15s starten<br/>2. Nach 5s auf "Stop"-Button klicken<br/>3. Verhalten prüfen                                                                                                            |
| Erwartetes Ergebnis | 1. `RadiationController.stop()` wird aufgerufen<br/>2. Strahlung stoppt<br/>3. Abbruch-MessageBox erscheint ("Abgebrochen nach 5.X Sekunden")<br/>4. UI wird zurückgesetzt (Button = "Start", BG = Grün) |
| Ist-Ergebnis        | Korrekt → Stop-Kette funktioniert vollständig                                                                                                                                                            |
| Status              | ✓ bestanden                                                                                                                                                                                              |

---

### 5. Integration-Testfall I5 - Controller aktualisiert ProgressBar in Echtzeit

**Ziel:** `update_progress()` wird vom Controller aufgerufen und UI aktualisiert sich

| Merkmal             | Beschreibung                                                                                                                                                  |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 5.1 (funktional)                                                                                                                                         |
| Komponente          | Steuerungslogik → GUI                                                                                                                                         |
| Modul/Methode       | `RadiationController._run_radiation()` → `RadiationUI.update_progress(elapsed, duration)`                                                                     |
| Vorbedingungen      | Strahlung bereit zu starten                                                                                                                                   |
| Ablauf              | 1. Strahlung mit 10s starten<br/>2. Nach 5s UI-Elemente überprüfen<br/>3. Nach 10s Endzustand prüfen                                                          |
| Erwartetes Ergebnis | 1. Nach 5s: ProgressBar ≈ 50%, Label zeigt "5.X s", Prozent-Label ≈ "50 %"<br/>2. Nach 10s: ProgressBar = 100%, Label zeigt "10.0 s", Prozent-Label = "100 %" |
| Ist-Ergebnis        | Korrekt → UI aktualisiert sich alle ~20ms, Werte sind präzise                                                                                                 |
| Status              | ✓ bestanden                                                                                                                                                   |

---

### 6. Integration-Testfall I6 - Automatisches Abschalten mit präzisem Timing

**Ziel:** Strahlung endet präzise nach eingestellter Dauer (±50ms)

| Merkmal             | Beschreibung                                                                                                                                   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 1.4 (nicht-funktional)                                                                                                                    |
| Komponente          | Steuerungslogik → Systemschicht                                                                                                                |
| Modul/Methode       | `RadiationController._run_radiation()` mit `SystemLayer.getCurrentTime()` und `SystemLayer.sleep()`                                            |
| Vorbedingungen      | Windows-System, Strahlung bereit zu starten                                                                                                    |
| Ablauf              | 1. Strahlung mit 5s starten<br/>2. Startzeit notieren (z.B. 14:30:00.000)<br/>3. Endzeit messen (z.B. 14:30:05.045)<br/>4. Differenz berechnen |
| Erwartetes Ergebnis | Strahlung endet nach 5.000s ± 0.050s (5000ms ± 50ms)<br/>Erfolgsmeldung erscheint<br/>Beep (400Hz, 600ms) ertönt                               |
| Ist-Ergebnis        | Korrekt → Gemessen: 5.042s (innerhalb ±50ms Toleranz)<br/>Beep ertönt, MessageBox "Erfolgreich nach 5 Sekunden" erscheint                      |
| Status              | ✓ bestanden                                                                                                                                    |

---

## Zusammenfassung Testergebnisse Sprint 2

| Testfall-ID | Typ         | Requirement | Beschreibung                          | Status      |
|-------------|-------------|-------------|---------------------------------------|-------------|
| **M4**      | Modul       | 4.1, 1.2    | Manuelles Stoppen setzt Flags korrekt | ✓ bestanden |
| **M5**      | Modul       | 1.2         | Thread beendet sich schnell (< 50ms)  | ✓ bestanden |
| **M6**      | Modul       | 5.1         | StatusLED wechselt Farbe korrekt      | ✓ bestanden |
| **I4**      | Integration | 4.1         | GUI Stop-Button → Controller Stop     | ✓ bestanden |
| **I5**      | Integration | 5.1         | Controller → UI ProgressBar Update    | ✓ bestanden |
| **I6**      | Integration | 1.4         | Präzises automatisches Abschalten     | ✓ bestanden |

**Gesamtergebnis Sprint 2: 6/6 Testfälle bestanden (100%)**

---

## Testumgebung

| Parameter       | Wert                  |
|-----------------|-----------------------|
| Betriebssystem  | Windows 11            |
| Python-Version  | 3.11.5                |
| Tkinter-Version | 8.6                   |
| Hardware        | Amd-Ryzen 5, 32GB RAM |
| Testdatum       | 07.12.2025            |
| Tester          | Leon Wühr             |

---


