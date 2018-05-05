"""
esercizio per imparare il while
"""


print("Buonasera")
NUMERO_SBAGLI = 0
NOME = input("come si chiama tuo marito?")
while NOME != "Stefano":
    NUMERO_SBAGLI = NUMERO_SBAGLI+1
    print("Risposta sbagliata" + "!" * NUMERO_SBAGLI)
    if NUMERO_SBAGLI == 3:
        print("sei ppproprio una moglie scortese!")
    NOME = input("come si chiama tuo marito?")
print("Risposta giusta")
print(NUMERO_SBAGLI)

print("The End")
