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

* das Package-in-Package-Prinzip **[→ ZP:Sheet4]**


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
* 3) (Er)finden Sie einen allgemein gültigen, in mehreren Instanzen parallel ausführbaren Prozess, 
  * der die bisher besprochenen Techniken nutzt 
  * der damit eine Nachricht von APP(BCA) zu APP(BCB) und die Antwort zurück übermittelt und
  * der die Regel beachtet, dass nur das Betriebssystem von der Netzwerkkarte lesen und auf die Netzwerkkarte schreiben kann.
* 4) Führen Sie Ihren Prozess als Schreibtischtest durch.
* 5) Dokumentieren Sie Prozess als Aktivitätsdiagramm

<!-- uebung::end -->

---


### 2. Die Kommunikation zwischen (Client)App und (Server)App


### 3. Der Echo-Client-Server-Verbund als Beispiel



### 4. Die Systematik der Portnummern


### 5. Die wichtigsten Services im Überblick
