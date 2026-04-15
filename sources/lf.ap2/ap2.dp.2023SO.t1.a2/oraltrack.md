<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 2a

#### 2a.I 
*Grundsätzliches Vorgehen zur Lösung auf Konzeptpapier* **quasi Bottom Up**

`/*`

* A) Schreibe den gewünschten / vorgegebenen Funktionsheader oben hin
* B) Schreibe das Returnstatement am Ende hin
* C) Schreibe die Funktion zur Berechnung/Erzeugung des Returnwerts vor das Returnstatement (Hier: Vorgegebener Konstruktor der Klasse Statistik)
* D) Konzipiere die Berechnungen der Konstruktorparameter, hier:
  * a) zähle die erfolgreichen Abschlüsse = Zähle Kunden mit Vertrragsdatum
  * b) berechne das Verhaltnis von Interressenten zu erfolgreichen Abschlüssen, hier `Anzahl der erfolreichen Abschlüsse / Länge der Interessentenliste`
  * c) berechne die durchschnittliche Dauer bis zum Eintritt des Misserfolgs, hier: *bestimme für alle Kunden ohne Vertrag die Differenz zwischen Erstgesprächsdatum und Auswertungsdatum 31.03*
* E) Fülle den Teil zwischen Returnstratementberechnung und Funktionskopf aus. Nutze dabei genau die vordefinierten Methoden und Eigenschaften.

Kommentar: 

* In der Aufgabe soll auch die "durchschnittliche Dauer des Prozesses ermittelt werden, wenn er nicht zum Vertrag führt".
* Eine Interessent ist ein Interessent, wenn der Kontaktaufgenommen worden ist, frühestens am 1.3
* Die Prozesddauer sind die Tage, die das Studio an den Kunden 'verschwendet' hat

`*/`

#### 2a.II 
Pseudocode

C++-stylig, weil vorgegebene Klassenzuweisung etwas mit Pythongruppierung kollidiert (s. `:`)


```
Auswerten(liste: Interessent[]) : Statistik /* wie vorgegeben */
{
  erfolgsanzahl=0
  misserfolgstage=0 

  for (candidate : Interessent  in liste) {
    if Empty(candiate.DatumVertrag) { 
      lastcontact=candiate.DatumTraining;
      if (!(lastcontact) lastcontact=candiate.DatumGespraech;
      if (!(lastcontact) lastcontact=candiate.DatumKontakt;
      misserfolgstage+=DateDiff(lastcontact,candidate.DatumKontakt);
    }
    else
      erfolgsanzahl+=1;
  }

  erfolgZuInteresse=erfolgsanzahl/liste.Length;
  avgAufwand=misserfolgstage/(liste.Length-erfolgsanzahl);

  statistik = Statistik(erfolgsanzahl, erfolgZuInteresse, avgAufwand);
  return statistik;
}
```
### 2b Bewertung der Statistikaussagen im Hinblick auf Prozesserfolg:

- `statistik.AnzahlErfolg` gibt die Anzahl der tatsächlich geschlossenen Verträge wieder = absoluter Erfolg = als Qualitätsmastab allein keine Aussagekraft
- `statistik.AnteilErfolg` gibt das Verhältnis zwischen möglichen und realen Vertragsanbschlüssen = relativer Erfolg
  - bei 1 hätte jeder Kontakt zu einem Vertrag geführt
  - bei 0 hätte kein Konakt zu einem Vertrag geführt
- `statistik.AvgDauerAubbruch` ist der Aufwand, den das Studio in Misserfolge gesteckt hat: wäre es bei allen Kandidaten bis zum Probetraining gekommen, wäre die 'vergebene Mühe' seitens des Studios am größten. Wenig Aussagekraft als Maßstab für Prozessqualität.

### 2c Andere Kriterien zur Prozessbewertung:

* Quantifizierung der Qualität des Probetrainings (aus Kundensicht)
* Quantifizierung der Qualität des Probetrainings (aus Kundensicht)
* Nachbefragung der Nicht-Kunden, was gestört hat


