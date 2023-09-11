def somma_multipli(n: int, a: int) -> int:
    while n % a != 0:
        n -= 1
    if n == a:
        return a
    else:
        return n + somma_multipli(n - a, a)
