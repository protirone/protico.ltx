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

EXC=sh2go-22
echo "executing Uebung $EXC"

# (1) Erzeugen Sie eine CSV-Datei mit dem Inhalt
#       Z1F1, Z1F2, Z1F3, Z1F4, active
#       Z2F1, Z2F2, Z2F3, Z2F4, inactive
#       Z3F1, Z3F2, Z3F3, Z3F4, active
#       Z4F1, Z4F2, Z4F3, Z4F4, inactive
# (2) Lesen Sie den Inhalt mit <cat> zeilenweise ein und geben Sie mit <awk>
#     nur bei den aktiven Zeilen das erste und das dritte Feld
#     in umgekehrter Reihenfolge aus.
# (3) Lassen Sie dann im nächsten Durchgang einen Bindstrich zwischen allen
#     Feldern ausgeben.
# (4) Lassen Sie schließlich im nächsten Durchgang zwischen allen Feldern ein Komma ausgeben.
# (5) Unterbinden Sie das Einfügen von Blanks bei print indem Sie
#     stattdessen die C-String-Formatierung printf("%s%s",$1,$2)  nutzen
# (6) Bauen Sie dann die gleichen Funktionalität mit <grep> und <sed> nach.

# Hintergrund:

# <awk> liest die Zeilen von stdin (eingelesen von <cat> und mit <|> an <awk>)
# führt einen Test auf die Zeile aus und arbeitet im Erfolgsfall einen
# Modifikationsbefehl auf die Zeile aus. Intern teilt <awk> jede Zeile in n-Felder, 
# wobei es als Trenner Blanks oder das an der Kommandozeile übergebene 
# Trennungssymbol auswertet.
# Beispiel:
#
# <echo -e "11 12 13\n21 22 23" | awk '{print $1, $03, $2}'>
# ergibt die Zeilen
#   11 13 12
#   21 23 22

# Soll statt des Blanks das Komma als Trenner fungieren, gibt man
# <awk> das Trennzeichen auf der Komanndozeile mit

# <echo -e "11,12,13\n21,22,23" | awk -F, '{print $1, $03, $2}' >
# ergibt wieder die Zeilen
#   11 13 12
#   21 23 22


# Zweck von <awk> ist also: 
# Aus Zeilen, die einem Muster folgen, einzelne Felder rauszusuchen und in 
# anderer Reihenfolge (modizifiert) wieder zusammenzusetzen.

# Zu dem kann <awk> die Zeilen auf die Erfüllung von Bedingungen testen.
# Die Bedingungen werden als REGEX geschrieben und in Slashes 
# dem Ausführungsbefehl vorangestellt.

# Beispiele

# <echo -e "11,12,13\n21,22,23" | awk -F, '/11/{print $2}'> ergibt 12
# <echo -e "11,12,13\n21,22,23" | awk -F, '/[1][0-9]/{print $2}'> ergibt 12
# <echo -e "11,12,13\n21,22,23" | awk -F, '/[0-9][0-9]/{print $2}'> ergibt 12 \n 22


# Zusatzhinweise:
# - awk kann noch viel mehr. Lesen Sie dazu z.B. 
#   https://openbook.rheinwerk-verlag.de/shell_programmierung/shell_015_003.htm
# 
# - $0 ist bei awk immer die eingelesene Zeile als Ganzes
#
# - Um das Herausnehmen von Teilen einer Zeile mit sed zu programmieren,
#   nutzen Sie die Klammerfunktion im Regex und geben Sie im Ersetzungsteil
#   die Nummer mit \n an:
# Beispiel:

# <echo -e "11,12,13\n21,22,23" | sed "s/\([0-9][0-9]\),\([0-9][0-9]\),\([0-9][0-9]\)/\2/">
# ergibt auch 12 \n 22

