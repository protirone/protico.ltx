<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1) Routingvarianten **[→ ZP:Sheet:2]**


Knüpft an Lösung der IPv4-Segmentierungsaufgabe *LF09:10* an

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:01**</span>

* [ ] Ermitteln Sie, wie viele Wege (ohne Schleifen) es vom Developer-Netz (192.168.1.64/26) ins Finance-Netz (192.168.1.128/27) gibt.  

<!-- uebung::end -->

Lösung: 6 Routen **[→ ZP:Sheet:3]**


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:02**</span>

* [ ] Ermitteln Sie, wie viele Wege (ohne Schleifen) es vom Developer-Netz (192.168.1.64/26) ins Finance-Netz (192.168.1.128/27) gibt, wenn man folgende Regel(n) strikt anwendet:
  * Jeder Router empfängt Pakete über seine eine Schnittstelle in dem Netz, für das er das Defaultgateway ist.
  * Sind die Pakete auf der IP-Adresse-Ebene *nicht* an ihn adressiert, versteht er sie als Weiterleitungsauftrag.
  * Bei jedem weiterzuleitenden Paket überprüft der Router zuerst, ob das Paket wenigstens in das Netz gehört, in das seine andere Schnittstelle eingebunden ist
  * Wenn ja, sendet er das Paket in diesem Netz per ARP an den Adressaten.
  * Wenn nein, sendet er das Paket in diesem Netz per ARP an den Router, das für seine andere Schnittstelle als Defaultgateway konfiguriert ist, damit dieses ihm den Weiterleitungsauftrag abnimmt.

<!-- uebung::end -->

Lösung: Nur eine Defaultroute nach draußen. Also keine Kommunikation von (192.168.1.64/26) zu (192.168.1.128/27)  **[→ ZP:Sheet:4]**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:03**</span>

* [ ] Schlagen Sie eine Lösung für die Diskrepanzen vor.

<!-- uebung::end -->

Lösung: Routingtabellen **[→ ZP:Sheet:5]**

---

### 2) Routing als Technik

**Router**

* informieren die ihnen benachbarten Router, 
  * welche Netze an sie angeschlossen sind
  * welche Netze die ihnen benachbarten Router kennen
* kommunizieren über Routingprotokolle
* berechnen mögliche Routen und schreiben sie in die eigenen Routingtabellen
* berücksichtigen mehrere Kriterien, um die beste Route zu finden
  * Anzahl der Hoppings
  * Durchsatzgeschwindigkeit
  * Auslastung

→ vgl. Schreiner: Computernetzwerke, 2014 (2014), S. 86f

Grundsatz:

* Sind mehrere Router in einer Broadcast-Domäne eingebunden
* gibt es (sofern nicht durch Firewalls unterbunden)
* auch mehrere Wege (Hoppingsequenzen), einen Rechner auf Layer III-Ebene zu erreichen. 

**Routen**

* sind Wege, an die ein Router eine Frage weiterreicht, wenn er den Zielrechner nicht in seiner Broadcastdomäne findet
* werden manuell oder automatisiert in Routingtabellen eingetragen.
* die innerhalb eines segmentierten Netzes zu anderen Broadcastdomänen führen, müssen manuell oder automatisiert gepflegt werden.
* werden (auch) über Firewalls unterbunden

**Routingprotokolle**

existieren

* nutzen Router, um sich wechselseitig über die je nähere Umgebung zu informieren
* existieren, weil Anzahl und Vorkommen von Routern für Routingtabellen zu volatil ist
* werden in zwei Klassen eingeteilt
  * *Distance Vector Protokolle* tauschen Routingtabellen mit ihren Nachbarn aus.
  * *Link State Protokolle* senden Netzbeschreibungen an die Router einer Routerdomäne.

> Erst die Idee, dass Router sich wechselseitig über die je nähere Umgebung informieren,
> macht die "Vorgabe" erfüllbar, "[...] ein selbstkonvergentes, vermaschtes und weltweites
> Netzwerk zu entwickeln". 
>
→ vgl. Schreiner: Computernetzwerke, 2014 (2014), S. 88

* **Distance Vector Protokolle** 
  * tauschen ganze Tabellen aus 
  * erwarten, dass Empfänger das Tabellenformat verstehen 
  * (simpler + resourcensparend)
* **Link State Protkolle** 
  * beschreiben ihr Netz
  * erlauben es den Empfängern eigene Berechnung
  * können weitere Kreise bedienen 
  * (flexibel + rechenintensiv).

**Routingtypen**:

* **Dynamisches Routing** 
  * automatische Berechnung von Routen 
  * anhand von Informationen in den Routingtabellen 
  * mittels Austausche von Informationen.
