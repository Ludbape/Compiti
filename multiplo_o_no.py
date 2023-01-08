n = int(input("Inserisci N:"))
while n <= 0:
    print("Inserisci un numeri strettamente positivo")
    n = int(input("Inserisci N:"))

for i in range(1, n + 1):
    numero = int(input("Inserisci un numero:"))
    if numero % i == 0:
        print("Multiplo")
    else:
        print("Non multiplo")
