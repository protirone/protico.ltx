<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 1.) Konzeption

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

<!-- uebung::start -->

####
1.A Zu beachtende Bereiche (Knowldege Areas)

**[→ ZP:Sheet:2]**

Grob gesagt, müssen Sie sich mindestens um folgende Fragen kümmern

1. Welches Betriebssystem soll auf meinem Server installiert werden?
2. Wie soll(en) die Festplatte(n) partioniert werden?
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
* [ ] Erfassen Sie Ihre Fragen einer Markdowndatei.
* [ ] Vergleichen Sie Ihre Einträge mit denen in der Mindmap `sbj-01.server-setup-tasks.mm` unter [https://github.com/protirone/protirone.lessons/tree/main/fachinformatik/lf.11d](https://github.com/protirone/protirone.lessons/tree/main/fachinformatik/lf.11d).
* [ ] Laden Sie sich diese Mindmap herunter und reichen Sie sie um die Aspekte aus Ihrer Markdowndatei an, die in der Mindmap fehlen.

<!-- uebung::end -->

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11d:01:Server-Installation:03**</span>


Beantworten Sie bitte dann die gesammelten Fragen und Aspekte, die es bei der Installation eines Servers zu berücksichtigen gilt, und entschieden Sie sich wo nötige für eine jetzt und hier umsetzbare Variante: 

* [ ] Diskutieren Sie die Fragen Ihrer Leit-Mindmap zur Installation eines Servers gruppenweise und/oder mit Ihrer Lehrerin.
* [ ] Markieren Sie die, für deren Beantwortung Sie noch Informationen von Ihrer Lehrerin benötigen. 
* [ ] Entscheiden Sie bei denen, die sie beantworten können, welche Varianten Sie wählen.
* [ ] Dokumentieren Sie Ihre Entscheidungen / Antworten in/mit entsprechenden Subknoten.
* [ ] Entscheiden Sie sich für eine Minimalinstallation, die Sie anschließend sukzessive erweitern können.

Gehen Sie bitte davon aus, dass Sie die Fragen / Entscheidungen nicht beantworten / treffen können, ohne die anderen Antworten / Entscheidungen im Blick zu haben. Gehen Sie Ihren Fragenkatalog mehrfach durch und stimmen Sie dabei die einen Antworten mit den anderen ab.

<!-- uebung::end -->

---


### 2.) Umsetzung


### 3.) Hintergrundinformationen


#### 3.A)
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
* deren Zuordnung zu Mountpoints entsprechend der intendierten Zwecke
* die Wahl des je dazu passenden Dateisystems
  
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

Unter Windows wird nur die erste Partition gefunden und angezeigt. Grund: Windows kennt
das Dateisystem *ext3* nicht.

---


#### 3.B)
Distribution / Operatingsystem

#### 3.C)
Kommandos zur Anreicherung / Modifikation der Installation

#### 3.D)
Ablage der Konfigurationsdateien

#### 3.D)
Dateisysteme

#### 3.E)
Installationsmedium (Bootstick etc.)

#### 3.F)
Tastaturlayout, Betriebssprache, Zeitzone und Zeitserver

#### 3.G)
Zu installierende Services (= Server)

#### 3.H)
User und Dateirechte

#### 3.I)
Datenablage

#### 3.J)
Datensicherungskonzept

#### 3.K)
Sonstiges



