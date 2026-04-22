<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


RAID *[→ ZP:Sheet:2]*

steht für: 

* **'Redundant Array of Independet Disks'** (heute)
* *Redundant Array of Inexpensive Disks* (früher)

Grund für Umbenennung:

* heute sind Festplatten kein (wesentlicher) Kostenfaktor mehr, 
* wohl aber die Lese- und Schreiboperationen (die den Datendurchsatz verlängern)

Zweck: Ein Verbund von Festplatten soll die *Mean Time Between Failures (MTBF)* erhöhen

#### 
RAID 0

* meint **Striping** 
* zwei Platten werden 
  * "in zusammenhängende Blöcke gleicher Größe aufgeteilt"
  * "im Reißverschlussverfahren zu einer [virtuellen] großen Festplatte angeordnet".
* dient der Lese Beschleunigung ohne Redundanz
  * Erhöht nur Datendurchsatz
  * Fällt eine Platte aus, ist das Gesamtsystem zerstört
  * Eigentlich keine Redundanz, also kein Raid

Bei n Platten der Größe S

* `Nutzdaten = n*S`

####
RAID 1

* meint **Mirroring** (*Spiegelung*)
* Zwei (oder mehr) Platten werden 
  * "in zusammenhängende Blöcke gleicher Größe aufgeteilt"
  * jeweils 'gleichzeitig' mit denselben Daten beschrieben.
* bietet volle Redundanz
  * fällt eine Platte aus, kann die andere einspringen bzw. die Ersatzplatte restaurieren.
  * Erhöht nur Lesedurchsatz
* *Subtypen*:
  * _**Mirroring** im engeren Sinne_
    * beide Platten nutzen denselben Controller. (1 Schreibbefehl, zweimal sequentiell ausgeführt)
    * Nachteil (I): Controller ist Single Point of Failure
    * Nachteil (II): Schreibprozess verlangsamt
  * _**Duplexing**: jede Platte ein eigener Controller
    * Vorteil (I): fällt Controller aus, bedient der zweite den Schreib und Leseprozess auf der anderen Platten
    * Vorteil (II): Schreiboperation schneller

Bei n Platten der Größe S

* `Nutzdaten = S`


####
RAID 4

* meint **Block-Level Striping mit gesonderter Paritätsinformation**
* n Festplatten 
  * bilden einen Verbund
  * aus den nächste n-1 Datenpaketen wird per XOR ein n. Datenpaket generiert
  * die n-1 Datenpakete werden im Reißverschlussverfahren (Striping) in dieselben Sektoren/Blöcke der Platten 1 - n-1 geschrieben,
  * die Paritätsinformation wird in denselben Sektor/Block der Platte n geschrieben
  
Paritätsinformationen / -daten

* eines Paritätsblocks werden "durch XOR-Verknüpfung der Daten aller Datenblöcke der Gruppe" berechnet,
* machen Daten restaurierbar: Paritätszahl xor erhaltener Block = Inhalt von zerstörtem Block


* Vorteil:
  * 1 Platte ist im Betrieb austauschbar
  * alle Nutzdatenplatten stehen für Leseoperationen zur Verfügung
* Nachteil: 
  * Je mehr Kapizität der *virtuellen* Platte, je teurer der reale Aufwand
  * Paritätsplatte ist der Single Point of Failure
  
Bei n Platten der Größe S

* `Nutzdaten = (n-1)*S`
* `Paritätsdaten = S`


####
RAID 5

* meint **Block-Level Striping mit verteilter Paritätsinformation**
* n Festplatten 
  * bilden einen Verbund
  * aus den nächste n-1 Datenpaketen wird per XOR ein n. Datenpaket generiert
  * die n Datenpakete werden Nutzungsdaten im Reißverschlussverfahren (Striping) geschrieben, 
  
Paritätsinformationen / -daten

* eines Paritätsblocks werden "durch XOR-Verknüpfung der Daten aller Datenblöcke der Gruppe" berechnet,
* machen Daten restaurierbar: Paritätszahl xor erhaltener Block = Inhalt von zerstörtem Block *[→ ZP:Sheet:3]*

* Vorteil:
  * 1 Platte ist im Betrieb austauschbar
  * alle Platten stehen für Leseoperationen zur Verfügung
* Nachteil: Je mehr Kapizität der *virtuellen* Platte, je teurer der reale Aufwand
  
Bei n Platten der Größe S

* `Nutzdaten = (n-1)*S`
* `Paritätsdaten = S`

####
RAID 6

* meint **Block-Level Striping mit verteilter doppelten Paritätsinformation**
* n Festplatten 
  * bilden einen Verbund
  * aus den nächste n-2 Datenpaketen wird per XOR ein n-1. und - verschoben - ein n.1 Datenpaket generiert
  * die n Datenpakete werden Nutzungsdaten im Reißverschlussverfahren (Striping) geschrieben, 
  
Paritätsinformationen / -daten

* Vorteil:
  * 2 Platten sind im Betrieb austauschbar
  * alle Platten stehen für Leseoperationen zur Verfügung
* Nachteil: Je mehr Kapizität der *virtuellen* Platte, je teurer der reale Aufwand
  
Bei n Platten der Größe S

* `Nutzdaten = (n-2)*S`
* `Paritätsdaten = 2S`



#### 
Sonderformen

* _**RAID 4**_ :- wie *Raid 5*, nur dass alle Paritätsinfos auf dieselbe Platte geschrieben werden. (Single Point of Failure)
* _**RAID 10**_ :- Vereinigung von RAID-0 (Striping) und RAID-1 (Mirroring) 
  * Daten werden über 2 je gespiegelte Paare gestriped. Verlangt also mindestens 4 Platten.
  

(vgl [https://de.wikipedia.org/wiki/RAID](https://de.wikipedia.org/wiki/RAID))
 *[→ ZP:Sheet:2]*

