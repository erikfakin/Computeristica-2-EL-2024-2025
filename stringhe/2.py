# Formattazione delle stringhe

# Utilizzando f-string (Python 3.6+)
nome = "Marco"
eta = 30
stringa = f"Ciao, mi chiamo {nome} e ho {eta} anni."

# Utilizzando il metodo format()
stringa = "Ciao, mi chiamo {} e ho {} anni.".format(nome, eta)

# Utilizzando l'operatore di formattazione
stringa = "Ciao, mi chiamo %s e ho %d anni." % (nome, eta)
