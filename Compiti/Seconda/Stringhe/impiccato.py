def impiccato(stringa: str) -> str:
    stringa = stringa.lower()
    stringa_risultante = ""
    vocali = "aeiou"
    for lettera in stringa:
        if lettera in vocali:
            stringa_risultante += "+"
        else:
            stringa_risultante += "-"

    return stringa_risultante


def main():
    s = input("Inserisci la parola da indovinare: ")
    print(impiccato(s))


if __name__ == "__main__":
    main()
