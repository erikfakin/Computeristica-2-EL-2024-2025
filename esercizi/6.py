# Esercizio
# Chiedi all'utente di inserire un voto da 1 a 5. Scrivere poi
# la valutazione in parole.
# Se il voto e' minore di 1 scriere - 'Il voto deve essere almeno 1'
# Se il voto e' maggiore di 5 scrivere - 'Il voto massimo e' 5' 

# Es.   input - 3
#       output - "Buono"

voto = int(input("Inserisci il voto:"))

if voto < 1:
    print("Il voto deve essere almeno 1")
elif voto > 5:
    print("Il voto deve essere minore di 5")
elif voto == 1:
    print("Insufficiente")
elif voto == 2:
    print("Sufficiente")
elif voto == 3:
    print("Buono")
elif voto == 4:
    print("Molto buono")
elif voto == 5:
    print("Ottimo")
