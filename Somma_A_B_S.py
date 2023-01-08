a = int(input('Inserisci A:'))
b = int(input('Inserisci B:'))
s = int(input('Inserisci S:'))
somma = 0
if a > b:
    maggiore = a
    minore = b
else:
    maggiore = b
    minore = a
if s > 0:
    for i in range(minore, maggiore, s):
        somma += i
elif s == 0:
    print('Input non valido')
else:
    for i in range(maggiore, minore, s):
        somma += i
print(somma)