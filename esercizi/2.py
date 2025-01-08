# Chiedi all'untente due numeri, il primo sara
# il dividendo (numero da dividere),
# e il secondo il divisore (numero per cui divideremo).
# Scrivi poi la parte intera e il resto della divisione.

a = int(input("Inserisci il dividendo"))
b = int(input("Inserisci il divisore"))

# l'operatore // mi da la parte intera della divisione
intero = a // b

# l'operatore % mi da il resto della divisione
resto = a % b

print("Nella divisione di", a ,"e",b,
      "la parte intera =", intero,"e il resto=",resto)

# con print(f...) posso formattare la stringa
# inserendo le variabili direttamente
# con """ scrivo una stringa multilinea (in piu righe)
print(f"Nella divisione di {a} e {b} la parte intera = {intero} e il resto = {resto}")












