# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

exercise="py2go-12"
print(f"solution for exercise {exercise}:")

'''
1. Belegen Sie eine Liste mit den Elementen "one", "two", "three".
2. Konstruieren Sie eine Schleife, dessen Schleifenkörper
   - unabhängig vom konkreten Füllgrad Ihrer Liste - auf jeden Fall einmal
   ausgeführt wird.
3. Löschen Sie alle Elemente bis auf eines.
4. Geben Sie jedes Mal die Anzahl der Listenelemente aus.

Hintergrund:

Andere Sprachen kennen die while-Schleife und die do-while-Schleife.
In der while-Schleife wird die Abbruchbedingung zuerst überprüft (s. py2go-10), 
in der do-while-Schleife erst am Ende. Das bedeutet, dass der Schleifenkörper
(= die Befehle, die in der Schleife abgearbeitet werden) in der do-while-Schleife 
mindestens einmal abgearbeitet wird, während die Befehle im Schleifenkörper der 
reinen while-Schleife u.U. nicht abgearbeitet werden, nämlich immer dann, wenn 
die Abbruchbedingung schon am Anfang wahr ist.

Python kennt nur die while-Schleife.

Allerdings kann man ein do-while-Schleife nachbauen, in dem man 
a.) die Abbruchbedingung auf wahr setzt (Endlosschleife).
b.) im Schleifenkörper eine eigenen zweiten Abbruchtest einbaut und
c.) mit einem break aus der Schleife rausspringt, wenn der eigene  Abbruchtest
    wahr wird.

num=100
while (True):
  print(f"Zähler steht auf {num}")
  if (num==42):
    break
  num-=1
'''

my_list=["one","two","three"]
while(True):
  my_list_len=len(my_list)
  print(f"meine Liste hat noch {my_list_len} Element(e)")
  if (my_list_len<=1):
    break
  my_list.pop()
