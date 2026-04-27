<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

## M5: proTironeComputatri: Freie Lehr- und Lerndokumente für die Ausbildung zur Fachinformatikerin an Berufsschulen

* Köln, Smartvillage
* Schanzenstraße 6-20, Gebäude Nr. 2.19/Kupferwerke 51063 Köln
* 17:00-17:45 UHR, Raum „Paraguay“


### 1.) Wie ich zum Thema 'Unterrichtsmaterialien' gekommen bin. **[→ ZP:Sheet:2]**

* Biete Schülerinnen Training zum Thema Präsentation an.
* Fachinformatiker brauchen das.
* Lehre immer: keine Selbstvorstellung.
* Und jetzt mache ich es selbst.
* Denn es ist eine legitime Frage: warum hier so ein Rentner?

* **01.10.2024**: Renteneintritt
  * vorher 35 Jahre Softwareentwickler
  * davon 26 Jahre eng verbandelt mit der Open-Source-Entwicklung
  * davon zuletzt 23 Jahre bei Deutsche Telekom
  * zuletzt als Principal-Open-Source-Advisor
* Wollte aber immer länger arbeiten.
* Warum nicht bei der Telekom? Betriebsrat / Abbauzahlen
* Selbsterinnerung: 1. Staatsexamen
* Bewerbung bei Schulamt Weilburg, völlig unbürokratisch
* 2 Anrufe
  * Grundschule an Grenze zu NRW: zu langer Fahrtweg
  * Stephan Bach, Gewerbliche Schulen Dillenburg: "Wir müssen reden"
  * bestes Bewerbungsgespräch meines Berufslebens
  * tolle Schule, Kollegium, Berufsschule

Aber:

* Einen Monat davor:
  * Studium des Rahmenlehrplans **[→ ZP:Sheet:3]**
  * Lernen der Lernfelder **[→ ZP:Sheet:4]**
  * ihre Verteilung über die 3 Lehrjahre, ihre Dauer
  * ernüchternde High-Flyer-Beschreibung im RLP
  * Entdecken der Prüfungskataloge mit etwas spezifischeren Anforderungen **[→ ZP:Sheet:5]**
    * (c) ZPA-Nord-West / Vertrieb U-Form-Verlag

**WAS ES ABER NICHT GAB**

* Stunden-/Stoffvermittlungspläne
* Unterrichtsmaterialien

Natürlich im Internet gesucht:

* immer wieder im universitären Kontext "Fach Informatik" gelandet,
* einige Unterrichtsmaterialien für gymnasiales Fach Informatik gefunden,
* aber keine systematische Abdeckung eines oder gar aller Lernfelder.
* Bei dem, was vorlag, Nutzungsrechte nicht oder unklar geregelt

Am 27.05.2025 in fachinformatiker.de gefragt

> Ich suche schon eine Weile nach Lernfeld-bezogenen Unterrichtsmaterialien für Fachinformatiker. Nur eben wirklich freie, also solche, die unter einer Creative-Commons-Lizenz oder einer Open-Source-Lizenz weitergegeben werden. Ich möchte halt sicher sein, dass ich sie wirklich nutzen und/oder bearbeiten und nutzen darf.
> Kennt jemand ein Repository, dass so etwas bereitstellt? Kennt jemand Lehrer, die ihre Arbeiten unter solch eine Lizenzierung weiterreichen?

Antwort der Lehrer/Lehrlinge:

* Nein.
* Antwort von skylake (Berufsschullehrer Fachinformatik u. Prüfer): 

> 1. 'Komplett von mir erstelltes Material gebe ich auch nicht mehr frei, da es bereits in der Vergangenheit vorkam, dass dieses dann von anderen unter deren Namen für Geld veräußert wurde oder zumindest der Urheber verfälscht wurde.'
> 2. 'Auch keiner meiner Kollegen veröffentlicht sein Material eben aus den genannten Gründen.'
> 3. Es gäbe aber 'inf-schule.de'. Die Materialien zielten aber auf Sek 1 und Sek 2 ab.


### 2.) Was hätte ich mir zu erhalten gewünscht. 

* 1. Für jedes Lernfeld 
  * eine Liste der Topics, die in einem Jahr (oder einem halben) zu behandeln wären 
  * ausgerichtet und abgeglichen mit den Prüfungskatalogen und den tatsächlichen Prüfungen. **[LF.09-Curriculum]**
