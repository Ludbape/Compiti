n = int(input("Inserisci un numero strettamente positivo: "))
s = 0
while n <= 0:
    print("Il numero deve essere positivo!")
    n = int(input("Inserisci un numero: "))
for i in range(n):
    x = int(input("Inserisci un numero:"))
    if x > n:
        s += x

print(s)
