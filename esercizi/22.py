# Chiedi all'utente di inserire
# una frase.
# Conta quante volte appare la
# la lettera 'a' nella frase.

frase = input("Inserisci una frase: ")

contatore = 0

for lettera in frase:
    if lettera == 'a' or lettera == 'A':
        contatore = contatore + 1

print(contatore)