* **Statisches Routing**
  * das manuelle Eintragen fester Routen an Routern
  * erfolgt meist an Grenzroutern
  * hat meist die Form *route alles, das nicht zu Deinem Adressbereich gehört, übers
Interface X zu Router Y*
  * kann lokal auch die Form haben *route alles [aus Subnetz X] an Subnetz Y über Router Z*
  * z.B. via `ip route add 192.168.1.0/24 via 10.0.0.1`

Hinweise:

* Provider nutzen *__Statisches und Dynamisches Routing__ mit speziellen __Weitverkehrsprotokollen__, um ganze Weitverkehrs-Routing-Domänen zu bilden.*
* __Dynamisches Routing__ impliziert Umlernen von Netzwerkstrukturen.
* Klassische Routingprotokolle sind
  * RIP (Router Information Protocol)
  * OSPF (Open Shortest Path First)
  * IGRP Interior Gateway Routing Protocol
* Moderne Protokolle mit VLSM (Variable Length of Subnet Masks) können fast
beliebig segmentieren, ältere nicht.
* Viele Protokolle sind proprietär und NICHT unbedingt auf Kompatibilität ausgelegt.

Konsequenz: Trotz *Vendorenfalle*

> " [...] in dynamischen gerouteten Umgebungen lieber einen definierten Hersteller wählen 
> und [...] eine möglichst homogene Umgebung aufbauen“

→ vgl. Schreiner: Computernetzwerke, 2014 (2014), S. 88


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:04**</span>

Das Tool `ip` (LNX) bzw. `route` (W11) kann aktuelle Routen auslesen und neue Routen setzen

* [ ] Schreiben Sie für alle Routen im Beispiel *LF09:10* bei den zuständigen Routern die Routingkonfiguration

<!-- uebung::end -->

Lösung **[→ ZP:Sheet:6]**

---


### 3) Firewalling als Technik

**Firewalls** können (mindestens)

* anhand der IP-Adresse eines Rechners
  * dessen Zugriff auf eine IP-Adresse oder ein IP-Subnetz 
  * zulassen oder blockieren (Layer III)
* anhand der Netz-Adresse eines Sub-Netzes allen Rechnern des Netzes
  * dessen Zugriff auf eine IP-Adresse oder ein IP-Subnetz
  * zulassen oder blockieren (Layer III)
* Anfragen an einen Port zulassen oder blockieren (Layer IV)
* Anfragen anhand von Mustern (Häufigkeit der Anfrage, Anfrageinhalt, Protokoll) 
  zulassen oder blockieren (Layer III - VII)

**Firewall-Strageien**

* __*ERLAUBE ZUERST ALLES, UNTERBINDE DANN DAS, WAS NICHT ERLAUBT SEIN SOLL*__:
  * 'Default Allow Principle'
  * Was nicht verboten ist, ist erlaubt/möglich 
  * Vorteil: einfach zu managen, weil 'Sonderwünsche' oft schon möglich sind.
  * Nachteil: eher unsicher, weil - Menschen bedingt - Schlupflöcher.
  
* __*UNTERBINDE ZUERST ALLES, ERMÖGLICHE DANN DAS, WAS ERLAUBT SEIN SOLL*__:
  * 'Default Deny Principle'
  * Was nicht erlaubt ist, ist verboten/unterbunden.
  * Vorteil: sicher (weil weniger Schlupflöcher)
  * Nachteil: aufwendig zu managen, weil 'Sonderwünsche' Aufwand bedeuten.



---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:05**</span>

* [ ] Ermitteln Sie, viele Firewalls Sie in diesem Netz mindestens wo brauchen, um alle Zugriffe so steuern zu können, wie in der Segmentationsaufgabe LF09/10 gewünscht.

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:7]**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:06**</span>

* [ ] Überlegen Sie, ob und wie Sie mit diesen Informationen über Routing- und Firewalltechniken die bisherige Lösung aus Teilnetzen und Routerübergängen verfeinern können.
* [ ] Zeichnen Sie das 'kondensierte Netz', wenn es existiert. 

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:8]**

---

### 4) Demilitarized Zone DMZ  **[→ ZP:Sheet:9]**

> "A 'demilitarized zone' is an area, agreed upon between the parties to an 
> armed conflict, which cannot be occupied or used for military purposes by 
> any party to the conflict." [→ [https://casebook.icrc.org/a_to_z/glossary/demilitarized-zones](https://casebook.icrc.org/a_to_z/glossary/demilitarized-zones)]

Hat in der IT aber eine andere Bedeutung:

Eine DMZ

* meint einen Bereich zwischen den Routern ins Internet und den Routern in nachgelagerte Netze (Intranet, ...).
* erlaubt es, mittels unterschiedlich starken Firewalls für nachgelagerte Rechner stärker geschützte Bereiche vom Eingangsbereich abzugrenzen

