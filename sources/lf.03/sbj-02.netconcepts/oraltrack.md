<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 1.) Grundlegende Begriffe **[→ ZP:Sheet:2]**

Im Lernfeld 03 kommt es in erster Linie darauf, Begriffe und Konzepte kennenzulernen. In der Mittelstufe in Lernfeld 09 wird es dann um das Zusammenwirken und das Ineinandergreifen gehen.

* [ ] Alarmanlage**: 
* [ ] Archivierungssystem**:
* [ ] Anwendungssoftware**:
* [ ] CRM**:
* [ ] ERP**:
* [ ] Datacenter**:
* [ ] Datenendgerät**:
* [ ] Datensicherung**:
* [ ] Drucker**:
* [ ] Gefahrenmeldeanlage**:
* [ ] Host**:
* [ ] Ip-Adresse**:
* [ ] Kopierer**:
* [ ] LAN**:
* [ ] Scanner**:
* [ ] Network-Devices**:
* [ ] PC-Arbeitsplätze**:
* [ ] Router**:
* [ ] Rechenzentrum**:
* [ ] Paket**:
* [ ] Server**:
* [ ] Speicher**:
* [ ] Switch**:
* [ ] Telefone**:
* [ ] TK-Anlage**:
* [ ] Videoüberwachung**:
* [ ] WLAN/Wi-Fi**:
* [ ] Zahlungsverkehr**:
* [ ] Zeiterfassung**:
* [ ] Zutrittskontrolle**:

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF03:02:Begriffe:01**</span>

* [ ] Suchen Sie in drawio Standardsymbole für Netzwerkgeräte. (Gruppe Network)
* [ ] Konzipieren und dokumentieren Sie ein Netzwerk, zu dessen sprachlicher Beschreibung man möglichst viele der o.a. Begriffe benötigte.  

Hinweis:

1. Beginnen Sie mit den Begriffen, die Netzwerkgeräte im engeren Sinne meinen.
2. Eine unvollständige repräsentierte Lösung ist besser als eine reine gedachte, vollständige.
3. Kooperieren Sie.


<!-- uebung::end -->

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF03:02:Begriffe:02**</span>

* [ ] Installieren Sie Freeplane auf Ihrem Rechner (eine freie Mindmap-Software)
* [ ] Bilden Sie zwei Gruppen
* [ ] Konzipieren Sie in ihrer Gruppe eine Mindmap, die obige Begriffe sortiert.
* [ ] Erstellen Sie eine Liste der Begriffe, die in dieser Liste noch fehlen.
* [ ] Ordnen Sie diese fehlenden Begriffe in Ihre Mindmap ein.

Hinweis:

1. Beginnen Sie mit den Begriffen, die Netzwerkgeräte im engeren Sinne meinen.
2. Eine unvollständige repräsentierte Lösung ist besser als eine reine gedachte, vollständige.
3. Kooperieren Sie.


<!-- uebung::end -->

---

### Definitionen zum Netzaufbau: [→ ZP:Sheet:3]

* **`arp`**:
  * Adress-Resolution-Protokoll
  * Tool, mit dem der Zustand des jeweiligen ARP-Caches angezeigt werden kann.
* **Broadcastdomain**:
  * wird von einem *Switch* 'aufgespannt'
  * umfasst alle Geräte, 
    * die an den Switch angeschlossen sind =
    * an die der *Broadcastrequest* gesendet wird
* **Broadcastadresse**:
  * meint alle Geräte einer Broadcastdomain,
  * nutzt auf MAC-Adressebene (Layer II) `FFFFFF`
  * nutzt auf IP-Adressebene (Layer III) höchste IP im Subnetz
* **CIDR-Notation**:
  * steht für *Classless Inter-Domain Routing*
  * wird hinter einer IP-Adresse notiert als '/XY'
  * *XY* ist die Anzahl der Bits, die zum Netzteil der IP-Adresse gehören 
* **DHCP**
  * ein Server, der einem Rechner auf Anfrage seine Netzschittstellenkonfiguration schickt
  * liefert auf Anfrage (mindestens) IP-Addresse, Subnetzmaske und Gateway-Ip-Adresse 
* **DMZ**:
  * steht für *Demilitarisierte Zone*
  * meint einen Bereich, in den es von außen leichter hineinzukommen ist
  * steht vor einem stärker geschützten Bereich
