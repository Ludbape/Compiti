def somma_dipari(n: int) -> int:
    if n % 2 == 0:
        n -= 1

    if n == 1:
        return 1
    else:
        return n + somma_dipari(n - 2)
