<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:1**</span>

* 1.1 Beschreiben Sie, was die Einbettung von einem Paket in ein anderes Paket auf dem nächst niedrigeren OSI-Layer meint. (4 Punkte) 
* 1.2 *Geben Sie an, auf welchen OSI-Layern die Netzwerkkarte-zu-Netzwerkkarte-Kommunikation organisiert wird.* (4 Z-Punkte) 

<!-- uebung::end -->

Lösung: 

* 1.1: 
  * Jedes Paket eines Protokolls besteht aus einem Header und einem Payload.
  * Ein Paket A in ein Paket B einer tieferen Stufe einzubetten meint, Paket A mit Header UND Payload in den Payload von Paket B zu schreiben.
* 1.2: Auf Layer 1 (Bitübertragung), 2 (Sicherung) und 3 (Vermittlung-/Paket)

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:2**</span>

* 2.1 Lösen Sie das Kürzel DMZ auf: wofür steht diese Abkürzung? (2 Punkte)
* 2.2 Beschreiben Sie den Unterschied zwischen einer einstufigen und einer zweistufigen DMZ. (2 Punkte)
* 2.3 *Beschreiben Sie die beiden wesentlichen DMZ-Strategien.* (4 Z-Punkte)

<!-- uebung::end -->

Lösung: 

* 2.1: Demilitarized Zone / Demilitarisierte Zone
* 2.2: Erstere hat nur eine Firewall, die die Pakete gemäß der Regeln weiterleitet bzw. blockt. Letztere hat zwei Firewalls: außen eine weiche, innen eine scharfe
* 2.3:
  * Strategie für die äußere Firewall: Erlaube initial alles. Verbiete dann nur dass, was gar nicht ins eigene Netz darf.
  * Strategie für die innere Firewall: Verbiete initial alles. Erlaube dann nur dass, was wirklich gebraucht wird.

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:3**</span>

* 3.1 Nennen Sie zwei der vier Hauptfähigkeiten von Firewalls. (2 Punkte)
* 3.2 *Beschreiben Sie, wie die Konzepte DMZ und Firewall ineinander greifen.* (2 Z-Punkte) 

<!-- uebung::end -->

Lösung: 

* 3.1:
  * Kommunikationsversuche von Rechnern anhand ihrer IP-Adresse zulassen oder blockieren
  * Kommunikationsversuche aller Rechner eines Subnetzes zulassen oder blockieren
  * Anfragen an eine Port zulassen oder verbinden
  * Anfragen anhand von Mustern zulassen oder verbinden
* 3.2: Eine DMZ nutzt Firewalls, um Netzsegemente gegeneinander abzuschirmen.

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:4**</span>


Sie haben schon ein komplexes Firmennetz aufgebaut. Die Netzwerkkarten aller angebundenen Rechner sind bereits mit je einer IPv4-Adresse, einer Subnetzmaske und einem Default-Gateway konfiguriert. Jedes Subnetz hat einen Router, der mit seinem 'zweiten Bein' in ein Verwaltungsnetz eingebunden ist. Das zweite Bein eines jeden Routers im Verwaltungsnetz haben Sie ebenfalls bereits mit IPv4-Adresse, einer Subnetzmaske und dem Default-Gateway konfiguriert. Dieses Default-Gateway ist der Router ins Internet. Ihre Chefin lässt sich den Stand der Dinge berichten. 

* 4.1 Kreuzen Sie die der folgenden Aussagen an, die Sie ihr bereits guten Gewissens zusagen können: (4 Punkte)
  * [ ] Alle eingebunden Rechner haben Zugang zum Internet.
  * [ ] Alle Rechner können mit den anderen Rechnern des Firmennetzes kommunizieren.
  * [ ] Alle Rechner eines Subnetzes können die anderen desselben Subnetzes kontaktieren.
  * [ ] Sie haben die Abschottung von Subnetzen von anderen bereits technisch vorbereitet.
* 4.2 Skizzieren Sie kurz, was Sie noch tun müssen, um das, was Sie noch nicht erreicht haben, auch noch zusagen zu können. (4 Punkte) 

<!-- uebung::end -->

Lösung: 

