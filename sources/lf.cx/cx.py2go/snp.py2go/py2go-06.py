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
A. Weisen Sie die Typveränderungen durch geeignete Ausdrücke nach.
B. Weisen Sie danach dem ersten Element der Liste das erste des Tupels zu und testen Sie auf Gleichheit.
C. Weisen Sie dann alle Elemente Ihres Tupels einer zweiten Liste zu und dann alle Element Ihre zweiten Liste der ersten Liste zu.
D. Zählen Sie das Vorkommen des ersten Elements der zweite Liste in der ersten Liste.
E. Weisen schließlich die zweite Liste der ersten als Element zu.
F. Weisen Sie schließlich dem ersten Element des Tupels das erste Element der Liste zu.
    Beschreiben Sie, was passiert? 
    und testen Sie auf Gleichheit

Hintergrund:

Der Zuweisungsoperator ist wieder das einfache Gleichheitszeichen.

* Ein 'String' ist ein Buchstaben-Zahlenfolge, die in einfache oder doppelte Anführungszeichen eingekleidet ist.
* Ein 'Integer' gibt es in 3+x Versionen:
  * als Dezimalzahl = einfache Folge von 0 - 9 :- 42
  * als Binärzahl = beginnend mit dem Präfix '0b' gefolgt von beliebig vielen 0  oder 1 :- 0b101010
  * als Hexadezimalzahl = beginnend mit dem Präfix '0x' gefolgt von beliebig vielen 0-9,A-F : 0x2A
* Eine 'Float'zahl besteht aus einer Folge von beliebig vielen 0 - 9 - einmal durch einen Punkt unterprochen. 42.24
* Eine Bool-'Zahl' kann die Werte 'True' oder 'False' annehmen.
  * Zusatz: ein leer String evaluiert zu boolschen Wert 'False'.
  * Zusatz: eine 0x00 oder 0b00 oder 0 evaluiert zu boolschen Wert 'False'.

* Eine Liste 
  * enthält als Element obige Werte (oder Listen oder Tupel)
  * wird markiert durch eckige Klammern, in denen die Element durch Kommata getrennt sind: [ 1, 2, '3']
  * erlaubt die Zugriff auf seine Element durch Indizes:
    * my_l= [ 1 , 2, 3 ] 
    * print(my_l) ergibt [ 1 , 2, 3 ]
    * print(my_l[2]) ergibt 3
  * erlaubt die Änderung einzelner Element durch neue Zuweisungen
    * my_l[0]= 'Häh?'
    * print(my_l) ergibt jetzt ['Häh?', 2, 3]
  * kann über die Methode *append* um ein Element erweitert werden:
    * my_l.append(0xFA)
    * print(my_l) ergibt jetzt ['Häh?', 2, 3, 250]
  * kann über die Methode *remove* um ein Element erweitert werden:
  * kann über die Methode *extend* um die Elemente eine anderen Liste erweitert werden
  * bietet die Methoden
    * len() = liefert die Länge der Liste
    * count() = liefert die Anzahl der Vorkommen des übergebenen Elements
    * sort() = sortiert die Werte in der Liste nach ihrer Wertigkeit

* Ein Tupel 
  * enthält als Element obige Werte (oder Listen oder Tupel)
  * wird markiert durch runden Klammern, in denen die Element durch Kommata getrennt sind: () 1, 2, '3')
  * beschützt seine Elemente vor Veränderungen - die nachträgliche Löschen, Ändern oder Erweitern ist nicht zulässig.
  * bietet die Methoden
    * len() = liefert die Länge der Liste
    * count() = liefert die Anzahl der Vorkommen des übergebenen Elements
    * index() = die Position des ersten Vorkommens eines Elements im Tupel

* Mit der allgemeinen Funktion type() erfährt man den Typ des Wertes, auf den die Variable zeigt:
  * myone=1
  * print(type(myone)) ergibt <class 'int'>

'''

