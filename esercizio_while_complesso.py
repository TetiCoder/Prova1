"""marito in while assai complesso
"""

print("Buonasera")
NUMERO_SBAGLI = 0
NOME = input("come si chiama tuo marito?")
while NOME != "Stefano" and NUMERO_SBAGLI < 3:
    NUMERO_SBAGLI = NUMERO_SBAGLI+1
    print("Risposta sbagliata" + "!" * NUMERO_SBAGLI)
    if NUMERO_SBAGLI == 3:
        print("sei ppproprio una moglie scortese!")
    else:
        NOME = input("come si chiama tuo marito?")

if NUMERO_SBAGLI < 3:
    print("Risposta giusta")
print("The End")
