# Traceability-Matrix Sprint 2

**Sprint 2 Zeitraum: 03.12.2025 bis 10.12.2025**

Im Sprint 2 werden folgende Requirements umgesetzt:
- **Req. 4.1** (funktional): Manuelles Stoppen
- **Req. 5.1** (funktional): Statusanzeige und Fortschrittsanzeige
- **Req. 1.2** (nicht-funktional): Sicherheit
- **Req. 1.4** (nicht-funktional): Zuverlässigkeit

---

## Funktionale Requirements (Sprint 2)

| **Req.-ID** | **Titel** | **Komponenten** | **Klassen** | **Schnittstellen / Methoden** | **Design-Pattern** | **Testfall-ID(s)** | **Status** |
|---|---|---|---|---|---|---|---|
| **4.1** | Manuelles Stoppen | GUI, Controller | `RadiationUI`<br/>`RadiationController` | **UI:**<br/>`stop_radiation()` (Button-Handler)<br/><br/>**Controller (via ILogicControl):**<br/>`stop()` → setzt `running = False` und `aborted = True`<br/><br/>**Callbacks (via IUIUpdate):**<br/>`show_abort_message(elapsed: float)`<br/>`reset_ui()` | • Observer (UI reagiert auf Stop-Event)<br/>• State Machine (`running`, `aborted` Flags)<br/>• Callback/Event Handler | M2, I2 | ✅ Umgesetzt |
| **5.1** | Statusanzeige & Fortschrittsbalken | GUI, Controller, System | `RadiationUI`<br/>`StatusLED`<br/>`RadiationController` | **UI:**<br/>`update_progress(elapsed: float, duration: float)`<br/>`progress` (ttk.Progressbar)<br/>`elapsedTime_label.config(text=...)`<br/>`progress_label.config(text=...)`<br/><br/>**StatusLED (via IStatusIndicator):**<br/>`set_active()` → LED grün<br/>`set_inactive()` → LED rot<br/><br/>**Controller → UI (via IUIUpdate):**<br/>Callback `update_progress()` alle 20ms | • Observer (UI beobachtet Controller)<br/>• Callback/Event Handler (entkoppelte Updates) | M2, I2 | ✅ Umgesetzt |

---

## Nicht-funktionale Requirements (Sprint 2)

| **Req.-ID** | **Titel** | **Komponenten** | **Klassen** | **Schnittstellen / Implementierung** | **Überprüfung / Metriken** | **Status** |
|---|---|---|---|---|---|---|
| **1.2** | Sicherheit:<br/>Zuverlässiges manuelles Stoppen | Controller | `RadiationController` | **Methoden:**<br/>`stop()` setzt Flags:<br/>• `aborted = True`<br/>• `running = False`<br/><br/>**Thread-Logik:**<br/>`_run_radiation()` prüft `running` in Schleife alle 20ms:<br/>```python```<br/>```while self.running:```<br/>```    if elapsed >= duration:```<br/>```        break```<br/>```    # ...```<br/>```    time.sleep(0.02)```<br/>`````` | **Test-Kriterien:**<br/>• Stop-Reaktionszeit < 50ms<br/>• Keine Race Conditions (GIL schützt Flags)<br/>• Thread beendet sich gracefully<br/><br/>**Ergebnis:**<br/>✅ Stop wird in < 50ms ausgeführt<br/>✅ Flag-basierte Kontrolle ist deterministisch | ✅ Erreicht |
| **1.4** | Zuverlässigkeit:<br/>Präzises automatisches Abschalten | Controller, System | `RadiationController`<br/>`SystemLayer` | **Methoden:**<br/>`_run_radiation(duration: int)`<br/><br/>**Timing via SystemLayer (ISystemAccess):**<br/>```python```<br/>```start_time = time.time()```<br/>```while self.running:```<br/>```    elapsed = time.time() - start_time```<br/>```    if elapsed >= duration:```<br/>```        break```<br/>```    time.sleep(0.02)  # 20ms Polling```<br/>`````` | **Test-Kriterien:**<br/>• Präzision: ±50ms auf Zieldauer<br/>• Konsistenz über mehrere Durchläufe<br/>• Keine Drift bei langen Strahlungszeiten<br/><br/>**Ergebnis:**<br/>✅ Genauigkeit: ±50ms (durch 20ms Polling-Intervall)<br/>✅ `time.time()` ist hochpräzise (Nanosekunden)<br/>✅ Konsistente Abschaltung in allen Tests | ✅ Erreicht |

---


