def divisore(a: int, b: int):
    if b % a == 0:
        return True
    else:
        return False


def stampa_divisori(n: int):
    for i in range(1, n):
        if divisore(i, n):
            print(i)


def main():
    numero = int(input("Inserisci n:"))
    stampa_divisori(numero)


if __name__ == "__main__":
    main()
