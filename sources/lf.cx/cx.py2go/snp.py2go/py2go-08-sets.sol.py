# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

exercise="py2go-08"
print(f"solution for exercise {exercise}:")

'''
1. Erzeugen Sie eine Menge (Set). Weisen Sie ihr die Elemente 'rot', 'blau', 'grün' 
   zu und geben Sie die Menge aus.
2. Geben Sie dann jedes Element einzeln aus
3. Fügen Sie Ihrem Set nachträglich das Element 'schwarz' hinzu und geben Sie ihn erneut aus.
4. Fügen Sie Ihrem Set nachträglich (noch einmal) das Element 'rot' hinzu und geben 
   Sie ihn erneut aus. Was fällt auf?
5. Erstellen Sie eine Sichtheitskopie dieser Menge. 
   Entfernen Sie das Element 'schwarz' aus der Originalmenge.
   Geben Sie Original und Kopie je aus.
6. Erzeugen Sie eine zweite Menge mit den Elementen 'rot', 'gelb', 'magenta' und geben Sie diese aus.
7. Geben Sie die Schnittmenge beider Mengen aus.
8. Geben Sie die Vereinigungsmenge beider Mengen aus.
9. Geben Sie die Differenzmenge(n) der beiden Mengen aus. Warum muss man beide Richtungen beachten?
A. Vergleichen Sie Original und Sicherheitskopie zuerst mit der Differenzmengemethode.
   Vergleichen Sie sie dann mit dem Gleichheitsoperator, dann mit dem Kleiner-als- 
   und dann mit dem Größer-als-Operator.
   Geben Sie die Ergebnisse jeweils aus.
B. Geben Sie die Anzahl der Elemente der Originalmenge aus.
C. Löschen Sie alle Elemente der Originalmenge. Geben Sie die veränderte Menge 
   und ihre Mächtigkeit (Anzahl) aus.

Hintergrund:

Mengen haben unveränderliche Elemente und sind unsortiert. Sie werden - gewissermaßen 
- wie Dictionaries ohne Key gebildet
  set_one={"v7","v2","V4"}
Trotzdem kann man über die Elemente wie in dictioniaries mit einer for-Schleife iterieren
  for v in set_one:
    print(v)
Allerdings kann man die einzelnen Elemente nicht verändern bzw. überschreiben, 
nur Löschen und neu hinzufügen.
  set_one.discard("V4")
  set_one.add("v4")
Die Menge als ganzes kann man auch leeren
  set_one.clear()
Mengen kann man kopieren und für verschiedene Menge die Schnittmenge, die Vereinigungsmenge 
und/oder die Differenzmenge bilden. (Die Differenzmenge ist die Menge aller Elemente, die 
in Menge A enthalten sind, aber nicht in Menge B.)
  set_copy=set_one.copy()
  set_two={"v7","v1","v3"}
  set_one.intersection(set_two)
  set_one.union(set_two)
  set_one.difference(set_two) ergibt etwas anderes als set_two.difference(set_one)
Schließlich kann man Mengen auch mit den üblichen Vergleichsoperatoren ==, >=, <= vergleichen
Die Anzahl der Elemente, ihre Mächtigkeit, liefert der übergeordneten Längenfunktion 
  len(set_one)

Alle Elemente einer Menge löschen kann man mit der Methode clear
  set_one.clear()

'''
print("Lösung zu Aufgabe 8.1:")
set_one={"rot","blau","grün"}
print(set_one)

print("---\nLösung zu Aufgabe 8.2:")
for elem in set_one:
  print(elem)

print("---\nLösung zu Aufgabe 8.3:")
set_one.add("schwarz")
print(set_one)

print("---\nLösung zu Aufgabe 8.4:")
set_one.add("rot")
print(set_one)

print("---\nLösung zu Aufgabe 8.5:")
set_copy=set_one.copy()
set_one.discard("schwarz")
print(set_one)
print(set_copy)

print("---\nLösung zu Aufgabe 8.6:")
set_two={"rot","gelb","magenta"}
print(set_two)

print("---\nLösung zu Aufgabe 8.7:")
print(set_one.intersection(set_two))
print("---\nLösung zu Aufgabe 8.8:")
print(set_one.union(set_two))

print("---\nLösung zu Aufgabe 8.9:")
print(set_one.difference(set_two))
print(set_two.difference(set_one))

print("---\nLösung zu Aufgabe 8.A:")
print(set_copy.difference(set_one))
print(set_one==set_copy)
print(set_one>set_copy)
print(set_one<set_copy)

print("---\nLösung zu Aufgabe 8.B:")
print(len(set_one))

print("---\nLösung zu Aufgabe 8.C:")
set_one.clear()
print(set_one,"hat nun",len(set_one),"Elemente")