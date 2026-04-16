<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 2a

#### 2a.I 
*Grundsätzliches Vorgehen, um zum Code zu kommen:* **quasi Bottom Up**

`/*`

* A) Schreibe den gewünschten / vorgegebenen Funktionsheader oben hin
* B) Schreibe das Returnstatement am Ende hin
* C) Schreibe die Funktion zur Berechnung/Erzeugung des Returnwerts vor das Returnstatement (Hier: Vorgegebener Konstruktor der Klasse Statistik)
* D) Konzipiere die Berechnungen der Konstruktorparameter, hier:
  * a) zähle die erfolgreichen Abschlüsse = Zähle Kunden mit Vertrragsdatum
  * b) berechne das Verhältnis von Interessenten zu erfolgreichen Abschlüssen, hier `Anzahl der erfolreichen Abschlüsse / Länge der Interessentenliste`
  * c) berechne die durchschnittliche Dauer bis zum Eintritt des Misserfolgs, hier: *bestimme für alle Kunden ohne Vertrag die Differenz zwischen Erstgesprächsdatum und Auswertungsdatum 31.03*
* E) Fülle den Teil zwischen Returnstratementberechnung und Funktionskopf aus. Nutze dabei genau die vordefinierten Methoden und Eigenschaften.

Kommentar: 

* In der Aufgabe soll auch die "durchschnittliche Dauer des Prozesses ermittelt werden, wenn er nicht zum Vertrag führt".
* Ein Interessent ist ein Interessent, wenn der Kontakt aufgenommen worden ist, frühestens am 1.3.
* Die Prozessdauer besteht aus den Tagen, die das Studio 'aktiv' an den Kunden 'verschwendet' hat.

`*/`

#### 2a.II 
Pseudocode

möglichst à la Python formuliert, Abweichungen davon folgen dem Aufgabenstil


```
Auswerten(liste: Interessent[]) : Statistik # vorgegeben, kein Python

  erfolgsanzahl=0
  misserfolgstage=0 

  for candidate in liste : # candidate ist implizit vom Typ Interessent
    if Empty(candiate.DatumVertrag) 
      lastcontact=candiate.DatumTraining
      if Empty(lastcontact) lastcontact=candiate.DatumGespraech
      if Empty(lastcontact) lastcontact=candiate.DatumKontakt
      # DateDiff(vorher,nachher)
      misserfolgstage+=DateDiff(candidate.DatumKontakt,lastcontact) 
    else :
      erfolgsanzahl+=1;

  erfolgZuInteresse=erfolgsanzahl/liste.Length;

  avgAufwand=0;
  if liste.Length>erfolgsanzahl: # DIV-by-Zero unterbinden
    avgAufwand=misserfolgstage/(liste.Length-erfolgsanzahl)

  return new Statistik(erfolgsanzahl, erfolgZuInteresse, avgAufwand)

```

Anmerkung: 

* Der ZPA-Lösungsvorschlag plottet noch die 'erfolgstage' mit. Die werden aber später zu keiner Berechnung herangezogen.
* Der ZPA-Lösungsvorschlag fragt zuerst die Existenz eines Gesprächsdatums ab. Nur wenn das nicht existiert, fragt sie die Existenz eines Trainingsdatums ab. In der Tabelle haben aber alle Einträge, die ein Trainingsdatum haben, auch ein Gesprächsdatum. Folglich geht der längere Zeitraum Kontaktdatum - Trainingsdatum niemals in die Zählung der 'misserfolgstage' ein. Die Abfrage hätte - wie hier umgesetzt - von hinten nach vorn erfolgen müssen. (Für diese Entdeckung an Genaro, 12ip/iv23, GSLDK)

### 2b Bewertung der Statistikaussagen im Hinblick auf Prozesserfolg:

- `statistik.AnzahlErfolg` gibt die Anzahl der tatsächlich geschlossenen Verträge wieder = absoluter Erfolg = als Qualitätsmaßtab allein keine Aussagekraft
- `statistik.AnteilErfolg` gibt das Verhältnis zwischen möglichen und realen Vertragsabschlüssen = relativer Erfolg
  - bei 1 hätte jeder Kontakt zu einem Vertrag geführt
  - bei 0 hätte kein Kontakt zu einem Vertrag geführt
- `statistik.AvgDauerAubbruch` ist der Aufwand, den das Studio in Misserfolge gesteckt hat: wäre es bei allen Kandidaten bis zum Probetraining gekommen, wäre die 'vergebene Mühe' seitens des Studios am größten. Wenig Aussagekraft als Maßstab für Prozessqualität.

### 2c Andere Kriterien zur Prozessbewertung:

* Quantifizierung der Qualität des Probetrainings (aus Kundensicht)
* Quantifizierung der Qualität des Probetrainings (aus Kundensicht)
* Nachbefragung der Nicht-Kunden, was gestört hat


