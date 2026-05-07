<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

*Tonspur* **[→ ZP:Sheet:1]**

### 1. Ausgangspunkt 

Wie haben ausführlich besprochen

* **[→ ZP:Sheet2]**
* die Aktivitäten, die nötig sind, um eine Nachricht über Broadcastgrenzen hinweg zu senden
  * Sender (BCA/IP):
    * Feststellen, ob Ziel-IP in eigener Broadcastdomain
    * Wenn nicht, ARP-Request bzgl. Router-MAC-Adresse
    * Nachricht an Ziel-IP und Router-MAC als Weiterleitungsauftrag
  * Router :
    * Feststellen, ob Ziel-IP in BCB
    * Wenn ja, ARP-Request bzgl. MAC-Adresse des Ziel-Ip-Rechners
    * Nachricht umformulieren
    * Nachricht an Ziel-IP mit Router-MAC und BCA-IP
  * Empfänger: verstehen

* die Abfolge der dafür nötigen Zwischennachrichten **[→ ZP:Sheet3]**

* den Unterschied zwischen ARP-Package und IP-Package **[→ ZP:Sheet4]**
  * den wir in der Dokumentation 'vernachlässigt' haben.

* das Package-in-Package-Prinzip **[→ ZP:Sheet5]**


**ABER**

* es reden *nicht Rechner mit Rechner*,
* sondern **_(Client-)_App** mit **_(Server-)_App**


**Wie geht das?**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/15:services:01**</span>

* 1) Bitte wählen Sie
  * 2 Mitschülerinnen, die je eine Routerhälfte mit eingebettetem Switch simulieren
  * 2 Mitschülerinnen, die je ein Betriebssystem simulieren
  * 2 Mitschülerinnen, die je eine Netzwerkkarte simulieren
  * 2 Mitschülerinnen, die je eine App simulieren
* 2) Wählen Sie ein oder zwei Protokollantinnen
* 3) (Er)finden Sie einen allgemeingültigen, in mehreren Instanzen parallel ausführbaren Prozess, 
  * der die bisher besprochenen Techniken nutzt 
  * der damit eine Nachricht von APP(BCA) zu APP(BCB) und die Antwort zurück übermittelt und
  * der die Regel beachtet, dass nur das Betriebssystem von der Netzwerkkarte lesen und auf die Netzwerkkarte schreiben kann.
* 4) Führen Sie Ihren Prozess als Schreibtischtest durch.
* 5) Dokumentieren Sie Prozess als Aktivitätsdiagramm

<!-- uebung::end -->

Lösung : Request (**[→ ZP:Sheet7]**) Response (**[→ ZP:Sheet8]**)

---


### 2. Die Kommunikation zwischen (Client)App und (Server)App

bedarf auf

* **Serverseite**:
  * **einer Akkreditierungsphase**:
    * ServApp beauftragt ServOps, ihm über einen Socket alle eingehenden Nachrichten zu einem Port zu übermitteln
    * ServApp beauftragt ServOps, alle Nachrichten, die die Server-App auf den Socket schreibt, angemessen über das Netzwerkinterface zu versenden.
    * ServOps gibt einen (an den Port gebundenen) Socket mit IO-Rechten für die Server-App zurück.
  * **einer Lausch-und Annahmephase**:
    * ServOps lauscht auf Netzwerkinterface.
    * ServOps analysiert eingehenden Nachrichten.
    * Geht eine Nachricht für den akkreditierten Port ein, schreibt ServOps sie auf den akkreditierten Socket.
    * ServApp lauscht auf akkreditierten Socket.
    * Geht eine Nachricht darauf, liest ServApp sie vom Socket und interpretiert sie.
  * **einer Schreibphase**:
    * ServApp schreibt Nachricht auf den Socket [mit Destination-IpAdresse (= Source-IpAdresse aus dem Request) und Destination-Port (= Source-Port aus dem Request)].
    * ServOps lauscht auf den akkreditierten Socket.
    * ServOps liest Nachricht vom akkreditierten Socket.
    * ServOps komplettiert Nachricht mit Source-IpAdresse und Source-Port (wie in der Akkreditierungsphase angestimmt).
    * ServOps versendet Nachricht mit ARP+MSG an Router.