* **Desktop PC**
  * Lokaler Rechner
  * steht auf dem Tisch
* **Drucker**:
  * Serverkomponente im Netz
  * nimmt Druckaufträge
  * liefert bedrucktes Papier.
  * **Netzwerdrucker**:
    * Serverkomponente im Netz
    * nimmt Aufträge von anderen Geräte im Netz
  * **Lokaler Drucker**:
    * angeschlossen an Rechner
    * nimmt Aufträge von diesem Rechner. 
    * Lokaler Drucker + Rechner zusammen können als Netzwerkdrucker fungieren
* **Firewall**
  * ist ein Programm
  * läuft meistens auf einem Router
  * erlaubt das Weiterleiten eines Paketes nur, wenn das den Regeln entspricht
  * kann Ip-Adressen, Netzadressen und/oder Ports blocken oder erlauben
  * wird zur Umsetzung zweier Strategien benutzt
    * *Default Allow Principle* = was nicht verboten ist, ist erlaubt
    * *Default Deny Principle* = was nicht erlaubt ist, ist verboten
* **Gateway-Adresse**:
  * Adresse des Routers, der die Weiterleitung von IP-Paketen in andere Netz übernimmt.
* **Hopping**:
  * bezeichnet das Weiterleiten eines Paketes von einem Netz ins nächste
  * meint das 'Hüpfen' des Paketes von einer Broadcastdomäne in die nächste.
* **IP-Adresse**: (s. sbj-09.ipv4-addresses\*, sbj-10.ipv4-classes\*)
*  **MAC-Adresse**: (s. sbj-07.mac-addresses\*)
* **Multicastadresse**:
  * adressiert impliziet eine Menge von Rechnern / Netzwerkinterfaces
  * adressiert eine bestimmte Komponente, die die Multicastadresse in mehre Unicastadressen auflöst und die Nachricht dahin weiterleitet
  * **`ping`**:
    * sendet ein Testpaket zu einem Rechner /Ip-Adresse, der das Testpaket zurückschickt,
    * dient zur Verifikation der Netzfunktionalität
* **Office-Lan**:
  * ein *Local-Area-Network*, in das Standgeräte von Nicht-IT-Mitarbeitern eingebunden sind
* **Remote Desktop**
  * "umgekehrter" Thin-Client
  * Desktopvisualisierung wird auf einem 'Server' berechnet,
  * aber zur eigentlichen Darstellung umgelenkt an einen Client
  * genutzt für Remotewartung
* **Route**
  * meint den Weg von einem Rechner zum nächsten,
  * hat ein Netz mehrere Router, kann es mehrere Wege von einem zum nächsten Rechner geben.
*  **Router**
   * ist in mindestens 2 Netze eingebunden,
   * leitet Pakete von einem Netz ins benachbarte weiter,
   * verbindet zwei Broadcastdomänen.
* **Smartphone** 
  * früher auch 'Handy',
  * englisch korrekt: Mobilephone
  * telefoniefähiger mobiler Kleincomputer
* **Switch**:
  * spannt eine Broadcastdomain auf,
  * **Layer-II-Switch**: 
    * arbeitet mit Layer-I/II-Mitteln
    * verwendet das Adress-Resolution-Protokoll (ARP) (Layer II)
    * versendet Nachrichten anhand von MAC-Adressen
  * **Layer-III-Switch**:
    * arbeiten mit Layer-I/III-Mitteln
    * baut Virtual Local Area Networks über der Layer-II-Switch-Funktionalität auf
    * verwendet außerdem das IP-Protokoll (Layer III)
* **Thin Client**
  * Komponente einer Client-Server-Architektur
  * bringt wenig eigene Rechenkapazität mit
  * delegiert viele Werte- und Visualisierungsberechnung an einen Server.
  * Je mehr der Server berechnet, desto stärker die Belastung des Netzes
* **Thick Client**
  * Komponente einer Client-Server-Architektur
  * bringt viele eigene Rechenkapazität mit
  * delegiert wenig Werteberechnungen einen Server.
  * "schont" das Netz
