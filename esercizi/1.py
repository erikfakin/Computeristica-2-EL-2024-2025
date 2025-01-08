# Chiedi all'utente di inserire un numero.
# Se il numero e' divisibile per 3 scrivi "Il numero e' divisibile per 3"
# altrimenti scrivi "Il numero non e' divisibile per 3"

# con input() chiedo all'utente di inserire un valore.
# input() mi ritnorna una stinga
# con int() trasformo la srtringa in un numero intero

numero = int(input("Inserisci un numero"))

if numero % 3 == 0:
    print("Il numero e' divisibile per 3.")
else:
    print("Il numero non e' divisibile per 3")
