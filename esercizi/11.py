# Esercizio

# Chiedi all'utente di inserire una frase.
# Scrivi poi
# 1) quanto e' lunga la frase ✓
# 2) la frase letta all'incontrario ✓
# 3) i primi 5 caratteri della frase ✓
# 4) gli ultimi 5 caratteri della frase ✓
# 5) se la frase contiene la parola "Ciao" ✓
# 6) sostituisci la lettera "a" nella frase con la lettera "x"

frase = input("Inserisci una frase: ")

print("La linghezza della frase e'", len(frase))

incontrario = frase[::-1]
print("La frase all'incontrario e'", incontrario)

primi_5 = frase[0:5]
print("I primi 5 caratteri sono:", primi_5)

ultimi_5 = frase[-5:]
print("GLi ultimi 5 caratteri sono:", ultimi_5)

contiene = frase.find("Ciao")
if contiene == -1:
    print("La frase non contiene la parola Ciao")
else:
    print("La frase continene la parola Ciao in posizione", contiene)

modificata = frase.replace("a", "x")
print("Modificata: ", modificata)



