def n_docenti() -> int:
    numero_docenti = int(input("Quanti docenti hai? "))
    return numero_docenti


def chiedi_docenti(numero_docenti: int) -> None:
    testo_finale = ""
    for indice_voto in range(1, numero_docenti + 1):
        nome = input(f"Cosa si chima l'insegnate {indice_voto}? ")
        materia = input(f"Cosa insegna {nome}? ")
        testo_finale += f"L'insegnate {nome} insegna {materia}"
    print(testo_finale)


def main():
    chiedi_docenti(n_docenti())


if __name__ == '__main__':
    main()
