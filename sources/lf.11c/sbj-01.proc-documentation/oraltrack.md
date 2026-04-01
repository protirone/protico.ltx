<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 1. Zusammenhänge:  **[→ ZP:Sheet:2]**

**(I) Prozesse** im Allgemeinen

* sind Schrittfolgen, die als solche einen initialen Zustand (von Daten, Werkstücken, Materialien, ...) in einen anderen Zustand überführen,
* sind als Schrittfolgen beschreibbar und (anhand dieser Beschreibung) wiederholbar,
* transformieren - als Einheit gesehen - ebenso den Input in einen veränderten Output,
* wie ihre Schritte den jeweiligen Input in einen veränderten Output umwandeln. (Rekursive Definition)
* haben eine innere Ordnung der Prozessschritte, die sich in einem Kontrollfluss manifestiert.

Ein **(II) Geschäftsprozess**

* ist "ein wiederkehrender, unternehmensbezogener Arbeitsablauf"
* "soll ein unternehmensbezogenes Ziel erreichen",
* "lässt sich als Abfolge von Einzelschritten darstellen",
* "findet wiederholt [...] statt",
* wird (oft) arbeitsteilig ausgeführt
* "startet mit Input (Informationen und/oder Ressourcen) und
* "endet mit Output (Informationen und/oder [...] Produkten)"

Eine **(III) Prozessanalyse**

kann einen Prozess im Hinblick auf

* die Ebene(n) untersuchen, auf der/denen dieser wirkt: *strategische Ebene*, *fachlich-konzeptionelle Ebene*, *operative Ebene*
* die Phasen betrachten, in denen er implementiert wird: *Konzeption*, *Prozessdesign*, *Prozessimplementierung*, *Prozess-Controlling*, *kontinuierliche Verbesserung*
* Sicht(weis)en durchleuchten, aus denen man ihn betrachtet: *organisatorische Einbettung*, *Geschäftsobjekt*, *Prozess als zu beurteilendes Objekt*, *Ressourcen*

Es gilt: **Keine verschiedenen Blickwinkel ohne _Prozessdokumentation_. Keine Prozessdokumentation ohne _Prozessanalyse_.**


[vgl. → Kersken: Daten- und Prozessanalyse für Fachinformatiker\*innen, 2021, S.424ff]


### 2. Einfaches Beispiel: **[→ ZP:Sheet:3]**

---

<!-- uebung::start -->

**Prozessbeschreibung:**

    cat MIT.dirty.txt |\
      sed 's/  */ /g' |\
      tr -d '\r' |\
      tr '\n' '$' |\
      sed 's/\$\$/\n\n/g' |\
      tr -d '$' |\
      tr 'a' 'a' |\
      sed 's/  */ /g' \
    >> x.txt

**Prozessschritte**:

* *cat* :- liest Daten aus Datei und gibt sie unverändert nach stdout aus.
* *sed* :- (= Stream-Editor) = liest Daten von *stdin*, ersetzt das zwischen `/ /` durch das danach `/ /` und gibt das Ergebnis nach *stdout* aus.
* *tr* :- liest Daten von *stdin*, ersetzt alle Zeichen 'A' durch 'B' bzw. löscht 'A' und schreibt nach *stdout*
* `>` :- liest von einem IO-Channel (hier *stdout*) und lenkt die Daten in eine Datei um.


<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:01:Prozessdokumentation:01**</span>

* [ ] Dokumentieren Sie obigen Prozess als *Aktivitätsdiagramm*. 

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:4]**

---

<!-- uebung::start -->

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:01:Prozessdokumentation:02**</span>


* [ ] Dokumentieren Sie cat|sed|tr-Prozess als *Flussdiagramm*. 
* [ ] Finden Sie Möglichkeiten, den Prozess zu verschlanken. 

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:5]** / Prozessschrittdoubletten sind ausgegraut

---



### 3. Komplexeres Beispiel: **[→ ZP:Sheet:6]**

---

<!-- uebung::start -->

**Prozessbeschreibung:** 

