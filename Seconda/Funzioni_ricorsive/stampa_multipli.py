def multipli(n, a):
    if n == 1:
        print(a)
    else:
        multipli(n - 1, a)
        print(a * n)


def main():
    A = int(input("Inserisci un numero di cui vuoi trocare i multipli:"))
    N = int(input("Inserisci quanti multipli vuoi trovare:"))
    multipli(N, A)


if __name__ == "__main__":
    main()
