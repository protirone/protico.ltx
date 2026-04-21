<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### A) Ausgangspunkt *AP[1|2]-Abarbeitungsprozess* (von cx.apx-strategy\*) **[→ ZP:Sheet:2]**

### B) *FMEA* 

* steht für *"Failure Mode and Effects Analysis"* = *"Fehlermöglichkeits- und Einflussanalyse"*,
* ist ein Verfahren, um auf Fehler / Abweichungen entsprechend ihrer relativen Wichtigkeit reagieren zu können,
* will mögliche Produktfehlern eine zu Kennzahl zuordnen, anhand derer die Dringlichkeit der Bearbeitung/Reaktion im Vergleich zu anderen Fehlern erkennbar wird, 
* berechnet die relative Wertigkeit aus
  * der Bedeutung des Fehlers für den Kunden (Auswirkung),
  * der Wahrscheinlichkeit des Fehlereintritts (Auftretenswahrscheinlichkeit),
  * der Wahrscheinlichkeit der Entdeckung des Fehlers (Entdeckungswahrscheinlichkeit),
 * → [https://de.wikipedia.org/wiki/FMEA](https://de.wikipedia.org/wiki/FMEA)
  
#### B.1) 

*FMEA*-Prozess  **[→ ZP:Sheet:3]**

* 1) Bilde interdisziplinäres Team (Experten) aus Konstruktion, Entwicklung, Versuch, Fertigungsplanung, Fertigungsausführung, Qualitätsmanagement.
* 2) Beschreibe das System/den Prozess hinsichtlich Struktur und Funktion der seiner Elemente.
* 3) Liste für jedes Subsystem potenzielle Fehler auf hinsichtlich Fehlerort, Fehlerart, Fehlerfolge und Fehlerursache auf - auf der Basis von
  * Fakten (Fehlerbeobachtungen, Erfahrungsberichte, ...),
  * Antizipationen (assoziativen Erkennungsmethoden, Kreativitätstechniken).
* 4) Bewerte den einzelnen Fehler hinsichtlich dreier Dimensionen (mit je auf einem Wert zwischen 1 und 10), und zwar hinsichtlich
  * der **B**edeutung (= **S**everity) der *Fehlerfolge* / Auswirkungen,
  * der **A**uftretenswahrscheinlichkeit (= **O**ccurrence ) der Fehlerursache,
  * der **E**ntdeckungswahrscheinlichkeit (=  **D**etection) des Fehlers oder seiner Ursache,.
* 5) Bilde für jeden Fehler die Risiko-Prioritätszahl **RPZ** als das Produkt `B*A*E`

#### B.2) 

*FMEA*-Bewertung

Grundidee:

* **B:** je gewichtiger die Auswirkungen eines Fehlers, desto wichtiger ist es, sich um die Beseitigung seiner Ursache zu kümmern
* **A:** je häufiger ein Fehler auftritt, desto wichtiger ist es, sich um die Beseitigung seiner Ursache zu kümmern
* **E:** je leichter / je schwere ein Fehler zu entdecken, desto mehr / weniger Ressourcen sollte man in die Bereinigungen stecken

`=>`

* Im Idealfall basieren *B*, *A* und *E*-Befunde auf empirisch gewonnenen Daten.
* Praktisch liegen oft Expertenschätzungen zugrunde.
* Gerade *E* ist eine Ermessenssache: 
  * vom pekuniären Standpunkt: wenn der Fehler schwer entdeckt wird, brauchen wir auch nix zu tun.
  * vom moralischen Standpunkt (Image): Gerade wenn er schwer entdeckt wird, kümmern wir uns.

 `=>`


 Jede Bewertung der Dimensionen muss eine auf den Firmenethos ausgerichtete Systematik zu Grunde gelegt werden.

#### B.3) 

*FMEA*-Subtypen

* *Design-FMEA* (D:FMEA): soll systematisch Produktfehler während der Konstruktionsphase entdecken
* ...
* *Prozess-FMEA* (P-FMEA): soll mögliche Schwachstellen im Herstellungsprozess zum Ziele der Qualitätssteigerung ermitteln 
  * hängt bzgl. Produktgüte mit D-FMEA zusammen,
  * als Mängel gelten dann z.B.
    * zu langsame Produktion
    * zu teure Produktion
    * zu fehlerbehafteter Output.
