n = int(input('Inserisci n: '))
if n % 2 == 0:
    for i in range(2, n + 2, 2):
        print(i)
else:
    for i in range(1, n + 1, 2):
        print(i)
