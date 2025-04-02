# Esercizio
# Chiedi all'utente di inserire una letter.
# Se il carattere e' una vocale scrivi "La lettera e' una vocale"
# altrimenti "La lettera non e' una vocale"

# Es    input -> b
#       output -> La lettera non e' una vocale

lettera = input("Inserisci una lettera: ").lower()
vocali = "aeiou"

if lettera in vocali:
    print("La lettera e' una vocale")
else:
    print("La lettera non e' una vocale")
