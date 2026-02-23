<!-- LTeX:Language=de-DE -->

### Datenqualität u. -management 

#### A
Riskmanagement

<!-- LTeX:Language=en-US -->
> *"Risk management is the identification, evaluation, and prioritization of risks,[1] followed by the minimization, monitoring, and control of the impact or probability of those risks occurring"* (vgl. [https://en.wikipedia.org/wiki/Risk_management](https://en.wikipedia.org/wiki/Risk_management))

<!-- LTeX:Language=de-DE -->
Risikomanagement umfasst 

* Risikobeurteilung, 
  * Risikoidentifikation
  * Risikoanalyse
  * Risikobewertung
* Risikobewältigung 
* Risikokommunikation

(vgl. [https://de.wikipedia.org/wiki/Risikomanagement](https://de.wikipedia.org/wiki/Risikomanagement))

Nach dem PMBoK (Project Management Body of Knowledge) des PMI (Project Management Institut) gibt es 5 Phasen, die sich als teilweise überlappende und/oder iterativ ausgeführte Teilprozesse organisieren:

* __*Risk Management Planning*__ meint die Entscheidung (einer Organisation, Firma, etc.) "[...] how to approach, plan, and execute the risk managment activities for a project"
* __*Risk Identification*__ meint den Prozess "[...] determining which risks might affect the project and documenting their characteristics" 
* __*Qualitative Risk Analysis*__ meint den Prozess "[... of] prioritizing risks for subsequent further analysis or action by assessing and combining their probalility of occurence and impact":

> *"Qualitative Risk Analysis assesses the priority of identified risks using their probability of occuring, the corresponding impact [...] as well as other factors  such as the time frame and risk tolerance [...]."*

* __*Quantitative Risk Analysis*__ meint den Prozesse "[... of] numerically analyzing the effect on overall project objectivities of identified risks" 
* *Risk Response Planning* meint den Prozess "[... of] developing options and actions to enhance opportunities, and to reduce threats to project objectives"
* __*Risk Monitoring And Control*_ meint den Prozess "[...] tracking identified risks, monitoring residual risks, identifying new risks, executing risk response plans, and evaluating their effectiveness throughout the project life cycle"  

(vgl. [https://mypmps.fodina.de/en/mypmps/knowledgeareas/risk/annotations.html](https://mypmps.fodina.de/en/mypmps/knowledgeareas/risk/annotations.html) u. ff)

Das bedeutet (serialisiert)

Step 1: **Risikoidentifikation** 

Was kann schiefgehen? Was könnte das zu erreichende Ziel hintertreiben? Wird ermittelt anhand von Wissen der Fachleute. 
* Leitende Fragen:
  * Welche groben Bereiche gibt es? Welche Subbereiche gibt es darin jeweils?
  * Was aus diesen Bereichen könnte die Zielerreichung behindern/erschweren?
* Leitende Meta-Segmentierung
  * Personelle Risiken
  * Zeitliche und finanzielle Risiken
  * Technologische Risiken 
  * Organisatortische Risiken
* Ergebnis: Risikoliste = Risk Register
  
Step 2A: **Risikoanalyse** 

* Worin besteht das Risiko genau? (Beschreibung, was genau gemeint ist)
* Woran erkennt man, dass es eingetreten ist?
* Welche Faktoren weisen mit welcher Wahrscheinlichkeit darauf hin

Step 2B: **Risikobewertung** = *Qualitative Risk Analysis*

Klassifikation der Risiken in je 1 -3 [+x] Kategorien auf der Basis von Experten**schätzungen** hinsichtlich der
  * **Eintrittswahrscheinlichkeit** 
    * *gering* | *mittel* | *hoch*
    * 0.1 - 0.3 | 0.4 - 0.6 | 0.7 - 0.9
  * **Auswirkung** 
    * *schwach* | *mittel* | *stark* 
    * *10K* | *100K* | *500K*
    *  0.1 - 0.3 | 0.4 - 0.6 | 0.7 - 0.9

[
  * Wahrscheinlichkeiten können Wertebereiche zwischen 0.1 und 0.9 geclustert, wenn numerische Werte zur Verfügung stehen
  * Auswirkungen können pekuniär ausgedrückt werden, wenn numerische Werte vergangener Schaden/Opportunities zur Verfügung stehen
  
]

**Hinweis:** 
* Risiken mit Wahrscheinlichkeit 0 treten NIE ein, brauchen also nicht gelistet zu werden
* Risiken mit Wahrscheinlichkeit 1 treten IMMER ein, müssen vom PM anders behandelt werden.

Egal, was gewählt:

**Definition**: **_Risikokennziffer_** = Eintrittswahrscheinlichkeit * Schadenspotential

| Impact/Propability | *gering* | *mittel* | *hoch* |
|---|---|---|---|
| *schwach* | absolut unwichtig | unwichtig | mäßig gefährlich |
| *mittel* | unwichtig | mäßig gefährlich | gefährlich |
| *stark* | mäßig gefährlich | gefährlich | absolut gefährlich |

Risikomanagement kostet Geld u. Resourcen. Je geringer der Aufwand, desto günstiger das Produkt aber desto größer das *gefühlte* Risiko. Gute Strategie: 

> **Kümmere Dich zuerst um Risiken mit hoher Eintrittswahrscheinlichkeit UND großer Auswirkung.**

Step 2C: **Risikobewertung** = *Quantitative Risk Analysis*

Beruhen auf numerisch erfassten Daten der Eintrittswahrscheinlichkeit und aus Schadenssummen aus (branchenübergreifend) vorgehenden Fällen.

Beispiel: 
* Prozess wird in Schritte eingeteilt. (Prozessdiagramm: EPK, BPMN)
* Für jeden Schritt wird die Ausfallquote (unzureichende Daten) bestimmt und DPMO aus gedrückt. (= Wahrscheinlichkeit)
* Für jeden Schritt wird das schon investierte Geld festgelegt. (= Schaden pro fehlerhaftem Stück)
* Damit wird Tabelle aufgebaut.
* Man liest ab, welcher Prozessschritt zuerst 'repariert werden muss*

Step 3: Risikobewältigung = **Riskresponseplanning** 

Für jedes Risiko wird - in Reihenfolge **_Risikokennziffer_** festgelegt, wie beim Risikoeintritt reagiert werden soll, und mit Maßnahmen aus folgender Typologie

* **AVOIDANCE** = Verhinderung des Eintretens = Änderung des Projektplans
* **TRANSFER** = Übertragung auf Dritte (vertrag. etc.)
* **MITIGATION** = Reduzierung der Einrittswahrscheinlichkeit oder der Auswirkung (mit Projekt- oder Finanzmitteln)
* **ACCEPTANCE** = Risktaking 'Wird schon klappen'

Step 4: Risikobeobachtung = **Risk Monitoring** 

Zu den Indikatoren wird eine Beobachtung aufgesetzt.

**Fachbegriffe dazu**:

* **PDCA-Zyklus** = *Plan* *Do* *Check* *ACT*
  * meint Planen, Durchführen, Überprüfen, Verbessern, Planen, ...
  * nicht nur auf Riskmanagement anwendbar
  * hat aber ähnliche Umsetzungstruktur: 
    * planen, was gemessen werden soll, SOLL-Werte und Messverfahren festlegen
    * Arbeit durchführen und IST-Werte messen
    * SOLL-IST Differenz feststellen
    * Methoden der Verbesserung eruieren
* **KVP** (= kontinuierlicher Verbesserungsprozess) = **CIP** (Continual / Continuous Improvement Process)
  * verwendet die Leifragen
    * "Wie soll es sein?" [*PLAN*]
    * "Was tun wir aktuell wie?" [*DO*]
    * "Was wurde erreicht?" [*CHECK*]
    * "Was ist noch zu tun?" [*ACT*]
  * [KVP](https://de.wikipedia.org/wiki/Kontinuierlicher_Verbesserungsprozess) ist die europäische Umsetzung des **KAIZEN**-Prozesses (vgl. [https://de.wikipedia.org/wiki/Kaizen](https://de.wikipedia.org/wiki/Kaizen))
* **MTBF** = Mean Time Between Failures
  * gibt die "mittlere Betriebszeit zwischen Ausfällen" an = "die Zeit, die im normalen Betrieb eines Systems, einer Einrichtung oder einer Systemkomponente wahrscheinlich vergeht, bevor es ausfällt" 
  * gemessen in Stunden
  * Beispiel: 10000 = "das Gerät arbeitet im Mittel 10.000 Stunden"
  * Oft genutzt zur Angabe der Robustheit bei Laufwerken und Festplattenlaufwerken
  * KEINE STANDARDISIERTE KENNZIFFER 
* **MTTR** = Mean Time To Repair
* **AFR** = Annual Failure Rate = Umrechnung von **MTBF** auf ein Jahr
  * Beispiel: MTBF = 100.000 (ein Ausfall in 100.000 Stunden ) = AFR-Wert von 8,76 %, "der besagt, dass von 11 Laufwerken im Schnitt jedes Jahr eines ausfällt."
  
(vgl. [https://fachglossar.platinus.at/docs/Glossar/M-Glossar/MTBF/](https://fachglossar.platinus.at/docs/Glossar/M-Glossar/MTBF/))

* smart-Bedeutung:
  * **SMART** steht für "Specific Measurable Achievable Reasonable Time-bound"  bzw. "Spezifisch, Messbar, Attraktiv, Realistisch und Terminiert" und bildet eine Meta-Anforderung für Ziele: Sie sollen 
    * Specific (Spezifisch) sein = eindeutig definiert, präzise wie möglich formuliert
    * Measurable (Messbar) sein 
    * Achievable (Erreichbar) sein = ansprechend bzw. erstrebenswert, akzeptiert
    * Reasonable (Angemessen) sein = möglich und realisierbar
    * Time-bound (terminiert) sein = mit einem fixen Enddatum festlegbar
    * Beispiel: 
      * Zähle alle Tiere, gegliedert nach Tierarten, des Tierheims im Juni 
      * Zähle alle Sterne der Milchstraße (+S+M+A+R-T) [heute geschätzt zwischen 100 und 200 Milliarden. Wenn ein Mensch pro Stunde einen Bereich mit durchschnittlich 1000 Sternen durchzählen kann, dann bräuchte er ~8.333.333 Tage = ~22831 Jahre ]
    * vgl. 
      * [https://de.wikipedia.org/wiki/SMART_(Projektmanagement)](https://de.wikipedia.org/wiki/SMART_(Projektmanagement))
      * [https://www.orghandbuch.de/Webs/OHB/DE/OrganisationshandbuchNEU/4_MethodenUndTechniken/Methoden_A_bis_Z/SMART_Regel_Methode/SMART_Regel_Methode_node.html](https://www.orghandbuch.de/Webs/OHB/DE/OrganisationshandbuchNEU/4_MethodenUndTechniken/Methoden_A_bis_Z/SMART_Regel_Methode/SMART_Regel_Methode_node.html)
  * **S.M.A.R.T** steht für "Self-Monitoring, Analysis and Reporting Technology"
    * Industriestandard zur Überwachung von Festplattenlaufwerken (HDD) und Solid-State-Drives (SSD)
    * dient der Vorhersage eines möglichen Ausfalls des Speichermedium
    * vgl. [https://de.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology](https://de.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology)

#### B)
Verfügbarkeitsanforderungen an Systeme

> Von Real-Time Communications (RTC) oder Echtzeitkommunikation wird bei jedem Modus gesprochen, bei dem Anwender Informationen sofort oder mit zu vernachlässigender Latenz austauschen können. In diesem Zusammenhang lässt sich der Ausdruck Echtzeitauch durch liveersetzen. (vgl. [https://www.computerweekly.com/de/definition/RTC-Real-Time-Communications-Echtzeitkommunikation](https://www.computerweekly.com/de/definition/RTC-Real-Time-Communications-Echtzeitkommunikation))


oder

> "Echtzeitkommunikation bezeichnet den sofortigen Austausch von Informationen ohne merkbare Verzögerung, wie er beispielsweise bei Telefonaten oder Videochats vorkommt." (vgl. [https://www.studysmarter.de/studium/ingenieurwissenschaften/automatisierung-in-der-informationstechnologie/echtzeitkommunikation/](https://www.studysmarter.de/studium/ingenieurwissenschaften/automatisierung-in-der-informationstechnologie/echtzeitkommunikation/))

Problem: "zu vernachlässigender Latenz" bzw. "nicht merkbar" hängt definitorisch vom Empfänger und dem Zweck ab.

* *Half-Duplex-Modus* = Daten werden derselben Leitung gesendet, aber pro Richtung sequentiell
* *Full-Duplex-Modus* = Daten werden "[...] in beide Richtungen simultan auf einem einzelnen Signalträger oder einem Schaltkreis übertragen. 
* Daten werden nicht zwischengespeichert
* Die Daten wandern aber von der Quelle zum Ziel und werden nicht zwischengespeichert.

Beispiel: 
* Realtime: Telefonie
* Nicht Realtime: Schwarzes Brett

Achtung: sehr weiche Definition. 

* Mailserver
  * bzgl. Versand und Wiederabruf: Echtzeitkommunikation nicht nötig
  * bzgl. Login und Abruf: 30sec. Timeout akzeptierte Grenze
* Webserver:
  * bzgl. Versand und Wiederabruf: Echtzeitkommunikation nicht unbedingt nötig
  * Browser-Timeout meist auf 30 sec. eingestellt, Menschen akzeptieren oft nur weniger.
* Groupware: 
  * bei Textnachrichten: Echtzeitkommunikation empfehlenswert
  * bei Sprachaustausch: Echtzeitkommunikation meist nötig
* Datenbanken:
  * abhängig vom Nutzungskontext (nutzendes Frontend)
* VoIP (Voice over IP), Videokonferenz, Telekonferenz Echtzeitkommunikation nötig

Beispiel:

* Whatsapp: Echtzeitkommunikation systemisch nicht nötig, [ist ein Schwarzes Brett-Verfahren], aber sehr hilfreich
* SMS: Echtzeitkommunikation nicht erwartet u. nicht zugesagt.

#### C
RAID

* meint (im IT-Kontext) 
  * früher: "Redundant Array of Inexpensive Disks" (Anlass war: organisiere Datensuicherungen ohne (damals) teure Platten nutzen zu müssen)
  * heute: "Redundant Array of Independet Disks" (heute sind Festplatten kein Kostenfaktor mehr, wohl aber die Lese- und Schreiboperationen, die den Datendurchsatz verlängern)
* dient dazu, in einem System mit Festplatten die *Mean Time Between Failures (MTBF)* zu erhöhen
   * *RAID 0* = Striping – Beschleunigung ohne Redundanz :- zwei Platten werden "in zusammenhängende Blöcke gleicher Größe aufgeteilt und im Reißverschlussverfahren zu einer großen Festplatte angeordnet".
    * Erhöht nur Datendurchsatz
    * Fällt eine Platte aus, ist das Gesamtsystem zerstört
    * Eigentlich keine Redundanz, also kein Raid
  * *RAID 1* = Mirroring – Spiegelung :-  Zwei (oder mehr) Platten werden "in zusammenhängende Blöcke gleicher Größe aufgeteilt" und jeweils 'gleichzeitig' mit denselben Daten beschrieben.
    * bietet volle Redundanz
    * fällt eine Platte aus, kann die andere einspringen bzw, die Ersatzplatte restaurieren.
    * Bei zu unterscheiden:
      * Mirroring: beide Platten nutzen denselben controller. (1 Schreibbefhl, zweimal ausgeführt)
        * Nachteil A: Controller: Single Point of Failure
        * Nachteil B: Schreibprozess verlangsamt
      * Duplexing: jede Platte ein eigener Controller
  * *RAID 5* :- Block-Level Striping mit verteilter Paritätsinformation
    * 3(+x) Festplatten bilden einen Verbund. Auf Platten 1-(3+x-1) werden Nutzungsdaten gespiegelt, auf Platte 3(+x) werden 'Paritätsinformationen' gespeichert
    * Die Pakete werden im Reißverschlussverfahren geschrieben
    * Pariätsinfomrationen = die Anzahl der gesetzten Bits + gerade/ungerade Bit
    * Vorteil: 
      * Daten restaurierbar, Konsistenz anhand Paritärprüfbar (welcher Sektor ist die richtig, welcher korrupt) 
      * Platte im Betrieb austauschbar
      * Alle Platten stehen für Leseoperationen zur Verfügung
    * Nachteil: Je mehr Platten, je teurer
  * *RAID 4* :- Wie Raid 5, nur dass Paritätsinfos auf dieselbe Platte geschrieben werden. (Single Point of Failure)
  * *RAID 10* :- Vereinigung von RAID-0 (Striping) und RAID-1 (Mirroring) Im Detail: Daten werden über über 2 gespiegelte Paare gestriped. Verlangt also mindestens 4 Platten.
(vgl [https://de.wikipedia.org/wiki/RAID](https://de.wikipedia.org/wiki/RAID))

#### D
Datensicherheit/Datenschutz

* **Datenschutz** 
  * ist gesetzlich vorgegeben
  * bezieht sich auf personenbezogene Daten
  * meint nicht nur elektronische erfasste Daten
  * grundsätzlich darf man keine personenbezogenen Daten elektronisch erfassen, es sei denn es gibt ein berechtigtes Interesse (notwendig zur Geschäftsabwicklung etc.). Wenn man Daten erfasst muss man 
    * ein Datenschutzkonzept entwickeln, das beschreibt, wer auf welche wo gespeicherten personenbezogenen Daten zugreifen darf
    * entsprechende TOMS implementieren
    * dem Eigner sagen,
      * welche Daten man erfasst
      * warum / wozu man sie braucht (das eigene berichtigte Interesse)
      * ggfls. dass man sie weitergibt und an wen
      * wie lange man sie aufhebt
      * wo und wie er die gespeicherten Daten abfragen kann
      * wo und wie er die gespeicherten Daten löschen lassen
      * wer der (firmen)spezifische Datenschutzbeauftragte ist (ab einer gewissen Firmengröße)
  * Cookies sind besonders:
    * Nutzer muss zustimmen, dass sie auf seinem Rechner gespeichert werden (konkludente Zustimmung)
    * Ansonsten wie oben
    * Einsicht und Löschen per Browser

* **Datensicherheit**
  * bezieht sich auf 
    * den Schutz von Daten vor ungewolltem Zugriff
    * den Schutz vor Datenverlust durch Systemfehler
  * RAID ist technische Lösung
  * Das Erstellen von Backups ist technisch-systemisch Lösung
    * Full Backup (Sichern des gesamten Datenbestandes auf externen 'Platte' / Cloud etc.)
    * Inkrementelles Backup (nur geänderte Daten seit dem letzten Full-Backup+vorgehende INC-Updates)
    * Differentielles Backup (immer alle geänderte Daten seit dem letzten Full-Backup)
  * braucht neben Backupstrategie: 
    * z.B. 3-2-1 Regel: Habe 3 Kopien Deines Datenbestandes, 2 davon auf unterschiedlichen Medien, 1 davon in einer anderen Location / Datacaneter
    * Rolling Backup: schiebe täglich eine Tagessicherung in den Wochenbestand, schiebe nach einer Woche die letzte Tagessicherung als nächste Wochensicherung in den Monatsbestand, schiebe nach einem Monat die letzte Wochensicherung als neue Monatssicherung in den Jahresbestand. Führe alle anderen Medien wieder dem Schreibprozess zu.
  * eine Recoverystrategie: (Was ist zu tun, wenn Daten zerstört sind.)



#### E)
Monitoring

* *Festlegen von Monitordaten* = Definition, was gemessen / mitgeplotted werden soll (Beispiel: Zeit der Beantwortung eines HTTP-Requests am Load-Balancer)
* *Festlegen von Schwellwerten* = Definition eines Wertes, ab dem ein Alert ausgeworfen werden soll.
* Systemlastanylyse: Aufzeichnung der Werte
* Resourcenengpass: Wenn Schwellwerte gerissen werden (Beispiel: Wird häufig geswappt und ist die Reaktion langsam, ist der Hauptspeicher zu gering )
* Prädiktive Instandhaltung = Predictive Maintaince (vgl. [https://de.wikipedia.org/wiki/Prädiktive_Instandhaltung](https://de.wikipedia.org/wiki/Prädiktive_Instandhaltung))
  * Instandhaltungsstrategie
  * "kontinuierlichen Erfassung und Analyse von Zustandsdaten mittels Sensorik"
  * Klassifikation von Zuständen bezogen auf Fehler
  * Voraussagen
  
siehe auch 'systemmonitor' und befehl top

#### F) SNMP

> Das Simple Network Management Protocol (SNMP; deutsch „Einfaches Netzwerkverwaltungsprotokoll“) ist ein Netzwerkprotokoll, das von der IETF entwickelt wurde, um Netzwerkelemente (z. B. Router, Server, Switches, Drucker, Computer usw.) von einer zentralen Station aus überwachen und steuern zu können. (vgl. [https://de.wikipedia.org/wiki/Simple_Network_Management_Protocol](https://de.wikipedia.org/wiki/Simple_Network_Management_Protocol))

* Auf den überwachten/gemanagten Client werden 'Agenten' installiert
* Die liefern per UDP Daten an Server und empfangen Befehle.


<!-- LTeX:Language=de-DE -->


