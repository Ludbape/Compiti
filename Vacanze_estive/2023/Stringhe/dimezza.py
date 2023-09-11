def dimezza(stringa: str) -> str:
    stringa_risultante = ""
    for lettera in stringa:
        if lettera.isnumeric():
            stringa_risultante += str(int(lettera) // 2)
        else:
            stringa_risultante += lettera
    return stringa_risultante