* 4.1 
  * [X] Alle eingebunden Rechner haben Zugang zum Internet.
  * [ ] Alle Rechner können mit den anderen Rechnern des Firmennetzes kommunizieren.
  * [X] Alle Rechner eines Subnetzes können die anderen des Subnetzes kontaktieren.
  * [ ] Sie haben die Abschottung von Subnetzen von anderen bereits technisch vorbereitena.
* 4.2  
  * Routingtabelle(n) einfügen, um andere als nur die Defaultrouten nach draußen nutzen zu können.
  * Firewalls auf geeignete Routern konfigurieren und aktivieren.

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:5**</span>

* 5.1 Beschreiben Sie, was ein WLAN ausmacht. (2 Punkte)
* 5.2 *Beschreiben Sie, was ein VLAN ausmacht.* (2 Z-Punkte)

<!-- uebung::end -->

Lösung: 

* 5.1: WLAN ist ein drahtloses Netzwerk mit eher geringerer Reichweite. 
* 5.2: 
  * Bei einem VLAN werden alle Geräte einer ORG-Einheit an je einen Port eines Layer-III-Switches angeschlossen.
  * Der Switch kennt auf Layer-II Ebene die Mac- und IP-Adressen der angeschlossenen Geräte und kann sie dem Port zuordnen, an dem sie angeschlossen sind.
  * Die Segmentierung in Untereinheiten / Subnetze wird anhand von Regeln organisiert, die die Rechner über ihre IP-Adressen zu Gruppen = Broadcastdomänen zusammen fassen.

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:6**</span>

* 6.1 Segmentieren Sie das Netz 192.168.3.0/24 in zwei /25 Netze: Geben Sie für jedes Ihrer neuen Netze Netzadresse, Subnetzmaske und Broadcastdresse an. (4 Punkte)
* 6.2 Segmentieren Sie das Netz 192.168.3.240/29 in zwei /30 Netze: Geben Sie für jedes Ihrer neuen Netze Netzadresse, Subnetzmaske und Broadcastdresse an. (4 Punkte)
* 6.3 *Geben Sie für jedes der vier neuen Netze aus 6.1 und 6.2 eine der üblicherweise genutzten Gatewayadressen an.* (4 Z-Punkte)

<!-- uebung::end -->

Lösung: 

* 6.1 
  * `192.168.3.0/25`: NA = `192.168.3.0`, NM: `255.255.255.128`, BC = `192.168.3.127`
  * `192.168.3.128/25`: NA = `192.168.3.128`, NM: `255.255.255.128`, BC = `192.168.3.255`
* 6.2 
  * `192.168.3.240/30`: NA = `192.168.3.240`, NM: `255.255.255.252`, BC = `192.168.3.243`
  * `192.168.3.244/30`: NA = `192.168.3.244`, NM: `255.255.255.252`, BC = `192.168.3.247`
* 6.3 
  * `192.168.3.0/25`: GW = `192.168.3.1` oder `192.168.3.126`
  * `192.168.3.128/25`: GW = `192.168.3.129` oder `192.168.3.254`
  * `192.168.3.240/30` GW = `192.168.3.241` oder `192.168.3.243`
  * `192.168.3.244/30` GW = `192.168.3.245` oder `192.168.3.246`


---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:7**</span>


Sie finden auf einem Gerät in Ihrem Firmennetz den Hinweis, dass dessen Netzwerkkarte aktuell die Adresse `fd9e:0:a92c:2323::1/64` nutze. Ihre Chefin - ihr Geburtstag ist der 01.10. - hat Ihnen vorab mitgeteilt, dass Ihr Firmenstandort zwar die Netzadresse `fd9e:0:a92c:2323::1/48` zugewiesen bekommen habe, dass aber trotzdem alle Geräte in demselben Firmennetz seien. Jetzt möchte sie von Ihnen einen Vorschlag zu Aufteilung in 4 getrennte Netze, von denen jedes einzelne prinzipiell alle Geräte am Standort aufnehmen können sollte. Sie wollen ihr eine persönliche Freude machen. 

* 7.1 Erläutern Sie am Beispiel dieser Adresse Merkmale und Struktur von IPv6-Adressen und geben Sie den Typ dieser speziellen Adresse an. (10 Punkte)
* 7.2 Erläutern Sie, welche Informationen Sie auf welcher Basis aus diesen Informationen über das bestehende Netz ableiten können. (6 Punkte)
* 7.3 *Geben Sie an, welche Netzsegmentierung Sie Ihrer Chefin empfehlen.* (8 Z-Punkte)

