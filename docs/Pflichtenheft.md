# Pflichtenheft: Verwaltung & Überwachung der Strahlungsdauer für ein Röntgengerät

1. Eingabe der Strahlungsdauer
   - Der Benutzer kann die Strahlungsdauer in Sekunden eingeben.
   - Die Eingabe wird auf gültige, positive Zahlen geprüft.
   - Ungültige Eingaben lösen eine **Fehlermeldung** aus.
2. Starten der Strahlung
   - Die Strahlung kann über einen "Start"-Button gestartet werden.
   - Der Timer startet mit der eingestellten Dauer.
   - Nach Start ist die Eingabe der Dauer & der Start-Button deaktiviert.
3. Stoppen der Strahlung
   - Die Strahlung kann **jederzeit** über einen "Stopp"-Button beendet werden (z.B. bei einem Notfall).
   - Stoppen setzt den Timer zurück.
   - Nach Stopp sind die Eingabe der Dauer und der Start-Button wieder aktiviert.
4. Automatisches Abschalten
   - Nach Ablauf der eingestellten Strahlungsdauer schaltet die Strahlung automatisch ab.
   - Der Benutzer wird über die automatische Beendung informiert (z.B. Signal oder Warnmeldung)
5. Statusanzeige
   - Stauts-LED zeigt den aktuellen Zustand der Strahlung an:
     - Grün für "Strahlung an"
     - Rot für "Strahlung aus"
6. Benachrichtigung und Signale
   - **optische und/oder akustische Signale** bei:
      - Start der Strahlung.
      - Ende der eingestellten Dauer (automatischer Stopp).
      - Manuellem Notfall-Stopp
   - Signale müssen auch **bei Umgebungsgeräuschen** wahrnehmbar sein (z.B. LED + Piepton)
      
8. Anzeigen der aktuellen Strahlungsdauer
   - Implementierung einer angenehm sichtbaren Anzeige der abgelaufenen Strahlungsdauer (z.B. in Form eines Timers & eines Fortschrittbalkens)
   - möglichst simpel und kompakt
   - verzögerungsfreie Aktualisierung
9. Ereignisprotokollierung
   - Alle wichtigen Vorgänge werden geloggt:
     - Startzeit, Stopzeit, eingestellte Dauer.
     - Art des Stopps (automatisch oder manuell).
   - Protokoll muss **fälschungssicher und eindeutig** sein.
10. Systemverhalten bei Fehlern oder UNterbrechungen
   - Bei Stromausfall oder Softwareabsturz:
     - Strahlung wird **sofort deaktiviert.**
     - Beim Neustart wird der **letzte bekannte Zustand angezeigt**, aber keine automatische Wiederaufnahme.
     - Fehlerhafte Eingaben oder fehlende Hardwareverbindung führen zu **Fehlermeldung** und Sperrung der Startfunktion.
