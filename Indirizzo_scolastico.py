def chiedi():
    global scelta
    print("1) Classico 100€ all'anno")
    print("2) Scientifico 150€ all'anno")
    print("3) Scienze applicate 200€ all'anno")


chiedi()
scelta = int(input('Che scuola scegli? '))
# noinspection PyUnboundLocalVariable
while scelta != 1 and scelta != 2 and scelta != 3:
    chiedi()
    scelta = int(input('Che scuola scegli? '))
prezzo = 0
if scelta == 1:
    prezzo = 100*5
elif scelta == 2:
    prezzo = 150*5
else:
    prezzo = 200 * 5

print("Il prezzo dell'iscrizione per 5 anni è:", prezzo)
