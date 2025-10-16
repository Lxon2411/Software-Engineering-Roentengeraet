# Requirements: Verwaltung & Überwachung der Strahlungsdauer bei einem Röntgengerät

### 1. Funktionale Requirements

<table>
  <thead>
    <tr>
      <th>Nr.</th>
      <th>Titel</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr >
      <td>1.1</td>
      <td>Benutzerdefinierte Strahlungsdauer</td>
      <td>Der Benutzer kann die auf einen sinnvollen Wertebereich (1-120 sec) begrenzte Strahlungsdauer manuell eingeben.</td>
    </tr>
    <tr>
      <td>2.1</td>
      <td>Strahlung starten</td>
      <td>Der Benutzer kann die Strahlung manuell starten.</td>
    </tr>
    <tr>
      <td>3.1</td>
      <td>Automatisches Abschalten</td>
      <td>Die Strahlung wird nach Ablauf der eingestellten Dauer automatisch beendet.</td>
    </tr>
    <tr>
      <td>4.1</td>
      <td>Manuelles Stoppen</td>
      <td>Die Strahlung kann jederzeit, wenn aktiv, manuell gestoppt werden.</td>
    </tr>
    <tr>
      <td>5.1</td>
      <td>Statusanzeige und Fortschrittsanzeige</td>
      <td>Die aktuelle Strahlungsdauer, der Status (aktiv/inaktiv) und ein Fortschrittsbalken werden angezeigt.</td>
    </tr>
    <tr>
      <td>5.2</td>
      <td>Ereignis-Logging</td>
      <td>Start, Stopp (manuell oder automatisch) sowie abgelaufene Strahlungsdauer werden protokolliert.</td>
    </tr>
    <tr>
  </tbody>
</table>

### 2. Nicht-funktionale Requirements

<table>
  <thead>
    <tr>
      <th>Nr.</th>
      <th>Titel</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.1</td>
      <td>Benutzerfreundlichkeit</td>
      <td>Eingabe und Bedienung sollten intuitiv und ohne Verzögerung (<500ms) erfolgen.</td>
    </tr>
    <tr>
      <td>1.2</td>
      <td>Sicherheit</td>
      <td>Das manuelle Stoppen muss jederzeit bei aktiver Strahlung zuverlässig funktionieren.</td>
    </tr>
    <tr>
      <td>1.3</td>
      <td>Verständlichkeit der Anzeige</td>
      <td>Statusanzeigen und Fortschrittsbalken müssen auch für farbenblinde und sehbehinderte Nutzer gut lesbar sein.</td>
    </tr>
    <tr>
      <td>1.4</td>
      <td>Zuverlässigkeit</td>
      <td>Das automatische Abschalten muss präzise und ohne Ausfälle erfolgen.</td>
    </tr>
      <tr>
      <td>1.5</td>
      <td>Ressourcen-Effizienz</td>
      <td>Die Software soll ressourcenschonend (30-70 MB RAM, 0-1% CPU Auslastung) arbeiten.</td>
    </tr>
  </tbody>
</table>

### 3. Abhängigkeiten zwischen Requirements
- Das automatische Abschalten (3.1) ist abhängig von der korrekt eingegebenen Strahlungsdauer (1.1).
- das manuelle Stoppen (4.1) kann jederzeit unabhängig von automatischen Ablauf ausgelöst werden.
- Die Statusanzeige (5.1) muss sowohl den Start (2.1) als auch das Stoppen (3.1, 4.1) korrekt wiederspiegeln.
- Das Ergeignis-Logging (5.2) erfordert verlässliche Meldungen aus allen anderen Funktionalitäten.

### 4. Konflikte zwischen Requirements
- Keine direkten Konflikte erkennbar, da manuelles Stoppen jederzeit Vorrang vor automatischen Abschalten hat.

### 5. Zusammengehörigkeiten zwischen Requirements
- Eingabe (1.1) und Start (2.1) bilden die Basis für die Dauerüberwachung.
- Automatisches Abschalten (3.1) und manuelles Stoppen (4.1) beeinflussen die Statusanzeige und das Logging (5.1, 5.2).
