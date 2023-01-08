n = int(input('Inserisci un numero:'))
while n <= 0 or n % 2 == 0:
    print('Il numero inserito non è valido!!\nInserire solo numeri positivi e dispari!')
    n = int(input('Inserisci un numero:'))
for i in range(n):
    for c in range(n):
        if i == 0 or c == (n // 2):
            print('#', end='')
        else:
            print(' ', end='')
    print()
