"""Esercizio per cambiare nome ai mariti"""


print("Hello World!")
NOME = input("come si chiama tuo marito?")
if NOME == "Stefano":
    print("Risposta giusta")
else:
    print("Ci deve essere un errore - riproviamo")

    NOME = input("come si chiama tuo marito?")
    if NOME == "Stefano":
        print("Risposta giusta")
    else:
        print("Brutta strega infedele")

print("The End")
