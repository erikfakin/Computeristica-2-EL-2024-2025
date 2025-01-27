# STRINGHE

# Concatenazione di stringhe
str1 = "Ciao"
str2 = "Mondo"
concatenazione = str1 + " " + str2
print(concatenazione) # Risultato: Ciao Mondo

# Slicing di stringhe
substring = concatenazione[0:4]
print(substring) #Risultato: Ciao

subtring_mondo = concatenazione[-5:]
print(subtring_mondo)# Risultato: Mondo

# Lunghezza della stringa
lunghezza = len(concatenazione)
print(lunghezza) #Risultato: 10

# Invertire una stringa
invertita = concatenazione[::-1]
print(invertita) #odnoM oaiC

# Ricerca di una sottostringa - mi ritorna la posizione della stringa
posizione = concatenazione.find("Mondo")
print(posizione) # Risultato: 5

# Sostituire un carattere o una sottostringa
sostituita = concatenazione.replace("Mondo", "Python")
print(sostituita)   # Risultato: Ciao Python
