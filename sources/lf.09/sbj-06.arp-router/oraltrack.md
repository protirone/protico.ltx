<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

---

Zur Erinnerung  **[→ ZP:Sheet:2]**

* **`(I)`** Ein **HUB** spannt eine **Kollisionsdomäne** auf, ein **Switch** eine **Broadcastdomäne** (Subnetz):
  * Mehrere Switches hintereinander vergrößern diese Broadcastdomäne. 
  * Die Distribution von MAC_Adressen findet nur innerhalb einer Broadcast-Domäne statt.
* **`(II)`** In einem vollverswitchten Netz hat die Kollisionsdomäne nur einen Rechner
  * (→ es gibt keine Kollisionen.)

---

<!-- uebung::start -->

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:06:ARP-Router:00**</span>

* [ ] (optional): Führen Sie einen Schreibtischtest für ein vollverswitshtes Netz mit 3 Rechnern und einem Switch durch. (Abstrahieren Sie dabei von der inneren Switch-Struktur.)
* [ ] Repräsentieren Sie diese Broadcastdomäne A jetzt durch Personen im Raum.
* [ ] Kreieren Sie eine eigenständige Broadcastdomäne B gleicher innerer Struktur und repräsentieren Sie die ebenfalls durch Personen.
* [ ] Erfinden Sie eine Methode, um eine Nachricht von Broadcastdomäne A nach B zu schicken. Wo nötig, erfinden Sie die fehlende Hardware. Beschreiben Sie deren Eigenschaften und Verhalten dann aber genau.
* [ ] Demonstrieren Sie Ihre Lösung in Form eines 'Schreibtischtestes' (Weiterreichen von vorbereiteten Nachrichten im Stehen)


<!-- uebung::end -->

Lösung: s.u.

---

### 1.B) Definitionen B **[→ ZP:Sheet:3]**

* **`(I)`** Ein **HUB** spannt eine **Kollisionsdomäne** auf, ein **Switch** eine **Broadcastdomäne** (Subnetz)
* **`(II)`** In einem vollverswitchten Netz hat die Kollisionsdomäne nur einen Rechner
  * (→ es gibt keine Kollisionen.)
* **`(III)`** **Hopping** ist der Prozess des Weiterleitens einer Nachricht über die Grenzen einer Broadcastdomäne hinweg.
* **`(IV)`** Zwei Netze werden einen Router zu einem größeren Netz verbunden.
* **`(V)`** Der Router hat ein Netzwerkinterface in jedes Teilnetz hinein.
* **`(VI)`** Er ist in jedem Netz ein Kommunikationsteilnehmer wie jeder andere Rechner auch.
* **`(VII)`** Für ein Netz fungiert er als Gateway: 
   * Nachrichten die nicht für die Broadcastdomäne bestimmt sind, übergeben die Rechner an den Router: 
   * Der leitet sie - wie eine eigene Nachricht - mit seinem zweiten Bein weiter.

Damit gilt auch in der Broadcastdomäne das, was auch bisher für voll-verswitchten Netze gilt:

* _Innerhalb der Broadcastdomäne werden Nachrichten per MAC-Adresse versendet_.
* _Um die zu erfragen, wird der ARP-Request genutzt_.

Hinzu kommt Folgendes:

