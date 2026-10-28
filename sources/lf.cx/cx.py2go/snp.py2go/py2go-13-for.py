# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

exercise="py2go-13"
print(f"solution for exercise {exercise}:")

'''
1. Belegen Sie eine Liste mit den Elementen "one", "two", "three".
2. Geben Sie die Liste am Anfang einmal komplett aus.
3. Iterieren Sie mit einer for-Scheife über alle Elemente der Liste und geben Sie sie einzelnd aus.
4. Nach der Ausgabe des Strings ersetzen Sie den String durch die entsprechende Zahl.
5. Geben Sie die veränderte Liste am Ende noch einmal komplett aus.
6. Konstruieren Sie dann ein entsprechendes Dictionary, iterieren Sie mit einer
   for-Schleife über alle Wertepaare und ersetzen Sie die Stringwerte
   durch Zahlen, ohne die Schlüssel zu ändern

Hintergrund:

Die for-Schleife dient zum Durchwandern iterierbare Objekte, z.B. Listen oder Dictionaries:

* for element in liste: 
    print(f"{element}")

* for key,val in dictionary.items():
    print(f"{key} -> {val}")

Ein Liste ist so iterierbar, ein Dictionary erst mittels der Methode "items()"

Um in einem Dictionary den Wert zu einem Schlüssel zu ändern, benutzen Sie
den schon erfragten Schlüssel:

  dictionary[key]="neuer Wert"

In einer Liste müssen Sie dazu erst den Index des aktuellen Elements erfragen

  index=liste.index(element)
  liste[index]="neuer Wert"
  
'''

