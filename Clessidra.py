n = int(input('Inserisci n:'))
while n <= 0:
    print("Input invalido!!\n Inserire un numero positvo!")
    n = int(input('Inserisci n:'))
inizio = 0
fine = n - 1
for riga in range(n):
    for colonna in range(n):
        if (inizio <= colonna <= fine) or (inizio >= colonna >= fine):
            print('#', end='')
        else:
            print(' ', end='')
    print()
    inizio += 1
    fine -= 1