1. Der Router hat (mindestens) zwei Netzwerkinterfaces und ist in beide Netze eingebunden.
2. Er kommuniziert in jedem einzelnen voll-verswitchten Netz wie jeder andere Rechner auch:
   1. Bekommt er aus dem Netz eine Nachricht mit einer MAC-Destination-Adresse, die nicht seine ist, ignoriert er die Nachricht.
   2. Bekommt er aus dem Netz eine Nachricht mit der Broadcast-**MAC**-Adresse und seiner IP-Adresse als IP-Destination-Adresse, wertet er das als einen an sich gerichteten ARP-Request und antwortet darauf, damit der Anfragende seine MAC-Adresse bekommt.
   3. Bekommt er aus dem Netz eine Nachricht mit seiner MAC-Adresse und einer IP-Adresse überprüft er, wohin die erhaltene IP-Adresse gehört:
      1. Gehört `D-IP-Address` in das Netz, aus dem die Nachricht gekommen ist, ignoriert er das Paket.
      2. Gehört `D-IP-Adress` in das zweite Netz, in das er eingebunden ist, schreibt er das Paket um und gibt es umgeschrieben an sein 2. Interface weiter:
         1. Als `S-MAC-Address` setzt er seine eigene MAC-Adresse ein, die ursprüngliche `S-IP-Address` bleibt erhalten.
         2. Dann startet er einen ARP-Request in seinem zweiten Netz, über den er nach der MAC-Adresse des Rechners mit der `D-IP-Address`
         3. Die erhaltene Ziel-MAC-Adresse setzt er in das umzuschreibende Paket ein und schickt die Nachricht an den Zielrechner.
      3. Gehört `D-IP-Address` in ganz anderes Netz, leitet er die mit denselben Mitteln an`das Gateway seines zweiten Netzes weiter (möge sich doch der Router drum kümmern ;-)):
    4. Bekommt er aus seinem zweiten Netz eine Nachricht an die ursprüngliche erhalten gebliebene Source-IP, ändert er die MAC-Adressen um und schreibt sie in sein erstes Netz zurück. - (ggfls. führt er einen neuen ARP-Request in das Ursprungsnetz hinein)


Der Algorithmus geht darüber hinaus so:

* Zuerst prüft derjenige Rechner (Sender/Source), der eine Nachricht an einen anderen Rechner (Empfänger/Destination) übertragen will, ob die Ziel-IP-Adresse des gewünschten Kommunikationspartners (Empfänger) zur eigenen Broadcast-Domain gehört.
* Gehört der Empfänger zur eigenen Broadcast-Domain, übermittelt der Sender die Nachricht mit Layer-II-Mitteln an den Empfänger:
  * ARP-Request `[ S-IP-Address S-MAc-Address D-IP-Address ff::ff]` per Switch an alle (außer sich)
  * ARP-Reply geht per Switch an ihn zurück.
* Wenn nicht, 
  * ARP-Request `[ S-IP-Address S-MAC-Address GATEWAY-IP-Adress ff::ff]` 
  * ARP-Reply per Switch vom Router an ihn zurück.
  * Nachricht `[ S-IP-Address S-MAC-Address D-IP-Address GATEWAY-MAC-Address]`


Der Witz bei der Sache ist dies:

* Sobald der Rechner, der eine Nachricht an einen Rechner außerhalb seiner Broadcastdomain senden will, die MAC-Adresse seines Routers
(Gateways) kennt, adressiert er die Nachricht auf Layer-III mit der ’fremden’ IP-Adresse und auf Layer-II mit der MAC-Adresse des
Routers.
* Für den Router ist die Diskrepanz zwischen MAC-Adresse (sein eigne) und IP-Adresse (fremd) der Auftrag zur Weitervermittlung.
* Sobald der Router die MAC-Adresse des Zielrechners (mitLayer-II/ARP-Mitteln) in der anderen Broadcastdomain ermittelt hat, schreibt er die zu sendende Nachricht um: Er ersetzt das Layer-II-Paket durch eines, das seine zweite/andere MAC-Adresse als Source-Adresse und die MAC-Adresse des Zielrechners als Destination-Adresse im Ethernetframe enthält.
  
### 2.) Aufgaben**

---

(optional wenn Aufgabe 00 nicht durchgeführt)
<!-- uebung::start -->

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:06:ARP-Router:01**</span>

Führen Sie einen Schreibtischtest passend zu [→  ZP:Sheet:2] durch, also für eine Kommunikation in einem ein Netz mit zwei getrennten Broadcast-Domänen mit einer Nachricht von RA1 zu RB3:

* [ ] Zwei Schülerinnen mögen sich als Dokumentarinnen bereitstellen: Sie dürfen sich frei bewegen, jede Akteurin befragen und sollen so ein Aktivitätsprotokoll erstellen.
* [ ] 1 Schülerin möge als Router agieren, 2 Schülerinnen als Switch-A bzw. Switch-B.
* [ ] 3 Schülerinnen mögen als Rechner RA1, RA2, RA3 agieren, drei andere als RB1, RB2, RB3.
* [ ] Die Routerschülerin stellt sich in die Mitte des Aktionsraums.
* [ ] Die 'A-'Schülerinnen stellen sich auf der einen Seite der Routerschülerin auf, die B-Schülerinnen auf die andere: Switch-A und Switch-B jeweils nah an die Routerschülerin.
* [ ] Schülerin RA1 und die Routerschülerin erhalten je einen kleinen Stapel an Zettel + Stift, Switch-A und Switch-B je einen größeren + Stift.
* [ ] Alle Rechnerschülerinnen geben sich je IP-Adresse (RAxI) und eine MAC-Adresse (RAxM), schreiben sich die auf ein Kreppband und kleben sich das auf die Brust.
* [ ] Die Routerschülerin braucht zwei IP-Adressen und zwei MAC-Adressen, je ein Paar für ein Interface.
* [ ] Die Lehrerin sagt, RA1 möge RB3 eine Nachricht schicken, und zwar unter Beachtung aller ARP- und Hoppingregeln in einem vollverswitchten Netz: Nachrichten hätten dabei immer die Struktur: `SIP SMAC DIP DMAC Payload` und würden von den richtigen Komponenten vervielfacht bzw. umgeschrieben.
* [ ] Während des Ablaufs fragt die Lehrerin jeweils (steuernd) nach, warum wer welche Nachricht bekäme und beachtet bzw. nicht beachtet.
* [ ] Die Dokumentarinnen halten fest, wer wann was tut.

<!-- uebung::end -->

---

__Lösung: Simulation mit Schreibtischtest: *[→ ZP:Sheet:4]*__

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:06:ARP-Router:02**</span>

* [ ] Erstellen Sie ein Aktivitätsdiagramm für ein Netz mit zwei getrennten Broadcast-Domänen mit einer Nachricht von RA1 zu RB3
* [ ] Erstellen Sie das dazu passende Sequenzdiagramm für ein Netz mit zwei getrennten Broadcast-Domänen mit einer Nachricht von RA1 zu RB3

<!-- uebung::end -->

---

Lösungen:

* Aktivitätsdiagramm: **[→ ZP:Sheet:5]** (Die Idee, das Merken der Absender-IP-Adresse gesondert als parallele Akzivität zu repräsentieren, verdanken wir Waldemar, GSLDK/11iv24 
* Sequenzdiagramm: **[→ ZP:Sheet:6]**, 
* verdichtetes Sequenzdiagramm: **[→ ZP:Sheet:7]**

