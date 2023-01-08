def negativo(n):
    if n < 0:
        return True
    else:
        return False


def modulo(numero):
    if negativo(numero):
        return -numero
    else:
        return numero


def main():
    N = int(input("N:"))
    print(modulo(N))
    for i in range(modulo(N)):
        x = int(input("Inserisci un numero:"))
        print(modulo(x))


if __name__ == "__main__":
    main()