* **`tracert`** (W11) bzw. **`traceroute`**
  * listet die Hoppings (von einer Broadcastdomain in die nächste) auf, die nötig sind, um einen Zielrechner zu erreichen
  * guter Testzielrechner dafür ist `8.8.8.8`, der Google-DNS-Server
* **Unicastadresse**:
  * IP-Adresse, die ein bestimmtes Netzwerkinterface eines Rechners identifiziert
  * umgangssprachlich oft den Rechner, in dem das Netzwerkinterface eingebaut ist

### Definitionen zur Netztaxonomien:

* **Netztaxonomie nach Reichweite:** [→ ZP:Sheet:4]
  * **PAN**:
    * steht für *Personal Area Network*
    * Netzwerk aus mobilen Kleingeräten 
    * per Kabel (USB, FireWire) oder per Funknetz (IrDa, Bluetooth, WLAN) 
    * Reichweite: sehr gering (wenige Meter)
    * Beispiel: Mobile Phone als WLAN-Hotspot 
  * **LAN**:
    * steht für *Local Area Network*
    * Netzwerk für/in/auf einer/m Wohnung, Gebäude, Firmengelände, Campus
    * kabelgebunden
    * Reichweite: mehrere hundert Meter
  * **WLAN**:
    * steht für *Wireless Local Area Network*
    * lokales Funknetz
    * Reichweite: wenige Meter bis zu 500 - 1000 m 
      * (Einschränkungen [Dämpfung] durch Bauweisen u. Umgebungen)
      * über (aktive) WLAN-Repeater weiter ausdehnbar.
  * **MAN**:
    * steht für *Metropolitan Area Network*
    * fassen Ballungsgebiete / Großstädte zusammen. 
    * Übertragungen zwischen LANs zwecks geringerer Dämpfung oft mit Lichtwellenleiter.
    * Reichweite: bis zu 100 km 
  * **WAN**:
    * steht für *Wide Area Network*
    * verbinden große geografische Bereiche innerhalb von Nationen / Kontinenten. 
    * Reichweite bis zu 1000km.
  * **GAN**:
    * steht für *Global Area Network*
    * Reichweite: weltweit
    * Beispiel: 
      * Internet
      * weltweites Firmennetz, getunnelt durchs Internet

* **Netztaxonomie nach Funktionsnetz:** [→ ZP:Sheet:5]
  * **Office-LAN**: 
    * lokales Subnetz 
    * mit Standgeräten
    * kabelgebunden
  * **Server-Lan**:
    * lokales Subnetz 
    * mit Servern (meist) ohne eigenen Monitorzugang
    * kabelgebunden
  * **WLan**:
    * lokales Subnetz 
    * mit Servern und Mobilgeräten
  * **Intranet**:
    * Local Area Network
    * (meist) von einer Organisation / Firma
    * (meist) bestehend aus mehreren Subnetzen
    * (meist) aus privaten Adressen aufgebaut, die nach außen hinter ein (oder mehrerer) öffentliche IPs 'versteckt' werden.
    * *intra* = etwas, das innerhalb bestimmter Grenzen agiert
  * **Firmen-LAN**: wie Intranet
  * **Internet**: Netz zwischen zwei Intranets
    *  *inter* = etwas, das zwischen bestimmter Einheiten agiert / steht
  * **Providernetz**: 
    * Teil des Internets
    * Provider verbinden Unternehmen, Behörden, Privatleute mit dem Internet
  * **Carriernetz**: 
    * Teil des Internets
    * Carrier = Netzbetreiber
  * **Telefonnetz**: 
    * **analoge Telefonie**: Sprache/Töne → Wellen → Sprache/Töne
    * **IP basierte Telefonie**: Sprache/Töne → IP-Pakete → Sprache/Töne