Idee:

> In der DMZ dürfen/können von außen kommende Rechner mehr als in der nachgelagerten geschützten Zone.


gibt es als: **[→ ZP:Sheet:10]**
  
* **einstufige DMZ**: trennt die Bereiche mit einem Router 
* **zweistufige DMZ**: trennt die Bereiche mit zwei Routern 

**Strategie für zweistufige DMZ**:

* Außenrouter/Gateway
  * Lasse initial alle Anfragen von außen zu. 
  * Erlaube alle Anfragen von innen nach außen.
  * Unterbinde danach nur die Art von Anfragen von außen aus, die an keiner Stelle zulässig sind, weder in der DMZ, noch im Intranet.
  * Verbiete außerdem die Art von Anfragen von innen nach außen, die Du generell keinem Rechner/Mitarbeiter erlauben willst.

* Binnenrouter/Intranet
  * Verbiete initial alle Zugriffe von außen. 
  * Erlaube danach von außen und innen nur die Serviceanfragen, die Du in dem Intranet(teil) erlauben willst (https, smtp, vpn-software)
  * Erlaube den Zugriff von außen für gewisse feste IP-Adressen (Vorsicht IP-SPOOFING)

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:07**</span>

Rekonzipieren Sie das bisherige 'IPv4-Firmennetz' im Hinblick auf Sicherheitsaspekte so, dass

* [ ] die Produktionsrechner in einer DMZ angesiedelt sind
* [ ] weiterhin nur Developer auf die DMZ-Rechner zugreifen können
* [ ] die Developerrechner nicht in der DMZ stehen.
* [ ] die Rechner aller anderen Abteilungen nicht in der DMZ stehen.

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:11]**

---


### 5) VLAN 

* steht für **Virtual Local Area Network**
* setzt Nutzung eines Layer-III-Switches voraus. **[→ ZP:Sheet:12]**

Dabei

* sind alle Rechner Teil desselben physisch vollverswitchten Netzes (Broadcastdomäne)
* weiß der Switch, welcher Rechner mit welcher IP-Adresse an welchem Port hängt
* leitet der Switch eine Nachricht anhand der Destination-IP-Adresse im Layer-III-Paket an den zuständigen Port
* werden mehrere Ports eines Switches per Konfiguration zu einer virtuellen Broadcastdomäne zusammengefasst
* garantiert der Switch, dass Broadcastanfragen (ARP-Requests) nur innerhalb der virtuellen Broadcastdomäne (Subnetz) propagiert werden
* verhindert der Switch (damit), dass Rechner in einer virtuellen Broadcastdomäne (ohne weitere Maßnahmen) 
  mit einem Rechner einer anderen Broadcastdomäne sprechen kann, obwohl beide an demselben Switch angeschlossen sind.


Das bedeutet:
  
* Layer-III-Switch versteht/interpretiert die Datenpakete verstehen/interpretieren.
  * Hinweis: Layer-3-Switch versteht alle Ebenen, Layer-2-Switch nur Layer-II-Anteile der Datenpakete (Ethernetframe)
* Wenn die Kommunikation zwischen virtuellen Broadcastdomänen ermöglicht werden sollen, muss ein Router so in den Switch eingebunden sein, dass "[...] in jedem VLAN ein Interface besitzt".  (→ vgl. Schreiner: Computernetzwerke, 2014 (2014), S. 127)


**Grundsatz:**

* Die tatsächlichen Fähigkeiten der Layer-III-Switche variieren:
  * einfachere Layer-III-Switche erwarten physikalisch angeschlossene Router zur Realisierung des lokalen Hoppings
  * komplexere Layer-III-Switche emulieren Router als Teil ihrer Software 
  
So gilt:

1. **Layer-III-Switch routet** von einer lokalen BCD in die nächste lokale BCD, gelegentlich ohne physisch vorhanden Router.
2. **Layer-III-Switch routet nicht** von sich aus ins Internet.


Disclaimer: Begriff VLAN (wie Begriff Netz) doppeldeutig benutzt:

* Bei einem LAN wird ein per Netzadresse und Netzmaske definiertes Netz in mehrere Subnetze segmentiert. Beide, LAN und Subnetze werden je nach Kontext sprachlich als 'Netze' bezeichnet.
* Ein VLAN meint meist die Gesamtheit einer über den/die Switchkette gebildetes Netz. Per definitionem besteht es ab aus Subnetzen, die nur virtuell realisiert werden.


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:13:routing:08**</span>

* [ ] Realisieren Sie die inneren Netze FIN, MNG und HR des rekonfigurierten 'IPv4-Firmennetzes' 
    jetzt mit einem(!) Layer-III-Switch als VLAN(s)


<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:13]**

---