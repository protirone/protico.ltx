<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->



### (1) Ausgang

* Aus Lernfeld 9 ist die Paketverschachtelung bekannt.

### (2) Layer-7-Services

Si


### (3) Portsystematik:


* Services numerisch durch Layer-IV-Port identifiziert.
* Server-App fordert beim Betriebssystem einen Socket an.
* Server teilt dem OS mit, welche Nachrichten (Layer IV) (= welchen Ports und Typs) es ihm aus der Netzwerkschnittstelle auf diesen Socket zum Empfang schreiben soll = auf welchen Port es für ihn 'lauschen' soll.


* Layer-IV-Port := Zahl zwischen 0 und 65535
  * **Systemport** := 0 - 1023 (auch 'well-known ports', weil registriert bei der IANA). Beispiel:
    * `7`:= ECHO-Service 
    * `20` := FTP (Datenübertragung: nur TCP) 
    * `21` := FTP (Verbindungsaufbau und Steuerung: TCP, UDP)
    * `22` := SSH (TCP, UDP)
    * `23` := Telnet (unverschlüsseltes Textprotokoll, z. B. für Fernwartung)
    * `25` := SMTP (Simple Mail Transfer Protocol)
    * `67` := Bootstrap Protocol (auch von DHCP genutzt: nur UDP)
    * `80` := HTTP (TCP, UDP)
    * `123`:= NTP (Network Time Protocol)
    * `319` := PTP (Precision Time Protocol) / Events (nur UDP)
    * `320` := PTP (Precision Time Protocol) / General Messages (nur UDP)
    * `443` := HTTPS (Hypertext Transfer Protocol over SSL/TLS: TCP, UDP)

  * **Registrierte Ports** := 1024 – 49151 (irgendwo registriert oder kraft Konvention / 'Gebrauchsrecht' festgelegt). Beispiel:
    * `1434` := MSSQL
    * `1883` := MQTT 
    * `3306` := Mysql
    * `8080` := HTTP Alternative, für Poxyserver (Vermittler zwischen Client und realem Server) genutzt
  
  * **Dynamische Ports** := 49152 – 65535 (Ports für Clients und Server-Clone)

vgl. [https://de.wikipedia.org/wiki/Liste_der_Portnummern]

## Transportart

* **TCP** = *Transport Control Protocol* ist ein "zuverlässiges, verbindungsorientiertes, paketvermitteltes Transportprotokoll" (vgl. [https://de.wikipedia.org/wiki/Transmission_Control_Protocol] )
  * etabliert eine Verbindung nach 3-Wege-Handshake
  * Pakete werde numeriert = Reihenfolge auf Empfängerseite rekonstruierbar 
  * organisiertdas Wiederanfordern 'verlorengegangener Pakete'
  * deshalb SOCK_STREAM 
* **UDP** = *User Datagram Protocol* = "minimales, verbindungsloses Netzwerkprotokoll" (vgl. [https://de.wikipedia.org/wiki/User_Datagram_Protocol])
  * Fire \& Forget
  * deshalb SOCK_DATAGRAM
  * trotzdem bei Streaming-Diensten genutzt
