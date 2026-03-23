#!/bin/bash
# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

# Hexsymbole [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f] als
# Ordner und Dateien mit 6 als Wurzelknoten und den Geschwisterknoten
# 0, 1, 3, 4, 5 und 8, 9 und a, b, c, e, f:

mkdir -p 6
(cd 6 && mkdir -p 2 7 d)
(cd 6/2 && mkdir -p 0 1 3 4 5)
(cd 6/7 && mkdir -p 8 9)
(cd 6/d && mkdir -p a b c e f)

tree 6
