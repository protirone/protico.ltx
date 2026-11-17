<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 0.) Vorbereitung 

--- 

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11d:01:Server-Installation:01**</span>

* [ ] Installieren Sie die für Sie passende freeplan-Version:
  * Windows:
    * `Freeplane-Setup-X.Y.Z.exe` von [https://github.com/freeplane/freeplane/releases](https://github.com/freeplane/freeplane/releases) downloaden & starten
    * GPL License akzeptierten = Installer laufen lassen
  * Linux(Ubuntu/Debian)
    * `freeplane_xxx~upstream-1_all.deb` Datei herunterladen
    * `sudo apt-get install ./freeplane_xxx~upstream-1_all.deb` (Menueintrag wird unter Kategorie *Office* angelegt)

* [ ] Laden Sie die Mindmap `sbj-01.server-setup-tasks.mm` von [https://github.com/protirone/protirone.lessons/tree/main/fachinformatik/lf.11d](https://github.com/protirone/protirone.lessons/tree/main/fachinformatik/lf.11d) herunter
<!-- uebung::start -->

### 1.) Konzeption einer Installation

**[→ ZP:Sheet:2]**

Grob gesagt, müssen Sie sich beim Aufsetzen eines Servers mindestens um folgende Fragen kümmern

1. Welches Betriebssystem soll auf meinem Server installiert werden?
2. Wie soll(en) die Festplatte(n) partitioniert werden?
3. Was sind Dateizugriffsregeln in ihrem Betriebssystem?
4. Welches Installationsmedium / -verfahren wollen Sie verwenden?
5. Welche Eigenschaften soll Ihr System für alle Nutzer mitbringen / vorgeben?
6. Welche Services (= Serverprogramme) wollen Sie installieren?
7. Welche Backupstrategie wollen Sie für Ihr System verwenden?
8. In welches Netzwerk wollen Sie Ihren Server einbinden.

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11d:01:Server-Installation:02**</span>

Konkretisieren Sie diese Wissensbereiche:

* [ ] Diskutieren Sie gruppenweise, was zu diesen Bereichen im Detail gehört
* [ ] Vergleichen Sie Ihre Sichtweise mit der Ordnung in der heruntergeladenen Mindmap `sbj-01.server-setup-tasks.mm`,
* [ ] Reichern Sie sie um die Aspekte an, die I.E. in der Mindmap fehlen.

<!-- uebung::end -->

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11d:01:Server-Installation:03**</span>


Beantworten Sie bitte dann die gesammelten Fragen und Aspekte, die es bei der Installation eines Servers zu berücksichtigen gilt, und entschieden Sie sich wo nötig für eine jetzt und hier umsetzbare Variante: 

* [ ] Diskutieren Sie die Fragen Ihrer Leit-Mindmap zur Installation eines Servers gruppenweise und/oder mit Ihrer Lehrerin.
* [ ] Markieren Sie die, für deren Beantwortung Sie noch Informationen von Ihrer Lehrerin benötigen. 
* [ ] Entscheiden Sie bei denen, die sie beantworten können, welche Varianten Sie wählen.
* [ ] Dokumentieren Sie Ihre Entscheidungen / Antworten in/mit entsprechenden Subknoten.
* [ ] Entscheiden Sie sich für eine Minimalinstallation, die Sie anschließend sukzessive erweitern können.

Gehen Sie bitte davon aus, dass Sie die Fragen / Entscheidungen nicht beantworten / treffen können, ohne die anderen Antworten / Entscheidungen im Blick zu haben. Gehen Sie Ihren Fragenkatalog mehrfach durch und stimmen Sie dabei die einen Antworten mit den anderen ab.

<!-- uebung::end -->

Lösung:


---

### 2.) Exkurse Hintergrundinformationen


#### 2.A)
Festplattendesign, Partitionen und Nutzungszuordnung

* __Unter W11__:
  * Zwischen Festplatten und Partitionen nach außen nicht unterschieden.
  * Jede Partition hat einen 'Laufwerksbuchstaben'
* __Unter LNX__:
  * Jede dem System zur Verfügung stehende Device erscheint unter /dev und hat seine eigene Geräte-Datei (→ `ls /dev`)
  * Festplatten vom Typ *ssd* (solid-state-drive) oder *hdd* (mit rotierenden Scheiben und mechanischen Köpfen)
    * beginnen mit dem Kürzel _hd_ bzw _sd_ 
    * gefolgt von einem Buchstaben als Kenner für die konkrete Platte (sda = erste SSD, sdb = zweite SSD, ...) 
  * Festplatten vom Typ *nvme-ssd* (Non-Volatile Memory Express Solid-State-Drive)
    * beginnen mit dem Kürzel _nvme_
    * gefolgt von einer Nummer als Kenner für die konkrete Platte (nvme0, nvme1, ...)
    * können durch weitere Namespaces eingeteilt werden, die aber mit 1 beginnen markiert durch ein `n` markiert sind (nvme0n1, nvme0n2, ...)
  * Festplatten können zudem in einzelnen Partitionen eingeteilt werden.
    * Partitionen auf Festplatten vom Typ *ssd* werden von 0 bis n durchnummeriert (sda1, sda2, sda3)
    * Partitionen auf Festplatten vom Typ *nvme-ssd* werden von 1 bis n durchnummeriert, haben aber ein p (partition) vor der Nummer ( nvme0n1p1, nvme0n1p1)
  * Partitionen werden unter LNX (u.a.) vom Tool `gparted` erzeugt, modifiziert oder gelöscht.
  * Jede Festplatte hat ihre eigene Partition-Table.
  * Jeder Partition hat ein eigenes Datei-System. Die Typen können sich unterscheiden.
    * *W11*:
      * `NTFS` = Standard Dateisystem (für MacOs oft nur lesbar)
      * `FAT32` = FAT32 stammt aus den 1990er-Jahren, sehr kompatibel / verbreitet, keine Dateien größer als 4GB
      * `exFAT` = Nachfolger für USB-Sticks, erlaubt Dateien größer als 4GB, anfällig für Laufzeitfehler
      * `ReFS` = Resilient File System, erschaffen für Server
    * *LNX*:
      * `ext4` = *Fourth Extended Filesystem*, Nachfolger von *ext2* und *ext3*, 
      * `btrfs` = *B-tree File System*
      * `xfs` = optimiert für große Dateien
      * `tmpfs` = Dateisystem, das komplett im Arbeitsspeicher (RAM) gehalten wird.
      * `swap` = Dateisystem zum Auslagern von Memory.
      * ...
      * (Linux kann auch Windowsdateisysteme lesen und schreiben.)
  * Partitionen werden in das über geordnete Dateisystem gemounted. Ohne Mountpoint keinen Zugriff.
  * Tools:
    * `ls /dev` liste die vorhandenen Devices auf.
    * `sudo fdisk -l` listet alle Partitionen und Eigenschaften auf.
    * `lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT` bzw. `lsblk` listet alle Partitionen mit Größe, FS.-Typ und Mountpoint auf.
    * `sudo gparted` erlaubt die Modifikation von Festplatten

Das Festplattendesign ist 

* die Einteilung der Festplatte in Partitionen,
* deren Zuordnung zu Mountpoints entsprechend der intendierten Zwecke,
* die Wahl des je dazu passenden Dateisystems.
  
Unter LNX gibt es Strategien für eine geeignetes `Festplattendesign`:

* 1. Alles auf eine Partition. Hohe Flexibilität aber:
  * kein paralleles Update des Betriebssystems,
  * keine Wiederverwendung von Daten nach Betriebssystemwechsel.
* 2. Für jede Datenhaltung eine eigene Partition:
  * *Bootpartition* (enthält bootbaren Kernel)
  * *Swappartition* (erlaubt Kernel die Programmauslagerung auf die Festplatte)
  * *Root-Partition* enthält das Betriebssystem, wird unter / gemountet
  * *Home-Partition* enthält die Home-Verzeichnisse alle (nicht Root-) User
  * *Var* oder *Vol*-Partition zur Datenaufnahme, gemountet unter /var oder /vol 
  * *Root-Partition II* nicht gemountet, nimmt das neue Betriebssystem auf, kann anstelle der eigentlichen Root-Partition eingehängt werden.


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11d:01:Server-Installation:04**</span>

* [ ] Loggen Sie sich auf dem Übungsserver ein und ermitteln Sie dessen Festplattendesign.
* [ ] Stecken Sie dann den USB-Stick ein.
* [ ] Rufen Sie `gparted` auf und ermitteln Sie dessen Festplattendesign.
* [ ] Löschen Sie dann die Partitionen des USB-Sticks und teilen Sie ihn in zwei Partitionen auf, 
  * [ ] die erste mit dem Dateisystem *FAT32*, *NTFS* oder *exFAT*,
  * [ ] die zweite mit dem Dateisystem *ext3*.
* [ ] Speichern Sie dann auf jeder Partition eine Datei mit Ihrem Namen als Content. Der Dateiname möge auf der ersten Partition `w11-datei.txt`, auf der zweiten `lnx-datei.txt`.
* [ ] Unmounten Sie den Stick geordnet und stecken Sie in eine Windowsrechner.
* [ ] Welchen Unterschied stellen Sie fest?
  
<!-- uebung::end -->


Lösung:

Unter Windows wird nur die erste Partition gefunden und angezeigt. Grund: Windows kennt das Dateisystem *ext3* nicht.

---

#### 2.B)
Was sind Tastaturlayouts

* Das Tastaturlayout stammt immer noch aus den Zeiten der Schreibmaschine: weniger oft verhaken.
* Layoutname sind die ersten 6 Tasten von links: 
* Im Deutschen ist das Z häufiger als das Y: deshalb: QUWERTZ statt QUERTY

#### 2.C)
Was ist eine ISO-Datei

**Ausgangspunkt**

* Festplatten werden partitioniert. (z.B. grparted, etc. ...)
* Partitionen werden formatiert (mit Filesystem versehen: gparted, etc...)
* Formatierte Paritionen werden gemounted (als Subordner/-dateien vom Mountpoint)
* Gemountete, formatierte Partitionen werden mit Dateien beschrieben.
* Sticks sind sozusagen 'kleinere' Festplatten.

**ISO-Dateien**

sind

* Abbilder aller Dateien und Pfade einer CD / DVD
* liefern das Filesystem intern mit
* lassen sich als virtuelle Laufwerke mounten.


**Konsequenzen**

1. Eine ISO Datei auf einen Stick zu kopieren (auf ein existierendes) Filesystem, macht den Inhalt nicht zugänglich.
2. ISO-Dateien müssen als Partition auf den Stick geschrieben werden. (Disk Creator, Brasero, etc.)
3. Sticks mit ISO-Dateien zu formatieren, um den ganzen Platz zurückzugewinnen, reicht nicht aus, weil Partion für ISO-File erhalten bleibt. Sie müssen repartioniert werden (gpartet)


#### 2.D)
Distribution / Operatingsystem

#### 2.E)
Kommandos zur Anreicherung / Modifikation der Installation

#### 2.F)
Dateisysteme

#### 2.G)
Installationsmedium (Bootstick etc.)

#### 2.H)
Betriebssprache, Zeitzone und Zeitserver

#### 2.I)
Zu installierende Services (= Server)

#### 2.J)
User und Dateirechte

#### 2.K)
Datenablage

#### 2.L)
Datensicherungskonzept

#### 2.m)
Manuelle Paketinstallation versus graphischer Paketmanager

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11d:01:Server-Installation:04**</span>




* [ ] Erstellen Sie einen bootbaren USB-Stick mit der ISO-Datei zur Installation Ihres Betriebssystem [UBUNTU 26.04.01]
* [ ] Booten Sie vom Stick (mit Hilfe des Bios des zu installierende Servers) [esc / F12]
* [ ] Übernehmen Sie Ihre Entscheidungen
* [ ] Wählen Sie die minimale Installation
* [ ] Booten Sie neu
* [ ] Updaten Sie die Pakete auf den je letzten Stand (apt-get update && apt-get upgrade)


<!-- uebung::end -->

Lösung:


Bewertung für BGE-Stunden:

| Step | Target | DoD | Points |
|---|---|---|---|
| 1. | Installation des Servers + Paketupdate | Booten | 1 |
| 2. | Installation Openssh | Synaptic Pakete zeigen + systemctl status ssh | 1 |
| 3. | Installation Nginx (Port 80 /var/www) | Nginx mit ps ermitteln + /var/www anzeigen | 1 |
| 4. | Installation Apache2 (Port 10080 /vol/www) | Apache2 mit ps ermitteln + /var/www anzeigen | 1 |
| 5. | Apache Module installieren | mod_php + mod_python status + rewrite | 1 |
| 6. | Alle ssh Verbindung | mod_php + mod_python status + rewrite | 1 |
 
---