* *Präventive FMEA*: soll proaktiv / möglichst früh Fehler identifizieren und schon während der Designphase beseitigen. [ANTIZIPATION]
* *Korrektive FMEA*: soll in späteren Phasen des Productlifecycles Fehler entdecken. [REAKTION]

Hinweis zur Unterscheidung:

Der *AP2-Abarbeitungsprozess* soll den Schülerinnen in der AP2 helfen. Mit der ersten Klasse haben wir in folgenden Schritten designt

1. Ich habe einen Prozess vorgeschlagen.
2. Die Klasse hatte gemurrt, zu ineffizient, zu störend.
3. Dann hatten wir gemeinsam den Prozess verschlankt.

 `=>` 
 
 * Diese Arbeit wäre - formal durchgeführt- als *Design-FMEA* / *Präventive FMEA* / *Prozess-FMEA* bezeichnet.
 * Würde man das reale Prüfungsvorgehen untersuchen, läge eine *Korrektive FMEA* vor.

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:sbj02:proc-analysis:01**</span>

* [ ] Formulieren Sie auf der Basis Ihrer Erfahrung 3 Fehler, die man während des AP2-Abarbeitungsprozesses machen kann.
* [ ] Führen Sie dafür eine FMEA-Analyse durch.
* [ ] Ranken Sie die Fehler entsprechend ihrer **RPZ**.

<!-- uebung::end -->

---

### C) **Fehlerbaumanalyse**  **[→ ZP:Sheet:4]**

