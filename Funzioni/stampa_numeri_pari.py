def stampa_numeri_pari(n):
    if n % 2 == 1:
        n -= 1
    for i in range(n, -1, -2):
        print(i)


def main():
    N = int(input("N:"))
    stampa_numeri_pari(N)


if __name__ == "__main__":
    main()