* **Netztaxonomie nach Struktur/Topologie:** [→ ZP:Sheet:6]
  * **Linien**-Topologie
    * alle beteiligten Komponenten in Reihe geschaltet
    * jeder Knoten auch aktivier Signalverstärker (Repeater)
  * **Bus**-Topologie:
    * alle Knoten linear über ein Medium verbunden. 
    * keine aktiven Komponenten dazwischen.
    * Pakete ’verschwinden’ am Ende des Busses.
  * **Ring**-Topologie:
    * Jeder Knoten auch Signalverstärker (Repeater), in dem er kreisendes Pakete liest und weiterschickt: 
      * Ist es leer, ’steckt’ er seine Nachricht hinein. 
      * Ist es für ihn, sendet er ein leeres Paket. 
      * Ist es nicht für ihn, schickt er es so weiter.
    * Vorteil: große Ringlängen von mehreren 100 m möglich.
    * Nachteil: 
      * Unterbrechung des Rings oder Ausfall eines Knotens führt zum Ausfall des ganzen Netzes
      * Teilnahme verlangt regelkonforme Kooperation 
  * **Stern**-Topologie:
    * Alle Knoten sind an zentrale Komponente (Hub, Switch) angeschlossen.
    * Vorteil: gute Erweiterbarkeit, Stabilität. Ausfall eines Knotens führt nicht zum Netzausfall
    * Nachteil: Ausfall der zentralen Komponente führt zu Netzausfall, hoher Verkabelungsaufwand
    * Beispiel: Fast-Ethernet, FibreChannel, InfiniBand und ’Token Ring’ (=logisch Ring, physisch Stern mit zentraler Einheit ’Media Access Unit)
  * **Maschen**-Topologie:
    * Jeder Knoten ist mit mehreren (teilvermascht) oder allen (vollvermascht) anderen Knoten verbunden.
    * Vorteil: 
      * Fallen Teilnehmer oder Verbindungen aus, sind alternative Routen möglich, hohe Ausfallsicherheit des Netzes an sich.
      * Vollvermaschte Netze brauchen kein Routing (Jeder kennt den Weg zu dem)
    * Nachteil: Exponentiell wachsender Verkabelungsaufwand, (n! Möglichkeiten). 
      * ein voll(ständig) vermaschtes Netz entspricht einem "Vollständigen Graph" (= jeder Knoten mit jedem anderen Knoten durch eine Kante verbunden)
      * und hat demnach die Berechnungsformel (n*(n-1))/2 = Gaus'sche Summenformel
      * In (teil(!))vermaschten System relativ aufwendiges Routing
      * kostenintensiv: Im vermaschten Subnetz mit n Knoten braucht jeder Maschine/Knoten (n*(n-1))/2 Netzwerkinterfaces oder einen zugeordneten Switch/Hub mit (n*(n-1))/2 Ports
    * **Namensclash:**
      * deutsch: *vollvermaschtes System* von Maschen.
      * englisch: *full mesh topology* oder *fully meshed system*, NICHT: *mashed*! (mash = Brei, Matsch mashed = zerquestscht) 
    * **Zellen**-Topologie:
      * Bereiche der Erreichbarkeit überlagern sich, Geräte ’wandern’ von einer Zelle zur anderen.
      * Vorteil: Ausfall eines Gerätes betrifft nicht das Netz als solches.
      * Nachteil: begrenzte Reichweite von Basisstation
  * **Baum**-Topologie:
    * Definition:
      * Knoten = Blatt oder Wurzel oder Knoten. 
      * Jede Wurzel hat 1-n Verbindungen zu (Tochter-)Knoten.
      * Jede Knoten ist ein Blatt oder hat 1-n Verbindungen zu (Tochter-)Knoten.
      * Kein Knoten ist Tochter mehrerer Vaterknoten.
      * Jeder Knoten mit Töchterknoten ist deren Vaterknoten
    * Vorteil: Ausfall eines Knotens lässt das Netz bestehen. Gute Erweiterbarkeit. Große Entfernungen realisierbar.
    * Nachteil: Je höher der Knoten im Baum, desto größer die Engpassgefahr. Beispiel: Switch- / Hub-Subnetz



### Definitionen zur Netztaxonomien: [→ ZP:Sheet:7]

