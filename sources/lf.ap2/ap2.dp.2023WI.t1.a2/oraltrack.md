<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->



### 2a

Zwei Vorteile bei der Nutzung von BPMN sind

- Vorgänger und Nachfolger von Arbeitsschritten wird transparent
- Zuständigkeiten werden deutlich

### 2b 

Anmerkungen:

* Gesagt wird, die Winzerin suche sich MO - SA pro Tag je ein neues Feld aus. Das zu modellieren, bläht das Diagramm auf. Deshalb verkürze ich das auf einen Prozessschritt *Feldauswahl*.
* Die Büroarbeit der Winzerin ist ihre Defaulttätigkeit, wenn nichts anderes ansteht. Das muss modelliert werden:
  * Weg 1: eine XOR-Verzweigung mit bedingten Zweigen und Defaultfall. (Vorteil: übersichtlich. Nachteil: IHK-BPMN-Symbole enhaltern nicht die aus der BPMN-Spezifikation, die man dazu braucht.) {Dies ist der Weg, den die IHK geht}
  * Weg 2: 2 verschachtelte XOR-Verzweigung. (Vorteil: angegebene Symbole bilden das ab. Diagramm wird komplexer) {meine Lösung}
* Der reine Aufgabentext erwähnt nicht, dass die Mitarbeiter tatsächlich etwas tun. Sie werden nicht beauftragt. Modlelliert werden soll streng genommen nur das Tun der Winzerin. Praktisch denken viele Lösungen diesen Aspekt mit. Meine Lösung bildet ab, wie dass dann korrekt aussehen müsste.

s. diagrams.pdf


### 2c

Andere Darstellungen von Geschäftswprozessen und ein jeweiliges Unterscheidungsmerkmal sind:

- eEPK (erweiterte) Ereignisgesteuerte Prozesskette:
  - vermerkt vor und nach jeder Aktion den Ausgangs- und den erreichten Zustand
- Aktivitätsdiagramm (UML):
  - gruppiert die Aktivitäten top/down in 'Lanes' für Akteure
  - erlaubt explizite Bedingungen

### 2d

Der Prozess könnte begründet wie folgt verbessert werden:

1. Die Winzerin entscheidet sich pro Tag für eine Aktion. Was aber, wenn mehrere Aktionen sachlich geboten sind? Sie sollte bei jeder Untersuchung mehrere Aktionen anstoßen können. (Mache aus 2. XOR inklusives OR)
2. Die Prüfung erfolgt - unabhängig von Jahreszeit und Wetter - jeden Tag. Vielleicht wäre je nach Jahreszeit und Wettervoraussage eine wöchtenliche Kontrolle sinnvoll (Resourceneinsparung).
