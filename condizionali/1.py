# Ci permettono di eseguire un blocco di codice
# solo se una condizione e' vera

x = int(input("Inserisci un numero"))

# operatori logici - mi ritnornano o True o False
# >, <, >=, <=, ==, !=
# congiunzioni - and, or
# opposto - not

if x > 0:
    print("Il numero e' positivo")
elif x == 0:
    print("Il numero e' uguale a 0")
else:
    print("Il numero e' negativo")


eta = int(input("Iserisci la tua eta'"))

if eta >= 14 and eta < 19:
    print("Vai alle medie")
elif eta < 6 or eta > 30:
    print("Non vai a scuola!")


username = "mauro"
password = "mauro52"

login_username = input("Inserisci il tuo username: ")
login_password = input("Inserisci la tua password: ")

if login_username == username and login_password == password:
    print("Login con successo!")
elif login_username != username:
    print("Il tuo username non esiste")
elif login_username == username and login_password != password:
    print("La password e' sbagliata")












        
