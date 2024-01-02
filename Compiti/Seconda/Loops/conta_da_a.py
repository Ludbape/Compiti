ordine = int(input("Inserisci  l'ordine:"))

while ordine != 1 and ordine != 0:
    print("Il valore inserito non è valodo!! \nI valori accettati sono 0 o 1")
    ordine = int(input("Inserisci  l'ordine:"))

a = int(input("Inserisci A: "))
b = int(input("Inserisci B: "))
first_con = ordine == 1
second_con = a < b
if first_con:
    if second_con:
        for i in range(a, b+1):
            print(i)
    else:
        for i in range(b, a+1):
            print(i)
else:
    if second_con:
        for i in range(b, a-1, -1):
            print(i)
    else:
        for i in range(a, b-1, -1):
            print(i)
