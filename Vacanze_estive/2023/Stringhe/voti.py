def n_voti() -> int:
    numero_voti = int(input("Quanti voti vuoi inserire? "))
    return numero_voti


def chiedi_voti(numero_voti: int) -> list:
    voti = []
    testo_finale = ""
    for indice_voto in range(1, numero_voti + 1):
        voto = float(input(f"Inserisci il voto {indice_voto}: "))
        testo_finale += f"Il voto {indice_voto} è {voto}. "
        voti.append(voto)
    print(testo_finale)
    return voti


def media(interable):
    return sum(interable) / len(interable)


def main():
    print(f"La media è {media(chiedi_voti(n_voti()))}")


if __name__ == '__main__':
    main()