<!-- uebung::end -->

Lösung: 

* 7.1 
  * IPv6-Adressen haben 16 Bytes bzw. 8 Bytepaare.
  * Der Wert eines Bytes wird hexadezimal notiert. 
  * Ein Bytepaar wird durch einen Doppelpunkt vom nächsten abgegrenzt.
  * Der Wert eines Bytepaares, in dem jedes Byte den Wert 0 hat, kann syntaktisch zu `:0:`.
  * Die erste 8 Bytes bilden den Netzanteil der IPv6-Adresse, die letzten 8 Byte den Identifier des adressierten Teilnehmers.
  * In den ersten 6 Bytes sind Netztyp und Zuweisungsinformationen (IANA,RIPE,) oder Netztyp und eine Zufallszahl encodiert.
  * In den letzten beiden Bytes des Netzanteils einer IPv6-Adresse ist die Subnetz-ID encodiert.
  * Das Präfix `fd` = kennzeichnet den nutzbaren Bereich eine Unique Local Adresse:
    * Formal ist eine ULA durch `fc::/7` definiert.
    * Der Bereich ist aber in zwei Segmente aufgeteilt, in `fc::/8` und `fd::/8`
    * `fc::/8` ist reserviert für zukünftige Zuteilungen, nutzbar ist nur `fd::/8`
* 7.2 
  * Es gibt im Firmenstandort nur ein Netz mit der Netzadresse `fd9e:0:a92c:2323::/64`.
  * Dieses Netz verwendet die Subnetzid `2323`.
  * Auf dem Firmenstandort sind höchstens `2^64-2` Geräte ans Netz angeschlossen. 
* 7.3 
  * `fd9e:0:a92c:1101::/64`
  * `fd9e:0:a92c:1102::/64`
  * `fd9e:0:a92c:1103::/64`
  * `fd9e:0:a92c:1104::/64`

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF09:95:8**</span>

8) Ihre Chefin bittet Sie, die beiden kleineren Netze aus 6.2 als VLAN so umzusetzen, dass jedes Gerät in einem Netz Zugang zum Internet hat. Dazu sollen Sie einen alten Layer-III-Switch mit 32 Ports ohne embedded Router-, DNS, oder Firewallfunktionen benutzen und dürfen sich aus dem Pool der einfachen alten Router frei bedienen.
* 8.1 Geben Sie an, wie viele Netze Sie für die Umsetzung brauchen. (4 Punkte)
* 8.2 Spezifizieren Sie die Netze, die sie über 6.2 hinaus brauchen. (4 Punkte)
* 8.3 Skizzieren Sie kurz, was Sie tun müssen, damit die Rechner aus dem einen Netz auch die aus dem anderen erreichen können. (2 Punkte)
* 8.4 Zeichnen Sie den zugehören Netzwerkplan. (10 Z-Punkte)

<!-- uebung::end -->

Lösung: 

* 8.1: 3
* 8.2: Neben den /30 Netzen braucht es noch mindestens ein drittes /29 Netz, z.B.
  * `192.168.3.248/29`: NA = `192.168.3.248`, NM: `255.255.255.248`, BC = `192.168.3.255` 
  * mit Hostanzahl 6
* 8.3: Routen in den beiden inneren Routern setzen
* 8.4: s. 

---

<!-- uebung::start -->

### Bewertung

* 50 Standardpunkte (P) + 34 Zusatzpunkte (ZP) möglich.
* 50 Punkte insgesamt = 2.0
* 58 Punkte insgesamt = 1.0
* Rest: [https://www.lehrerfreund.de/notenschluesselrechner/form-ihk-notenschluessel] mit dem Höchstwert 58 

<!-- uebung::end -->


Im Detail:

| Pt | Note | Pt | Note | Pt | Note | Pt | Note |
|---|---|---|---|---|---|---|---|
| 58 | 1 | 57 | 1,1 | 56 | 1,2 | 55 | 1,3
| 54 | 1,4 | 53 | 1,5 | 52 | 1,7 | 51 | 1,9
| 50 | 2 | 49 | 2,1 | 48 | 2,3 | 47 | 2,4
| 46 | 2,5 | 44 | 2,8 | 43 | 2,9 | 42 | 3.0

---
