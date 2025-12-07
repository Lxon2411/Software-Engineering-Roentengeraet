# Traceability-Matrix Sprint 2

## Funktionale Requirements

| **Req.-ID** | **Titel** | **Komponenten** | **Klassen** | **Schnittstellen / Methoden** | **Design-Pattern** | **Testfall-ID(s)** | **Status** |
|---|---|---|---|---|---|---|---|
| **1.1** | Benutzerdefinierte Strahlungsdauer | GUI | `RadiationUI` | `duration_entry` (tkinter.Entry)<br/>`start_radiation()` → Input-Validierung (1 ≤ dauer ≤ 120) | Facade (UI validiert Input) | M1, I1 | ✅ Umgesetzt |
| **2.1** | Strahlung starten | GUI, Controller | `RadiationUI`<br/>`RadiationController` | `start_radiation()` (UI)<br/>`start(duration: int)` (Controller, via ILogicControl)<br/>`_run_radiation(duration: int)` (privat) | Strategy (start() vs stop()) | M1, I1 | ✅ Umgesetzt |
| **3.1** | Automatisches Abschalten | Controller, System | `RadiationController`<br/>`SystemLayer` | `_run_radiation()` (Controller)<br/>`getCurrentTime()` (SystemLayer, via ISystemAccess)<br/>`stop()` (Controller)<br/>`update_progress()` (UI-Callback, via IUIUpdate) | State Machine<br/>Proxy (Zeit abstrahiert) | M3, I3 | ✅ Umgesetzt |
| **4.1** | Manuelles Stoppen | GUI, Controller | `RadiationUI`<br/>`RadiationController` | `stop_radiation()` (UI)<br/>`stop()` (Controller, via ILogicControl)<br/>`running = False` / `aborted = True` (State)<br/>`show_abort_message(elapsed)` (UI-Callback, via IUIUpdate) | Observer (UI reagiert auf stop)<br/>State Machine | M2, I2 | ✅ Umgesetzt |
| **5.1** | Statusanzeige & Fortschrittsbalken | GUI, Controller, System | `RadiationUI`<br/>`StatusLED`<br/>`RadiationController` | `update_progress(elapsed, duration)` (Controller → UI, via IUIUpdate)<br/>`progress` (ttk.Progressbar)<br/>`elapsedTime_label.config()`<br/>`progress_label.config()`<br/>`StatusLED.set_active()` / `set_inactive()` | Observer (UI beobachtet)<br/>Callback/Event Handler | M2, I2 | ✅ Umgesetzt |
| **5.2** | Ereignis-Logging | GUI, Controller | `RadiationUI`<br/>`RadiationController` | `show_finished_message(duration)` (UI-Callback, via IUIUpdate)<br/>`show_abort_message(elapsed)` (UI-Callback, via IUIUpdate)<br/>`messagebox.showinfo()` / `showwarning()` | Callback (entkoppeltes Logging) | M3, I3 | ⚠️ Teilweise (nur Messageboxen, kein persistentes Logging) |

## Nicht-funktionale Requirements

| **Req.-ID** | **Titel** | **Komponenten** | **Klassen** | **Schnittstellen / Implementierung** | **Überprüfung** | **Status** |
|---|---|---|---|---|---|---|
| **1.1** | Benutzerfreundlichkeit (<500ms Latenz) | GUI, Controller | `RadiationUI` | Eingabefeld akzeptiert Zahleneingaben<br/>`start()` / `stop()` Methoden sind responsive | Button-Reaktion < 50ms (lokal)<br/>Thread verursacht keine UI-Blockierung | ✅ Erreicht |
| **1.2** | Sicherheit (zuverlässiges Stop) | Controller, System | `RadiationController` | `stop()` setzt `aborted = True` und `running = False`<br/>Thread prüft `running` in Schleife<br/>`sleep()` via `SystemLayer` (unterbrechbar) | Manuelle Tests: Stop wird in < 50ms ausgeführt<br/>Flag-basierte Kontrolle (nicht unterbrochen) | ✅ Erreicht |
| **1.3** | Verständlichkeit (Farbenblindheit) | GUI | `StatusLED`<br/>`RadiationUI` | StatusLED zeigt Rot/Grün an<br/>Labels zeigen auch Text ("Strahlung: aktiv/inaktiv")<br/>ProgressBar mit Prozent-Label | Status wird textlich angezeigt (nicht nur Farbe) | ⚠️ Teilweise (LED nur Farbe, aber Labels redundant) |
| **1.4** | Zuverlässigkeit (präzises Abschalten) | Controller, System | `RadiationController`<br/>`SystemLayer` | Daemon-Thread mit `time.time()` (hochpräzise)<br/>`sleep(0.02)` → ~50ms Genauigkeit<br/>Zustandsflags sind thread-sicher (GIL) | Präzision: ±50ms auf Zieldauer<br/>Tests bestätigen konsistente Abschaltung | ✅ Erreicht (±50ms) |
| **1.5** | Ressourcen-Effizienz (RAM, CPU) | Alle | Alle | Daemon-Thread schläft 98% der Zeit (`sleep(0.02)`)<br/>UI Update nur bei Änderung (`update_idletasks()`)<br/>Keine persistenten Datenstrukturen | RAM: ~50MB (Tkinter baseline)<br/>CPU: ~0.5% (idle)<br/>CPU: ~5% (während Strahlung aktiv) | ✅ Erreicht |