* heißt auch *Fault Tree Analysis (FTA)*  
* ist ein Verfahren zur Zuverlässigkeitsanalyse von technischen Anlagen und Systemen unter Ausnutzung der boolschen Algebra
* ist DIN normiert (DIN EN 61025)
* arbeitet 'halb assoziativ'
* → [https://de.wikipedia.org/wiki/Fehlerbaumanalyse](https://de.wikipedia.org/wiki/Fehlerbaumanalyse)

#### C.1)
Vorgehen

* 1. Zeichne die Struktur des zu begutachtenden Systems als Baum von Subsystemen
* 2. Erstelle zu jedem Subsystem einen Fehlerbaum = liste alle Zustände auf, die zu einem Ausfall des Systems führen können.
* 3. Sammle zu jedem Zustand die Zustände, die den oberen Zustand auslösen.
  * Erlaube dabei Und-Cluster (wenn zustand a + b + c eintritt, dann zustand x) oder Oder-Cluster (wenn zustand a | b | c eintritt, dann zustand x)
  * Trage an jedem Zustandsblatt die Wahrscheinlichkeit ein.  
  * Berechne dadurch die Ausfallwahrscheinlichkeit der Komponente.
  
#### C.2)
Bewertung

* Vorteile: Verspricht Genauigkeit
* Nachteile:
  * aufwendiges Verfahren
  * mathematisch schwer/aufwendig auszuführen bei komplexen Systemen


### D) **ABC**-Analyse:  **[→ ZP:Sheet:5]**

* ist ein betriebswirtschaftliches Analyseverfahren zum Klassifizieren von Ereignisse in wichtige, mittlere und unwichtige Fehler, Befunde, Ereignisse
* setzt eine Liste von Wertepaaren (Typ -> Wert) voraus
* → [https://de.wikipedia.org/wiki/ABC-Analyse](https://de.wikipedia.org/wiki/ABC-Analyse)
* 
#### D.1)
Vorgehen

* 1. Ermittle alle Fehler
* 2. Ermittle für jeden Fehler den absoluten Wert des Schadens
* 3. Ermittle für jeden Fehler seine Häufigkeit
* 4. Ermittle für jeden Fehler den relativen Schadenswert (Häufigkeit*abs.Schadenswert)
* 5. Addiere alle relativen Schadenswerte zum Gesamtschaden
* 6. Ermittle für jeden relativen Schadenswert den Anteil am Gesamtschaden
* 7. Erzeuge eine Liste von Wertpaaren 'Fehler:Anteil am Gesamtschaden'
* 8. Sortiere die Liste absteigend
* 9. Erzeuge drei Cluster (Klassen):
  * **Klasse A Fehler**: die ersten Fehler, die zusammen 80\% des Gesamtschadens ausmachen.
  * **Klasse B Fehler**: die nächsten Fehler, die zusammen 15\% des Gesamtschadens ausmachen.
  * **Klasse C Fehler:** die letzten Fehler, die zusammen 5\% des Gesamtschadens ausmachen.
* 10. Kümmere Dich als zuerst um die Klasse A Fehler

#### D.2)
Beispiel **[→ ZP:Sheet:6]**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:sbj02:proc-analysis:02**</span>

Gesetzt, Sie wollten ermitteln, worum Sie am ehesten kümmern sollten, wenn Sie die Nutzung Ihres nächsten Füllers signifikant verbessern wollten. 

* [ ] Gehen Sie von folgenden Erfahrungen aus:
  * Ein neuer Füller kostet 300,-- €. 
  * Bei jedem 10. neuen Gerät ist im Kolben ein Haarriss.
  * Eine neue Feder kostet 30,-- €. 
  * Bei jedem 2. neuen Gerät ist die Feder per Werk verbogen.
  * Sie brauchen über die Lebenszeit des Füllers 50 Tintenfässer.
  * Jedes Tintenfass kostet 10€.
  * Bei jeder 5. Lieferung eines Fasses ist die Tinte vertrocknet.
  * Sie füllen den Füller über seine Lebenszeit 1000 mal.
  * Bei jeder 5. Füllung läuft die Tinte über. Die Beseitigung der Flecken kostet Sie 1 Euro.

* [ ] Ermitteln Sie anhand einer **ABC**-Analyse, ob Sie sich - auf der Basis der bisherigen Erfahrungen - am ehesten eine neue Füllerlieferantin und/oder eine neue Tintenlieferantin und/oder eine neue Befüllungsmethode organisieren sollten.

<!-- uebung::end -->

Lösung: **[→ ZP:Sheet:7]**

*Prozessschritte pro Füllerleben*:

| Schritt | Fehler | Häufigkeit | Fehlerwert | av. Schaden | Anteil Einzelschaden an Gesamtschaden in % |
|---|---|---|---|---|---|
| Füllerkauf | Haarriss im Kolben | 1 * 0.1 | 300€ | 30 € | 0.09
| Füllerkauf | Feder verbogen | 1 * 0.5 | 30€ | 15 € | 0.04
| Tintenkauf | Tinte vertrocknet | 50 * 0.2 | 10 € | 100 € | 0.29
| Befüllung | Kolbenüberlauf | 1000 * 0.2 | 1€ | 200€ | 0.58
| | | | sum(Schaden): | 345 | 


*sortierte Fehlertyp -> Schadenswert-Liste ( pro Füllerleben)*

| Fehler | %(SUM(Auswirkung)) | Klasse | ABC-Befund
|---|---|---|---|
| Kolbenüberlauf |0.58 | A | wichtig |
| Tinte trocken | 0.29 | A | wichtig |
| Feder verbogen | 0.09 | B | unwichtig |
| Haarriss | 0.04 | C | unwichtig |

*Ergebnis*: Sie sollten die Füllerbefüllung neu trainieren und sich eine neue Füllerlieferantin suchen, wenn Sie Ihren Füllerprozess um 80% verbessern wollen.

---

### E) Nutzwert-Analyse: **[→ ZP:Sheet:8]**

* ist eine systematische Methode zur Bewertung von Alternativen, 
* erlaubt es, qualitative und/oder quantitative Kriterien einzubeziehen.
* dient einer geordnete Entscheidungsfindung
* →  [https://www.munich-business-school.de/l/bwl-lexikon/nutzwertanalyse](https://www.munich-business-school.de/l/bwl-lexikon/nutzwertanalyse)

#### E.1)
Vorgehen

1. Liste die Alternativen auf
2. Liste die Bewertungskriterien auf
3. Gewichte die Bewertungskriterien nach relativer Wichtigkeit zu anderen Kriterien
4. Ermittle für jede Alternative für jedes Kriterium den zuständigen Wert
5. Multipliziere für jede Alternative den Kriteriumswert mit dem Gewicht
6. Multipliziere alles zum Gesamtnutzen der Alternative

#### E.2)
Bewertung

* *Vorteil*: mathematisch
* *Nachteil*: 
  * Kriterienwahl und -bewertung beeinflusst Ergebnis
  * für normierte Systematik umfangreiche mathematische Absicherung nötig

#### E.3)
Beispiel:

Es gelte:

  * Funktionsgleiche Prozessschritte Ps1, Ps2, Ps3 sollen verglichen werden.
  * Kriterien: Kosten pro Durchlauf (in €), Zeit pro Durchlauf (in H)
  * Ranking: Schnelligkeit vor Kosten, 0.7 für Zeit, 0.3 für Kosten


| PS | €/DL | H/DL | gw(€) | gw(H) | Gesamtnutzen
|---|---|---|---|---|---|
|     |     |   | €/DL\*0.3 | H/DL\*0.7 | €/DL\*0.3 \* H/DL\*0.7
| Ps1 | 100 | 5 | 30 | 3.5 | 105
| Ps2 | 200 | 2 | 60 | 1.4 | 84
| Ps3 | 50 | 6 | 15 | 4.2 | 63


Ergebnis: Gewonnen hat Ps1

### F) Entscheidungsmatrix **[→ ZP:Sheet:9]**

* liefert fundierte Entscheidungen
* berücksichtigt dabei einzelne Kriterien 
* → [https://studyflix.de/wirtschaft/entscheidungsmatrix-7025](https://studyflix.de/wirtschaft/entscheidungsmatrix-7025)

#### F.1)
Vorgehen

* 1. Konzipiere Punktevergabe
* 2. Konzipiere Kriteriumsgewichtung
* 3. Vergib pro Kriterium die geplanten Punkte
* 4. Berechne die gewichtete Punktzahl pro Kriterium
* 5. Addiere die gewichteten Punkte  

#### F.2)
Beispiel

Es gelte:

  * Funktionsgleiche Prozessschritte Ps1, Ps2, Ps3 sollen verglichen werden.
  * Kriterien: Kosten pro Durchlauf (in €), Zeit pro Durchlauf (in H)
  * Ranking: Schnelligkeit vor Kosten, 0.7 für Zeit, 0.3 für Kosten

| Kriterium | Gewicht | PS1 | PS2 | PS3 |
|---|---|---|---|---|
| Kosten | 0.3 | 100*0.3 = 30 | 200*0.3=60 | 50*0.3= 15 |
| Geschwindigkeit | 0.7 | 5*0.7=3.5 | 2*0.7= 1.4 | 6*0.7= 4.2 | 
| Gesamt | 1 | 33.5 | 61,4 | 19.2 |

Hier gewinnt Ps2



### G) **Ursache-Wirkungsdiagramm** **[→ ZP:Sheet:3]**

* ist assoziatives Verfahren, um 'nichts' aus dem Blick zu verlieren,
* trennt Identifikation und Aggregation von der Analyse,
* stellt Ursache und Wirkung grafische dar, die zu einem Ergebnis führen oder dieses maßgeblich beeinflussen, 
* expliziert faktische Abhängigkeiten,
* hat mehrere Namen
  *  **Ishikawa-Diagramm** bekannteste Form (stammt aus Qualitätsmanagement),
  *  **Fischgrät-Diagramm** = Fischgräten-Diagramm = *Fishbone Diagram*,
* dient zur systematischen und vollständigen Ermittlung von Problemursachen,
* analysiert und strukturiert die Wirkung von Prozessschritten (Welche Phasen bewirken was),
* → [https://de.wikipedia.org/wiki/Ursache-Wirkungs-Diagramm](https://de.wikipedia.org/wiki/Ursache-Wirkungs-Diagramm)

#### G.1)
Vorgehen

* (I) **Formaler Start**
  * 1) Trage rechts einen Fehlerbefund oder ein (noch nicht erreichtes Ziel) ein
  * 2) Zeichne eine Linie von links nach rechts bis zum (Fehler)befund. Bedeutung: Alles, was die Linie berührt, beeinflusst / verursacht den Fehler / Zielerreichung
  * 3) Trage von links nach rechts - ober- und unterhalb der Einflusslinie - die Einflusskategorien (als 'Quasilanes') ein - z.B.
    * die vier Ms: Material, Maschine, Methode, Mensch
    * die acht Ms: 4Ms + Management, Mitwelt (Milieu), Messung (Measurement) und Geld (Money)
    * andere Verursacher: Prozesse etc.
  * 4) Verbinde jede Haupteinflussgröße mit einem schräg zum Hauptpfeil verlaufenden Pfeil.
* (II) Die eigentliche, assoziative* **Sammlungsarbeit**
  * 5) Trage zu jeder Einflusskategorie die entsprechenden Ursachen/Wirkungen ein.
  * 6) Schließe die Identifikation mit einem Vollständigkeitscheck ab
  * 7) Lass Experten die identifizierten Ursachen nach dem Grad ihrer Wirkung / ihres Einflusses im Hinblick auf den Fehler klassifizieren

