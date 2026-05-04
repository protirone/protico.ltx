<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


---

### Block 1: Allgemeine 'Netzwerkkonzepte'

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:90:1.1**</span>

*Netzwerke werden auch nach der Art ihrer Struktur klassifiziert.*

* 1.1.1 __Nennen Sie zwei Netzwerk-Topologien.__ (3P)
* 1.1.2 __Beschreiben Sie eine dieser Topologien.__ (3P)
* 1.1.3 __*Definieren Sie die Topologie 'BAUM'.*__ (3ZP)

<!-- uebung::end -->

Lösung: 

* lf.09/sbj-02.network-concepts-zenprese.pdf Sheet 6
* gerichteter azyklischer Graph + 
  * jeder Knoten 0-1 Vaterknoten
  * jeder Knoten 0-n Töchterknoten
  * Wurzelknoten: 0 Vaterknoten
  * Blatknoten: 0 Töchterknoten

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:90:1.2**</span>

*Es gibt zwei Schichtenmodelle, die Begriffe und Konzepte der Netzwerktechnologie ordnen sollen.*

* 1.2.1 __Nennen Sie die Namen beider Modelle.__ (2P)
* 1.2.2 __Nennen Sie die Namen der vier unteren Schichten des feineren Modells.__ (2P)
* 1.2.3 __*Beschreiben Sie Funktion der beiden unteren Schichten (des feineren Modells).*__ (2ZP)

<!-- uebung::end -->


Lösung:

* OSI-Referenzmodell u. TCP/IP-Schichtmodell
* physikalische Schicht, Sicherungsschicht, Vermittlungsschicht, Transportschicht
* *Extrapunkte:* physikalische Schicht = Bitübertragung, Sicherungsschicht = Absicherung der Übertragung gegen physikalische Einschränkungen

---

### Block 2: Präsentationen und Rechte 

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:90:2**</span>

Es gibt ein spezielles Lizenzsystem für freie Bilder und Texte, über das uns die Autorinnen ihre Nutzungsrechte verlässlich übertragen können:

* 2.1: __Nennen Sie den Lizenzoberbegriff und den Namen zweier konkreter Lizenzen.__ (3P)
* 2.2: __Beschreiben Sie, welche Rechter Dritter wir sonst noch beachten müssen, selbst wenn wir ein nach diesem freien Lizenzsystem lizenziertes Bild in unsere Präsentationen einbauen__. (1 Punkt)
* 2.3: __*Nennen Sie den Namen der Regelung, mit der wir Fotografien von Gebäuden legal nutzen können, und beschreiben Sie, wie sie funktioniert.*__ (4ZP)

<!-- uebung::end -->


Lösung:

* Creative Commons Lizenzen, CC-BY CC-BY-ND, ...
* Das Recht am Bild der Aufgenommenen, Persönlichkeitsrecht
* Panoramafreiheit: Ich darf aufnehmen und verwenden, was ich von einem frei zugänglichen Weg/Ort aufnehmen kann.

---

### Block 3: Layer-II-Elemente
  
<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:90:3**</span>

* 3.1.1 __Beschreiben Sie, was ein *Repeater* seiner intendierten Aufgabe nach tut.__ (2P)
* 3.1.2 __Beschreiben Sie, was ein *Hub* seiner intendierten Aufgabe nach tut.__ (2P)
* 3.1.3 __*Erläutern Sie den strukturellen Zusammenhang zwischen Hub und Repeater.*__ (1ZP)

* 3.2.1 __Beschreiben Sie, was eine *Bridge* ihrer intendierten Aufgabe nach tut.__ (2P)
* 3.2.2 __Beschreiben Sie, was ein Layer-II-*Switch* seiner intendierten Aufgabe nach tut.__ (2P)
* 3.2.3 __*Erläutern Sie den strukturellen Zusammenhang zwischen Hub, Switch und Bridge.*__ (1ZP)

* 3.3 __*Erklären Sie, welche Fähigkeiten Switch und Bridge haben, die Repeater und Hub nicht haben.*__ (2ZP) 

<!-- uebung::end -->

Lösung: 

* Repeater: zwei IO-Ports, nimmt ein eingehendes Signal an, verstärkt es und sendet es an die je andere Seite weiter. 
* Hub: mehrere IO-Ports, nimmt ein eingehendes Signal an, verstärkt es und sendet es **an ALLE anderen** weiter.
* Ein Hub ist ein Repeater mit mehreren Ausgängen.

* Bridge: Minderung der Kollisionen*
* Switch: Gewährleistung der Kollisionsfreiheit in einem voll-verswitchten Netz.
* Ein Switch ist ein Hub hinter dessen jedem IO-Port jeweils eine Bridge hängt.
 
* Repeater und Hub leiten die Signale einfach nur durch. Sie sind dumm. Bridge und Switch interpretieren die Signale und arbeiten mit den darin enkodierte Source- und Destination-Angaben

---

### Block 4: Dokumentationen / Diagramme

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:90:4**</span>

*Die Kommunikation auf Layer-II bzw. auf Hub-, Bridge- oder Switchebene ist mittels des Adress-Resolution-Protokolls geregelt*:

* 4.1.A __Dokumentieren Sie per Sequenzdiagramm die Übermittlung der Nachricht "Welcome R3, your R1" in einem rein HUB basierten Netz, bestehend aus 3 Rechnern + HUB. Die Nachricht möge von R1 zu R3 gesendet werden.__ (6P)

  **ODER** 

* 4.1.B __Dokumentieren Sie per Aktivitätsdiagramm die Übermittlung der Nachricht "Welcome R3, your R1" in einem rein HUB basierten Netz, bestehend aus 3 Rechnern + HUB. Die Nachricht möge von R1 zu R3 gesendet werden.__ (6P)

* 4.2 __Dokumentieren Sie per Sequenzdiagramm die Übermittlung der Nachricht "Welcome R3, your R1" in einem vollverswitchten Netz, bestehend aus 3 Rechnern + Layer-II-Switch. Die Nachricht möge von R1 zu R3 gesendet werden.__ (8ZP) [Abstrahieren Sie dabei vom inneren Aufbau Layer-II-Switches]

<!-- uebung::end -->


Lösung:

* für 4.1.A: analog zu sbj-04.arp-hub-zenprese.pdf / Folie 06
* für 4.1.b: analog zu sbj-04.arp-hub-zenprese.pdf / Folie 05
* für 4.2: analog zu sbj-06.arp-router-zenprese.pdf / Folie 06

---

<!-- uebung::start -->

### Bewertung

* 28 Standardpunkte (P) + 21 Zusatzpunkte (ZP) möglich.
* 28 Punkte insgesamt = 2.0
* 33 Punkte insgesamt = 1.0
* Rest: [https://www.lehrerfreund.de/notenschluesselrechner/form-ihk-notenschluessel] mit dem Höchstwert 33

<!-- uebung::end -->

---