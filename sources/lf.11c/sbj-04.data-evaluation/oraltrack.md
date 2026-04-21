<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### Definitionen


* **Datenauswertung** = **[→ ZP:Sheet:2]**
  * aus den Daten Aussagen über den repräsentierten Weltausschnitt ableiten
  * nach **Trends** suchen = Bereiche, die Prognosen erlauben
  * nach **Abweichungen** suchen = die Trends auffällig unterbrechen (Peaks, Ausreißer)

* **Datenvisualisierung** = **[→ ZP:Sheet:3]**
  * grafische Aufbereitung der Daten zwecks Ableitung von Aussagen 
    anhand visueller Auffälligkeiten
  * **Linien- und Flächendiagramme** :- zur Darstellung des Werteverlaufs über die Zeit
  * **Balkendiagramme** :- konfrontative Darstellung von erreichten Werten pro Werteträger (= Wahlergebnisse)
  * **Tortendiagramme** : Darstellung von Anteilen an einer Gesamtanzahl
  * **Streudiagramm** : Verteilung von zweidimensionalen Messungen zwecks Einteilung in Gruppen
  * **Blasendiagramm** : Verteilung von dreidimensionalen Messungen
  * **Wortwolken** : assoziative Begriffsdarstellung mit Gewichtung per Größe.

  * Hier beispielhaft vorgeführt an den bereinigten dsp-beta-Daten:
    * CSV-Daten in LibreOffice-Calc (Excel) laden
    * Alle Daten vom Typ Text in intendierte Typen wandeln (hier Datum und Zeit)
    * Diagrammtyp auswählen
    * Datenranges zusammstellen.
  * Achtung: Nicht alle Diagrammtypen sind für alle Daten visuell angmessen:
    * Eine abfallende Linie für *Sunrise* und eine aufsteigende für *Sunset* macht Sinn.
    * Ein Balkendiagramm zur Visualisierung der steigenden Tageslänge macht Sinn.
    * Eine aggregierte Balkendarstellung ist nur schwer zu verstehen.

* **Statistische Analyse** =  **[→ ZP:Sheet:4]**
  * **Minimum** = kleinster Wert einer Datenreihe
  * **Maximum** = größter Wert einer Datenreihe
  * **Spannweite** = Maximum - Minimum
  * **Mittelwert** =
    * addiere alle Werte und Teile die Summe durch die Anzahl der addierten Werte
    * *aussagekräftig* für gleichmäßig verteilten Werte
  * **Median** =
    * sortiere alle Werte nach Größe und wähle den Wert, sodass gleich viel 
      Werte oberhalb und unterhalb liegen. (*Bei einer ungeraden Anzahl von Messungen 
      ist der Wert, der genau in der Mitte der Liste liegt. Bei einer gerade 
      Anzahl der Messungen ist es der Mittelwert der beiden Werte, die die Mitte der 
      Liste bilden.*)
    * Ausreißer fallen nicht so ins Gewicht
  
Zwischenfrage: **Wozu sind diese Werte eigentlich gut?**

Intuitives Verfahren in grafischen Datendiagrammen: Ermittle die Normalität (*Mittelwert*, *Median*, *Trends*), dann die *Ausreißer*, dann die Gründe.

