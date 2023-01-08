n = int(input('Inserisci n:'))
while n <= 0:
    print("Input invalido!!\n Inserire un numero positvo!")
    n = int(input('Inserisci n:'))
inizio = 0
fine = n - 1
righe = 0
if n % 2 == 0:
    righe = n // 2
else:
    righe = n // 2 + 1
for riga in range(righe):
    for colonna in range(n):
        if colonna == inizio or colonna == fine:
            print('#', end='')
        else:
            print(' ', end='')
    print()
    inizio += 1
    fine -= 1
