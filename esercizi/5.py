# Chiedi all'utente di inserire 2 numeri a e b
# Voglio che a sia il numero minore e b quello maggiore, indifferentemente
# da quello che inserisce l'utente.

# Es l'utente scrive 10 e 8
# Volgio che a diventi 8 e b 10

a = float(input("Inserisci il numero a"))
b = float(input("Inserisci il numero b"))

if a > b:
    temp = a
    a = b
    b = temp

print("a =", a, "b =", b)