Das geht auch mathematisch / programmiertechnisch. Mit folgenden Definitionen: 

  * **Varianz** =
    * durchschnittliche Abweichung vom Mittelwert
    * Berechnung:
      * Subtrahiere von jedem Wert einer Datenreihe den Mittelwert und quadriere das Ergebnis.
      * Addiere die so berechneten Werte und teile das Ergebnis durch die Anzahl Summanden.
    * Idee: je kleiner die Varianz, desto geringer die Streuung im Durchschnitt
  * **Standardabweichung** =
    * alternative Form der durchschnittlichen Abweichung vom Mittelwert
    * rechnet das Quadrat wird wieder heraus
    * wird wegen Ähnlichkeit zu den 'gemessenen' Werten oft bevorzugt
    * **je kleiner Standardabweichung, desto kleiner Abweichung vom Mittelwert im Durchschnitt** 
      *= desto 'gleichförmiger' die Messungen*
    * Berechnung:
      * Bilde zweite Wurzel aus der Varianz
      * Nimm den |Betrag| (= die positive Lösung)
  * **Kovarianz** = 
    * "gibt Auskunft über den Zusammenhang von zwei metrischen Variablen".
    * (vgl. [https://www.scribbr.de/statistik/kovarianz/](https://www.scribbr.de/statistik/kovarianz/))
    * ist "ein nichtstandardisiertes Zusammenhangsmaß [...] und damit nur begrenzt vergleichbar."
    * > "Ein positiver Wert der Kovarianz sagt dir, dass wenn die eine Variable steigt, 
        dies auch für die andere der Fall ist. Gleichermaßen zeigt ein negatives Vorzeichen, 
        dass wenn die eine Variable steigt, die andere sinkt."
    * Berechnung:
      * Bestimme das arithmetische Mittel jeder Wertereihe.
      * Subtrahiere von jedem Wert einer jeden Wertereihe das jeweilige arithmetische Mittel.
      * Multipliziere die so gewonnenen Ergebnisse paarweise.
      * Addiere die so gewonnenen Werte. 
      * Dividiere den so gewonnenen Wert durch die Anzahl
  * **Korrelationskoeffizient** nach [https://www.scribbr.de/statistik/kovarianz/](https://www.scribbr.de/statistik/kovarianz/) 
    * "gibt die standardisierte Kovarianz an" 
    * (vgl. [https://www.scribbr.de/statistik/kovarianz/](https://www.scribbr.de/statistik/kovarianz/) )
    * normiert das Ergebnis auf einen Bereich zwischen -1 und +1:
      * Korrelationskoeffizient = ~0 : es gibt keinen Zusammenhang
      * Korrelationskoeffizient > 0 : Je größer die Kovarianz, desto größer die
        Wahrscheinlichkeit, dass der zweite Wert auch steigt, wenn der erste Wert steigt.
      * Korrelationskoeffizient < 0 : Je kleiner die Kovarianz, desto **größer!** 
        die Wahrscheinlichkeit, dass der zweite Wert steigt, wenn der erste Wert sinkt.
    * Berechnung
      * Berechne die Standardabweichungen zweier Datenspalten einer Datenmessung 
      * Berechne die Kovarianz bezogen auf diese Datenspalten.
      * Dividiere die Kovarianz durch das Produkt beider Standardabweichungen.
  * **Defects per Million Opportunities** (*DPMO*)
    * gibt an, wie viel falsche (falsch erfasste, repräsentierte, ...) Daten pro 1 Millionen Möglichkeiten
  
> *DPMO represents the number of defects that could occur per million opportunities in any given process, 
> thus providing a standardized measure for evaluating process performance and quality across 
> different industries and scales of operation.* 
> ( vgl. [https://www.sixsigmaonline.org/defects-per-million-opportunities-dpmo-six-sigma](https://www.sixsigmaonline.org/defects-per-million-opportunities-dpmo-six-sigma))

* Berechnung:
  * Anzahl der gemessenen Fehler = D (was als Fehler gilt, wird definiert)
  * Anzahl der produzierten / verglichenen Einheiten (units) = N (zählen)
  * Anzahl der *möglichen* Fehler pro produzierter / verglichener Einheit = O(opportunities)
  * Formel **`DPMO=(D/(N\*O))*1,000,000`**
  * ( vgl. [https://six-sigma-deutschland.de/defects-per-million-opportunities-dpmo/](https://six-sigma-deutschland.de/defects-per-million-opportunities-dpmo/) )

  * **Six Sigma** (*6S*)
    * meint Qualität eines Prozesses
    * bester realistisch möglicher Wert = 3.4 DPMO



### Beispiel:  **[→ ZP:Sheet:5]**

| Typ | unsortierte Werteliste | sortierte Werteliste |
|---|---|---|
| Systole | `[ 182, 158, 179, 170]` | `[ 158, 170, 179, 182 ]` |
| Puls | `[ 66, 75, 67, 78]` | `[ 66, 67, 75, 78]` |

* **Systole**:
  * Minimum: `158`
  * Maximum: `182`
  * Spannweite: `182 - 158 = 24`
  * Mittelwert: `(182 + 158 + 179 + 170)/4 = ~172`
  * Median: `average(midpair()) = average(170,179) = (170+179)/2 = 174,5` 
  
* **Puls**:
  * Minimum: `66`
  * Maximum: `78`
  * Spannweite: `78 - 66 = 12`
  * Mittelwert: `(66 + 75 + 67 + 78)/4 = 71,5`
  * Median: `average(midpair()) = average(67,75) = (67+75)/2 = 71` 

* **Varianz**:
  * Systole:
```
  ( (158-172)^2 + (170-172)^2 + (179-172)^2 + (182-172)^2 ) / 4
= (    -14^2     +    -2^2     +    7^2         + 10^2    ) / 4 
= (      196     +      4      +     49         + 100     ) / 4 
=                     349                                   / 4
=  87,25 ~= 87
```
  * Puls:
```
  ( (66-72)^2 + (75-72)^2 + (67-72)^2 + (78-72)^2 ) / 4
= (   -6^2    +    3^2    +   -5^2    +   6^2     ) / 4
= (    36     +     9     +     25    +    36     ) / 4
=                        106                        / 4 
= 26,5 ~= 27
```
* **Standardabweichung**:
  * Systole: `sqrt(87)` ~= *9,32*
  * Puls: `sqrt(27)` ~= *5,2*

* **Kovarianz** 

| Systole | Puls | Systole-MW(Systole) | Puls-mw(PULS) | Sp3 * Sp4 |
|---|---|---|---|---| 
| 182 | 66 | 182 - 172 = 10 | 66 - 71 = -5 | - 50 |
| 158 | 75 | 158 - 172 = -14 | 75 - 71 = 3 | - 42 |
| 179 | 67 | 178 - 172 = 6 | 67 - 71 = -4 | - 24 |
| 170 | 78 | 170 - 172 = - 2| 78 - 71 = -7 | 14 |
| | | | | = -112 / 4 = **-28**

* **Korrelationskoeffizient** 
```
Standardabweichung(Systole) = 9,32
Standardabweichung(Puls) = 5,2
Kovarianz(Systole,Puls) = -28
Korrelationskoeffizient = -28/(9,32*5,2) = -28/4846 ~= -0,57
```

*Aussage: Wenn die Systole sinkt, steigt der Puls u.u.*

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF11c:04:Datenauswertung:01**</span>


Führen Sie ein Mini-Scrumprojekt durch. Gegenstand des Projektes sind bereinigten Daten `dsp-alpha.csv`. 
Ziel des Projektes ist es, möglichst gute Aussagen über Verlauf und Wirkung der Bluthochdruckbehandlung 
und des Patienten zu liefern. Ausgang für Implementationen ist der Konverter `dsp-alpha-conv.py`.

* [ ] Das Projekt läuft über 5 Sprints von je einer Doppelstunde.
* [ ] Wählen Sie zu Anfang eine ScrumMasterin. Sie arbeitet nicht mit, sondern sorgt für die 
      Einhaltung der Regeln - insbesondere dafür, dass Zeitbegrenzungen eingehalten werden!
* [ ] **SprintPlanning**: Beginnen Sie jeden Sprint (= jede Doppelstunde) mit einem Scrumplanning von höchstens 15 min:
  * [ ] *Verkürzter __Sprintpoker__*: Schätzen Sie neue Aufgaben im Productbacklog per Zuruf hinsichtlich Komplexität/Aufwand. 
   (einfach: 1, mittel: 3, komplex: 5, unbekannt: 13). Einigen Sie sich schnell auf einen Wert.
  * [ ] Einigen Sie sich auf die Anzahl der Punkte, die Sie als Team in diesem Sprint (bis zur nächsten Pause) abarbeiten werden.
  * [ ] Greifen Sie sich von oben so viele Einträge aus dem Productbacklog, bis Sie ihre Punktzahl erreicht haben.
  * [ ] Einigen Sie sich untereinander, wer welche (Teil)Aufgaben übernimmt.
* [ ] **Daily**: Treffen Sie sich in einem Sprint einmal nach 45 min. zu einem 'Daily' <= 10 min: 
  * [ ] Stellen Sie sich dabei in den Kreis. 
  * [ ] Erzählen Sie reihum jeweils äußerst kurz, 
    * [ ] woran Sie in den letzten 45 min gearbeitet haben, 
    * [ ] bei welchen Hindernissen (Impediments) Sie noch Hilfe benötigen, 
    * [ ] was Sie in den nächsten 45 min tun werden.
* [ ] Der letzte Sprint dauert nur 60 Min inklusive Ergebnispräsentation. Er dient vornehmlich für Planung der Präsentation.
* [ ] Nach dem letzten Sprint gibt es 30 min Sprintreview.

Werden Sie ein gutes Team: Ein gutes Team versucht, so viel wie möglich zu erreichen. 
Ein gutes Team überfordert sich aber auch nicht.

**ProductBacklog**

---

1. Entwickeln Sie (mindestens) 2 Plausibilitätstest für die Daten.
2. Implementieren Sie den/die Plausibilitätstests.
3. Bestimmen Sie den Umgang mit Abweichungen.
4. Passen Sie die Inputdaten ggfls. entsprechend an.

---

11. Evaluieren Sie mögliche Visualisierung der Daten in Excel/LibreOfficeCalc.
12. Laden Sie die Daten in ein Sheet und visualisieren Sie sie mit der Grafik Ihrer Wahl.
13. Leiten Sie qualitative Aussagen über Verlauf und Auffälligkeiten ab.
14. Implementieren Sie Methoden, die das Minimum, das Maximum, die Spannweite, den
      Mittelwert und den Median für die Systolenwerte, die Diastolenwerte und die Pulswerte berechnet

---

21. Implementieren Sie Methoden, die die **durchschnittliche Abweichung (Varianz) vom**
      jeweiligen **_Mittelwert_** der Systolenwerte, der Diastolenwerte und der Pulswerte berechnet
22. Implementieren Sie Methoden, die die **durchschnittliche Abweichung (Varianz) vom**
      jeweiligen **_Median_** der Systolenwerte, der Diastolenwerte und der Pulswerte berechnet
23. Bewerten Sie den Unterschied der beiden durchschnittlichen Abweichungen (Varianzen).
24. Implementieren Sie Methoden, die die **Standardabweichung** der Pulswerte, 
      der Systolen- und der Diastolenwerte **vom** jeweiligen **Mittelwert** ermitteln.

---

31. Teilen Sie die Daten gemäß visueller Einteilung in Bereiche größer Gleichheit ein.
32. Berechnen Sie Minimum, Maximum, Spannweite, Mittelwerte, Median, durchschnittliche Abweichung und Standardabweichung für diese Bereiche.
33. Stellen Sie die Aussagen zu den einzelnen Bereichen gegenüber.

---

41. Implementieren Sie Methoden, die die Kovarianz für Systole zu Diastole, für Systole zu Puls und für Diastole zu Puls berechnen.
42. Implementieren Sie Methoden, die den Korrelationskoeffizienten für Systole zu Diastole, für Systole zu Puls und für Diastole zu Puls berechnen.
43. Ermitteln Sie, wie sich diese Werte zueinander verhalten.

---

51. Ermitteln Sie den DPMO (Defects per Million) Wert für die ursprüngliche Messreihe `dsp-alpha.xyz` mit ihren syntaktischen Fehlern und Unplausibilitäten.
52. Sagen Sie etwas über die Qualität dieser Messreihe im Vergleich zu SixSigma vom 3.4 DPMO aus.

---

**Anregungen:**

* Beim Verabreichung blutdrucksenkender Mittel pendeln sich die Werte -- nach Einschwingen auf die Dosis -- auf ein neues Niveau ein. Also sollte man erwarten, diese unterschiedlichen Level anhand verschiedener Minima, Maxima, Spannweiten, Mittelwerte und Mediane voneinander abgrenzen zu können.
* Medikamentös wird der Bluthochdruck mit drei sukkzessive 'hinzugeschalteten' Medikamenten behandelt: Zuerst mit einem einen Blutdrucksenker (hier Ramipril), dann mit einem Entwässerer (hier HCT) und schließlich mit einem Calucium-Präparat (hier Amlodipin). Versuchen Sie entsprechende Phasen zu finden. (Es ist nicht gesagt, dass diese genau erkennbar sind. Denn es gehört auch zur Therapie, die Dosis eines jeden dieser Medikamente im Verlauf zu steigern. Das wurde leider nicht mitprotokolliert.)

<!-- uebung::end -->

---

**Hinweis für Lehrerin**: nach Aufgaben 1.x bis 2.x neue Daten `dsp.alpha.ii.csv` mit Report ins Spiel bringen:

Szenario: 

* PO Rücksprache mit Produktion
* Differenzen in bereinigter Datengrundlage festgestellt.
* Produktion hat darum selbst einen Datenset im Format des Teams aufbereitet (dsp.alpha.ii.csv)
* Produktion hat Abweichungen beschrieben, gezählt und reportet. (dsp.alpha.ii-report.csv)
