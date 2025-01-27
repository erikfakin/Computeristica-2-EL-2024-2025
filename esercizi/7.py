# Esercizio
# Chiediamo all'utente di inserire una frase e una lettera
# Scriviamo poi se la lettera e' presente o meno nella frase.

# input - "Oggi c'e' il sole."
#       - "e"
# output - "La lettera 'e' e' presente nella frase 'Oggi c'e' il sole'".

frase = input("Inserisci la frase: ")
lettera = input("Inserisci la lettera: ")

if lettera in frase:
    print("La lettera", lettera, "e' presente nella frase", frase)
else:
    print("La lettera", lettera, "non e' presente nella frase", frase)