* **Clientseite**:
  * **einer Akkreditierungsphase**:
    * ClientApp beauftragt OPS, ihm einen an einen Interimsport gebundenen Socket für eine Nachricht zu übergeben.
    * ClientApp schreibt Nachricht auf den Socket [mit Destination-IpAdresse (bekannt) und Destination-Port (= erhaltener Interimsport) auf den Socket.
    * ClientOps lauscht auf den akkreditierten Socket.
    * ClientOps liest Nachricht vom akkreditierten Socket.
    * ClientOps komplettiert Nachricht mit Source-IpAdresse (wie in der Akkreditierungsphase angestimmt).
    * ClientOps versendet Nachricht mit ARP+MSG an Router.

Anmerkung:

Wer genau welche Source-IP und Source-Port in das Paket einfügt, hängt von der Implementierung der IP-Bibliothek ab


### 3. Die Verpackungssystematik **[→ ZP:Sheet9]**

Welche Protokolle im Payload eines Packages zulässig sind, gibt jeweils ein Kenner an. Das Kennungsfeld heißt

* im Ethernetpackage: **Ethertype**. Zu möglichen Werten, siehe:
  * [https://de.wikipedia.org/wiki/Datenframe](https://de.wikipedia.org/wiki/Datenframe)
  * [https://de.wikipedia.org/wiki/Ethernet](https://de.wikipedia.org/wiki/Ethernet)
* im IPv4-Package: **Protokoll**. Zu möglichen Werten, siehe:
  * [https://de.wikipedia.org/wiki/IPv4](https://de.wikipedia.org/wiki/IPv4)
* im IPv6-Package: **Next Header**. Zu möglichen Werten, siehe:
  * [https://de.wikipedia.org/wiki/IPv6](https://de.wikipedia.org/wiki/IPv6)
* im TCP-Package: **Destination Port**. Zu möglichen Werten, siehe:
  * [https://de.wikipedia.org/wiki/Transmission_Control_Protocol](https://de.wikipedia.org/wiki/Transmission_Control_Protocol)
* im UDP-Package: **Destination Port**. Zu möglichen Werten, siehe:
  * [https://de.wikipedia.org/wiki/User_Datagram_Protocol](https://de.wikipedia.org/wiki/User_Datagram_Protocol)

### 4. Die Systematik der Portnummern  **[→ ZP:Sheet10]**

* (Layer-IV)-Port := Zahl zwischen 0 und 65535

* **Systemport** := 0 - 1023 (auch 'well-known ports', weil registriert bei der IANA). Beispiel:
  * `7`:= ECHO-Service 
  * `20` := FTP (Datenübertragung: nur TCP) 
  * `21` := FTP (Verbindungsaufbau und Steuerung: TCP, UDP)
  * `22` := SSH (TCP, UDP)
  * `23` := Telnet (unverschlüsseltes Textprotokoll, z. B. für Fernwartung)
  * `25` := SMTP (Simple Mail Transfer Protocol) /* Kommunikation unter Mailservern */
    * `110` :- pop3 /* Kommunikation Mailclient zu Mailserver */
    * `143` (`993`) :- imap(s) /* Kommunikation Mailclient zu Mailserver */
  * `67` := Bootstrap Protocol (auch von DHCP genutzt: nur per UDP)
  * `80` := HTTP (TCP, UDP)
  * `123`:= NTP (Network Time Protocol)
  * `319` := PTP (Precision Time Protocol) / Events (nur UDP)
  * `320` := PTP (Precision Time Protocol) / General Messages (nur UDP)
  * `443` := HTTPS (Hypertext Transfer Protocol over SSL/TLS: TCP, UDP)

* **Registrierte Ports** := 1024 – 49151 (irgendwo registriert oder kraft Konvention / 'Gebrauchsrecht' festgelegt). Beispiel:
  * `1434` := MSSQL
  * `1883` := MQTT 
  * `3306` := Mysql
  * `8080` := HTTP Alternative, für Proxyserver (Vermittler zwischen Client und realem Server) genutzt
  
* **Dynamische Ports** := 49152 – 65535 (Ports für Clients und Server-Clone)

vgl. [https://de.wikipedia.org/wiki/Liste_der_Portnummern]


### 5. Die wichtigsten Services im Überblick **[→ ZP:Sheet11]**


---

Bauanleitung:

1. Organisieren Sie 4 * 3 ineinander legbare Kartons.
2. Drucken Sie preambels.odt aus.
3. Legen Sie in jedes innerste Paket die Message.
4. Schneiden Sie für jedes Paket die Präambelzeilen ab
5. Kleben Sie die Präambeln von innen nach außen an die Unterseite der einzeln Schachteln.
6. Verpacken Sie alles zusammen in Geschenkpapier (steht für Ethernetpackage)

<!-- uebung::start -->

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/15:services:02**</span>

* [ ] Bitte teilen Sie sich in vier Gruppen auf
* [ ] Bitte nehmen Sie gruppenweise Ihr 'Geschenk' entgegen und entpacken Sie es vorsichtig.
* [ ] Kriegen Sie bitte heraus, was Sie da bekommen haben. Das sollten Sie in ca. 40 Min. erledigen können.
* [ ] Erstellten Sie dann in ca. 20 Min. eine kurze Präsentation, anhand Sie Ihren Mitschülerinnen charmant erläutern können, was Sie da bekommen haben. Leitfragen sind:
  * Was haben Sie bekommen?
  * Wie ist es aufgebaut und wie funktioniert es?
  * Wofür stehen die Komponenten des 'Geschenks' in der Wirklichkeit

<!-- uebung::end -->


Lösung:

__P1 *echo* (tcp/ipv4)__

* L7: 
> "Well done"
* L4 (tcp): `0xFFFB 0x0007 4*x 4*x 0x0 3*x 4*x
* L3 (ip): 4*x 4*x 1*x 0x06 2*x 0x23451234 0x43215423>
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x0800 4*? 12*x

Besonderheit: 

* Echo-Server-Port = 7 = 0x07, 
* Protocol-Nummer für TCP = 6 = 0x06
* EType für IP = 0x0800
* Geschenkpapier ist Ethernetpackage.

__P2 *http* (tcp/ipv4)__

* L7: 
> "GET /index.html HTTP/1.1\n
> Host: http://tierschutz.hessen.de/\n
> \n
> "
* L4 (tcp): `0xFFFA 0x0050 4*x 4*x 0x0 3*x 4*x`
* L3 (ip): 4*x 4*x 1*x 0x06 2*x 0x23451234 0x43215423
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x0800 4*? 12*x

Besonderheit: 

* Http-Server-Port = 80 = 0x50
* Protocol-Nummer für TCP = 6 = 0x06
* EType für IP = 0x0800
* Geschenkpapier ist Ethernetpackage.



__P3 *http* (udp/ipv4)__

* L7: 
> "GET /index.html HTTP/3.0\n
> Host: http://vegan.de/\n
> \n
> "
* L4 (udp): `0xFFFC 0x0050 0x0030 2*x`
* L3 (ip): 4*x 4*x 1*x 0x11 2*x 0x23451234 0x43215423
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x0800 4*? 12*a
* Geschenkpapier ist Ethernetpackage.

Besonderheit: 

* Http-Server-Port = 80 = 0x50
* Protocol-Nummer für UDP = 17 = 0x11
* EType für IP = 0x0800
* Geschenkpapier ist Ethernetpackage.

__P4 *telnet* (tcp/ipv6)__

* L7:
> "echo ‘well done’"
* L4 (tcp): `0xFFFD 0x0017 4*x 4*x 0x0 0x? 3*x 4*x`
* L3 (ipv6): 4*x 0x10 0x06 1*x 0x2001234767891618 0x2001816198767432
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x86DD 4*? 12*

Besonderheit: 

* Telnet-Server-Port = 23 = 0x17
* Protocol-Nummer für TCP = 6 = 0x06
* EType für IPv6 = 0x86DD
* Geschenkpapier ist Ethernetpackage.

---
