<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

**[→ ZP:Sheet:2]**

### 1.A Netzwerk-Challenge

* **Netzwerk** = ein ganzer Stack aus Hardware und Software, nicht nur Rechner und Kabel =

> eine ganze Infrastruktur, die Datenendgeräten die Kommunikation, den Datenaustausch und die Nutzung gemeinsamer Ressourcen transparent ermöglicht (→ Schreiner: Computernetzwerke, 2014, S.3)

* **Transparent** bedeutet
	
>  der **Endbenutzer** muss sich nicht darum kümmern, mithilfe welcher Verfahren, Geräte und Medien die Informationen transportiert werden. (→ Schreiner: Computernetzwerke, 2014, S.3)

* **Aufbau** eines Netzwerkes meint also die Gesamtheit der Komponenten und ihr Zusammenwirken im Blick zu haben,
  * obwohl die *Menge der Netzwerkkomponenten* sehr heterogen ist (Kabel, Hub, Switch, Protokolle, Sender- und Empfängersoftware, Client- und Serverapplikationen, etc. etc.)
	* obwohl die Nutzung des Netzes für die Endbenutzerin transparent sein soll, 
	* obwohl es unklar ist, wer überhaupt die 'Endbenutzerin' ist:
  	* die, die die Komponenten zum System verkabelt?
  	* die, die einen in sich passenden Softwarestack zusammenstellt
  	* die, die eine Webapplikation mit Client-Server-Architektur programmiert
  	* die, die eine Webapplikation im Browser nutzt?

### 1.B Netzwerk-Ordnung: Die Referenzmodelle

**Lösung**: 

* Entwicklung eines Modells von je autonomen Schichten
* Zuordnung der Komponenten / Teile / Techniken zu den entsprechenden Schichten

**Realisierung 1: OSI-Referenzmodell [→ ZP:Sheet:3]**

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
  

**Realisierung 2: TCP/IP-Referenzmodell [→ ZP:Sheet:5]**

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


### 2 Netzwerk-Klassifikation anhand von Topologien [→ ZP:Sheet:6]**

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

Anmerkung:

* Ring-Topologie verlangt besondere Kooperation: Wer nach einem Paket an sich nicht ein leeres Paket reinstellt, sondern gleich ein neues eigenes, schließt andere von der Kommunikation aus.
* Baumtopologie ist eine hierarchische Erweiterung der Sterntopologie
* Netzwerke meist eng an der Topologie entlang grafisch dargestellt. (Netzstrukturplan, Network Architecture Diagram, etc.)
  * UML verwendet zudem mindestens 2 Grafiken, um das Funktionieren eines Netzes komplett darzustellen, nämlich *Sequenzdiagramm* (Nachrichtfluss) und *Aktivitätsdiagramm* (Übermittlungsaktivitäten).
  
* → [https://www.elektronik-kompendium.de/sites/net/0503281.htm](https://www.elektronik-kompendium.de/sites/net/0503281.htm)
* → [https://de.wikipedia.org/wiki/Topologie_(Rechnernetz)](https://de.wikipedia.org/wiki/Topologie_(Rechnernetz))
* → [https://de.wikipedia.org/wiki/Vollst%C3%A4ndiger_Graph](https://de.wikipedia.org/wiki/Vollst%C3%A4ndiger_Graph)

Hinweis:

Netzwerke zumeist als Topologie dargestellt. ()

### 3 Netzwerk-Klassifikation anhand von Reichweiten [→ ZP:Sheet:7]**

**Technische Grundidee**:

> Die größeren Einheiten setzen sich aus den nächste kleineren zusammen, wobei die ’Gateways’ der kleineren zu Komponenten eines Netzes der nächst größeren Art verbunden werden


* **Personal Area Network** (*PAN*): 
  * Netzwerk aus mobilen Kleingeräten 
  * per Kabel (USB, FireWire) oder per Funknetz (IrDa, Bluetooth, WLAN) 
  * verbundenen Netze mit sehr geringer Reichweite (wenige Meter)
* **Local Area Network** (*LAN)*: 
  * Netzwerk für/in/auf einer/m Wohnung, Gebäude, Firmengelände, Campus. 
  * Heute meist auf Ethernet-Standards (IEEE 802.3) basierend, 
  * früher (bis 1990) auch als Token Ring (IEEE 802.5) realisiert.
* **Wireless Local Area Network** (*WLAN*): 
  * Lokales Funknetz
  * zumeist auf Normenfamilie 802.11 basierend,
  * Ausdehnung von wenigen Meter bis zu 500 - 1000 m 
  * (Einschränkungen [Dämpfung] durch Bauweisen u. Umgebungen)
  * Über (aktive) WLAN-Repeater weiter ausdehnbar.
* **Metropolitan Area Network** (*MAN*): 
  * Verbinden LANs
  * fassen Ballungsgebiete / Großstädte bis zu 100 km zusammen. 
  * Übertragungen zwischen LANs zwecks geringerer Dämpfung oft mit Lichtwellenleiter. 
  * Für entsprechende Funknetze s. Standard WiMAX (Worldwide Interoperability for Microwave Access) (gemäß IEEE 802.16) [https://de.wikipedia.org/wiki/WiMAX](https://de.wikipedia.org/wiki/WiMAX)
* **Wide Area Network** (*WAN*): 
  * verbinden große geografische Bereiche innerhalb von Nationen / Kontinenten. 
  * Ausdehnung bis zu 1000km.
  * heute realisiert mit: Ethernet mit Durchsatzrate vom 10+xGBit/s
  * früher reslisiert mit: Asynchronous Transfer Mode (ATM) realisiert. 
* **Global Area Network** (*GAN*): 
  * Erstreckt sich über unbegrenzte geografische Entfernungen. 
  * Beispiel: Internet, weltweites Firmennetz

Ein Beispiel kann dies sein:

1. **PAN** :- eine Verbindung via Bluetooth zwischen unserem Laptop und unserem Smartphone im Klassenraum
2. **WLAN** bzw. **LAN** :- das WLAN / LAN in den Gewerblichen Schulen Dillenburg (oder mein Heimnetz in Altenkirchen)
3. **MAN** :- das Kupfer- bzw. Glasfasernetz der Telekom im Lahn-Dill-kreis (oder in Frankfurt)
4. **WAN** :- die Summe der verschalteten Netze in Deutschland (oder in Europa)
5. **GAN** :- das weltweite Internet

vgl.: Baun: Computernetze kompakt, 2022, S. 20ff

### 4 Netzwerkdesign in der Projektkommunikation [→ ZP:Sheet:8]**

* Strenge Netzwerkdiagramme sind in der Projektkommunikation nicht immer hilfreich
* Manchmal hilft ein "Bild" besser, das alle Aspekte übergreifend 'widerspiegelt'
* besonders wiederkehrend verwenden, um mit dem Wiedererkennungswert eine Botschaft zu verankern bzw. aufzufrischen.

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:02:Netzwerkbegriffe:01**</span>

* [ ] Analysieren Sie, was die Grafik [→ ZP:Sheet:8] widerspiegelt.

Hinweis: Sie ist in der Deutschen Telekom real verwendet worden, um ein Projektziel zu "skizzieren".

<!-- uebung::end -->

---
