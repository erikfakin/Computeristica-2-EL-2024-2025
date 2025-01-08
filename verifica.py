# Esercizio 1

# Chiedi all'untente di inserire 5 voti di una materia.
# Salva i voti in una lista
# Scrivi poi all'untente la media dei voti e la valutazione
# insuffieciente, sufficiente, buono, molto buono o ottimo.
# Scrivi il massimo dei voti e il minimo.

# 5 putni

voti = []
for i in range(5):
    voti.append(int(input("Inserisci un voto")))

massimo = max(voti)
minimo = min(voti)
media = sum(voti) / len(voti)

if media >= 4.5:
    print("Ottimo")
if media >= 3.5:
    print("Molto buono")
if media >= 2.5:
    print("Buono")
if media >= 1.5:
    print("Sufficiente")
else:
    print("Insufficiente")

print("min", minimo)
print("max", massimo)

# Esercizio 2

# Chiedi all'utente di inserire un numero intero maggiore di 0
# Usando il ciclo for fai un programma che somma tutti i numeri pari da 0
# al numero inserito dall'utente

#4 punti

numero = input("Inserisci un numero maggiore di 0")

somma = 0
for i in range(numero):
    if i % 2 == 0:
        somma = somma + i

print(i)

# Esercizio 3

# In un ciclo while chiedi all'untente di inserire numeri fino a che
# non inserisce lo 0. Scrivi poi la somma di tutti i numeri divisibili
# per 3 inseriti dall'utente nel ciclo while.

# 4 putni

numero = int(input("Inserisci un numero o 0 se vuoi uscure"))
if numero % 3 == 0:
    somma = numero
else:
    somma = 0
while numero != 0:
    numero = int(input("Inserisci un numero o 0 se vuoi uscure"))
    if numero % 3 == 0:
        somma = somma + numero

print("Somma", somma)


