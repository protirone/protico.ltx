<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1) IPv6-Adresse [→ ZP:Sheet:2]


* bestehen aus 128 Bits (= 16 Bytes)
* werden zur Verschriftlichung in 8 Blöcke zu je 2 Bytes aufgeteilt
* jedes Bytes hexadezimal notiert
* 2 benachbarte Bytes bilden ein Paar und werden vom folgenden durch einen \texttt{:} abgetrennt.
* Die Bytes werden mit abnehmender Wertigkeit von links nach rechts ausgegeben.
* Führende Nullen in einem Byte-Paar weglassbar. 
* Einmal in einer zusammenhängenden Gruppe von Null-Blöcken alle 0 weglassbar

Beispiel:

* 2001:0db8:0000:08d3:0000:8a2e:0070:7344 
* → 2001:db8:0:8d3:0:8a2e:70:7344
* → 2001:db8::8d3:0:8a2e:70:7344
* [ → [https://de.wikipedia.org/wiki/IPv6](https://de.wikipedia.org/wiki/IPv6) ]

Anmerkung:

* In IPv6-Adressen gibt es keine Netzmaske! Der Netzanteil wird ausschließlich in CIDR-Notation markiert 
* Verteilung:
  * IANA → RIR (Regional Internet Registry) (z.B. ripe.net): /32-Ipv6-Netz
  * RIR → ISP (Internetprovider): /48-IPv6-Netz
  * ISP → Kunde: /56-IPv6-Netz
  * Kunde → jedes Gerät : 64Bit-Identifier


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">LF09:11:IPv6:01</span>

Finden Sie mit `ipconfig` bzw.  `ifconfig` Ihre IPv6-Adresse im Schulnetz

* [ ] Finden Sie mit `ipconfig` bzw.  `ifconfig` Ihre IPv6-Adresse im Schulnetz
* [ ] Geben Sie die IPv6-Netzadresse des Schulnetzes an.
  
<!-- uebung::end -->

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">LF09:11:IPv6:02</span>

* [ ] Verdichten Sie die IPv6-Adresse `2001:0db8:0000:08d3:0000:0000:8a2e:7344`
* [ ] Expandieren Sie die IPv6-Adresse `fc00::8a2e:0:0:70:7344`
  
<!-- uebung::end -->

Lösung:

* `2001:0db8:0000:08d3:0000:0000:8a2e:7344` => `2001:db8:0:08d3::8a2e:7344`
* `fc00::8a2e:0:0:70:7344` => `fc00:0000:0000:8a2e:0000:0000:0070:7344`

---


**[→ ZP:Sheet:3]**

* Zahlenmäßig stünden mit 16 Bytes `2^{128}` = `3,4 * 10^{38}` = `340 Sextillionen` IPv6-Adressen zur Verfügung
* Teil man die Zahl auf 8.000.000.000 Menschen auf ergibt sich:

`2^128 / 8.000.000.000 Menschen = ~3,4*10^38 / 8*10^9 = ~4,2 * 10^28 Adressen pro Mensch` 


Das ist immer noch unvorstellbar groß

### 2) IPv6-Adresstypen [→ ZP:Sheet:4]

* Adressklassen wie bei IPv4 gibt es in IPv6 nicht
* Adressentypen im Hinblick auf die Zwecke gibt es in IPv6 (fast) genaus, wie in IPv4 - nur heißen Sie anders:

* __Unspecified Address__ = 0:0:0:0:0:0:0:0/128 = ::/128
* __Global Unicast Address__ = 
  * weltweit gültig, 
  * ins Internet routbar
  * Erkennungspräfix: 2000::/3 ( 0x[20|00] = 00100000|00000000 )
* __Link Local Unicast-Address__ = 
  * nur innnerhalb einer Broadcastdomäne gültig, 
  * nicht routbar 
  * quasi MAC-Adresse
  * Erkennungspräfix: fe80::/10 ( 0x[fe|80] = 111111110|100000000)
* __Unique Local Address__ = 
  * ULA
  * nicht ins Internet routbar
  * in einem privaten Netz routbar
  * wie private IPv4-Adressen
  * Erkennungspräfix: fc00::/7 ( 0x[fc|00] = 11111100|000000000)
* __Loopback__ = 
  * allows a host to talk to itself over IPv6
  * wie superprivate Adressen
  * Erkennungspräfix: ::1/128 (= es gibt nur eine)

* __Unicast Address__ =
  * One-To-One-Adresse
  * _Global Unicast Address_ u. Link Local Unicast-Address u. Unique Local Address
* __Multicast Address__ =
  * One-to-Many-Adresse
  * wie IPv4 Multicastadressen 224.0.0.0/4
  * Erkennungspräfix: ff00::/8
* __Anycast Address__ =
  * One-to-Nearest-Adresse
  * Erkennungspräfix: Wie Global Unicast Adressen. Unterschied konfigurativ.

Für weitere Einzelheiten vgl. [https://www.ripe.net/media/documents/ipv6_reference_card.pdf](https://www.ripe.net/media/documents/ipv6_reference_card.pdf)


**Denkfrage:**

Wenn doch jedes Interface eines Rechners leicht eine routbare IPv6-Adresse bekommen kann,
wozu braucht man dann *Unique Local Addresses*?

*Antwort*: Um *Unique Local Addresses* zu verwenden, braucht man keinen Provider zu involvieren, muss also für dessen Bereitstellungsleistung auch nichts bezahlen.

### 3) IPv6-Segmentierung [→ ZP:Sheet:5]


**Grundsatz**: 

* 128-Bit IPv6-Adresse wird in 2 64Bit-Blöcke aufgeteilt.
* Die ersten 64 Bit identifizieren das Netzwerk (bei IPv4: Netzadresse)
* Die zweiten 64 Bit identifizieren das Interface (bei IPv4: Hostanteil)
* eine Segmentierung der Interface-ID ist  nicht möglich.
* ein Subnetting findet nur im Netzteil statt.

**Verfahren:**

* IANA →   RIR (Regional Internet Registry): /32-Ipv6-Netz
* RIR →  ISP (Internetprovider): /48-IPv6-Netz
* ISP →   Kunde: /56-IPv6-Netz
* Kunde →   Gerät : 64Bit-Identifier

Also:

1. Kunde kann - wenn er ein /64-IPv6-Netz erhält - 2^64 Geräte in die BCD einbinden.
2. Kunde kann - wenn er ein /64-IPv6-Netz erhält - damit keine Subnetzstruktur bilden.
3. Kunde kann Subnetting nur betreiben, wenn er IPb6-Netz mit kleinerer CIDR-Notation erhält:

Kleinstes mögliches Subnetting: /63-Netz ermöglicht 2 /64-Netze.

Anmerkungen: [→ ZP:Sheet:6]

---

[→ ZP:Sheet:7]

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">LF09:11:IPv6:03</span>

Ihre Start-up hat 2 Bereiche: Das Management (8 Personen mit je 4 Geräten) und 
die Entwicklung (4 Personen mit je 8 Geräten). Keine Gruppe soll
auf die Rechner der anderen Gruppe zugreifen können. Die Internetverbindung ist schon
über einen Internetrouter mit globaler IPv4 - und Global Unicast IPv6 Addresse gewährleistet.
Nach innen soll Firma ein IPv6-Netz ohne *Global Unicast Adressen* verwenden.

* [ ] Setzen Sie ein passendes IPv6-Netz auf, das ein Personalwachstum von 400% mit abdeckt.

  
<!-- uebung::end -->

Lösung: [→ ZP:Sheet:8]

1. /64 Subnetz pro Abteilung bedeutet (2^64)-1 anschließbare Geräte. Das ist zukunftssicher.
2. Nur *Unique Local*-Adressen mit Präfix `fc00:` verwenden.
3. Aus 1. und 2. folgt: Durchnumerierung der Subnetze reicht

---

### 4) IPv6-MacAdressen [→ ZP:Sheet:9]

Grundfrage: Könnte man eine Mac-Adresse (weltweit eindeutig) nicht als IPv6-Adresse verwenden?

Ausgang:

* MAC-Adresse hat 6 Bytes
* Die erste 3 spezifizieren den Hardwarehersteller
* Die letzten drei sind die Interfacenummer = Netzwerkkarten-ID. 
  
MAC-Adresse sollte als in eine IPv6 *Link Local Unicast Address* umgewandelt werden können

Umwandlungsalgorithmus: **[→ ZP:Sheet:10]**

* Mac-Adresse (Hex-Notation) in zwei 3-Byte-Blöcke aufteilen:
  * `(52:74:f2:b1:a8:7f` → `52:74:f2 und b1:a8:7f)`
* Dazwischen den Wert FF:FE einfügen: 
  * `(52:74:f2 + FF:FE + b1:a8:7f` → `52:74:f2:FF:FE:b1:a8:7f)`
* Ergebnis in die IPv6-Format umformen: 
  * `(52:74:f2:FF:FE:b1:a8:7f` → `5274:f2ff:feb1:a87f )`
* Das erste Oktett in Binärnotation umwandeln und das 7. Bit invertieren
  * `(52` → `01010010` → `01010000)`
* Binärwert in Hex-Code umwandeln
  * `(01010000` → `50)`
* Das erste Oktet durch den neuen Wert ersetzen:
  * `(5274:f2ff:feb1:a87f` → `5074:f2ff:feb1:a87f)`
* Dem Ganzen das Link-Local-Prefix `fe80::` voransetzen:
  *  `( 5074:f2ff:feb1:a87f` → `fe80::5074:f2ff:feb1:a87f)`

Warum die Bit-Konvertierung? 

* Um der Begrenzung der traditionellen Mac-Adresse zu kommen, ist das EUI-64 Format für Mac-Adressen erfunden worden.
* Im EUI-64 Format soll das 7 Bit (wie im alten 48-Bit-Format) anzeigen, ob die MAC-Adresse 
  global unique = administriert ist, oder lokal generiert worden ist. 
* Algorithmus verändert eine global administrierte MAC-Adresse lokal: ergo muss sie den uniquen Status verlieren. 
* Deshalb die Inversion der 7. Bits.
*  [ → [https://ben.akrin.com/mac-address-to-ipv6-link-local-address-online-converter/](https]://ben.akrin.com/mac-address-to-ipv6-link-local-address-online-converter/)]
*  [ → [https://community.cisco.com/t5/networking-knowledge-base/why-we-flip-the-7th-bit-in-eui-64-a-comprehensive-analysis/ta-p/4951015](https://community.cisco.com/t5/networking-knowledge-base/why-we-flip-the-7th-bit-in-eui-64-a-comprehensive-analysis/ta-p/4951015)]
*  

CISCO Community sagt dazu:

1. "The 7th bit in a MAC address is known as the Universal/Local (U/L) bit, which indicates whether the address is globally administered or locally administered."
2. "When this bit is set to '0' the address is considered globally unique, and when it is set to '1' it signifies a locally administered address."
3 "Inverting the 7th bit (U/L bit) ensures that the resulting identifiers are appropriately designated for local significance, avoiding conflicts with globally administered addresses and allowing for efficient local network configuration."

Daraus folgt: Wäre das 7. Bit schon gesetzt, würde es - 'invertiert' - eine lokal generierte MAC/Ipv6-Adresse als global verwaltet markieren.

Es gibt Anmerkungen, dass das 'Flippen' in der Spezifikation besser formuliert werden sollte. ([https://forums.whirlpool.net.au/archive/2324153]) 

*Hinweis:* Liest man die Erklärungen genau, geht es nur deshalb um das 'Flippen'
/ Invertieren des  7Bits, weil es als gesetzt vorausgesetzt wird. Von der Idee her
muss es gelöscht werden, wenn es gesetzt ist.

Anmerkung zu **DHCP** in IPv6: **[→ ZP:Sheet:11]**

1. Es heißt, man spare sich in IPv6 den DHCP-Server.
2. Das stimmt nur bzgl. der IPv6-Kommunikation in einer Broadcast-Domain: Die Link-Local-Unicast-Adresse kann aus der MAC ausgerechnet werden.
3. Also: In einer BCD tatsächlich kein DHCP nötig.
4. Tatsächlich gibt es auch einen DHCP-v6 Dienst: [https://en.wikipedia.org/wiki/DHCPv6](https://en.wikipedia.org/wiki/DHCPv6)


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">LF09:11:IPv6:04</span>

* [ ] Ermitteln Sie über `ipconfig` bzw. `ifconfig` die MAC-Adresse Ihrer Netzwerkkarte.
* [ ] Wandeln Sie die in eine IPv6 Link-Local-Unicast-Adresse um.
* [ ] Ermitteln Sie Ihre reale Link-Local-Unicast-Adresse. Gibt es einen Zusammenhang?

<!-- uebung::end -->

**Lösung:**

1. MAC-Adresse feststellen: `a0:d3:65:d3:60:ee`
2. splitten und FF:FE einfügen: `a0:d3:65:ff:fe:d3:60:ee`
3. in IPv6-Format umwandeln: `a0d3:65ff:fed3:60:ee`
4. erstes Oktett in Binärnotation umwandeln: `a0` = `10100000`
5. 7. Bit invertieren: `10100000` = `10100010`
6. in Hexzahl zurück verwandeln: `10100010` = `a2`
7. erstes Oktett durch neuen Wert ersetzen `a0d3:65ff:fed3:60:ee` = `a2d3:65ff:fed3:60:ee`
8. das Link-Local-Unicast-Prefix voransetzen: `fe00::a2d3:65ff:fed3:60:ee`
9. real `fe80::4645:ebfc:8c20:fc82`



---