#### G.2)
Bewertung

* Vorteile:
  * liefert gute Diskussionsgrundlage für Gruppenarbeit,
  * ermöglicht vielseitige Betrachtungsweise,
  * braucht wenig Aufwand bei der Durchführung,
  * ist leicht erlern- und anwendbar.
* Nachteile:
  * ist unübersichtlich und umfangreich bei komplexen Problemen,
  * stellt keine vernetzten Ursache-Wirkungs-Zusammenhänge dar,
  * erfasst keine Wechselwirkungen und zeitliche Abhängigkeiten.

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:sbj02:proc-analysis:02**</span>

* [ ] Führen Sie für den wichtigsten der 3 ermittelten Fehler eine Ursache-Wirkungsanalyse durch. Nutzen Sie dabei die vier Ms.

<!-- uebung::end -->

---


### H) Prozess-Analyse-Kritierien:


* **Wirtschaftlichkeit**:- pekuniäreWirkung(Prozess) > pekuniärerAufwand(Prozess),
* **Rentabilität**: wenn val(Output)> val(Input), je größer, je produktiver,
* **Produktivität**: val(Output)/val(Input), je größer, je produktiver
* **Amortisation**: Anschaffungskosten + Betriebskosten*Zeit - Gewinn*Zeit = 0
* **Break Even**: Zeitpunkt der Amortisation
* **Pareto Prinzip**: Kümmere dich zuerst um das, was 80% deiner Probleme verursacht.
* → [https://www.munich-business-school.de/l/bwl-lexikon/finanzwissen/amortisation](https://www.munich-business-school.de/l/bwl-lexikon/finanzwissen/amortisation)

Anmerkungen: können in F+G eingearbeitet werden

### I) Managementmethoden zur Prozessverbesserung

#### I.1) 
Kaizen

* stammt aus Japan
* ist Ursprungsform vom 
  * **KVP** (= kontinuierlicher Verbesserungsprozess) = 
  * **CIP** (Continual / Continuous Improvement Process)
* verwendet die Leitfragen
  * "Wie soll es sein?" [*PLAN*]
  * "Was tun wir aktuell wie?" [*DO*]
  * "Was wurde erreicht?" [*CHECK*]
  * "Was ist noch zu tun?" [*ACT*]

* Verfahren: 
  * werde in ganz kleinen Schritten besser,
  * wenn ein Schritt nicht klappt, verkleinere ihn (beim nächsten Mal),
  * hat allgemein gerade einen Hype mit der 1%-Methode

* → [https://de.wikipedia.org/wiki/Kontinuierlicher_Verbesserungsprozess](https://de.wikipedia.org/wiki/Kontinuierlicher_Verbesserungsprozess) 
* → [https://de.wikipedia.org/wiki/Kaizen](https://de.wikipedia.org/wiki/Kaizen)

#### I.2)
Lean Management:

> "Durch gezielte Analyse der Abläufe sucht das Lean Management nach Verbesserungsmöglichkeiten in der Wertschöpfungskette, um mit minimalem Aufwand bestmögliche Ergebnisse zu erzielen. Der kontinuierliche Verbesserungsprozess stellt dabei Kund:innen in den Mittelpunkt, da ihre Bedürfnisse und Erwartungen definieren, was als wertschöpfend oder verschwenderisch gilt." 


* optimiert Prozesse durch die Vermeidung von „Verschwendung“ ,
* setzt Ressourcen effizienter ein,
* fokussiert sich auf die Maximierungen der Zufriedenheit von Kund:innen,
* nutzt 5 Prinzipien (fordert Menschen/Prozesse auf, sie anzuwenden):
  * **Wert aus Kundensicht definieren**,
  * **Wertstrom analysieren**: "Der Wertstrom beschreibt den gesamten Prozess, den ein Produkt oder eine Dienstleistung durchläuft – von der Entstehung bis zur Lieferung an Kund:innen. Jeder Schritt im Prozess wird daraufhin untersucht, ob er zur Wertschöpfung beiträgt."
  * **Wertfluss sicherstellen**: "Prozesse sollten so organisiert sein, dass ein kontinuierlicher Arbeitsfluss ohne Unterbrechungen entsteht. Dies minimiert Verzögerungen und Wartezeiten im Produktionsprozess."
  * **Pull-Prinzip etablieren**: Produkte nicht auf Vorrat produziert, sondern auf Anfragen von Kund:innen
  * **Perfektion anstreben**: sich kontinuierlich verbessern, "die eigene Arbeit stets kritisch zu hinterfragen und nach neuen Wegen zu suchen, um Prozesse effizienter und zielgruppenorientierter zu gestalten."
* → [https://ifm-business.de/aktuelles/business-news/was-ist-lean-management-definition-methoden.html](https://ifm-business.de/aktuelles/business-news/was-ist-lean-management-definition-methoden.html)


#### I.3)
TQM

* steht für Total Quality Management 
* meint die

> "Optimierung der Qualität von Produkten und Dienstleistungen eines Unternehmens in allen Funktionsbereichen und auf allen Ebenen durch Mitwirkung aller Mitarbeiter." 

* "strebt die Erhöhung der Kundenzufriedenheit an."
* grenzt sich gegen das "Qualitätsmanagement", das nur *Planung, Steuerung und Überwachung der Qualität eines Prozesses bzw. Prozessergebnisses* meint

* → [https://wirtschaftslexikon.gabler.de/definition/total-quality-management-tqm-47755](https://wirtschaftslexikon.gabler.de/definition/total-quality-management-tqm-47755)



### J) **DMAIC** Prozess

* steht für  Define – Measure – Analyse – Improve – Control = Definieren – Messen – Analysieren – Verbessern – Steuern 
* bildet den Kernprozess des Qualitätsmanagement-Ansatzes Six Sigma 
* will Prozesse so gestalten, dass diese stabil ein vorgegebenes 6 Sigma-Leistungsniveau halten
* nutzt die Phasen
  * *Definition* = definiere Sollzustand (= definiere Fehler)
  * *Datenerhebung* = finde Methoden und Instrumente zur Sammlung von Daten über den IST-Zustand der Leistungsmerkmale
  * *Analyse* = finde Ursachen der Abweichung von den definierten Leistungszielen
  * *Verbesserung* = finde Lösungen für die in der Analyse-Phase identifizierten Probleme 
  * *Steuern* =  verankere gefundenen Verbesserungen im Alltagsbetrieb 
* vgl. [https://de.wikipedia.org/wiki/DMAIC](https://de.wikipedia.org/wiki/DMAIC) 

#### J.1)
DPMO

* ist zentrale Kenngröße für die Qualität eines Prozesses
* nutzt die Definition aus DMAIC, was als Fehler gilt
* wird so berechnet
  * ermittle die Anzahl der gemessenen Fehler = D im Bezugszeitraum / Umfang / ... (was als Fehler gilt, wird definiert)
  * ermittle die Anzahl der produzierten / verglichenen Einheiten (units) = N im Bezugszeitraum
  * ermittle die Anzahl der *möglichen* Fehler pro produzierter / verglichener Einheit = O(opportunities)
  * berechne den DPMO-Wert nach der Formel **`DPMO=(D/(N\*O))*1,000,000`**

#### J.2) 
SixSigma 

* gilt als Kennzahl der Prozessgüte
* sagt eigentlich nur etwas über die Güte eines Prozesses im Vergleich zu vorherigen Prozessversionen aus,
* wird oft als generelle Aussage über die Qualität des eigenen Tuns im Vergleich zu anderen genutzt
* wendet DMAIC an, 
* ist selbst ein statisch basiertes Verfahren zur Annäherung an einen idealen Zustand.
  
> "Der Name „Six Sigma“ resultiert aus der Forderung, dass die nächstgelegene Toleranzgrenze mindestens sechs Standardabweichungen (6Gr.Sigma, englisch ausgesprochen „Six Sigma“) vom Mittelwert entfernt liegen soll".

SixSigma- Konzeption:

* Realiter schwankt die Qualität von Prozessdurchläufen über längere Zeiträume, sie haben also einen DPMO-Wert größer 0
  * Im besten Fall wäre jedes Prozessergebnis in jedem Prozessdurchlauf in jeder Hinsicht richtig (= 0 DPMO)
  * Im schlimmsten Fall wäre jedes Prozessergebnis in jedem Prozessdurchlauf in jeder Hinsicht defekt (= 1.000.000 DPMO)
* Deswegen wird der Überschreitungsanteil für die Grenze 6sigma mit 3,4 DPMO festgelegt.
* Verfahren: Wende DMAIC an und verkleinere den DPMO-Wert Deines Prozesses, sodass Du Dir gemäß folgenden Tabelle einen besseren 6Sigma-Wert zuordnen kannst


| Sigma Level	| DPMO	| fehlerhaft | fehlerfrei |
|---|---|---|---|
| 1	| 691.462	| 68 %	| 32 % |
| 2	| 308.538	| 31 %	| 69 % |
| 3	| 66.807	| 6,7 %	| 93,3 %|	
| 4	| 6.210	| 0,62 %	| 99,38 %	|
| 5	| 233	| 0,023 %	| 99,977 %	|
| 6	| 3,4	| 0,00034 %	| 99,99966 |
| 7	| 0,019	| 0,0000019 %	| 99,9999981 |


* Vorteile: Verspricht mathematische Genauigkeit
* Nachteile: hängt von der eigenen Fehlerdefinition ab

#### J.3) 
Beispiel

> 1. Ich hatte meinen Blutdruck zwischen 05/2024 u. 03/2025 163 mal gemessen: `N=163`* 
> 2. Dabei hatte ich manchmal das Datum im falschen Format eingetragen, manchmal Systole und Diastole vertauscht, manchmal beides: `O=2`
> 3. Bei 10 Datensätzen war nur das Datum falsch, bei 24 war das Datum falsch und Systole und Diastole vertauscht: `D=10+24*2=58`
> 4. Formel: `DPMO=(D/(N*O))*1.000.000=(58/163*2)*1000000=0,17791411*1000000=177914,11`
> 5. Demnach gehörte mein Blutdruckmessungsprozess zur 6Sigma-Klasse von 2,x

#### J.4)
Zusammenspiel von **Normalverteilung** und **SixSigma**:

* Die Idee ist, dass oft durchgeführte Prozesse zwar einen (idealen) Erwartungswert haben, im konkreten aber davon abweichen.
* Kleinere Abweichungen tauchen häufiger auf, größere seltener.
* Empirisch zeigt sich, dass die Abweichungen entsprechend der Gaus'schen Glockenkurve auftreten: 
  * die x-Achse beschreibt erreichbare Werte
  * die y-Achse die Häufigkeit * Varianz / bzw. Standardabweichung 
  * Der Erwartungswert bildet den Peak.
  * Hinweis: 
    * Erhöhung des Erwartungswertes verschiebt die Kurve nach rechts
    * Erhöhung der Standardabweichung streckt sie. 
  
* SixSigma dreht das System um: 
  * Der Erwartungswert ist das, was nicht erwartet/gewünscht ist, nämlich das alle Produkte (bezogen auf die definierten Fehler) falsch sind.
  * Das ist 'messbar': wenn es 1.000.000 dpmo gibt: `DPMO=(D/(N*O))*1000000` ergibt 100000 bei => D/(N*O)=1.
  * Der Unerwartungswert ist das, was nerwartet/gewünscht ist, nämlich das alle Produkte (bezogen auf die definierten Fehler) richtig sind.
  * Die Abweichung von ganz falsch wird zum Grad der Richtigkeit (Glockenkurve).
  * Die Glockenkurve wird nach re und li in 6 Schritte geteilt.
  * DPMO 0 ist praktisch nicht erreichbar.
  * Der beste DPMO Wert wird bei 3,4 festgelegt.