* OSI = "Open Systems Interconnection model“
* [ OSI auch: [Open Source Initiative]{https://opensource.org/} ]
* = "Referenzmodell für Netzwerkprotokolle"
* teilt die Kommunikation zwischen Rechnern in ”sieben in sich abgeschlossene Schichten auf" (→ Schreiner: Computernetzwerke, 2014, S.3): **[→ ZP:Sheet:4]**
  * **Layer VII** : *Application Layer* (= Anwendungsschicht)
    * Client-Server-Lösungen
  * **Layer VI** : *Presentation Layer* (= Darstellungsschicht)
    * MPEG, PNG, GIF, ASCII, UTF8,
  * **Layer V** : *Session Layer* (= Kommunikationsschicht)
    * http-Protokoll, smtp-Protokoll, ssh, ipsec
  * **Layer IV** : *Transport Layer* (= Transportschicht)
    * TCP-Protokoll, UDP-Protokoll, Ports
  * **Layer III** : *Network Layer* (= Vermittlungsschicht)
    * Routing, IP-Protokoll & -Adressen
  * **Layer II** : *Data Link Layer* (= Sicherungsschicht)
    * Switch, Hardwareadressen, MAC-Adresse, HUB
  * **Layer I**: *Physical Layer* (= Physikalische Schicht)
    * [L|W]AN: Kupferkabel | Glasfaser
    * [WLAN]: Richtfunk | Satelliten-Funk, Signalformen, Frequenzen,
    * TRANSmitter+reCIEVER, RJ-45 Kabel, CSMA/CD, Token-Ring, Kollisionsvermeidung


*Aber*

* Deutsche Namen z.T. irreführend:
  * Bei der 'Sicherungsschicht' geht es nicht um Datenverschlüsselung, sondern um die Sicherstellung der Zustellung von Datenpaketen.
  * Bei der 'Kommunikationsschicht' geht es nicht um die Kommunikation überhaupt, sondern um den Zusammenhang mehrerer Kommunikationsschritte. (= eben einer Session von Nachrichten)
* Zuordnung hat etwas Willkürliches an sich:
  * Ist das http-Protokoll ein Sessionprotokoll, kein Transportprotokoll? Andererseits setzt es ja auf TCP/IP auf.
  * Ist Layer V wirklich unabhängig von Layer IV, wenn einige Services nicht mit UDP umsetzbar sind, andere nicht mit TCP? 
  * Faktisch werden Layer-II und Layer-III-Elemente schon beim reinen ARP mit HUB gebraucht.
  
> OSI-Layer sind ein gute grobe Themenklusterung, keine strenge Taxonomie

vgl.:
* → [https://de.wikipedia.org/wiki/OSI-Modell](https://de.wikipedia.org/wiki/OSI-Modell)
* → [https://en.wikipedia.org/wiki/OSI_model](https://en.wikipedia.org/wiki/OSI_model) 
  

**Realisierung 2: TCP/IP-Referenzmodell [→ ZP:Sheet:8]**

verwendet nur 4 Schichten:

* **Applicationlayer** (Anwendung)
  * HTTP, UDS, FTP, SMTP, POP, Telnet, DHCP, OPC UA
  * TLS, SOCKS
* **Transportlayer** (Transport)
  * TCP, UDP, SCTP
* **Internetlayer** (Internet)
  * IP (IPv4, IPv6), ICMP (über IP)
* **Linklayer** (Netzzugang)
  * Ethernet, Token Bus, Token Ring, FDDI


* → [https://de.wikipedia.org/wiki/Internetprotokollfamilie](https://de.wikipedia.org/wiki/Internetprotokollfamilie)
* → [https://en.wikipedia.org/wiki/Internet_protocol_suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)


### Graphentheorie im Crashkurs
#### 
Theorie

* **Graph** = eine aus *Knoten* und *Kanten* bestehen Struktur
* **Knoten** = ein etikettierbarer Punkt/Ecke in einem Graph
* **Kante** = eine (direkte) etikettierbare Verbindung zwischen zwei Knoten
* **Pfad** ist eine Möglichkeit, von einem Knoten zum nächsten zu kommen (rekursive Definition):
  * Wenn in einem Graph *A* und *B* zwei Knoten sind und *AB* eine(!) Kante dazwischen ist,
    dann ist <*A*,*B*,*AB*> ein Pfad
  * Wenn <*X*, *A*, *XA*> ein Pfad ist und *A* und *B* zwei Knoten sind und *AB* eine Kante dazwischen ist,
    dann ist auch <*X, *B*, *XB*> ein Pfad
* **Ungerichteter Graph**: seine Kanten
  * werden durch Linien gekennzeichnet
  * haben keine Richtung
  * können in beide Richtungen durchlaufen werden
* **Gerichteter Graph** (engl. *Digraph*): seine Kanten
  * werden durch (implizite) Pfeile gekennzeichnet 
  * haben ein Richtung
  * können nur in Richtung der Pfeile durchlaufen werden
* **Zyklus in einem (gerichteten) Graph**:
  * Wenn <*X*, *A*, *XA*> ein gerichteter Pfad ist und *AX* eine von *XA* verschiednete Kante ist,
    dann ist <*X, *X*, *XB*> ein zyklischer Pfad (kurz: Zyklus)
* **Gerichteter azyklischer Graph** (engl. *DAG* / *directed acyclic graph*):
  * ist ein gerichteter Graph
  * enthält keine zyklischen Pfade
* **Baum** :- azyklischer Graph
  * Jeder Knoten hat 0 - 1 Väterknoten 
  * Jeder Knoten hat 0 - n Töchterknoten
  * **Vaterknoten**: In einem Pfad *AB* ist *A* der Vaterknoten von *B*
  * **Tochterknoten**: In einem Pfad *AB* ist *B* der Vaterknoten von *B*
  * **Geschwisterknoten**: Sind *A*,*B* und *C* Knoten mit Pfaden *AB* und *AC*, 
    dann sind *B* und *C* Geschwister 
  * **Wurzelknoten**: der Knoten mit 0 Väterknoten
  * **Blatt(knoten)**: die Knoten mit 0 Töchterknoten
* [→[https://de.wikipedia.org/wiki/Graph_(Graphentheorie)](https://de.wikipedia.org/wiki/Graph_(Graphentheorie)) ]

#### 
Praxis:

* IP-Adresssystematik 
* Domain-Namen
* Dateisystem

weil: 

* die jeweils nächst tiefer eingebettete Einheit entsteht durch Pfadverlängerung.
  * Verlängerung der Netzmaske
  * Verlängerung des Domainnamens durch weitere Spezifikatoren
* außer an der obersten Stelle sind zu jedem Pfad Geschwisterknoten denkbar



---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF03:02:Begriffe:01**</span>

* [ ] Repräsentieren Sie die Hexsymbole [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f] 
      als Liste von Listen mit 6 als Wurzelknoten und den Geschwisterknoten
      0, 1, 3, 4, 5 und 8, 9 und a, b, c, e, f:

* [ ] Erzeugen Sie dieselbe Struktur als System von Ordnern und Dateien und lassen
      Sie Ihr Ergebnis per `tree`ausgeben 

<!-- uebung::end -->

Lösung [→ ZP:Sheet:9,10]

---


### Protokolle und Pakete im Crashkurs 

**Pakete**

* haben immer eine Präambel und einen Payload
  * Die Präambel enthält die zur Adressierung notwendigen Informationen
  * Der Payload enthält die Nachricht
  * Def.:
    * PA mit <PRAEA [PAYA]> und PAYA=MESSAGE ist ein Paket.
    * Sind PX mit <PRAEX [PAYX]> und PY mit <PRAEY [PAYY]> Pakete, 
      dann ist auch <PRAEX [PRAEY [PAYY]]> ein Paket

Beispiel: 

* Einbettung IP-Paket in Ethernetframe im ARP (Adress-Resolution-Protokoll) [→ ZP:Sheet:11]
* Das kann ins Grundsätzliche gewendet werden [→ ZP:Sheet:12]
* IP-Adressen identifizieren Rechner/Netzwerkschnittstellen
* Ports identifizieren Applikationen, die das Betriebssystem beauftragt haben, bestimmte Pakete an sie weiterzuleiten. [→ ZP:Sheet:13]

**Protokolle**
* regeln welche Nachrichten in welchen Paketen mit welcher Abfolge erfolgen
* Beispiel: TCP/IP 3-Wege-Handshake

Beispiele: 

* http(s): 
  * Port 80 / 443 
  * Zum Download von Dokumenten mit den Schritten GET, POST, PUT, DELETE, ...
* smtp(s): 
  * Port 25 / 587 
  * Zum Versenden von Textdokumenten (Mails)
* ssh: Port 22
  * Zum Versenden von verschlüsselten Nachrichten
* ICMP: 
  * Internet Control Message Protocol
  * wird von Routern und Hosts benutzt, um Reports/Irritationen zu übermitteln

<!-- **Denkfrage:** Wieviel Pfade gibt es in einem ungerichteten Graph mit -->


