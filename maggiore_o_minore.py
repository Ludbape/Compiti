n = int(input("Inserisci N:"))
while n <= 0:
    print("Inserisci un numeri strettamente positivo")
    n = int(input("Inserisci N:"))

for i in range(1, n + 1):
    numero = int(input("Inserisci un numero:"))
    if numero % 2 == 0:
        print("Pari")
    else:
        print("Dispari")