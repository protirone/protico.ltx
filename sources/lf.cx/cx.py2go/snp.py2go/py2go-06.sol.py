# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

'''
1. Weisen Sie einer Variable 'my_int' eine Integerzahl zu
2. Weisen Sie einer Variable 'my_float' eine Floatzahl zu.
3. Weisen Sie einer Variable 'my_bool' einen Wahrheitswert zu.
4. Weisen Sie einer Variable 'my_string' Ihren Vornamen zu.
5. Weisen Sie einer Variable 'my_list' eine Liste mit den Elementen "Z1", 1, "Z2" und 2 zu.
6. Weisen Sie einer Variable 'my_tupel' einen Tupel mit den Elementen "Z1", 1, "Z2" und 2 zu.
7. Testen Sie alle Variablen auf Gleichheit mit dem Wert, den Sie zugewiesen haben. 
   Geben Sie das Ergebnis aus.
8. Testen sie alle Variablen mit allen anderen auf Gleichheit. Geben Sie das Ergebnis aus.
9. Weisen Sie jetzt jeder Variable den Wert einer anderen zu.
   wiederholen Sie 8 mit den ursprünglich zugewiesen Werten.
10. Weisen Sie danach dem ersten Element der Liste das erste des Tupels zu 
    und testen Sie auf Gleichheit
11. Weisen Sie schließlich dem ersten Element des Tupels das erste der Liste zu.
    Beschreiben Sie, was passiert? 
    und testen Sie auf Gleichheit

Hintergrund:

Der Zuweisungsoperator ist das einfache Gleichheitszeichen.



Andere Sprachen weisen einer Variable eine spezifische Speicherstelle zu und
vermerken den Typ, der zu dieser Speicherstelle gehört. Variable und
Speicherstelle bleiben verbunden (solange Sie nicht mit Pointerarithmetik 
manuell eingreifen.) [Statische Typedeklaration]

Python abstrahiert davon einen Schritt: [Dynamische Typedeklaration]

* Wenn sie einer Variable einen (bisher nicht verwendeten) Wert zuweisen, erzeugt 
  Python intern ein Objekt mit diesem Wert.
* Dann weist Python Ihrer Variable als Wert die Speicheradresse des Objektes zu.
* Fragen Sie nach dem Wert der Variable, liest Python den aus dem Objekt aus,
  ohne dass Sie etwas dafür tun müssten.
* Weisen Sie dann einer neuen Variable den schon verwendeten Wert zu, erzeugt
  Python kein neues Objekt, sondern weist Ihrer neuen Variable einfach die
  Speicheradresse des Objektes mit dem schon verwendeten Wert zu
* Die angelegten Objekte haben eine ID. Und die kann mit dem Operator id(VAR)
  abfragen, wobei VAR Ihre Variable im Quelltext ist.

Tests auf gleich und Ungleichheit schreiben Sie in Python als if-statement:

- Ein if-Statement startet mit der if-Clause (`if(TEST)`) gefolgt von enem Doppelpunkt.
- Ein Test ist ein Vergleich, der zu einem der Wahrheitswerte True oder False
  ausgewertet wird.
- Ergibt der Test den Wert 'True', werden die nachfolgenden Befehle ausgeführt,
  die nach dem Test um eine Einheit (2 Blanks oder 1 Tab oder 4 Blanks oder ...)
  eingerückt sind.
- Wollen Sie Befehle ausführen lassen, wenn der Test scheitert,
  hängen sie noch (uneingerückt) eine else-Zeile und ein oder mehrere
  eingrückte Befehle an.
- TESTs sind Vergleichsoperationen wie 
  - gleich '=='
  - ungleich '=='
  - größer '>'
  - kleiner '<'

Die weiter hineinkriechen wollen, mögen die Frage beantwortet, was passiert,
wenn man nach einer Zuweisung die ids nicht neu ermittelt. Kommentieren Sie
ihre entsprechenden Zeilen aus und probieren sie es aus.

'''
