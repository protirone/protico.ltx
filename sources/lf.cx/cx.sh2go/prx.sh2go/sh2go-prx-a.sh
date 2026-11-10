#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC=sh2go-prx-a
echo "executing solution of task <$EXC>"

# Im Arbeitsordner mit dieser Aufgabe befindet sich ein Unterordner namens
# `preson-files`. Er enthält eine Reihe von Dateien, die in unterschiedlich
# tief verschachtelten Ordnern abgelegt sind.
#
# Die Dateien enthalten keine, eine oder mehrere Zeilen, die iggfls. jeweils 
# nur das Präfix #xc- plus einen Usernamen enthalten. Die User können sein
# Alexander, Daniel, David, Evelina oder Georgios.
#
# Eine Datei, die den Namen 'Georgios' enthielte, enthielte also eine Zeile
# `#xc-Georgios`, sie könnte zusätzlich aber auch eine Zeile mit `#xc-Alexander`
# enthalten.

# PREX-A: Schreiben Sie ein bash-Skript,  
# das a) alle Dateien samt Pfad aus dem Ordner <students> auflistet und 
# das b) (nur) unter dem Listeneintrag den Code `#xc-IHRVORNAME` ausgibt,
# wenn die Datei Ihren wirklichen Vornahmen enthält.
