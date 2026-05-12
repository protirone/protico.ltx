<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:95:task:1**</span>

## Block 1: 'Binäroperatoren'

*Bytes werden gelegentlich binär mit anderen Bytes verknüpft. Dafür gibt es Verknüpfungsregeln, z.B.*

* **sprachlich:**
  * A. Ist das Bit-X im Quellbyte-A gesetzt und ist das Bit-X in Quellbyte-B gesetzt, wird auch das Bit-X im Zielbyte gesetzt.
  * B. Ist das Bit-X im Quellbyte-A gesetzt, aber das Bit-X in Quellbyte-B nicht, wird auch das Bit-X im Zielbyte gesetzt.
  * C. Ist das Bit-X im Quellbyte-A nicht gesetzt, aber das Bit-X in Quellbyte-B, wird auch das Bit-X im Zielbyte gesetzt.
  * D. Ist das Bit-X im Quellbyte-A nicht gesetzt und ist auch das Bit-X nicht im Quellbyte-B gesetzt, wird auch das Bit-X im Zielbyte nicht gesetzt.
* **schematisch:**

| Regel | X(QbA) | X(QbB) | X(Zb) |
|---|---|---|---|
| A | x | x | x |
| B | x | - | x |
| C | - | x | x |
| D | - | - | - |

* 1.1 __Geben Sie in einem der beiden Formate die Verknüpfungsregeln für eine Binäre-Und-Verknüpfung an.__ (4P)
* 1.2 __Geben Sie an, welche Binäre-Verknüpfung durch die obigen Regeln A - D definiert ist.__ (4P)
* 1.3 __*Ermitteln Sie, was sich ergibt, wenn man dezimal `22` mit hexadezimal `0xFF` nach den Regeln des Binären-Unds miteinander verknüpft.*__ (4ZP)
* 1.4 __*Ermitteln Sie, was sich ergibt, wenn man die Dezimalzahl `22` mit der Hexadezimalzahl `0x80` nach den Regeln der Binären-Unds miteinander verknüpft.*__ (4ZP)


<!-- uebung::end -->

Lösung:

* 1.1:
  
| Regel | X(QbA) | X(QbB) | X(Zb) |
|---|---|---|---|
| A | x | x | x |
| B | x | - | - |
| C | - | x | - |
| D | - | - | - |


* 1.2: binary or
* 1.3: `22` = `0x16` = `0b00010110` & `0b11111111` = `0b00010110` =  `0x16` = `22`
* 1.4: `22` = `0b00010110` & `0b10000000` = `0b00000000` = `0x00` = `0`

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:95:task:2**</span>

Übliche Datenaustauschformate sind CSV, INI, JSON, XML und YAML. Datenmengen - auch in solchen Dateien - können nach dem gängigen Präfixsystem *Kilo = `10^3`, Mega = `10^6`, Giga = `10^9`, ...* spezifiziert werden. Oder nach dem 'Informatik'-Präfixsystem *Kibi = `2^10`, Mebi = `2^20`, Gibi = `2^30`,... *.

* 2.1 __Geben Sie an, wofür die Abkürzung *CSV* steht.__ (4P)
* 2.2 __Beschreiben Sie die Struktur eines CSV-Datei__ (2P)
* 2.3 __*Geben Sie an, wie viel Kilobyte eine 10 Kibibits große INI-Datei enthält*__ (4ZP)
* 2.4 __*Geben Sie an, wie viel Mebibyte eine 8 Mebibits große XML-Datei enthält*__ (2ZP)

<!-- uebung::end -->

Lösung:

* 2.1: Comma Separated Values
* 2.2: 
  * Pro Zeile ein Datensatz.
  * Jeder Wert in einem Datensatz durch ein Komma vom nächsten getrennt.
* 2.3: 
  * 10 Kibibits = 10\*(2^10) Bits = 10 \* 1024 = 10240 Bits. 
  * 10240 Bits / 8 = 1280 Bytes = **1,28 Kilobytes**.
* 2.4: 8 Mebibits / 8 = 1 Mebibyte
 
---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:95:task:3**</span>

IPv6-Adressen haben eine innere Struktur und definieren im Verbund ein Netz.

* 3.1 __Beschreiben Sie, wie viele Bytes eine IPv6-Adresse hat__ (3P)
* 3.2 __Nennen zwei der IPv6-Adresstypen__ (3P)
* 3.3 __*Nennen Sie zu einem der IPv6-Adresstypen die entsprechende Klasse in den IPv4-Adressen.*__ (2ZP)
* 3.4 __*Geben Sie an, wie viele Bytepaare(!) der Interface Identifier in einer IPv6-Adresse ist.*__ (2ZP)
* 3.5 __*Geben Sie an, wie viele Geräte maximal zum 64-Bit-Netzpräfix einer IPv6-Adresse gehören können.*__ (2ZP)

Hinweis: Potenzzahl reicht

<!-- uebung::end -->

Lösung:

* 3.1: 16 Bytes = 8 Bytepaare
* 3.2: Global Unicast Address, Link Local Unicast-Address, Unique Local Address, Loopback Address
* 3.3: Öffentliche Ip-Adresse, wie MAC-Adresse nicht routbar, private Adresse, superprivate Adresse
* 3.4: 4 Bytepaare = 8 Bytes
* 3.5: 2^64

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:95:task:4**</span>

* 4.1 __Geben Sie die Definition eines Baumes (aus der Grafentheorie) an.__ (2P)
* 4.2 __Beschreiben Sie, wofür die CIDR-Notation bei der Angaben von IPv4-Adressen benutzt wird.__ (2P)
* 4.3 __Erklären Sie die Aufgabe eines DHCP-Servers.__ (2P)
* 4.4 __Erklären Sie die Aufgabe einer IPv4-Adresse.__ (2P)
* 4.5 __Erklären Sie die Aufgabe eines Switches.__ (2P)
* 4.6 __Erklären Sie die Aufgabe eines Routers.__ (2P)
 
<!-- uebung::end -->

Lösung:

* 4.1: 
  * Ein Baum besteht aus Knoten und Kanten.
  * Jeder Knoten hat 0 - 1 Väterknoten.
  * Jeder Knoten hat 0 - n Töchterknoten.
  * Knoten ohne Töchter sind Blätter.
  * Der Knoten ohne Vaterknoten ist der Wurzelknoten. 
* 4.2: Die Anzahl der von links nach rechts zu berücksichtigen Bits, die die Netzadresse ausmachen.
* 4.3: Reicht auf Anfrage die zur Einbindung in eine Domäne nötigen Konfigurationsdaten an einen Client, der seine eigene Netzwerkschnittelle damit konfiguriert.
* 4.4: Identifiziert einen Rechner (bzw. dessen Netzwerkkarte).
* 4.5: Verbindet Geräte zu einer Broadcastdomäne.
* 4.6: Organisiert das Weiterleiten von Paketen in benachbarte Broadcastdomänen.


---

<!-- uebung::start -->

<span style="color: green;">_Bewertung_</span> <span style="color:magenta;">**LF03:95**</span>

* 32 Standardpunkte (P) + 20 Zusatzpunkte (ZP) möglich.
* 32 Punkte insgesamt = 2.0
* ab 37 Punkte insgesamt = 1.0
* Rest: [https://www.lehrerfreund.de/notenschluesselrechner/form-ihk-notenschluessel](https://www.lehrerfreund.de/notenschluesselrechner/form-ihk-notenschluessel) mit dem Höchstwert 37


<!-- uebung::end -->

---

