# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

exercise="py2go-10"
print(f"solution for exercise {exercise}:")

'''
1. Setzen Sie die Variable nahrung auf einen der Begriffe
   Apfel, Birne, Rettich, Zwiebel, Steak oder Hack.
2. Erzeugen Sie mittels eines Case-Konstuktes einen Klassifikator, der
   a. zu Apfel oder Birne die Klasse Obst 
   b. zu Rettich oder Zwiebel die Klasse Gemüse
   c. zu Steak oder Hack die Klasse Fleisch
   ausgibt.


Hintergrund:

Natürlich kann man zu Tieren bzw. Pflanzen mittels mehrerer if-elif-Statements die Klassen nennen:

tier="Eidechse"
if (tier == "Adler"):
  print(f"Ein {tier} ist ein Vogel")
elif (tier == "Papagei"):
  print(f"Ein {tier} ist ein Vogel")
elif (tier == "Löwe"):
  print(f"Ein {tier} ist eine Raubkatze")
...
elif (tier == "Schlange"):
  print(f"Eine {tier} ist ein Reptil")
else:
   print(f"Keine Ahnung, was ein(e) {tier} ist.")


Aber das ist sperrig.

Für eine elegantere Schreibweise ist das match-case-Konstrukt erfunden worden

tier="Eidechse"

match tier:
  case "Adler" | "Papagei":
    print(f"Ein {tier} ist ein Vogel")
  case "Löwe" | "Tiger":
    print(f"Ein {tier} ist eine Raubkatze")
  case "Eidechse" | "Schlange":
    print(f"Eine {tier} ist ein Reptil")
  case _:
    print(f"Keine Ahnung, was ein(e) {tier} ist.")

Zum Verständnis: 

- Das Pipesymbol | wird hier als logisches Oder gelesen.
- Der Unterstrich meint den Wert, auf den die Variablke tier gerade zeigt.

'''
nahrung="Apfel"

match nahrung:
  case "Apfel" | "Birne":
    print(f"Ein {nahrung} ist Obst")
  case "Rettich" | "Zwiebel":
    print(f"Ein(e) {nahrung} ist Gemüse")
  case "Steak" | "Hack":
    print(f"Ein {nahrung} ist Fleisch")
  case _:
    print(f"Keine Ahnung, was {nahrung} ist.")

