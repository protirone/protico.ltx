<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

*Tonspur* **[→ ZP:Sheet:1]**

### DNS im Überblick

* steht für Domain Name Service,
* bildet die uns vertrauten Domainnamen auf IP-Adressen ab,
* kommt in der ARP/IP4-Kommunikation noch vor der Kontaktaufnahme zum Zielrechner:
  * Schritt 0: Wenn nur Domain-Name des Kommunikationspartners bekannt, dann DNS-Anfrage beim DNS-Server
  * Schritt 1 bei der Kommunikation: Berechne, ob IP-Adresse des Partners im eigener Broadcastdomain.
  * Schritt 1.A: Wenn ja, ARP-Request.
  * Schritt 1.B: Wenn nein, ARP-Request zum Router zwecks Weiterleitungsauftrag.

* Root und Top-Level-Domains (TLD): werden von IANA verwaltet. Sie unterscheidet zwei Gruppen: 
   * GTLD steht für generische Top-Level-Domains
   * CCTLD für Country Code Top-Level-Domains, abgeleitet von den ISO-3166-1-Ländercodes
* Von den initialen sieben GTLDs aus 1985 waren zuerst nur 3 frei registrierbar. 2001 hat die IANA neue aufgenommen.
* Die Verwaltung der TLDs wird von der IANA an Registrare delegiert.
* Die .de-Domäne wird von der [Denic](https://www.denic.de/) gemanagt.
* Provider lassen dort im Namen Ihrer Kunden ihre Domänen registrieren. Manche bieten dem Kunden den Service, eigene Subdomänen anzulegen.
* Aus der Baumstruktur ergibt sich, dass jeder generierbare Name eindeutig ist.


Grund für Parallelität von Namen und IP-Adressen:

* Namen sind für Menschen einfacher zu merken als Zahlen.
* Sind sprechender Name und IP-Adresse entkoppelt, können Rechner einfacher in andere Netze migriert werden.

* → [https://www.netplanet.org](https://www.netplanet.org)
* → [https://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste](https://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste)
* → [https://www.denic.de/](https://www.denic.de/)

### DNS Server

Domain-Name und IP-Adresse müssen verlässlich aufeinander abgebildet werden. Deshalb die Regeln:

* „Jeder, der Namen und IP-Adressbereiche registriert und zur Verwaltung bekommt, muss einen Nameserver führen, der weltweit zur Verfügung steht.“
* Jeder, der Namens- und Adressbereiche weiterreicht, gibt die Adresse(!) seines/r Nameserver(s) an seine Kunden weiter.
* Jeder, der einen Nameserver aufsetzt, trägt die Adresse des vom Provider erhaltenen Nameservers als (Quasi) ’Gateway’ für den eigenen  Nameserver ein, an den der aufgesetzte Nameserver Fragen weiterreicht, die er nicht beantworten kann.
* Nameserver reichen die eigenen arpa-in-addr-Subbäume nach oben weiter.

* → Schreiner2014a, S.91

Jeder Nameserver hat zwei Bereiche:

* **Forward-Lookup-Zone** = Informationen zur Auflösung von Namen auf IP-Adressen.
  * Baum mit allen auflösbaren Domainnamen, an dessen Blätter die IP-Adressen vermerkt sind.
  * Nicht auflösbare angefragte Domainnamen werden an höhere Instanzen weitergereicht.
  * Nur teilweise auflösbare Domainnamen werden an den zuständigen tieferen Nameserver weitergereicht.
  * `nslookup $DOMAINNAME$` löst den Namen zur IPv4-Adresse auf.
* **Reverse-Lookup-Zone** = Informationen zur Auflösung von IP-Adressen auf Domainnamen.
  * Baum mit allen IP-Adressen, an dessen Blätter die Domainnamen vermerkt sind.
  * `nslookup $IPADDRESS$` löst den IPv4-Adresse zum Namen auf.




---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:14:DNS:01**</span>

* [ ] Ermitteln Sie die IP-Adresse von `dns.google`
* [ ] Ermitteln Sie den Domainnamen von `8.8.8.8`

<!-- uebung::end -->

---



