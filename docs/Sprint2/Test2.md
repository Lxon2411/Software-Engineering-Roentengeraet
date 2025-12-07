# Test
## Testfälle auf Modulebene (algorithmische Korrektheit)
Diese Tests prüfen einzelne Methoden/Algorithmen, NICHT das Zusammenspiel der GUI.

### 1. Modul-Testfall M1 - Prüfung der Eingabevalidierung

**Ziel:** ```start_radiation()``` akzeptiert nur Eingaben zwischen 1 und 120 Sekunden

| Merkmal             | Beschreibung                                                                                           |
|---------------------|--------------------------------------------------------------------------------------------------------|
| Requirement         | Req. 1.1 (funktional)                                                                                  |
| Komponente          | Steuerungslogik                                                                                        |
| Modul/Methode       | ```RadiationController.start_radiation()```                                                            |
| Vorbedingungen      | -                                                                                                      |
| Input               | Dauer = ```"999"```, ```"-1"```, ```"0"```                                                             |
| Erwartetes Ergebnis | Fehlermeldung *"Bitte eine Zahl zwischen 1 und 120 eingeben."* wird angezeigt; Strahlung startet nicht |
| Ist-Ergebnis        | korrekt → Fehlermeldung erscheint                                                                      |
| Status              | ✓ bestanden                                                                                            |

### 2. Modul-Testfall M2 - Fortschrittsberechnung

**Ziel:** Korrektheit der Prozentberechnung beim Timer.

| Merkmal             | Beschreibung                            |
|---------------------|-----------------------------------------|
| Requirement         | Req. 5.1 (funktional)                   |
| Komponente          | Steuerungslogik                         |
| Modul/Methode       | ```update_timer()```                    |
| Vorbedingungen      | max_duration = 10 s, elapsed_time = 5 s |
| Erwartetes Ergebnis | progress = 50 %                         |
| Ist-Ergebnis        | korrekt → UI zeigt 50 %                 |
| Status              | ✓ bestanden                             |

### 3. Modul-Testfall M3 - Automatisches Stoppen bei Maximaldauer

**Ziel:** Strahlung stoppt automatisch bei Ablauf der eingestellten Zeit.

| Merkmal             | Beschreibung                                                                                  |
|---------------------|-----------------------------------------------------------------------------------------------|
| Requirement         | Req. 3.1 (funktional)                                                                         |
| Komponente          | Steuerungslogik                                                                               |
| Modul/Methode       | ```update_timer()```                                                                          |
| Vorbedingungen      | max_duration = 2                                                                              |
| Ablauf              | Timer mehrfach aufgerufen bis Zeit >= 2 s                                                     |
| Erwartetes Ergebnis | Strahlung wird automatisch gestoppt, Warnmeldung und -signal erscheint, UI wird zurückgesetzt |
| Ist-Ergebnis        | korrekt                                                                                       |
| Status              | ✓ bestanden                                                                                   |


## Testfälle auf Integrationsebene (Zusammenarbeit zweier Komponenten)
### 1. Integration-Testfall I1 - GUI ruft Controller korrekt auf

**Ziel:** Prüfen, ob der Start/Stop-Button den Controller korrekt triggert.

| Merkmal             | Beschreibung                                             |
|---------------------|----------------------------------------------------------|
| Requirement         | Req. 2.1 (funktional)                                    |
| Komponente          | GUI → Steuerungslogik                                    |
| Modul/Methode       | ```start_radiation```, ```RadiationController.start()``` |
| Vorbedingungen      | -                                                        |
| Ablauf              | Benutzer klickt auf "Start"                              |
| Erwartetes Ergebnis | Controller startet Strahlung, Progress startet           |
| Ist-Ergebnis        | korrekt                                                  |
| Status              | ✓ bestanden                                              |

### 2. Integration-Testfall I2 - Controller aktualisiert UI korrekt

**Ziel:** Steuerungslogik setzt UI-Elemente korrekt.

| Merkmal             | Beschreibung                                               |
|---------------------|------------------------------------------------------------|
| Requirement         | Req. 5.1 (funktional)                                      |
| Komponente          | Steuerungslogik → GUI                                      |
| Modul/Methode       | ```progress['value']=...```, ```progress_label.config()``` |
| Vorbedingungen      | -                                                          |
| Ablauf              | Strahlung läuft für 3 Sekunden                             |
| Erwartetes Ergebnis | Fortschritt > 0 %                                          |
| Ist-Ergebnis        | korrekt                                                    |
| Status              | ✓ bestanden                                                |

### 3. Integration-Testfall I3 - Controller nutzt Systemfunktionen (Beep, Timer)

**Ziel:** Prüfen, ob die Systemschicht richtig aufgerufen wird.

| Merkmal             | Beschreibung                             |
|---------------------|------------------------------------------|
| Requirement         | Req. 3.1 (funktional)                    |
| Komponente          | Steuerungslogik → Systemschicht          |
| Modul/Methode       | ```winsound.Beep()```, ```time.time()``` |
| Vorbedingungen      | Windows-System, Dauer wird überschritten |
| Erwartetes Ergebnis | Warnton ertönt & Warnmeldung             |
| Ist-Ergebnis        | korrekt                                  |
| Status              | ✓ bestanden                              |

