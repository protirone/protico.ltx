# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

exercise="py2go-09"
print(f"solution for exercise {exercise}:")

'''
1. Belegen Sie zwei Variablen mit je einer Zahl. Vergleichen Sie beide maschinell. 
   Wenn die erste Zahl im Vergleich größer ist als die zweite, geben Sie aus: 1. größer als 2.
   Wenn die zweite Zahl im Vergleich größer ist als die erste, geben Sie aus: 1. kleiner als 2.
   Wenn die erste Zahl gleich der zweiten ist, geben Sie aus: 1. gleich 2.
   Nutzen Sie dazu nur einfdache 'Wenn-Dann'-Konstrukte.
2. Verdichten Sie Ihre Lösung von Aufgabe 1, in dem Sie zwei wenn-dann-sonst-Konstrukte verschachteln.
3. Verdichten Sie Ihre Lösung von Aufgabe 2, in dem Sie in ein wenn-dann-sonst-Konstrukt 
   mehrere Abfragen und REaktionen hinterinander schachteln.
4. Bauen Sie Ihr Programm so um, dass Sie alle Fälle durch Auskommentieren testen können
5. Belegen Sie eine Variable mit Ihrem Vornamen, die zweite mit Ihrem Nachnamen.
   Vergleichen Sie die Variablen hinsichtlich der Größe. Erklären Sie, wie das Ergebnis entsteht.


Hintergrund:

Auch Python bietet Vergleichsoperatoren
* '=='  :- ist gleich
* '>='  :  ist größer oder gleich
* '>'   :  ist größer
* '<='  :  ist kleiner oder gleich
* '<'   :  ist kleiner

Vergleichen kann man Variablen desselben Typs. Was als faktisch größer oder kleiner gewertet 
wird, hängt vom Typ ab. Auswertet werdenn Vergleiche die Wahrheitswerte 'True' bzw. 'False'

Als Reaktion auf einen Vergleich soll in der Regel eine Aktion, ein Kommando folgen. Solche
Verbindungen stellt (z.B.) das Wenn-Dann- bzw. if-then-Stetemant her. Hier der syntaktische Aufbau

if (24 > 42):
    print("24 ist größer als 42")

Natürlich kann man mehrere if-Statements hintereinander schreiben:

if (24 > 42):
    print("24 ist größer als 42")
if (24 < 42):
    print("24 ist kleiner als 42")

Das kann man verdichten, in dem man eine Wenn-Dann-Sonst-KOnstruktur bzw. 'if-then-else'-Statement benutzt:

if (24 > 42):
    print("24 ist größer als 42")
else:
    print("24 ist kleiner als 42")

Außerdem kann man mehrere if-Statements mit else-if-Verbindungen (= elif) verschalten:

if (24 < 42):
    print("24 ist kleiner als 42")
elif (25 < 42):
    print("25 ist kleiner als 42") 
elif (26 < 42):
    print("25 ist kleiner als 42") 
else:
    print("andere Zahlen können größer oder kleiner als 24 sein")

'''


num_a=42
#num_a=24
num_b=24
#num_b=42


print(f"Lösung für Aufabe 9.1:")

if (num_a > num_b):
    print(f"1. Zahl ({num_a}) größer als 2. Zahl ({num_b})")
if (num_a < num_b):
    print(f"1. Zahl ({num_a}) kleiner als 2. Zahl ({num_b})")
if (num_a == num_b):
    print(f"1. Zahl ({num_a}) gleich 2. Zahl ({num_b})")

print(f"Lösung für Aufabe 9.2:")

if (num_a >= num_b):
  if (num_a > num_b):
    print(f"1. Zahl ({num_a}) größer als 2. Zahl ({num_b})")
  else:
    print(f"1. Zahl ({num_a}) gleich 2. Zahl ({num_b})")
else:
  print(f"1. Zahl ({num_a}) kleiner als 2. Zahl ({num_b})")


print(f"Lösung für Aufabe 9.3:")

if (num_a > num_b):
  print(f"1. Zahl ({num_a}) größer als 2. Zahl ({num_b})")
elif (num_a < num_b):
  print(f"1. Zahl ({num_a}) kleiner als 2. Zahl ({num_b})")
else:
  print(f"1. Zahl ({num_a}) kleiner als 2. Zahl ({num_b})")

print(f"Lösung für Aufabe 9.5:")

name="Reincke"
prename="Karsten"

if (name<prename):
  print(f"{name} ist kleiner als {prename}")
elif (name>prename):
  print(f"{name} ist größer als {prename}")
else:
  print(f"{name} ist gleich {prename}")

print("größer/kleiner bei Strings gemäß alphabetischer Sortierung")