* Ich bin bei uns für's Einkaufen zuständig.
* Meine Frau schreibt den Einkaufszettel, schrittweise, wann immer ihr etwas einfällt, manchmal bis zur letzten Minute.
* Irgendwann, bevor ich losfahre, checke ich, was uns an Wasch- und Hygieneartikel fehlt, und notiere das auf unserem Einkaufszettel.
* Zum Einkaufen fahre ich freitags oder samstags.
* Muss ich auch zur Reinigung, fahre ich allein nach *Herborn*, gebe dort die Kleidung ab, nehme fertige wieder mit und kaufe danach auch dort im Rewe und ggf. auch im DM ein.
* Meistens fahre ich aber nur zum Rewe nach *Niederweidbach*.
* Steht Drogeriebedarf auf dem Zettel und muss ich nicht zur Reinigung, kaufe ich dagegen in *Erda* ein, beim Rossmannm und im Edeka gegenüber.
* Manchmal kommt meine Frau mit nach *Niederweidbach* oder *Erda*.
* Bin ich allein in *Erda*, kaufe ich erst bei Rossmann und dann bei Edeka ein - oder umgekehrt.
* Sind wir zu zweit in *Erda*, beginnt meine Frau bei Rossmann, ich bei Edeka. Danach beenden wir den Edeka-Einkauf gemeinsam.
* Auf dem Rückweg lutsche ich Lakritze - wenn ich allein bin.

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:01:Prozessdokumentation:03**</span>


* [ ] Dokumentieren Sie den Einkaufsprozess als *BPMN-Diagramm*. 
* [ ] Finden Sie Möglichkeiten, den Prozess zu verschlanken. 

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:7]**

---

<!-- uebung::start -->

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:01:Prozessdokumentation:04**</span>


* [ ] Dokumentieren Sie den Einkaufsprozess als *eEPK-Diagramm*. 

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:8]**

---

### 4. Ausgefallenes Beispiel: **[→ ZP:Sheet:9]**

---

<!-- uebung::start -->

**Prozessbeschreibung:**

In der Zentrale der Sportfirma 'Switchi' arbeiten vier Schwestern, **Anna**, **Berta**, **Charlotte** und **Dora** Bridgerton. Jede Schwester betreut eine Abteilung: Anna das **Angeln**, Berta das **Baden**, Charlotte das **Curling** und Dora **Darts**. Ihre Aufgabe ist es, den Informationsaustausch zwischen den Abteilungen zu ermöglichen:

1. Bekommt eine der Schwestern *einen Brief* aus der Abteilung, für die sie zuständig ist, *analysiert* sie den oder *die Adressaten*. 
2. Ist der Brief an alle anderen Abteilungen adressiert, *läuft sie zum Kopierer*, *kopiert ihn zweimal* und *übergibt jeder* ihrer Schwestern *einen Brief*. 
3. Ist der Brief dagegen an eine bestimmte Abteilung adressiert, *übergibt sie den Brief direkt* an die Schwester, die für diese Abteilung zuständig ist. 
4. *Reicht eine Schwester einen Brief an eine andere* Schwester, *schickt diese den an ihre Abteilung*, für die sie zuständig ist.

Der Chef lässt die Abteilungen allerdings oft und überraschend in andere Zimmer ziehen. Weil das - wie er sagt - den Teamgeist fördere. Deshalb kennen die Abteilungen erst einmal nur ihre eigene, aktuell gerade gültige Adresse. Und sie müssen, wollen sie eine andere Abteilung kontaktieren, darum zuerst deren aktuelle Adresse ermitteln. Dazu schicken zuerst an alle Abteilungen die Frage nach der Adresse der Abteilung, mit der sie reden wollen. 

Abteilungen, die mit der Frage nicht gemeint sind, ignorieren diese. Die tatsächlich gemeinte Abteilung schickt der anfragenden Abteilung -- sie hat deren Adresse im Absender gefunden -- jedoch als Antwort ihre eigene Adresse. Danach können die beiden Abteilungen für eine kleine Weile direkt Nachrichten austauschen.

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:01:Prozessdokumentation:05**</span>

* [ ] Wählen Sie aus den Prozessdokumentationstechniken *UML-Aktivitätsdiagramm*, *UML-Sequenzdiagramm*, *Flussdiagramm*, *BPMN-Diagramm* und *EPK-Diagramm* zunächst die aus, die Ihnen am leichtesten fällt. Und dann die, die für Sie am schwierigsten ist.
* [ ] Dokumentieren Sie den *Switchi*-Prozess in beiden Diagrammformen. 
* [ ] Gehen Sie dabei strikt nach dem Arbeitsschema vor, dass Ihnen das Diagramm-Tonspurdokument angeboten hat.

<!-- uebung::end -->

Lösung für BPMN-Diagramm: **[→ ZP:Sheet:10]**

Lösung für EPK-Diagramm: **[→ ZP:Sheet:11]**

---