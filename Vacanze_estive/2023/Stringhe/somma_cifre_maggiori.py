def somma_cifre_maggiori(stringa: str) -> int:
    somma = 0
    for lettera in stringa:
        if lettera.isnumeric() and int(lettera) > 5:
            somma += int(lettera)
    return somma
