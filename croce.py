n = int(input('Inserisci un numero:'))
while n <= 0 or n % 2 == 0:
    print('Il numero inserito non è valido!!\nInserire solo numeri positivi e dispari!')
    n = int(input('Inserisci un numero:'))
for riga in range(n):
    for colonna in range(n):
        if colonna == n // 2:
            print('o', end='')
        elif riga == n // 2:
            print('#', end='')
        else:
            print(' ', end='')
    print()
