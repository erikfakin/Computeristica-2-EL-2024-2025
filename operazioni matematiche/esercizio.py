# ESERCIZIO
# 1 - chiedere all'utente di inserire due numeri interi a e b
# 2 - scrivere il risultato di a + b
# 3 - scrivere se la somma e' pari o dispari

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))

print("a + b =", a + b)

if (a+b)%2 == 0:
    print("La somma e' pari")
else:
    print("La somma e' dispari")

