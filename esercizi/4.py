#Esercizio

#Chiedi all'utente di inserire un numero.
#Scrivi poi la somma di tutti i numeri da 1 al numeri inserito.
#(Usa un ciclo for)

numero = int(input("Inserisci un numero intero positivo"))
somma = 0
# 1+2+3+4+...+998+999+1000
# 1001*500=500500
somma = (numero + 1)*numero/2
for i in range(numero + 1):
    somma = somma + i

print(f"Somma da 1 a {numero} = {somma}")
    
