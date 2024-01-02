h = int(input("Inserisci H:"))
while h < 0:
    print("H deve essere positivo!")
    h = int(input("Inserisci H:"))

for riga in range(h, 0, -1):
    for colonna in range(1, riga + 1):
        print(colonna * 2, end=" ")
    print()