* 2. Eine aufeinander aufbauende Folge von Unterrichtseinheiten - den Topics zugeordnet. **[LF.09-Curriculum-Checkliste]**
* 3. Für jedes Topic ein (oder mehrere) Unterrichtseinheiten - klar zugeordnet **[LF.09-Topi-Checkliste]**
* 4. Für jede Unterrichtseinheit (z.B. arp-router)
  * eine visualisierende Präsentation zur Veranschaulichung für die Schülerinnen,
  * ein Tonspur-Dokument, das den von mir anhand der Folien einzubringenden Stoff in Stichworten vorgibt,
  * darin eingebetteten Schüleraufgaben und Lösungen,
  * ein Aufgabenexzerpt ohne Lösungen zum Verteilen an die Schüler.

Und das alles unter einer CC- oder einer Open-Source-Lizenz. 

Im Zuge der Suche danach, bin ich auf erfreuliche Tatsachen gestoßen **[→ ZP:Sheet:6]**

1. Es gibt schon einen Begriff dafür: *Open Educational Resources*.
2. Der Begriff ist international und institutionell hoch aufgehängt: bei der UNESCO
3. Deutschland arbeitet in der Sektion mit.
4. In Deutschland gibt es mit OERinfo eine Organisation, die diese Idee aktiv vorantreibt.
5. Das Ministerium für Bildung, Familie, Senioren, Frauen und Jugend unterstützt das mit einer Konferenz.


Sehr tröstlich!

### 3.) Wie hätte ich so etwas als Open-Source umgesetzt?

