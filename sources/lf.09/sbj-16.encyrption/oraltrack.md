<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 1. Einstieg **[→ ZP:Sheet2]**

---

<!-- uebung::start -->

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/16:Verschlüsselung:01**</span>

* [ ] Bitte entschlüsseln Sie den Text

```
xvd-sulydwh-gdwhq-yrq-vlfkhukhlwvsrolwlnhuq-lp-qhwC
```

<!-- uebung::end -->

Lösung:

* Der Text steht für `usa-private-daten-von-sicherheitspolitikern-im-netz`
* Er ist Teil eines Links zu einem Spiegelartikel:

[https://www.spiegel.de/netzwelt/web/usa-private-daten-von-sicherheitspolitikern-im-netz-a-132886fa-7d7e-4698-9507-a3423b23bddc](https://www.spiegel.de/netzwelt/web/usa-private-daten-von-sicherheitspolitikern-im-netz-a-132886fa-7d7e-4698-9507-a3423b23bddc)

* Die Verschlüsselung ist die Caesar-Verschlüsselung in der Standardkonfiguration
  * Algorithmus: Verschiebe den realen Buchstaben um n Buchstaben nach rechts.
  * Schlüssel: n
* → Onlinetool: [https://www.kryptowissen.de/caesar-chiffre-praxis.php](https://www.kryptowissen.de/caesar-chiffre-praxis.php)
* → Algorithmus: [https://www.kryptowissen.de/caesar-chiffre.html](https://www.kryptowissen.de/caesar-chiffre.html)
* → Veranschaulichung: [https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung](https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung)
---

### 2. Begriffe 

* **Verschlüsselung** (= Chiffrierung, Codierung)
  * = Umwandlung (elektronischer) Texte, Bilder, Sprachnachrichten, Sourcecode, Payloads eines Netzpaketes - will sagen: den 'Klartext' - "[...] in eine unverständliche Zeichenfolge" - will sagen: in den 'Geheimtext' (Chiffrat [BSI])
  * dient: der Geheimhaltung und soll "[...] gegen unbefugtes 'Mitlesen' zu schützen".
  * braucht: i.d.R einen Schlüssel und eine Vorschrift, wie der auf den Klartext anzuwenden ist, damit das Chiffrat entsteht.
* **Entschlüsselung** (= Dechiffrierung, Decodierung) 
  * meint die systematische Umkehr der Verschlüsselung in Kenntnis des Schlüssels.
* **Entzifferung**
  * meint die 'Enträtselung' eines codierten Textes in Unkenntnis Schlüssels
* **Kryptologie** = Wissenschaft von der Verschlüsselung (Oberbegriff)
  * *Kryptanalyse* (= Kryptoanalyse) = Wissenschaft von der Entzifferung von Geheimtexten
  * *Kryptographie* = Wissenschaft von den Verschlüsselungstechniken = dem Erzeugen gut verschlüsselter Texte
* **Schlüssel** (= Passwort)
* **Zielvorgabe**:
  * Verschlüsselung und Entschlüsselung muss (für einen Computer) einfach sein, wenn der Schlüssel bekannt ist.
  * Ohne Kenntnis des Schlüssels soll eine Enträtselung / Entschlüsselung nicht möglich sein = selbst mit beträchtlichen Ressourcen oder in Kenntnis des Verfahrens.
  
**Konsequenz:** im obigen Beispiel ist

1. `xvd-sulydwh-gdwhq-yrq-vlfkhukhlwvsrolwlnhuq-lp-qhwC` das Chiffrat, 
2. das mit dem Caesar-Verfahren *entschlüsselt* wird,
3. wenn man die Zahl 3 als Schlüssel hat.
4. Wenn man den Schlüssel nicht hat, muss man den verschlüsselten String (das Chiffrat) *entziffern* (dechiffrieren).
5. Die Zielvorgabe ist nicht erfüllt: Entschlüsselung ist einfach, Entzifferung (ohne Schlüssel) aber auch (Brute-Force-Ausprobieren.) (hängt linear von der Anzahl der Buchstaben im Alphabet ab.)


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/16:Verschlüsselung:02**</span>

* [ ] Vereinbaren Sie einen Kanal/Medium, über den/das Sie Nachrichten an alle Mitglieder der Klasse versenden können.
* [ ] Teilen Sie sich in zwei Gruppen auf.
* [ ] Einigen Sie sich in jeder Gruppe auf einen Verschlüsselungsalgorithmus und einen Schlüssel. Lassen Sie Ihre Fantasie walten.
* [ ] Testen Sie Prozedere in der Gruppe.
* [ ] Jede Gruppe sende eine Emissärin aus Ihrer Gruppe mit ihrem Messanger zur Lehrerin. 
* [ ] Jede Emissärin setze sich deutlich getrennt von Ihrer Gruppe (und der Konkurrenz) hin und
  * [ ] empfange eine spezifische Nachricht, 
  * [ ] verschlüssele diese Nachricht gemäß des Gruppenalgorithmus/Schlüssels
  * [ ] versende diese Nachricht über den für alle Schülerinnen zugänglichen Kanal.
* [ ] Jede Gruppe 
  * [ ] empfange die Nachricht,
  * [ ] entschlüssele sie
  * [ ] und notiere sie
  * [ ] stecke die Notiz in einem Umschlang und
  * [ ] notieren sich die verschlüsselte Nachricht der anderen Gruppe
* [ ] Jede Gruppe versuche, die Nachricht der anderen Gruppe zu entziffern.

Hinweis:

* Sie dürfen für die Verschlüsselung, Entschlüsselung und/oder Entzifferung jede Methode anwenden, die Ihnen einfällt - außer solche, die Gewalt beinhalten.
* Überlegen Sie schon bei der Konzeption Ihrer Verschlüsselung ein Verfahren zur Entzifferung / Entschlüsselung der Gegenseite.


<!-- uebung::end -->

Lösung: 


---

### Verfahren:

* **symmetrische Verfahren** verwenden zur Ver- und Entschlüsselung denselben Schlüssel
  * *Substitutionsverfahren* = z.B. Monoalphabetische Substitution: Caesar-Verschlüsselung [A>C]
  * *Transpositionsverfahren* = Durcheinanderwürfeln des Textes
  * *Stromverschlüsslung*: die Zeichen des Klartextes jeweils einzeln und nacheinander verschlüsselt.
  * *Blockverschlüsselung*: Klartext vorab in Blöcke aufgeteilt, die (kontextbedingt) verschlüsselt werden
  * moderne Verfahren:
    * **RC4** (Rivest Cipher 4)
      * verarbeitet Daten als Bitstrom
      * Schwachstellen bekannt
    * **AES** (Advanced Encryption Standard) 
      *  = 1998 entwickelt
      *  Schlüssellänge von 128, 192 oder 256 Bit 
      *  arbeitet mit festen 128-Bit-Datenblöcke
      *  gilt als sicher  
  * Vorteil: schnellere Berechnung 
  * Nachteil: Schlüssel ist mehreren bekannt.
* **asymmetrische Verfahren** (= Public-key cryptography), benutzen zur Verschlüsselung einen "völlig anderen" Schlüssel als zur Entschlüsselung
  * *öffentlicher Schlüssel* zum Verschlüsseln 
    * wird weitergegeben
    * kann den Text NICHT entschlüsseln, (nicht mal vom Verschlüssler)
  * *privater Schlüssel* zum Entschlüsseln 
    * wird NICHT weitergegeben
  * *Bedingung* 
    * privater Schlüssel darf nicht in absehbarer Zeit (Jahre) aus dem öffentlichen Schlüssel berechnet werden können
    * benötigt **Einwegfunktion** = eine mathematische Funktion, die einfach zu berechnen ist, ihre Umkehrung jedoch nur sehr schwer.
      * Modulo-Division
      * einfach zwei große Primzahlen zu multiplizieren, jedoch sehr schwer das Ergebnis wieder in seine Primfaktoren zu zerlegen.
  * Beispiel
    * 1975: erste Idee von Diffie und Hellmann
    * 1977: **RSA**=Algorithmus = erste anwendbarer Funktion 
      * erfunden L. Rivest, A. Shamir und L. M. Adleman 
      * Grundidee: es gibt keinen effizienten Algorithmus gibt, um eine große natürliche Zahl in ihre Primfaktoren zu zerlegen.
    * 1978 McEliece Kryptosystem, 
    * 1979 das Rabin Kryptosystem, 
    * 1984 das Chor-Rivest Kryptosystem u
    * 1985 das ElGamal Kryptosystem 
  * Vorteil: Schlüsselaustausch über unsichere Netzwerke möglich.
  * Nachteil: die erhöhte Rechenleistung (RSA 1000 mal langsamer als AES)
* **hybride Verfahren**: organisieren Schlüsselaustausch asymmetrisch, die Verschlüsselung symmetrisch.

### Hashverfahren

**Hashfunktion** bildet einen Text variabler Länge (große Daten) auf kleineren Text/Zahl fester Länge ab.
* Der Hashwert sollte für jeden Text eineindeutig sein.
* kurzer Hash:
  * Vorteil: schnellere Berechnung
  * Nachteil: größere Gefahr der Kollision
* langer Hash:
  * aufwendige Berechnung
  * kleine Kollisionsgefahr,
* **md5** ( = Message Digest 5) älterer Algorithmus v. 1991 
* **SHA** ( Secure Hash Algorithm) in verschiedenen Versionen
  * SHA-1 = 160-Bit-Ausgabe
  * SHA-2 = 224-, 256-, 384- oder 512-Bit-Ausgabe
  * SHA-3 = 24-, 256-, 384- oder 512-Bit-Ausgabe
  * SHA256 spezielle Version von SHA-2
* Entscheidungskriterium 
  * 'sicher': SHA-2 oder SHA-3
  * Effizienz: MD5 oder SHA-1 (aber knackbar = leicht Kollision zu erzeugen)
* Anwendungs
    * Download-Verifikation
    * s. google.
* Anwendungen
  * bash/LX: `echo "Hello world" | openssl sha256`
  * bash/LX: `echo 'hello world' | sha256sum`
  * powershell/WIN: Get-FileHash
  * commandshell: CertUtil


### Verschlüsselung in Netzwerken

* **Leitungsverschlüsselung** = Nachricht nur jeweils für den Nachbarrechner verschlüsselt, der entschlüsselt die Nachricht, verschlüsselt sie wiederum (mit einem möglicherweise anderen Verfahren) und schickt sie an seinen Nachbarn
  * Vorteil: nur Nachbarrechner müssen sich auf ein Verschlüsselungsverfahren und verwendete Schlüssel einigen
  * Vorteil: Übertragung auf niedriger Protokollebene (auch Übertragungs-Hardware) möglich
  * Nachteil: jeder einzelne Rechner auf dem Übertragungsweg muss vertrauenswürdig und sicher sein.
* **Ende-zu-Ende-Verschlüsselung** = Nachricht vom Absender verschlüsselt und in dieser Form unverändert über mehrere Rechner hinweg zum Empfänger übertragen
  * Vorteil: Man-in-the-Middle-Attacks nicht möglich
  * Nachteil: Sender muss mit jedem Empfänger ein Verschlüsselungsverfahren und zugehörige(n) Schlüssel ausmachen

* **TSL** (= Transport Layer Security ) Verschlüsselung zwischen Layer VII und Layer IV 
  * Beispiels `https` - aber auch andere. 
  * TSL 1.0/1999 1.1/2006 1.2/2008 1.3/2018
  * Vorgänger Secure Sockets Layer (SSL 1.0/1994 - SSL 3.0/1996)
  * Handshake s. Bild
* **IPSEC** (Internet Protocol Security) 
  * arbeitet direkt auf der Vermittlungsschicht (Internet Layer, entspricht OSI Layer 3
  * soll verschlüsselungsbasierte Sicherheit auf Netzwerkebene bereitstellen
  * soll das Mitlesen beim Umschreiben / Routing verhindern
  * führt bei NAT u.U. zu Problem (Änderung quell-IP)


* **Signatur/Unterschrift**: Nachweise der Autorenschaft
  * Allgemeines Eigenschaft: *öffentliche Schlüssel* können entschlüsseln, was *Private* Schlüssel **ver**schlüsselt haben. (Reziproke Anwendung)
  * Anwendung:
    * Aus Text wird ein Hash erzeugt.
    * Autor verschlüsselt des Hash mit seinem privaten Schlüssel.
    * reicht beides zusammen weiter.
    * Empfänger des Textes entschlüsselt Text mit öffentlichem Schlüssel des Autors: Nachweis erbracht.
  * Voraussetzung: verlässliche Schlüsselweitergabe **Schlüsselparties**






* → [https://de.wikipedia.org/wiki/Verschlüsselung](https://de.wikipedia.org/wiki/Verschlüsselung)
* → [BSI/Datenverschlüsselung](https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datenverschluesselung/datenverschluesselung_node.html)
* → [https://studyflix.de/informatik/asymmetrische-verschlusselung-1609](https://studyflix.de/informatik/asymmetrische-verschlusselung-1609)
* → [https://www.conductor.com/de/academy/glossar/ssl-verschluesselung/](https://www.conductor.com/de/academy/glossar/ssl-verschluesselung/)
* → [https://www.cloudflare.com/de-de/learning/ssl/transport-layer-security-tls/](https://www.cloudflare.com/de-de/learning/ssl/transport-layer-security-tls/)
* → [https://www.cloudflare.com/de-de/learning/ssl/transport-layer-security-tls/](https://www.cloudflare.com/de-de/learning/ssl/transport-layer-security-tls/)
* → [https://www.ibm.com/docs/de/ibm-mq/9.2?topic=tls-overview-ssltls-handshake](https://www.ibm.com/docs/de/ibm-mq/9.2?topic=tls-overview-ssltls-handshake)
* [https://de.wikipedia.org/wiki/Transport_Layer_Security](https://de.wikipedia.org/wiki/Transport_Layer_Security)
* → [https://www.ecos.de/blog/asymmetrische-verschluesselung-einfach-erklaert](https://www.ecos.de/blog/asymmetrische-verschluesselung-einfach-erklaert)
* → [https://www.heise.de/tipps-tricks/SSH-Tunnel-nutzen-so-geht-s-4320041.html](https://www.heise.de/tipps-tricks/SSH-Tunnel-nutzen-so-geht-s-4320041.html)
* → [https://de.wikipedia.org/wiki/Virtual_Private_Network](https://de.wikipedia.org/wiki/Virtual_Private_Network)
* → [https://aws.amazon.com/de/what-is/vpn/](https://aws.amazon.com/de/what-is/vpn/)
* → [https://de.wikipedia.org/wiki/IPsec](https://de.wikipedia.org/wiki/IPsec)
* → [https://www.security-insider.de/was-ist-ipsec-a-781354/](https://www.security-insider.de/was-ist-ipsec-a-781354/)