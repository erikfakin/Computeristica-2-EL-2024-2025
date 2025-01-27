# Esercizio

# Chiedi all'utente di inserire i cateti di un triangolo reattngolo.

# Il programma deve calcolare l'area e il perimetro del triangolo
# e scriverlo all'untente

# Es.
# input -> 3, 4
# output -> "perimetro: 12, area: 6"

# a, b - cateti
# c - ipotenusa

# c^2 = a^2 + b^2 ->  c = sqrt(a**2 + b**2)


# perimetro = a + b + c
# area = a*b / 2

import math

a = float(input("Inserisci il primo cateto: "))
b = float(input("Inserisci il secondo cateto: "))

c = math.sqrt(a**2 + b**2)

perimetro = a + b + c
area = a * b / 2

print("perimetro: ", perimetro, "area: ", area)

