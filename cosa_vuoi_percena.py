""" cosa vuoi per cena?
"""

print("Benvenuto")
NUMERO_SBAGLI = 0
RISPOSTA_CORRETTA = False               #tradotto: il cliente mi ha dato la risposta corretta? = RISPOSTA CORRETTA --> A PRIORI DICIAMO DI NO!!!!!!


while NUMERO_SBAGLI < 3 and not RISPOSTA_CORRETTA == True:
    PIATTO = input("cosa vuoi per cena?")
    if (PIATTO == "pasta" or PIATTO == "carne"):
        RISPOSTA_CORRETTA = True
    else:
        print("sbagliato")
        NUMERO_SBAGLI = NUMERO_SBAGLI+1

if RISPOSTA_CORRETTA:
    print("risposta corretta")
    print("buon appetito!")
    print("eccoti la " + PIATTO)
