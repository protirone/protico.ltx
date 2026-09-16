#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

# Lesehinweis: 
# In spitzen Klammern schreibe ich stets Tools und ihre Parameter.
# Die Tools stellt Ihnen Betriebssystem zur Verfügung.
#
# Beispiel: 
# Rufen Sie <echo dies> auf, meint, dass Sie an der
# Kommandozeile echo dies eingeben. Wo sich das Tool, hier
# <echo> bei Ihnen befindet, können Sie mit <which echo> erfragen

EXC=sh2go-05
echo "executing Uebung $EXC"

# (1) Weisen Sie einer Variable das heutige Datum zu. Nutzen Sie dafür das Tool <date> 
# (2) Lassen Sie den Wert Ihrer Variable in eine Datei 'heute.txt' schreiben.

# Hintergrund: 
#
# (A) <date> gibt das heutige Datum aus.
# (B) Das Format kann man per Parameter <date +'%Y-%m-%d'> bestimmen
# (C) Welche Parameter es gibt, liefert Ihnen <data --help>
# (D <cat DateiX> liest DateiX von der Platte und gibt sie zeilenweise wieder aus

# Sie müssen zur Lösung allerdingsa einmal um die Ecke denken:
# a) Zuerst müssen Sie den Befehl date ausführen lassen. Das tun Sie, indem sie
#    den Befehl in eine Befehlszeile eintragen.
#    <date +'%Y-%m-%d'>
# b) Tatsächlich wollen Sie hier aber das Ergebnis des Date-Befehls in einer Variable speichern.
#    Also müssten Sie den Date-Befehl einer Variable zuweisen. Das liest die Bash aber so,
#    dass Sie der Variable den Befehlstext zuweisen.
#    <MYDATE=date +'%Y-%m-%d'>
# c) Also müssten Sie die bash überreden, den Datebefehl erst auszuführen und das Ergebnis
#    der Variable zuzuweisen. Dazu setzen Sie den Befehl nach dem zuweisenden Glecihheitszeichen
#    in Backticks:
#    <MYDATE=`date +'%Y-%m-%d'`>
#    Oder Sie nutzen die neue Technik, bei der ein $ die Evaluation anstößt
#    und Klammern abzeigen, was ausgewertet werden soll
#    <MYDATE=$(date +'%Y-%m-%d')>
#    
