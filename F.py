n = int(input("Inserisci n:"))
while n > 10 or n < 0:
    print("N dev'essere compreso tra 0 e 10")
    n = int(input("Inserisci n:"))
    
for riga in range(n):
    for colonna in range(n):
        if riga == 0 or colonna == 0 or riga == n//2:
            print("#", end="")
        else:
            print(" ", end="")
    print()