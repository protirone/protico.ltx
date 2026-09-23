# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

'''
1. Erzeugen Sie ein Dictionary, in dem die Nachnamen von Schülerinnen
   Ihrer Klasse jeweils auf den Vornamen der entsprechenden Schülerin verweise.
   Geben Sie dieses Dictionary aus.
2. Sortieren Sie dieses Dictionary nach Nachnamen und geben Sie es erneut aus.
   Geben Sie dabei alle einzelnen Modifikationen gesondert aus.
3. Sortieren Sie das Dictionary nach Vornnamen und geben Sie es erneut aus.
   Geben Sie dabei alle einzelnen Modifikationen gesondert aus.
   Beobachten Sie den Unterschied!
4. Erweitern Sie das Dictionary um ein Klassenbuch in Form einer Liste hinzu,
   das für jede Schülerin deren Stammdaten in einem Tupel erfasst. 
   Die Stammdaten seien Name, Vorname, Klasse und Lernfeld. 
   Geben Sie dieses erweiterte Dictionary aus.
5. Begründen Sie, warum es eine schlechte Idee ist, die Stammdaten so zu erfassen.
6. Geben Sie die Namen aller Schülerinnen Dictionary einzelnd aus.
7. Geben Sie die Stammdaten aller Schülerinnen einzelnd aus.
8. Erweitern Sie Ihr Dictionary um ein weiteres Dictionary, das alle Lernfelder
   enthält, die Ihre Klasse jemals besucht hat und noch besuchen wird.

Hintergrund:

Python kennt kein Arrays im traditionellen Sinne! An deren Stelle kann man in Python 
Listen oder Tupels nutzen.

Ein assoziatives Array im traditionellen Sinne heißt bei Python 'dictionary'. Es besteht aus
Schlüssel-Wert-Paaren:

* Schlüssel sind immer Strings. 
* Werte können Zahlen, Strings, Listen, Tupels und wieder Dictionaries sein. 


Ein leeres Dictionary wird erzeugt, indem man einer Variable

a.) eine 'leere Menge' zuweist und diese schrittweise befüllt
    my_animals={}
    my_animals["cat1_name"]="Lola"
    my_animals["cat1_age"]=1.6
    my_animals["cat2_name"]="Emmi"
    my_animals["cat2_age"]=1.6
    my_animals["dog"]="Crispie"
    my_animals["dog_age"]=2.7

oder

b) direkt mit den Schlüssel-Wert-Paaren initialisiert: sie werden in gescxhweifte Klammern gesetzt 
   und mit Kammata von einander getrennt.
    my_animals={
      'cat1_name': 'Lola', 
      'cat1_age': 1.6, 
      'cat2_name': 'Emmi', 
      'cat2_age': 1.6, 
      'dog': 'Crispie', 
      'dog_age': 2.7}

Auf die Einträge eines Dictionaries greift man mit den Schlüsseln zu. Über die kann
man die bestehenden Werte auch ändern:

  my_animals["cat2_name]="Emmili"

Greift man auf einen nicht im Dictionary enthaltenen Schlüssel, erhält man einen Fehler.

Die Funktion <sorted> gibt generell eine sortierte Liste aller Werte eines iterierbaren Objektes zurück.
Sie sortiert nicht die Ausgangsdaten. 

Eine Dictionary bringt die Methoden '.items()' und '.keys()' mit, die aus einem Dictionary
ein iterierbares Objekt erzeugen (Hier: eine Liste mit Tupeln):

* .items() erzeugt eine Liste von Tupeln, in denen jeweils die Key und Value stehen
* .keys() erzeugt eine Liste, die alle Keys enthält.

Auf diese Ergebnisse kann man die Funktion sorted anwenden.

die Funktion 'dict' macht dann aus dem Ergebnis der Sortierung wieder ein Dictionary


Über ein Dictionary iteriert man (u.a.) mit einer for-Schleife

dic={}
for key in dic:
   print(key,dic{key}) 
'''
