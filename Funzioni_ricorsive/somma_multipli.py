def somma_multipli(n, a):
    if n == 0:
        return 0
    else:
        return a * n + somma_multipli(n - 1, a)

