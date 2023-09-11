def prodotto_cifre_pari(stringa: str) -> int:
    prod = 1
    for lettera in stringa:
        if lettera.isnumeric() and int(lettera) % 2 == 0 and int(lettera) != 0:
            prod *= int(lettera)
    return prod


