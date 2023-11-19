def stampa_al_contrario(n: int):
    if n < 10:  # Se il numero è di una cifra stampalo
        print(n, end="")
    else:
        stampa_al_contrario(int(str(n)[1:]))  # Stampa prima tutte le cifre tranne la prima
        print(str(n)[0], end="")  # Stampa la prima cifra


def main():
    n_pos = int(input("Inserisci un numero positivo: "))
    stampa_al_contrario(n_pos)


if __name__ == '__main__':
    main()
