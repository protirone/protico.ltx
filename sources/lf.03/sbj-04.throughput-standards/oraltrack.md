<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1. Kabeltypen **[→ ZP:Sheet:2]**

* **Thin-Wire** (Koaxialkabel):
  * *10BASE2* = dünnes, flexibles Koaxialkabel (→  Thin Ethernet, ThinWire oder Cheapernet)
  * *10BASE5* = dickes, unflexibles, teures Koaxialkabel
  * für Bus-Topologien
  * (→ [https://de.wikipedia.org/wiki/10BASE2](https://de.wikipedia.org/wiki/10BASE2))
* **Twisted Pair** für die universelle Gebäude-Verkabelung (UGV)
  * *10BASE-T* für Stern-Topologien 
* **Glasfaser** für die universelle Gebäude-Verkabelung (UGV)

Differenziert auch nach der Kabelabschirmung **[→ ZP:Sheet:3]**

Benennungsschema nach ISO-11801: **[→ ZP:Sheet:4]**

* Gesamtabschirmung '/' Adernpaarabschirmung InnererKabeltyp

* Gesamtabschirmung :- [ U (ungeschirmt/unshieled) | F (Folienschirm/foiled) | S (Geflechtschirm/screened) | SF (Geflecht- und Folienschirm) ]
* Adernpaarabschirmung :- [ U (ungeschirmt/unshieled) | F (Folienschirm/foiled) | S (Geflechtschirm/shieled) ]
* InnererKabeltyp* :- [ TP (Twisted Pair) | QP (Quad Pair) ]

ergibt: U/UTP, S/STP, F/STP, S/UTP, F/UTP oder SF/UTP

Vereinfacht:

* **U/UTP** = *Unshielded Twisted Pair* (Cat5e-Kabel): 
  * Kabel einzeln gegen andere abgeschirmt (keine sonstige Abschirmung)
  * Kabel paarweise verdrillt (twisted).
  * Genutzt bei Fast- und Gigabit-Ethernet.
* **U/STP** = *Shielded Twisted Pair*: 
  * Kabel einzeln gegen andere abgeschirmt 
  * Kabel paarweise verdrillt (twisted).
  * Mit einer unbekannten Abschirmung der Paare gegeneinander.
  * Genutzt bei Fast- und Gigabit-Ethernet.
* **S/STP** = *Screened Shielded Twisted Pair*: 
  * Kabel einzeln gegen andere abgeschirmt 
  * Kabel paarweise verdrillt (twisted).
  * Kabel paarweise mit Geflecht gegen andere Paare abgeschirmt.
* **S/FTP** = *Screened/Foiled Shielded Twisted Pair*: 
  * Kabel einzeln gegen andere abgeschirmt 
  * Kabel paarweise verdrillt (twisted).
  * Kabel paarweise mit Geflecht gegen andere Paare abgeschirmt
  * Kabel zusammen mit einer Folie gegen Außeneinfluss abgeschirmt.
  * Für CAT6a-Kabel und CAT7-Kabel verwendet.
* [→ Gratzke et.al: Technische IT Berufe, Lernfelder 6-9, 2022, S. 325ff]
* [→ [https://de.wikipedia.org/wiki/Twisted-Pair-Kabel](https://de.wikipedia.org/wiki/Twisted-Pair-Kabel)]

Achtung: Englische Seite nutzt leicht andere Bezeichner. Dort wird 'Screened' (versus Foilded) als
Bezeichnung für den Schutz des Kabelpaares benutzt, nicht für die Umhüllung als Ganzes.
[→ [https://en.wikipedia.org/wiki/Twisted_pair](https://en.wikipedia.org/wiki/Twisted_pair)]

Grundsatz: je komplexer die Abschirmung, desto teurer

Industriebenennungen weichen von der ISO-Norm ab.

**Weitere Kabeltypisierung:**

| Category | Construction | Bandwidth | Application |
| --- | --- | --- | --- |
| Cat 3	| UTP |	16 MHz |	10BASE-T, 100BASE-T4 |
| Cat 4	| UTP |	20 MHz |	16 Mbit/s Token Ring |
| Cat 5	| UTP	| 100 MHz |	100BASE-TX, 1000BASE-T |
| Cat 5e	| UTP, F/UTP, U/FTP |	100 MHz |	1000BASE-T, 2.5GBASE-T |
| Cat 6	  | UTP, F/UTP, U/FTP |	250 MHz |	5GBASE-T, 10GBASE-T |
| Cat 6A	| UTP, F/UTP, U/FTP, S/FTP | 500 MHz | 5GBASE-T, 10GBASE-T |
| Cat 7	  | S/FTP, F/FTP | 600 MHz | ? |
| Cat 7A	| S/FTP, F/FTP | 1 GHz  | ? |
| Cat 8.1	| F/UTP, U/FTP | 2 GHz  |	25GBASE-T, 40GBASE-T |
| Cat 8.2 | S/FTP, F/FTP | 2 GHz	| 25GBASE-T, 40GBASE-T |

[→ [https://en.wikipedia.org/wiki/Twisted_pair](https://en.wikipedia.org/wiki/Twisted_pair)]

Grundsatz: Je höher die Kategorie (Kabeltyp), desto höher die Bandbreite und komplexer die Abschirmung


### 2. Datendurchsatz **[→ ZP:Sheet:5]**

Übertragungsgeschwindigkeit (max. Datendurchsatz) in einem Kabel 

* = `max(Datenmenge)/ Zeit`
* oft ausgedrückt als **Mbps** = Mega**bits** per Seconds

Hinweis:

* **MB/s** steht für *Mega__bytes_* per Seconds
* **Mbps** steht für *Mega__bits_* per Seconds (MBits/s)
  * Im Internetkontext auch: **Mbit/s**: `1 Mbps = 1 Mbit/s = 1.000.000 Bits pro Sekunde.`


* Kleinere Einheiten:
  * **KB/S** = **Kilo**_bytes_ per Seconds
  * **Kbps** = **Kilo**_bits_ per Seconds
* Zusammenhang Bits:
  * `1000 Bits per Second` = `10^3 Bps` = `1 Kbps`
  * `1000 Kilobits per Second` = `10^3 Kbps` = `1 Mbps` = `10^3*10^3=10^6 Bps`
* Zusammenhang Bytes:
  * `1000 Bytes / s` = `10^3 B/s` = `1 KB/s`
  * `1000 Kilobytes / s` = `10^3 KB/s` = `1 MB/s` = `10^3*10^3=10^6 B/s`

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF03:03:Verdrahtung:01**</span>

Gesetzt, ein Kabel kann maximal 512 Kbps übertragen. Wie lang braucht die Übertragung
von ein 2 Megabyte großes Bild, wenn man von Störung und den Protokollbytes/-bits abstrahiert?

<!-- uebung::end -->

**Lösung:** 

```
1.)  2 MB = 2000 KB = 16.000 KBits
2.)  16.000 Kbits /  512 Kbps = 31.25 sec.

```

---

### 3. Ethernetstandards **[→ ZP:Sheet:6]**


Ethernetstandards basieren auf *Mbps*:

* **Ethernet** = IEEE Standard 802.3 = *10 Mbps*
* **Fast Ethernet / 100Base-T** = IEEE Standard 802.3u = *100 Mbps*
* **Gigabit Ethernet/ GigE** = IEEE Standard 802.3z = *1000 Mbps*
* **10 Gigabit Ethernet** = IEEE Standard 802.3ae = *10 Gbps*


### 4. Verfeinerte Größenangaben **[→ ZP:Sheet:7]**


Umrechnung von Kilo[byte/bits] in [Bytes/Bits] oft unklar kommuniziert: 

* Besteht 1 Kilo[byte] nun 1000 oder 1024 [Bytes/Bits]? Unklar, weil
* *Kilo* (`10^3`), *Mega* (`10^6`), *Giga* (`10^9`) auf das metrische System bezogen 
* Bytes und Bits auf das duale System bezogen:

> Da `2^10` = 1024 sehr nahe bei 1000 liegt, bürgerte es sich ein, bei 
> Größenangaben von Datenmengen in Bit und Byte den 
> Vorsatz Kilo für 1024 zu verwenden 
> 
> (→ [https://de.wikipedia.org/wiki/Vorsätze_für_Maßeinheiten](https://de.wikipedia.org/wiki/Vors\ätze_für_Maßeinheiten))

Beispiel: 

* Vom *Atari Mega STE 4* wurde gesagt, er habe "4 **MB** ST RAM"
(→ [https://en.wikipedia.org/wiki/Atari_MEGA_STE](https://en.wikipedia.org/wiki/Atari_MEGA_STE)). 
* Das wären 1000 Kilobytes = 1000*1000 = 10^6 Bytes gewesen.
* Tatsächlich und von der Sache her hatte er aber eine 2er-Potenz-Zahl an Ram.
* Nämlich 1024*1024 = 2^20 = Bytes

Deshalb gibt es zwei gesonderte Präfixsysteme als Standard:

Dezimal | Kürzel | Größe | Binär | Kürzel | Größe
|---|---|---|---|---|---|
| Kilo | K | `10^3` | Kibi | Ki | `2^10` |
| Mega | M | `10^6` | Mebi | Mi | `2^20` |
| Giga | G | `10^9` | Gibi | Gi | `2^30` |
| ... | ... | ... | ... | ... | ... |

Da Kibi etc. im Binärkontext entstanden und verwendet spricht man dann von

* Kibibytes (KiB) / Kibibits
* Mebibibytes (MiB) / Mebibits
* Gibibibytes (GiB) / Gibibits

usw. für Tera/Tebi, Peta/Pebi, Exa/Exbi, Zetta/Zebi, Yotta/Yobi, Ronna/Robi, Quetta/Quebi


* **Bit** = `2^1` mögliche Zustände
* **Nibble** = *Halb-Byte* = `2^4` = 16 mögliche Zustände
* **Byte** = *Oktett* = 2 *Nibble* = `2^8` = 256 mögliche Zustände
* **Kilobyte** (*KB*) = `10^3` Byte = 1000 Byte 
* **Kibibyte** (*KiB*) = `2^10` Byte = 1024 Byte
* **Megabyte** (*MB*) = `10^6` Byte = 1.000.000 Byte 
* **Mebibyte** (*MeB*) = `2^20` Byte = 1.048.576 Byte
* **Gigabyte** (*GB*) = `10^9` Byte =  1.000.000.000 Byte
* **Gibibyte** (*GiB*) = `2^30` Byte = 1.073.741.824 Byte
* **Terabyte** (*TB*) = `10^12` Byte = 1000 GB
* **Tebibyte** (*TiB*) = `2^40` Byte = 1.099.511.627.776 Byte

usw. für Peta/Pebi, Exa/Exbi, Zetta/Zebi, Yotta/Yobi

* [→ [https://de.wikipedia.org/wiki/Datenmenge](https://de.wikipedia.org/wiki/Datenmenge)]
* [→ [https://de.wikipedia.org/wiki/Vorsätze_für_Maßeinheiten](https://de.wikipedia.org/wiki/Vors\ätze_für_Maßeinheiten)]

Hinweis: Die implizite Größenerweiterung betrifft u.U. auch die Dateisysteme und Dateien 
(falls das Format mit 2^x-Vielfachen arbeitet)

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF03:03:Verdrahtung:02**</span>

Gesetzt,

* es wird von einem Rechner zu seinem Gateway eine 12 Mebibyte große Datei übertragen,
* Rechner und Gateway sind mit einer Gigabit Ethernet/ GigE verbunden (= *1000 Mbps* Durchsatz),
* Störungen und Protokollbits können vernachlässigt werden,
  
Wie lang braucht die Übertragung?

<!-- uebung::end -->

**Lösung:**

```
1.) 12 MiB = 12 * 2^20 * 8 =  12 * 1048576 * 8 
    = 100.663.296 Bits = 100,663296 Mbits
2.) 100,663296 Mbits / 1000 Mbps = 0.100663296 s

```

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:03:Verdrahtung:03**</span>

Nehmen Sie an, sie hätten 3840 Messungen in einer Datei gespeichert und das jede einzelnen Messung 
in drei 32-Bit-Zahlen erfasst sei.

1. [ ] Berechnen Sie, wie viele Kibibyte Sie benötigen, um die 3840 Messungen zu speichern. 
2. [ ] Nehmen Sie jetzt an, jede Messung solle zusätzliche durch ein 3 Byte großes Integer verfeinert werden. Berechnen Sie,
      wieviel verschiedene Werte sich mit den 3 Bytes erfassen lassen.
3. [ ] Berechnen Sie, wie viel Prozent Speicher Sie pro Messung zusätzlich benötigen, um auch das 3-Byte-Integer mit zu erfassen.

<!-- uebung::end -->


**Lösung:** 

*zu 1.)*

```
A.) Bei 3840 Messung mit je drei 32 Bit-Werten  
    ergeben sich 3840 * 3 * 32 = 368640 Bits
B.) 1 Kibibyte = 2^10 Bytes * 8 = 8192 Bits
C.) 368640 Bits / 8192 = 45 KiB

```

*zu 2.)*

```
3 Bytes a 2^8 Bits = 2^8 * 2^8 * 2^8 = 2^(8+8+8) 
  = 2^24 = 16.777.216
```

*zu 3.)*

```
A) Bisher pro Messung 3*32 Bits = 96 Bits.
B) Zusätzlicher Speicherbedarf 3-Byte-Integer: 
   3*8 Bits = 24Bits
C) Speicherbedarf insgesamt jetzt 120Bits.
D) Mehrbedarf von 24Bits sind 25% von 96Bits (24/96*100=25%)
E) Vom neuen Gesamtbedarf aus gesehen, sind
   - 96 Bits 80% von 120 Bits (96*100/12=80%)
   - 24 Bits 20% von 120 Bits (24*100/120=20%)
```

---

### 5. Wlan-Standards **[→ ZP:Sheet:8]**


WLAN-Typen/Techniken werden ebenfalls anhand der in einer Sekunde übertragbaren 
Datenmenge klassifiziert:

* **IEEE 802.11a** = max. 54 Mbps im 5GHz Band
* **IEEE 802.11b** = max 11 Mbps im 2,4 GHz Band
* **IEEE 802.11g** = max 54 Mbps im 2,4 GHz Band
* **IEEE 802.11n** = Wi-Fi4 = erlaubt max 289 Mbps im 2,4 GHz Band + max 600 Mbps im 5GHz Band
* **IEEE 802.11ac** = Wi-Fi5 = seit 2014 mit max. 6933 Mbps nur 5GHz Band
* **IEEE 802.11ax** = Wi-Fi6 = seit 2021 mit max. 9600 Mbps im 2,4-GHz- + im 5-GHz-Band 
* **IEEE 802.11be** = Wi-Fi7 = seit 2024 mit 46 Gbit/s im 2,4-GHz-, 5-GHz- und 6-GHz-Band
* **IEEE 802.11 Mrd.** = Wi-Fi8 = voraussichtlich 2028 
* [→ Gratzke et.al: Technische IT Berufe, Lernfelder 6-9, 2022, S. 326ff]

* GHz-Bänder = Frequenzbänder, in denen Daten übertragen werden. 
* Je höher die GHz-Zahl, desto größer die Geschwindigkeit bei geringerer Reichweite!

Zu den neueren Standards vgl.:

* [→ [https://praxistipps.chip.de/wifi-4-5-6-7-wifi-8-das-sind-die-unterschiede\_114441](https://praxistipps.chip.de/wifi-4-5-6-7-wifi-8-das-sind-die-unterschiede\_114441)]
* [→ [https://de.wikipedia.org/wiki/Wireless\_Local\_Area\_Network](https://de.wikipedia.org/wiki/Wireless\_Local\_Area\_Network)]


### 6. Wlan-Sicherheit **[→ ZP:Sheet:9,10]**

* Netze auf Kabelbasis sind physikalisch vor ungewolltem Zugriff geschützt. 
  * (Anm.: Jedenfalls in Maßen: mit kriminellem Aufwand können Kabel physikalisch 'angebohrt' werden.)
* WLAN-Netze anhand ihrer SSID identifizierbar
* Kommunikation über ARP. D.h. Pakete sind prinzipiell mitlesbar.
* Deshalb schon sie Netzwerkebene verschlüsselt mit WEP, WPA, WPA2 und WPA3 
* [→ [https://www.security-insider.de/was-ist-wlan-verschluesselung-a-742212/](https://www.security-insider.de/was-ist-wlan-verschluesselung-a-742212/) und dessen Subseiten zu WEP, WPA, WPA2 und WPA3 ]

* **WEP** = *Wired Equivalent Privacy* 
  * Verschlüsselung: RC4-Verschlüsselung, kleiner 24Bit-Schlüssel, konstanter mit übertragener Initialisierungsvektor 
  * Angriff: Sammle möglichst viele Nachrichten, probiere die `2^24` = 16.777.216 Varianten einfach aus (Brute Force Attack) 
* **WPA** = Wie WEP, aber mit TKIP (Temporal Key Integrity Protocol) zur Verschlüsselung 
  * Jede Nachricht kriegt eigenen Schlüssel. Aber: hängt von Qualität des Schlüssels ab (= Pre-shared Keys). 
  * Wegen weiter verwendeter RC4-Verschlüsselung ebenfalls knackbar.
* **WPA2** = verbesserte Verschlüsselungsmethode 
  * Jetzt mit AES (Advanced Encryption Standard) und CCMP (Counter Mode with Cipher Block Chaining Message Authentication Code Protocol) als Protokoll für die einzelne Verschlüsselung. 
  * Gilt als sicher bei großem Passwort (= Pre-shared Key), aus denen die Sitzungsschlüssel errechnet und ausgetauscht werden (obwohl 2017 ein Angriff skizziert worden ist) 

Zur Frage nach der Sicherheit in WLANs gehört Verschlüsselung (s.o.) und Authentifizierung (s.u). 

* **WPA-PSK** = Pre-Shared-Key (= nutzungsberechtigt, wer das Passwort des WLAN-Netzes kennt)
  - Vorteil: Um jmdn. Zugriff zu gewähren, reicht es, das Passwort weiterzureichen.
  - Nachteil: Dasselbe Passwort für alle. Gefahr der 'unerlaubten' Weitergabe.
  - Nachteil: Den Zugang für eine zu verhindern, heißt, das Passwort (= den Pre-Shared-Key) für alle zu ändern.
- **Radius-Server** = * Remote Authentication Dial-In User Service* (= De-facto-Standard bei der zentralen Authentifizierung von Einwahlverbindungen über Modem, ISDN, VPN, WLAN (IEEE 802.1X) und DSL )
  - zentraler personenbezogener Authentifizierungsserver
  - wird über EAP (Extensible Authentication Protocol) angesprochen
  - [→ [https://de.wikipedia.org/wiki/Remote\_Authentication\_Dial-In\_User\_Service](https://de.wikipedia.org/wiki/Remote\_Authentication\_Dial-In\_User\_Service)]

* **WPA3** = nochmals verbesserte Verschlüsselungsmethode mit Aufgabe pre-shared-Key

