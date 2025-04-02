# Esercizio

# Chiedi all'utente di inserire una password.
# Ignora le lettere maiuscole o minuscole e gli spazi vuoti prima e dopo
# della password.
# Compara poi la password dell'utente con una password segreta


# Es.
# password segreta e' casa
# l'utente inserisce "    CaSa     "
# risultato: la password e' giusta

password_segreta = "casa"

password = input("Inserisci la password:")
password = password.lower()
password = password.strip()

if password == password_segreta:
    print("Password corretta. Benvenuto Batman.")
else:
    print("La password e' sbagliata. Buon tentativo Joker!")





