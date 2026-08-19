<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

**[→ ZP:Sheet:1]**

---

### 1. Übungen

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:01-Fadennetzwerk:01**</span>


* [ ] Bauen Sie ein Netzwerk. Als 'Hardware' dürfen Sie dabei nur die Bindfäden, die Schere und sich selbst verwenden.
* [ ] In Ihrem Netzwerk soll schließlich eine einstellige Zahl von einem Endgerät zu einem anderen übertragen werden. Welche Zahl es sein wird und von wo nach wo sie übertragen wird, lege ich adhoc fest, wenn Sie Ihr Ergebnis präsentieren.
* [ ] Wenn Ihr Netzwerk läuft, dürfen Sie als Mensch nicht sprechen, nicht lächeln, nicht blinzeln und auch nicht anders mit Ihren Mitschülerinnen kommunizieren. 
* [ ] Es gibt eine maximale Übertragungslänge von ca. 2 Metern pro Faden.
* [ ] Die Zahl muss über mindestens ZWEI Fäden maximaler Länge übertragen werden.

Hinweis: Wenn Sie in Versuchung kommen, beim 'Ablaufen lassen' des Netzwerkes aus dem 'Zusehen' Zusatzinformationen abzuleiten und zu verwenden, lassen Sie Ihr Netzwerk mit geschlossenen Augen etc. ablaufen.

*[Gruppenarbeit: ca. 1 STD, dann Präsentation]*

<!-- uebung::end -->

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:01-Fadennetzwerk:02**</span>


* [ ] Beschreiben Sie jeder in einem Markdowntext - von nicht mehr als 800 Zeichen - die Idee und Kernelemente Ihres Fadennetzwerkes
* [ ] Laden Sie Ihre Datei unter dem Dateinamen `lf09-ueb-YYYYMMDD-IHRNAME.md` in den Übungsordner hoch. *YYYYMMDD* möge nach [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601) als Datum aufgelöst werden. Für Ihren Namen (im Prinzip reicht der Vorname) nutzen Sie bitte Kleinbuchstaben.

<!-- uebung::end -->

---

### 2. Auswertung

Sie haben folgende Lösung(en) gefunden: *[mündliche Beschreibung]*

Das mappt gut auf die Lösungen, die früheren Klassen auch gefunden haben. 

**[→ ZP:Sheet:2]**

**[→ ZP:Sheet:3]**

Gemeinsam war Ihren Lösungen, dass Sie folgendes 'erfunden' haben:

* ein physikalisches Verfahren zum Senden und Empfangen von Zahlen (Layer I)
* eine physikalische Komponente zum erneuerten Weitersenden von Nachrichten
* ein physikalisches Anzeichen für das *Symbolende* (Layer I)
* eine Methode zur Abbildung von Nachrichten auf das physikalische Verfahren (Layer II)
* eine Methode zur Adressierung der beteiligten *Komponenten* (**Netzwerkadresse**)
* eine wiederkehrende einheitliche Nachrichtenstruktur. (**Protokoll**)
* eine Aufteilung einer Nachricht in Adressat und Inhalt. (**Packaging mit Header und Payload**)
  
  Einige Gruppen Gruppe haben dabei

* eine **Ringtopologie** verwendet und manchmal sogar fast einen kompletten *Token-Ring* umgesetzt
* eine physikalische Komponente zum erneuerten Weitersenden von Nachrichten 'erfunden' (*Repeater*)


Andere Gruppen haben

* eine **Sterntopologie** verwendet,
* dabei eine physikalische Komponente zum adressgenauen Weiterreichen von Nachrichten 'erfunden' (*Switch*)
* und gelegentlich sogar den Wechsel in ein anderes Netzsegment eingebaut


Wir werden im LF09-Unterricht diesen Aspekten genauer nachgehen.

**[→ ZP:Sheet:4]**

Am Ende werden Sie verstanden haben,

* warum und wie - trotz konzeptioneller Trennung - in der Netzwerkkommunikation alles miteinander zusammenhängt *und*
* warum es sinnvoll ist, sich die Übertragung eine Nachricht im Internet in einem ganz anderen Sinne als eine *Welle* vorzustellen:
  1. Bei Sender wird auf oberster Ebene eine Nachricht formuliert und über mehrere Schichten immer wieder und weiter eingepackt.
  2. Bei manchen Empfängern werden nur die zwei-drei letzten Pakete entpackt, um das Versenden weiter vorantreiben zu können.
  3. Und beim endgültigen Empfänger werden alle Pakete von außen nach innen entpackt und an die je zuständige Instanz auf der nächst höheren Ebene weitergereicht, bis der intendierte Adressat seine Nachricht bekommen hat.



---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:01-Fadennetzwerk:03**</span>

* [ ] Suchen Sie in drawio die Palette mit den Netzwerksymbolen.
* [ ] Dokumentieren Sie Ihr Fadennetzwerk mit diesen Symbolen.


*[Benutzen Sie dazu die Diagramm-Anleitung `crx.diagramming`. Wie Sie das Tool `drawio` installieren, erläutert die Anleitung `crx.tooling`]*

<!-- uebung::end -->

---


---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09:01-Fadennetzwerk:04**</span>

* [ ] Teilen Sie nun Ihre Gruppen in zwei Untergruppen auf.
* [ ] Die eine Gruppe möge in einem UML-Sequenzdiagramm dokumentieren, wer bei der Demonstration wem welche Nachrichten übersandt hat.
* [ ] Die andere Gruppe möge in einem UML-Aktivitätsdiagramm dokumentieren, wer bei der Demonstration was getan hat.

*[Benutzen Sie dazu die Diagramm-Anleitung `crx.diagramming`. Wie Sie das Tool `drawio` installieren, erläutert die Anleitung `crx.tooling`]*

<!-- uebung::end -->

---
