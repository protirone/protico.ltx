<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1) MAC-Adresse [→ ZP:Sheet:2]

Anknüpfung: Paket**übertragung** auf Layer-II-Ebene (ARP) ausschließlich mit MAC-Adressen

**MAC-Address** steht für _**M**edium **A**ccess **C**ontrol Address_. Jede MAC-Adresse

* besteht aus 6 Bytes
* wird als 6-Byte-Code hexadezimal geschrieben, byteweise getrennt durch Bindestriche oder Doppelpunkte, z.B.  `48:e7:da:06:ef:85` (→  [https://de.wikipedia.org/wiki/MAC-Adresse](https://de.wikipedia.org/wiki/MAC-Adresse))
* wird vom Hersteller fest in die Hardware einkodiert,
* besteht aus 2 Gruppen:
  - die vorderen 3 Bytes kennzeichnen den Hersteller (Vendorencode) (= `Organizationally Unique Identifier`)
  - die hinteren 3 Bytes sind eine vendorenspezifische Seriennummer
* sollte weltweit *unique* sein (= *eindeutig*, *nur ein Exemplar*)
* wird auf Layer I/II benutzt, um Pakete via Hub bzw. Switch von Rechner A zu B zu schicken

| Byte     |\| |  `B6`  | `B5`   | `B4`   |\| | `B3`   | `B2`   | `B1`   |
|----------|---|--------|--------|--------|---|--------|--------|--------|
| Value    |\| | `0x48` | `0xe7` | `0xda` |\| | `0x06` | `0xef` | `0x85` |
| OUI-MASK |\| | `0xff` | `0xff` | `0xff` |\| | `0x00` | `0x00` | `0x00` |
| OUI      |\| | `0x48` | `0xe7` | `0xda` |\| | `0x00` | `0x00` | `0x00` |

OUI-Segment hier = `48:E7:DA:00:00:00` - `48:E7:DA:FF:FF:FF`

> vgl. dazu
> * Zisler: Computer-Netzwerke, 2022, S. 85f.
> * Schreiner: Computernetzwerke, 2014, S. 43f

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:07:Addressing:01**</span>

* [ ] Ermitteln Sie die MAC-Adresse der Netzwerkkarte Ihres Rechners
* [ ] Ermitteln Sie den Hersteller Ihrer Netzwerkkarte
* [ ] Dokumentieren Sie Ihre Informationsquelle

Hinweis: Nutzen Sie dazu zuerst eine Shell, recherchieren Sie dann den Vendor im Internet.

1. WIN11: in *Powershell* cmd `ipconfig` bzw. `ipconfig /a` oder `getmac /v`
2. LNX/WSL: in *bash* cmd `ifconfig` oder `ip addr show`
3. Internetrecherche z.B. mit [https://www.dein-ip-check.de/tools/macfinder]([https://www.dein-ip-check.de/tools/macfinder)

MAC-Adressen sind die Strings mit 6 Hexwerten hintereinander, getrennt durch `:` oder `-`

<!-- uebung::end -->

---

**Lösung:** Infos in obigen Angaben

*Anmerkung*: 

* Der Vendorencode (= Organizationally Unique Identifiers (OUI)) einer MAC-Adresse wird vom [IEEE](https://www.ieee.org/) (Institute of Electrical and Electronics Engineers) vergeben
* Gemäß [https://www.dein-ip-check.de/tools/macfinder?oui=48%3Ae7%3Ada%3A06%3Aef%3A85&page=1](https://www.dein-ip-check.de/tools/macfinder?oui=48%3Ae7%3Ada%3A06%3Aef%3A85&page=1)
   - gehört die MAC-Adresse `48:e7:da:06:ef:85` der Firma *AzureWave Technology Inc.*
   - ist Teil des MAC-Segments	`48:E7:DA:00:00:00` - `48:E7:DA:FF:FF:FF`
   - was als *MA-L*-Segment an *AzureWave Technology Inc.* vergeben worden ist

vgl. 

* [https://macaddress.io/faq/what-is-a-ma-l-ma-m-ma-s-assignment](https://macaddress.io/faq/what-is-a-ma-l-ma-m-ma-s-assignment)
* [https://macaddress.io/faq/what-is-an-organizationally-unique-identifier-oui](https://macaddress.io/faq/what-is-an-organizationally-unique-identifier-oui)
* 

**Mengenabschätzung: [→ ZP:Sheet 3]**

* Zahlenmäßig stünden mit 6 Bytes ~ 280 Billionen MAC-Adressen zur Verfügung
  
```
2^8 * 2^8 * 2^8 * 2^8 * 2^8 * 2^8 
= 2^(8+8+8+8+8+8) 
= 2^48 
= 281.474.976.710.656 
```

**Kontextfrage: [→ ZP:Sheet 4]** 

*Gibt es - analog zur IPv4-Adressenknappheit - auch eine MAC-Adressenknappheit?*


* Bei einer Weltbevölkerung von 8.000.000.000 ergäbe das ~ `35184` Adressen pro Person 
* Ältere Berechnungen, die auf mehr Geräte/Netzwerkkarten pro Person der Weltbevölkerung kamen, sind von einer kleineren Weltbevölkerung ausgegangen.
* Bei der Aufteilung 3 Bytes (= `2^8* 2^8 * 2^8` = `2^(8+8+8)` = `2^24` = `16777216` ) pro Vendorenidentifier und Seriennummern können `16.777.216 Vendoren` je `16.777.216` Netzwerkkarten`etc. verkaufen
* Zu Entlastung dieser Verknappung haben manche Firmen bereits mehrere Vendorenkenner geclaimt.

* **Antwort: _JA, es gibt bereits eine Verknappung_**
* Die neuere Segmentierung ist `MA-L`, `MA-M`, `MA-S` einer Reaktion darauf:


* Die strikte Aufteilung in 2^24 Vendoren, die je über 2^24 Kennungen verfügen ist mittlerweile - in Analogie zu feineren IP-Netzsegmentierung mit CIDR-Notation - verfeinert. 
* Es gibt jetzt **[→ ZP:Sheet 5]**
  * **OUI-24**: `MA-L`-Segemente (= MAC Address Block Large) ~ bisheriger OUI (Organizationally Unique Identifier)	Aufteilung :- (2^24 ~= 16 Million)
  * **OUI-28**: `MA-M`-Segemente (= MAC Address Block Medium)	:-	2^20 ~= 1 Million
  * **OUI-36**: `MA-S`-Segemente (=	MAC Address Block Small) ~ bisheriger	OUI-36 :-	2^12 ~= 4,096

vgl. 

* [https://macaddress.io/faq/what-is-a-ma-l-ma-m-ma-s-assignment](https://macaddress.io/faq/what-is-a-ma-l-ma-m-ma-s-assignment)
* [https://macaddress.io/faq/what-is-an-organizationally-unique-identifier-oui](https://macaddress.io/faq/what-is-an-organizationally-unique-identifier-oui)
* [https://de.wikipedia.org/wiki/MAC-Adresse](https://de.wikipedia.org/wiki/MAC-Adresse)


*Konsequenz:*

* Es gibt m.W. keinen formalen Bestätigungsprozess für die Eindeutigkeit. Das wäre als weltübergreifender Prozess zu teuer.
* MAC-Adressen können doppelt erscheinen.

**Kontextfrage:**

*Führen doppelt vergebene MAC-Adresse in einem Netz zu Irritationen? Warum sind die doppelt vergebenen Adressen trotzdem nur ein kleines Problem:*

**Auflösung:**

* JA: Ist in einem Layer-II-Netz eine MAC-Adresse doppelt vergeben, fühlen sich immer 2 Rechner angesprochen und antworten. (Traffiksteigerung, Kollisionen)
* VIELLEICHT: Vergleicht der Empfänger die Ziel-IP-Adresse NICHT, sondern verlässt er sich auf die MAC-Adresse und reicht die Nachricht gleich auf den LAYER-IV, reagieren u.U. zwei Systeme
* NEIN: Über die Netzgrenzen hinaus verursachen doppelte MAC-Adressen kein Problem. Denn sie werden NIEMALS geroutet.

vgl. dazu

* Ältere Analyse: [https://www.heise.de/ratgeber/Werden-MAC-Adressen-auch-knapp-1183242.html](https://www.heise.de/ratgeber/Werden-MAC-Adressen-auch-knapp-1183242.html)
* Älterer Forecast: [https://www.golem.de/news/ieee-in-25-jahren-koennten-mac-adressen-knapp-werden-1303-98213.html](https://www.golem.de/news/ieee-in-25-jahren-koennten-mac-adressen-knapp-werden-1303-98213.html)
* [https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4](https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4)