* eine GitHub-Organisation als Rahmen/Anlaufstelle für verschiedener Repositories
  * → [https://github.com/protirone/](https://github.com/protirone/)
* darin ein "UE-Download-Repo", das 
  * die fertigen Materialien für die 'Fachinformatik' 
  * nach Lernfeldern sortiert
  * als PDFs zum Download bereitstellt.
  * → [https://github.com/protirone/protirone.lessons](https://github.com/protirone/protirone.lessons)
* darin auch ein "UE-Quell-Repository" mit 
  * dem Source-Code oder der veränderbare Datei
  * allen Bildern, 
  * und Makefiles,
  * aus und mit denen die PDFs generiert werden
  * → [https://github.com/protirone/protico.ltx](https://github.com/protirone/protico.ltx)
* bei jedem Repository für Außenstehende die Möglichkeit, mit BUG- und Features-Issues schnell mal Änderungen anzustoßen
  *  → [https://github.com/protirone/protico.ltx/issues](https://github.com/protirone/protico.ltx/issues)

### 4.) Was hätte die Allgemeinheit davon? 

1. Lehrer hätten fein-granulare systematisch verbunden Unterlagen, auf die sie aufsetzen, weiterverwenden könnten und dürften. 
2. Schüler könnten diese freien Lehrmittel auch als Lernmittel verwenden und ausgehändigt gekommen.
3. Lehrer/Schülerinnen könnten Arbeiten durchsehen, kommentierten und mit automatisierten Prozessen verbessern.
4. Das Einzelkämpferdasein der Lehrer (unter- und gegeneinander) hörte auf: Viele könnten ihr Weniges einbringen und es entstünde eine große Fülle und Vielfalt!
5. Schüler könnten sich das, was bei Ihnen im Unterricht fehlt (30:60-Regel) holen.
6. Es bräuchte keine Institution und kein Budget, um die Materialien zu hosten. (GitHub frei, MS gesponsert. *inf-schule.de* dagegen vom "Pädagogisches Landesinstitut Rheinland-Pfalz. Was, wenn das Budget gekürzt wird?).
7. Es bestünde keine Gefahr des Datenverlustes wegen Plattformabschalten: git/github ist ein verteiltes System

### 5.) Womit hätte bei solch einer Unternehmung kommunikativ rechnen müssen? **[→ ZP:Sheet:7]**

Wer freie Dokumente offen anfragt oder bereitstellt, trifft auf einen rauen Ton:

* Mir wurde Faulheit unterstellt

> Whiz-zarD@fachinformatiker.de: 'Ich denke, er sucht komplett fertige Aufgaben/Präsentationen, die er einfach nur runterladen braucht. Sprich, er möchte seine Arbeit outsourcen und das gratis'

* Wegen Fehlern wurde meine Kompetenz angriffen und die Arbeit an sich desavouiert: 

> Skylake@fachinformatiker.de: 'absolute Grundvoraussetzungen, dass Unterrichtsmaterialien fehlerfrei sind', 

> Skylake@fachinformatiker.de: 'wäre der Kollege bei mir in der Probezeit hätte er zumindest ein weniger angenehmes Dienstgespräch.'
> Skylake@fachinformatiker.de: 'Mich nervt es persönlich, dass der Berufsstand Lehrer so negativ verschrien ist und genau solche Materialien sind dann ein Grund, warum Personen meinen, Lehrer haben per se alle keine Ahnung.'

(Anlass war eine falsche Zuordnung von HUB zu Layer-II und HTTP zu Layer V statt VII im OSI-Modell)


Wer in der Open-Source-Szene arbeitet, muss damit rechnen, dass einige, die 'kommentieren'
* die schrittweise Verbesserung in der Open-Source-Entwicklung selbst nicht erlebt haben
* von einem selbst erdachten 'So-Ist-Es-'-Modell ausgehen.


### 6.) Braucht es wirklich eine Qualitätssicherung? **[→ ZP:Sheet:8]**

In einer Diskussion ging es um die Forderung nach einer institutionalisierten Qualitätssicherung:


> hellerKopf@fachinformatiker.de: Es gibt noch eine 'wichtige Zwischenstufe', die 'Qualitätssicherung'. 'Es ist eben nicht nur wichtig, dass etwas öffentlich verfügbar ist, sondern auch, dass es didaktisch bzw. fachlich belastbar veröffentlicht ist. Nicht, weil man sich abschotten sollte, sondern weil es sinnvoll wäre, wenn Material erst einmal von einem kleineren Kreis geprüft, kommentiert und überarbeitet werden könnte, bevor es für alle sichtbar öffentlich wird.'

* Dahinter steht das Denkmodell 'Arbeiter' und 'Prüfer' und 'Zertifikat der Korrektheit'.
* Das ist 'institutionalisierte Qualitätssicherung' - wie ofzt in großen Firmen verankert.
* Aber: Das Komplementäruniversum ist unendlich:
  * Es gibt unendlich viel mehr mögliche Fehler als Richtiges.
  * Zu überprüfen, dass die Fehler nicht eintreten etc., ist unmöglich.
  * Deshalb clustern Qualitätssicherungsabteilung.
  * Und damit ist der Nachweis einer absoluten Fehlerlosigkeit schon unterlaufen.

* Die Open-Source-Entwicklung geht anders vor:
  * Offenheit des Quellcodes als prinzipielle Kontrollmöglichkeit
  * freie Nutzbarkeit ohne Qualitätszusagen (Disclaimer)
  * uninstitutionalisierte Communities als Umsetzung des Mehraugenprinzips (Die noch extremere Variante des Xtreme-Programmings).
  * Das Bereitstellen eines öffentlichen Reporting-, Debugging- und Verbesserungssystems.

* Erfahrung in meinem Unterricht: Meine Schülerinnen
  * mögen es, auf Ungenauigkeiten und Fehler hinweisen zu dürfen
  * durchdenken Dinge genauer, wenn sie die Wirken ihres Mitdenkens in Verbesserungen sehen
  * sind stolz darauf, als Kontributoren genannt zu werden. **→ [https://github.com/protirone/protico.ltx/blob/main/CONTRIBUTORS.md](https://github.com/protirone/protico.ltx/blob/main/CONTRIBUTORS.md)**

für OER-Verbesserung 

* keine 'institutionalisierte Qualitätskontrolle',
* sondern mehr Mitwirkende, die mehr sehen.

### 7.) Was wäre mein BIG-Picture? 

* 1) Es würden weitere Fachinformatiklehrerinnen ein Lernfeld übernehmen: Eigenes Repository ...
   * →  [https://github.com/protirone/protico.ltx/tree/main/sources](https://github.com/protirone/protico.ltx/tree/main/sources)
* 2) Es gäbe für die Lernfelder die Kern von Aktiven und das Feld der Diskutanten und Reviewer
* 3) Es stießen andere Unterrichtsfächer zu diesem Modell der OER-Entwicklung dazu
  * →  [https://github.com/protirone/protirone.lessons](https://github.com/protirone/protirone.lessons)

Oder kurz:

Es gäbe ein ganzes Biotop von OER-Dokumenten für die Fachinformatik an Berufsschulen - und für alle anderen Schulenformen auch.

