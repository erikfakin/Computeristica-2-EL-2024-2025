# Esercizio 1
# Chiedi due numeri all'utente e mostra il piu' grande utilizzando print.
# Per trovare il numeri piu grande utilizza max()
numero1 = int(input("Inserisci il num"))
numero2 = int(input("Inserisci il num"))

print(max(numero1, numero2))
# __________________________________________________________________
# Esercizio 2
# Chiedi all'utente di inserire una lettera.
# Se il carattere e' una vocale scrivi "La lettera e' una vocale"
# altrimenti "La lettera non e' una vocale"
vocali = "aeiouAEIOU"

lettera = input("Inserisci una lettera")
if lettera in vocali:
    print("La lettera e' una vocale")
else:
    print("La lettera non e una vocale")
#_______________________________________________________________________
# Esercizio 3
# Scrivi un ciclo for che somma tutti i numeri da 1 a 1000
# 1 + 2 + 3 + ... + 1000

totale = 0
for i in range(1, 1001):
    totale = totale + i
print(totale)
#_______________________________________________________________________
# Esercizio 4
# Con un ciclo for scrivi la tabellina del numero 7.

for i in range(1, 11):
    print(7*i)

#_______________________________________________________________________
# Esercizio 5
# Chiedi all'utente di inserire un numero.
# Se il numero e' divisibile per 3 scrivi "Il numero e' divisibile per 3"
# altrimenti scrivi "Il numero non e' divisibile per 3"

numero = int(input("inserisci un numero"))

if numero%3 == 0:
    print("Il numero e' divisibile per 3")
else:
    print("Il numero non e' divisibile per 3")



