# Esercizio
# Chiedi all'intente di inserire una mese, un giorno, e una anno
# Verifica poi se la data e' valida.

# Es.   input - mese = 5, giorno = 15, anno = 1920
#       output - la data e' valida

# Es.   input - mese = 13, giorno = 1, anno = 2018
#       output - la data non e' valida

giorno = int(input("Inserisci il giorno:"))
mese = int(input("Inserisci il mese:"))
anno = int(input("Inserisci l'anno:"))

if giorno > 31 or giorno < 1:
    print("La data non e' valida")

elif mese > 12 or mese < 1:
    print("La data non e' valida)

elif mese == 4 and giorno == 31:
    print("La data non e' valida")
elif mese == 6 and giorno == 31:
    print("La data non e' valida")
elif mese == 9 and giorno == 31:
    print("La data non e' valida")
elif mese == 11 and giorno == 31:
    print("La data non e' valida")
else:
    print("La data e' valida")


