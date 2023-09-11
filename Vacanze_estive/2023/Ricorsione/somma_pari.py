def somma_pari(n: int) -> int:
    if not n % 2 == 0:
        n -= 1
    if n == 2:
        return 2
    else:
        return n + somma_pari(n - 2)


print(somma_pari(11))
