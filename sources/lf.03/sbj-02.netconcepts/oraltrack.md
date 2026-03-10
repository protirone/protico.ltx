<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 1.) Grundlegende Begriffe **[→ ZP:Sheet:2]**

Im Lernfeld 03 kommt es in erster Linie darauf, Begriffe und Konzepte kennenzulernen. In der Mittelstufe in Lernfeld 09 wird es dann um das Zusammenwirken und Ineinandergreifen gehen.

Um das Lernen der Begriffe zu erleichtern, folgen ich im LF03-Unterricht relativ eng dem Grundstufenbuch (Lernfelder 1-5) für die IT-Berufe aus dem Westermann-Verlag [→  Gratzke et.al: Grundstufe: Lernfelder 01-05, 2020] /* Bibliographische Angaben im FI-Literaturverzeichnis */  

Hier die erste entsprechende Wortwolke:

* [ ] Alarmanlage
* [ ] Archivierungssystem
* [ ] Anwendungssoftware
* [ ] CRM
* [ ] ERP
* [ ] Datacenter
* [ ] Datenendgerät
* [ ] Datensicherung
* [ ] Drucker
* [ ] Gefahrenmeldeanlage
* [ ] Host
* [ ] Ip-Adresse
* [ ] Kopierer
* [ ] LAN
* [ ] Scanner
* [ ] Network-Devices
* [ ] PC-Arbeitsplätze
* [ ] Router
* [ ] Rechenzentrum
* [ ] Paket
* [ ] Server
* [ ] Speicher
* [ ] Switch
* [ ] Telefone
* [ ] TK-Anlage
* [ ] Videoüberwachung
* [ ] WLAN/Wi-Fi
* [ ] Zahlungsverkehr
* [ ] Zeiterfassung
* [ ] Zutrittskontrolle

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

### Definitionen zum Netzaufbau:


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
* **Firewall**
  * ist ein Programm
  * läuft meistens auf einem Router
  * erlaubt das Weiterleiten eines Paketes nur, wenn das den Regeln entspricht
  * kann Ip-Adressen, Netzadressen und/oder Ports blocken oder arlauben
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
* **Route**
  * meint den Weg von einem Rechner zum nächsten,
  * hat ein Netz mehrere Router, kann es mehrere Wege von einem zum nächsten Rechner geben.
*  **Router**
   * ist in mindestens 2 Netze eingebunden,
   * leitet Pakete von einem Netz ins benachbarte weiter,
   * verbindet zwei Broadcastdomänen.
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
* **`tracert`** (W11) bzw. **`traceroute`**
  * listet die Hoppings (von einer Broadcastdomain in die nächste) auf, die nötig sind, um einen Zielrechner zu erreichen
  * guter Testzielrechner dafür ist `8.8.8.8`, der Google-DNS-Server
* **Unicastadresse**:
  * IP-Adresse, die ein bestimmtes Netzwerkinterface eines Rechners identifiziert
  * umgangssprachlich oft den Rechner, in dem das Netzwerkinterface eingebaut ist
