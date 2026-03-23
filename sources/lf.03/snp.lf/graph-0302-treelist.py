# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

# Hexsymbole [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f] als
# Liste von Listen mit 6 als Wurzelknoten und den Geschwisterknoten
# 0, 1, 3, 4, 5 und 8, 9 und a, b, c, e, f:

tree=[ '6', [ '2', [ '0', 
                     '1', 
                     '3', 
                     '4', 
                     '5' ], 
              '7', [ '8', 
                     '9',], 
              'd', [ 'a', 
                     'b', 
                     'c', 
                     'e', 
                     'f']]]

print(f"unbalanced tree of hex symbols:\n{tree}")