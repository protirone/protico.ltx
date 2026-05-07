<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:task:1**</span>

*Netzwerksysteme werden auch nach der Art ihrer Struktur klassifiziert.*

* 1.1 __Skizzieren Sie (sprachlich und/oder per Diagramm) eine Client-Server-Architektur.__ (3P)
* 1.2 __*Skizzieren Sie (sprachlich und/oder per Diagramm) eine Peer-To-Peer-Architektur.*__ (1ZP)

<!-- uebung::end -->

Lösung: 

1.1:

```
CL1---|                                   |--SERV2
      (Internet)---ROUTER---Loadbalancer--|--SERV1    
CL2---|                                   |--SERV3
```

1.2:

```
(CL+SV)1 --- (CL+SV)3
   |      X     |
(CL+SV)2 --- (CL+SV)4
```

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:task:2**</span>

MAC-Adressen dienen zur weltweit eindeutigen Nummerierung von Netzwerkinterfaces/-karten:

* 2.1: __Beschreiben Sie, wie viele Bytes eine MAC-Adresse hat und welche Bytes davon (standardmäßig) zum Vendorencode gehören.__ (3P)
* 2.2: __*Rechnen Sie vor, wie viele verschiedene MAC-Adressen es maximal geben kann.*__ (1ZP)

Hinweis: Exponentialzahl reicht als Lösung.

<!-- uebung::end -->

Lösung: 


* 2.1: 6 Bytes = die linken 3 Bytes = Vendorencode, die rechten 3 Bytes = Seriennummer
* 2.2: 2^8 * 2^8 * 2^8 * 2^8 * 2^8 * 2^8 = 2^(8+8+8+8+8+8) = 2^48

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:task:3**</span>

IPv4-Adressen keine innere Struktur. Sie wird ihnen über die Subnetzmaske zugeschrieben. Zusammen definieren sie im Verbund ein Netz.

* 3.1 __Beschreiben Sie, wie viele Bytes eine IPv4-Adresse hat__ (2P)
* 3.2 __*Berechnen Sie mit Bitoperatoren aus der IPv4-Adresse '192.168.110.42' und der Subnetzmaske '255.255.255.0' die folgenden Adressen:*__
  * _Netzadresse_ (1ZP)
  * _Broadcastadresse_ (1ZP)
  * _eine der üblicherweise genutzten Gatewayadressen_* (1ZP)

Hinweis: Beschreiben Sie Ihren Rechenweg.

<!-- uebung::end -->

Lösung: 

* 3.1: 4 Bytes
* 3.2:
  * `192&255 -> 192`
  * `168&255 -> 168`
  * `110&255 -> 110`
  * ` 42&0   ->  0` 
  * Netzadresse = `192.168.110.0` (kleinste Zahl im Hostabteil)
  * Broadcastadresse = `129.168.119.255` (höchste Zahl im Hostanteil) 
  * Gateway =  `192.168.110.1` oder `129.168.110.254`

---

<!-- uebung::start -->

<span style="color: green;">_AUFGABE_</span> <span style="color:magenta;">**LF03:90:task:4**</span>

Außerdem sind IPv4-Adressen in Gruppen mit speziellen Zwecken geordnet.

* 4.1. __Beschreiben Sie, wozu man private IPv4-Adressen nutzt.__ (2P)
* 4.2. __*Beschreiben Sie, wozu und wie man (wer?) APIPA-Adressen nutzt.*__ (2ZP)
 

<!-- uebung::end -->

Lösung: 

* 4.1 Private Adressen nutzt man für ein privates Netz, das auch segmentiert sein kann. Private Adressen werden über Router im privaten Netz geroutet. Sie werden aber niemals ins Internet geroutet.
* 4.2 Erhält ein Rechner bei einer DHCP-Anfrage kein Konfigurationspaket, darf er sich selbst eine Adresse aus dem APIPA-Bereich nehmen. Er sollte dazu einen Algorithmus mit Zufallssteuerung verwenden, um die Wahrscheinlichkeit zu minimieren, dass andere dieselbe Adresse herausgreifen.

---

<!-- uebung::start -->

<span style="color: green;">_BEWERTUNG_</span> <span style="color:magenta;">**LF03:90**</span>

* 10 Standardpunkte (P) + 7 Zusatzpunkte (ZP) möglich.
* 10 Punkte insgesamt = 2.0
* ab 12 Punkte insgesamt = 1.0
* Rest: [https://www.lehrerfreund.de/notenschluesselrechner/form-ihk-notenschluessel] mit dem Höchstwert 12

<!-- uebung::end -->
