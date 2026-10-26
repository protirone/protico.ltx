<!-- LTeX:Language=de-DE -->

### Prozessbewertung u. Optimierung 


#### A)
Analysemethoden

* **FMEA**: "Failure Mode and Effects Analysis" = "Fehlermöglichkeits- und Einflussanalyse"
  * meint eine analytische Methode, um qualitative Aussagen über mögliche Produktfehler zu gewinnen
  * **Ziel**: mögliche Produktfehler nach ihrer Bedeutung für den Kunden, ihrer Auftretenswahrscheinlichkeit und ihrer Entdeckungswahrscheinlichkeit mit jeweils einer zu Kennzahl bewerten, anhand derer die Dringlichkeit der Bearbeitung/Reaktion im Vergleich zu anderen Fehlern erkennbar wird 
  * **Vorgehen**:
    * Bilde interdisziplinäres Team (Experten) aus Konstruktion, Entwicklung, Versuch, Fertigungsplanung, Fertigungsausführung, Qualitätsmanagement
    * Beschreibe das System/den Prozess hinsichtlich Struktur und Funktion der Strukurelemente
    * Liste für jedes Subsystem potenzielle Fehler auf hinsichtlich Fehlerort, Fehlerart bestimmt, die Fehlerfolge, Fehlerursache (dafür können auch  assoziativen Erkennungsmethoden / Kreativitätstechniken verwendet werden)
    * Bewerte jeden Fehler hinsichtlich
      * **B**edeutung (= **S**everity) der *Fehlerfolge* 
      * **A**uftretenswahrscheinlichkeit (= **O**ccurrence ) der Fehlerursache,
      * **E**ntdeckungswahrscheinlichkeit (=  **D**etection) Fehlers oder seiner Ursache
      * jeweils auf einer Skala zwischen 1-10.
    * Bilde für jeden Fehler die Risiko-Prioritätszahl **RPZ** als Produkt B*A*E
  * **Subtypen**:
    * *Design-FMEA* (D:FMEA): soll systematische Fehler während der Konstruktionsphase entdecken
    * ...
    * **Prozess-FMEA** (P-FMEA): soll mögliche Schwachstellen im Prozess zum Ziele der Qualitätssteigerung ermitteln (hängt bzgl. Produktgüte mit D-FMEA zusammen). Mängel können sein:
      * zu langsame Produktion
      * zu teure Produktion
      * fehlerhafter Output
    * (hängt mit D-FMEA zusammen, weil Schwachstellen im Prozess sich in Fehlern des Produktes)
  * **Zwecke** = Verbesserte / erleichtertre Erreichung von Unternehmesnzielen
    * *Präventive FMEA* soll proaktiven bzw. möglichst frühen Fehler identifizieren und schon während der Designphase beseitigen. [ANTIZIPATION]
    * *Korrektive FMEA* soll in späten Lebensphasen Fehler entdecken. [REAKTION]
  * vgl: [https://de.wikipedia.org/wiki/FMEA](https://de.wikipedia.org/wiki/FMEA)

* **Ursache-Wirkungsdiagramm** = grafische Darstellung von Ursachen, die zu einem Ergebnis führen oder dieses maßgeblich beeinflussen, bei der auch sollen Abhängigkeiten dargestellt werden
  * hat mehrere Synonyme
    * **Ishikawa-Diagramm** bekannteste Form (stammt aus Qualitätsmanagement)
    * **Fischgrät-Diagramm** = Fischgräten-Diagramm = Fishbone Diagramm
  * dient
    * Zur systematischen und vollständigen Ermittlung von Problemursachen
    * Analyse und Strukturierung von Prozessen (Welche Phasen bewirken was)
  * **Vorgehen**
    * Trage rechts einen Fehlerbefund oder ein (noch nicht erreichtes Ziel) ein
    * Zeichne eine Linie von links nach rechts zum Fehlerbefund: Bedeutung: In dieser vorgehenden Zeit sind Dinge geschehen, die den Fehlerbefund bewirkt haben
    * trage von links nach rechts die Haupteinflussgrößen (als Quasilanes) ein. Kandidaten dafür sind
      * die vier Ms: Material, Maschine, Methode, Mensch
      * die acht Ms: 4Ms + Management, Mitwelt (Milieu), Messung (Measurement) und Geld (Money)
      * andere Verursache: Prozesse etc.
    * Verbinde jede Haupteinflussgröße mit einem schräg zum Zeitpfeil verlaufenden Pfeil ein
    * Trage zu jeder Haupteinflussgröße einflussnehmende Subursachen/Wirkungen ein.
    * Schließe die Identifikation mit einem Vollständigkeitscheck ab
    * lass Experten die identifizierten Kandidaten nach dem Grad ihrer Wirkung /ihres Einflusses im Hinblick auf den Fehler klassifizieren
  * **Zweck**: assoziatives Verfahren, um 'nichts' aus dem Blick zu verlieren. Trennt Identifikation von Analyse.
  * Vorteile:
    * Liefert gute Diskussionsgrundlage für Gruppenarbeit
    * ermöglicht vielseitige Betrachtungsweise
    * Geringer Aufwand bei der Durchführung
    * Leicht erlern- und anwendbar
  * Nachteile:
    * Unübersichtlich und umfangreich bei komplexen Problemen
    * Keine vernetzten Ursache-Wirkungs-Zusammenhänge darstellbar
    * Wechselwirkungen und zeitliche Abhängigkeiten werden nicht erfasst 
  * vgl. [https://de.wikipedia.org/wiki/Ursache-Wirkungs-Diagramm](https://de.wikipedia.org/wiki/Ursache-Wirkungs-Diagramm)
  
* **Fehlerbaumanalyse** = Fault Tree Analysis (FTA) =  Verfahren zur Zuverlässigkeitsanalyse von technischen Anlagen und Systemen unter Ausnutzung der boolschen Algebra
  * Ist DIN normiert (DIN EN 61025)
  * arbeitet 'halb assozioativ'
  * **Verfahren**
    * Zeichne die Systemstruktur als Baum von Subsystemen
    * Erstelle zu jedem Subsystem einen Fehlerbaum = liste alle Zustände auf, die zu einem Ausfall des Systems führen können
    * Sammle zu jedem Zustand die Zustände, den oberen Zustand auslösen.
      * Erlaube dabei Und-Cluster (wenn zustand a + b + c eintritt, dann zustand x) oder Oder-Cluster (wenn zustand a | b | c eintritt, dann zustand x)
    * Trage an jeden Zustandsblatt die Wahscheinlichkeit ein.  
    * Berechne dadurch die Ausfallwahrscheinlichkeit der Komponente
  * Vorteile: Verspricht Genauigkeit
  * Nachteile:
    * aufwendiges Verfahren
    * mathematisch schwer/aufwendig auszuführen bei komplexen Systemen

#### B)
Bewertungsmethoden

* **ABC**-Analyse: betriebswirtschaftliches Analyseverfahren zum Klassifizieren von Ereignisse in wichtige, mittlere und unwichtige Gefunde, Ereignise
  * *Voraussetzung*: Listen von Wertepaaren (Typ -> Wert)
  * *Verfahren*: 
    * Sortiere Liste absteigend
    * Ermittle für jeden Eintrag den Anteil am Gesamtbestand
    * Schaffe 3 Klassen: 
      * wichtig: alle, die an 80% Beitrag zum Gesamtergebnisse beteiligt sind.
      * mittel: alle, die an 15% Beitrag zum Gesamtergebnisse beteiligt sind.
      * unwichtig: alle, die an 5% Beitrag zum Gesamtergebnisse beteiligt sind.
    * Kümmere dich zuerst um die 80%-Beiträger
  * vgl. [https://de.wikipedia.org/wiki/ABC-Analyse](https://de.wikipedia.org/wiki/ABC-Analyse)
  
Beispiel: 

  Prozess:
  * Kaufe Füller
  * Kaufe Tinte
  * Befülle Füller

  Prozessschritte pro Füllerleben:

  | Schritt | Fehler | Häufigkeit | Fehlerwert | Schaden | %(SUM(Schaden))
  |---|---|---|---|---|---|
  | Füllerkauf | Haarriss im Kolben | 1 * 0.1 | 300€ | 30 € | 0.09
  | Füllerkauf | Feder verbogen | 1 * 0.5 | 30€ | 15 € | 0.04
  | Tintenkauf | Tinte vertrocknet | 50 * 0.2 | 10 € | 100 € | 0.29
  | Befüllung | Kolbenüberlauf | 1000 * 0.2 | 1€ | 200€ | 0.58
  | | | | sum(Schaden): | 345 | 

  Typ -> Wert
  | Fehler | %(SUM(Auswirkung)) | Klasse
  |---|---|---
  | Kolbenüberlauf |0.58 | A
  | Tinte trocken | 0.29 | A
  | Feder verbogen | 0.09 | B
  | Haarriss | 0.04 | C 

Ergebnis: Kümmere Dich nicht zuerst darum, einen Füllerlieferanten zu kaufen,
sondern lerne besser, den Füller zu füllen und finde einen besseren Tintenglaslieferanten

Hinweis: Eigentlich müssten die %-Werte zusammen 1 ergeben. Wer den Fehler findet, hat einen gut ;-)

* **Nutzwert**-Analyse: systematische Methode zur Bewertung von Alternativen, die sowohl qualitative als auch quantitative Kriterien einbezieht.
  * **Zweck**: Geordnete Entschiedungsfindung
  * **Verfahren**:
    * Liste die Alternativen auf
    * Liste die Bewertungskriterien auf
    * Gewichte die Bewertungskriterien nach relativer Wichtigkeit zu anderen Kriterien
    * Ermittle für jede Alternative für jedes Kriterium den zuständigen Wert
    * Multipliziere für jede Alternative den Kriteriumswert mit dem Gewicht
    * Multipliziere alles zum Gesamtnutzen der Alternative
  * *Vorteil*: mathematisch
  * *Nachteil*: Kriterien- und berwertung beeinflusst Ergebnis
  * *Nachteil*: für normierte Systematik umfangreiche mathematische Absicherung nötig
  * vgl. [https://www.munich-business-school.de/l/bwl-lexikon/nutzwertanalyse](https://www.munich-business-school.de/l/bwl-lexikon/nutzwertanalyse)

Beispiel:

  * funktionsgleiche Prozessschritte Ps1, Ps2, Ps3 sollen verglichen werden
  * Kriterien: Kosten pro Durchlauf (in €), Zeit pro Durchlauf (in H)
  * Schnelligkeit vor Kosten, 0.7 für Zeit, 0.3 für Kosten

| PS | €/DL | H/DL | gw(€) | gw(H) | Gesamtwert
|---|---|---|---|---|---|
| Ps1 | 100 | 5 | 30 | 3.5 | 105
| Ps2 | 200 | 2 | 60 | 1.4 | 84
| Ps3 | 50 | 6 | 15 | 4.2 | 63

Gewonnen hat Ps1

* **Entscheidungsmatrix**
  * liefert fundierte Entscheidungen unter Berücksichtigung einzelner Kriterien 
  * pro Kriterium werden Punkte vergeben
  * Kriterium können gewichtet sein
  * Punkte werden gewichtet addiert 
  * vgl. [https://studyflix.de/wirtschaft/entscheidungsmatrix-7025](https://studyflix.de/wirtschaft/entscheidungsmatrix-7025)

Beispiel

  * funktionsgleiche Prozessschritte Ps1, Ps2, Ps3 sollen verglichen werden
  * Kriterien: Kosten pro Durchlauf (in €), Zeit pro Durchlauf (in H)
  * Schnelligkeit vor Kosten, 0.7 für Zeit, 0.3 für Kosten
 
| Kriterium | Gewicht | PS1 | PS2 | PS3 |
|---|---|---|---|---|
| Kosten | 0.3 | 100*0.3 = 30 | 200*0.6=60 | 50*0.3= 15 |
| Geschwindigkeit | 0.7 | 5*0.7=3.5 | 2*0.7= 1.4 | 6*0.7= 4.2 | 
| Gesamt | 1 | 33.5 | 61,4 | 19.2 |

Hiewr gewinnt Ps2

* **Prozzes-Analyse-Kritierien**:
  * **Wirtschaftlichkeit** :- pekuniäreWirkung(Prozess) > pekuniärerAufwand(Prozess)
  * **Rentabiliät**: wenn val(Output)> val(Input), je größer, je produktiver
  * **Produktivität** : val(Output)/val(Input), je größer, je produktiver
  * **Amortisation** : Anschaffungskosten + Betriebskosten*Zeit - Gewinn*Zeit = 0
  * **Break Even** : Zeitpunkt der Amortisation
  * **Pareto Prinzip** : Kümmere Dich zuerst um das, was 80% Deiner Problem verursacht.
  * vgl. https://www.munich-business-school.de/l/bwl-lexikon/finanzwissen/amortisation etc.

#### C)
Managementmethoden

* **Kaizen** Ursprungsform vom* *KVP** (= kontinuierlicher Verbesserungsprozess) = **CIP** (Continual / Continuous Improvement Process)
  * verwendet die Leifragen
    * "Wie soll es sein?" [*PLAN*]
    * "Was tun wir aktuell wie?" [*DO*]
    * "Was wurde erreicht?" [*CHECK*]
    * "Was ist noch zu tun?" [*ACT*]
  * [KVP](https://de.wikipedia.org/wiki/Kontinuierlicher_Verbesserungsprozess) ist die europäische Umsetzung des **KAIZEN**-Prozesses (vgl. [https://de.wikipedia.org/wiki/Kaizen](https://de.wikipedia.org/wiki/Kaizen))

* **Lean Management**:
> "Durch gezielte Analyse der Abläufe sucht das Lean Management nach Verbesserungsmöglichkeiten in der Wertschöpfungskette, um mit minimalem Aufwand bestmögliche Ergebnisse zu erzielen. Der kontinuierliche Verbesserungsprozess stellt dabei Kund:innen in den Mittelpunkt, da ihre Bedürfnisse und Erwartungen definieren, was als wertschöpfend oder verschwenderisch gilt." 

  * will
    * Prozesse durch die Vermeidung von „Verschwendung“ zu optimieren. 
    * Ressourcen effizienter einzsetzen
    * die Zufriedenheit von Kund:innen maximieren.
  * nutzt 5 Prinzipien (fordert Menschen/Prozesse auf, sie anzuwenden) 
    * Wert aus Kundensicht definieren
    * **Wertstrom analysieren**: "Der Wertstrom beschreibt den gesamten Prozess, den ein Produkt oder eine Dienstleistung durchläuft – von der Entstehung bis zur Lieferung an Kund:innen. Jeder Schritt im Prozess wird daraufhin untersucht, ob er zur Wertschöpfung beiträgt."
    * **Wertfluss sicherstellen**: "Prozesse sollten so organisiert sein, dass ein kontinuierlicher Arbeitsfluss ohne Unterbrechungen entsteht. Dies minimiert Verzögerungen und Wartezeiten im Produktionsprozess."
    * **Pull-Prinzip etablieren**: Produkte nicht auf Vorrat produziert, sondern auf Anfragen von Kund:innen
    * **Perfektion anstreben**: sich kontinuierlich verbessern, "die eigene Arbeit stets kritisch zu hinterfragen und nach neuen Wegen zu suchen, um Prozesse effizienter und zielgruppenorientierter zu gestalten."
    * (vgl. [https://ifm-business.de/aktuelles/business-news/was-ist-lean-management-definition-methoden.html](https://ifm-business.de/aktuelles/business-news/was-ist-lean-management-definition-methoden.html))

* **TQM** = Total Quality Management 
> "Optimierung der Qualität von Produkten und Dienstleistungen eines Unternehmens in allen Funktionsbereichen und auf allen Ebenen durch Mitwirkung aller Mitarbeiter. Total Quality Management strebt die Erhöhung der Kundenzufriedenheit an."

  * Qualitätsmanagement meint dagegen 'nur: Planung, Steuerung und Überwachung der Qualität eines Prozesses bzw. Prozessergebnisses
  * vgl. [https://wirtschaftslexikon.gabler.de/definition/total-quality-management-tqm-47755](https://wirtschaftslexikon.gabler.de/definition/total-quality-management-tqm-47755)

* **DMAIC** =  Define – Measure – Analyse – Improve – Control = Definieren – Messen – Analysieren – Verbessern – Steuern 
  * Kernprozess des Qualitätsmanagement-Ansatzes Six Sigma 
  * will Prozesse so gestalten, dass diese stabil ein vorgegebenes 6 Sigma-Leistungsniveau halten
  * Phasen sind
    * *Definition* = definiere Sollzustand
    * *Datenerhebung* = finde Methoden und Instrumente zur Sammlung von Daten über den IST-Zustand der Leistungsmerkmale
    * *Analyse* = finde Ursachen der Abweichung von den definierten Leistungszielen
    * *Verbesserung* = finde Lösungen für die in der Analyse-Phase identifizierten Probleme 
    * *Steuern* =  verankere gefundenen Verbesserungen im Alltagsbetrieb 
  * vgl. [https://de.wikipedia.org/wiki/DMAIC](https://de.wikipedia.org/wiki/DMAIC) 

* **SixSigma** wendet DMAIC an, ist selbst ein statisch basiertes Verfahren zur Annäherung an einen idela Zustand.
> "Der Name „Six Sigma“ resultiert aus der Forderung, dass die nächstgelegene Toleranzgrenze mindestens sechs Standardabweichungen (6σ, englisch ausgesprochen „Six Sigma“) vom Mittelwert entfernt liegen soll"

  * Überlegung
    * Prozesse über lange Zeiträume schwanken, sie haben einen DPMO-Wert größer 0
    * "Es wäre also zu optimistisch, davon auszugehen, dass der Abstand zwischen dem Mittelwert und der kritischen Toleranzgrenze immer konstant 6 Standardabweichungen betragen würde"
    * Deswegen wird der Überschreitungsanteil für die Grenze 6σ mit 3,4 DPMO festgelegt.
  * Verfahren: Wende DMAIC an und verkleinere den DPMO-Wert Deines Prozesses, sodass Du Dir gemäß folgeden TZabelle einen besseren 6Sigma-Wert zuordnen kannst

| Sigma level	| DPMO	| fehlerhaft | fehlerfrei |
|---|---|---|---|
| 1	| 691.462	| 68 %	| 32 % |
| 2	| 308.538	| 31 %	| 69 % |
| 3	| 66.807	| 6,7 %	| 93,3 %|	
| 4	| 6.210	| 0,62 %	| 99,38 %	|
| 5	| 233	| 0,023 %	| 99,977 %	|
| 6	| 3,4	| 0,00034 %	| 99,99966 |
| 7	| 0,019	| 0,0000019 %	| 99,9999981 |

>  * Beispiel
>    1. Ich hatte meinen Blutdruck zwischen 05/2024 u. 03/2025 163 mal gemessen: `N=163`* 
>    2. Dabei hatte ich manchmal das Datum im falschen Format eingetragen, manchmal Systole und Diastole vertauscht, manchmal beides: `O=2`
>    3. Bei 10 Datensätzen war nur das Datum falsch, bei 24 war das Datum falsch und Systole und Diastole vertauscht: `D=10+24*2=58`
>    4. Formel: `DPMO=(D/(N*O))*1.000.000=(58/163*2)*1000000=0,17791411*1000000=177914,11`
>    * Demnach hätte mein Blutdruckmessungsprozess einen 6Sigma-Wert von 2,x

* **Normalverteilung** und **SixSigma**: das Zusammenspiel
  * Die Idee ist, dass oft durchgeführte Prozesse zwar einen (idealen) Erwartungswert haben, im konkreten aber davon abweichen.
  * Kleinere Abweichungen tauchen häufiger auf, größere seltener.
  * Das ergibt die Glockenkurve: 
    * die x-Achse beschreibt erreichbare Werte
    * die y-Achse die Häufigkeit * Varianz / bzw. Standardabweichung 
    * Der Erwartungswert bildet den Peak.
  * Hinweis: 
    * Erhöhung des Erwartungswertes verschiebt die Kurve nach rechts
    * Erhöhung der Standardabweichung streckt sie. 
  * SixSigma dreht es um: 
    * Der Erwartungswert ist das, was nicht erwartet/gewünscht ist, nämlich das alle Produkte falsch sind.
    * Das ist 'messbar', wenn es 1.000.000 dpmo gibt `DPMO=(D/(N*O))*1000000` => D/(N*O)=1
    * Die Abweichung von ganz falsch wird zum Grad der Richtigkeit (Glockenkurve)
    * Die Glockenkurve wird nach re und li in 6 Schritte geteilt
    * Dann wird gefragt: bei welchem Wert können wir mit dem Prozessergebnis zufrieden sein. 

* **Data Mining** = will branchen-, software- und anwendungsunabhängigen standardisierten Prozessablauf des Data Minings für Unternehmen bereitstellen
  * **Problem**: in großen unstrukturierten Datenmengen sind enhaltene Informationen nicht direkt ableitbar
  * **Lösung**: Prozess aus 6 Schritten
    * **Business Understanding (Aufgabendefinition)**: verstehe, was zu welchem Zweck gesucht werden soll
    * **Data Understanding** : verstehe wie vorliegende Daten erzeugt worden sind, suche nach Ergänzungsdaten
    * **Data Preparation** : erzeuge den endgültigen Datensatz
    * **Modeling** : wähle das Modellierungsverfahren und erzeuge das (elektroniische) Modell der natürlichen Daten
    * **Evalusiere** : Vergleiche ob sich Modell und Ausgangsdaten hinsichtlich Anwendung / Anfragen gleich verhalten
    * **Deploymenmt** : Bringe das Modell in den Betrieb und lass es die natürlichen Daten ersetzen.
  * vgl. [https://datasolut.com/crisp-dm-standard/](https://datasolut.com/crisp-dm-standard/) 

* **ETL** ist keine Managementmethode, sondern meint den Prozess *Extract, Transform, Load*,  mit dem Daten aus mehreren, gegebenenfalls unterschiedlich strukturierten Datenquellen in einer Zieldatenbank vereinigt werden.
  * oft genutzt im Datawarehouse Bereich
  * **Vorgehen**:
      * *Extrahiere* Daten aus verschiedenen Quellen
      * *Transformiere* die Daten in das Schema und Format der Zieldatenbank (= setzt Konverter voraus)
      * *Lade* die Daten in die Zieldatenbank
  * **Anlass** kann periodisch oder ereignisgesteuert sein
  * **Syntaktische Transformation** = Verbesserung und/oder Korrektur der Daten basierend auf formalen Aspekten.
  * **Semantische Transformation** = inhaltliche Aspekte überprüfen und wenn nötig Daten modifizieren und/oder angereichert
    * Duplikate entfernen
    * Datenwerte anpassen
    * offensichtliche Fehlerbereinigen 
  * **Laden** ...
* Variante **ELT**: Daten werden wie extrahiert geladen = onthefly-Konvertierung 
  * Vorteil: 
    * angeblich schneller
    * angeblich sicherer, weil Originaldaten erhalten
* vgl. [https://de.wikipedia.org/wiki/ETL-Prozess](https://de.wikipedia.org/wiki/ETL-Prozess)