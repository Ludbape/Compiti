def funzione(n):
    uno = []
    for i in range(n):
        x = int(input("Inserisci un numero: "))
        while x == 0:
            x = int(input("Inserisci un numero: "))
        else:
            uno.append(x)

    for valore in uno:
        if valore > 0:
            print(" " * 10, "*" * valore)
        else:
            spazio = 10 + valore
            print(" " * spazio, "*" * -valore)


if __name__ == '__main__':
    n = int(input("Quanti numeri vuoi inserire? "))
    funzione(n)
