n = int(input('Inserisci un numero:'))
while n <= 0:
    print('Il numero inserito non è valido!!\nInserire solo numeri positivi!')
    n = int(input('Inserisci un numero:'))

for c in range(n):
    for i in range(n):
        if c == 0 or c == n - 1 or i == 0:
            print('#', end='')
        else:
            print(' ', end='')
    print()

