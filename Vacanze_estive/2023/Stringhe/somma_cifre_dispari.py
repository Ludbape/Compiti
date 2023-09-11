def somma_cifre_dispari(stringa: str) -> int:
    somma = 0
    for lettera in stringa:
        if lettera.isnumeric() and int(lettera) % 2 == 1 and int(lettera) != 0:
            somma += int(lettera)
    return somma


