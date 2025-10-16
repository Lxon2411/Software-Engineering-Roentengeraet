# Pflichtenheft: Kontrolle der Strahlungsdauer für ein Röntgengerät

1. Eingabe der Strahlungsdauer
   - Der Benutzer kann die Strahlungsdauer in Sekunden eingeben.
   - Die Eingabe wird auf gültige, positive Zahlen geprüft.
   - Ungültige Eingaben lösen eine Fehlermeldung aus.
2. Starten der Strahlung
   - Die Strahlung kann über einen "Start"-Button gestartet werden.
   - Der Timer startet mit der eingestellten Dauer.
   - Nach Start ist die Eingabe der Dauer & der Start-Button deaktiviert.
3. Stoppen der Strahlung
   - Die Strahlung kann jederzeit über einen "Stopp"-Button beendet werden (z.B. bei einem Notfall).
   - Stoppen setzt den Timer zurück.
   - Nach Stopp sind die Eingabe der Dauer und der Start-Button wieder aktiviert.
4. Automatisches Abschalten
   - Nach Ablauf der eingestellten Strahlungsdauer schaltet die Strahlung automatisch ab.
   - Der Benutzer wird über die automatische Beendung informiert (z.B. Signal oder Warnmeldung)
5. Statusanzeige
   - Stauts-LED zeigt den aktuellen Zustand der Strahlung an:
     - Grün für "Strahlung an"
     - Rot für "Strahlung aus"
6. Anzeigen der aktuellen Strahlungsdauer
   - Implementierung einer angenehm sichtbaren Anzeige der aktuellen Strahlungszeit (z.B. in Form eines Timers & eines Fortschrittbalkens)
   - möglichst simpel und kompakt
   - verzögerungsfreie Aktualisierung
