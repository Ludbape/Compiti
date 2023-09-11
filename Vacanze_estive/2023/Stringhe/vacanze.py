if __name__ == '__main__':
    testo_finale = ""
    n_vacanze = int(input("Quante vacanze farai? "))
    for indice_vacanze in range(1, n_vacanze + 1):
        luogo = input(f"Dove andrai nella vacanza {indice_vacanze}? ")
        mese = input(f"Quando andari in {luogo}? ")
        testo_finale += f"A {mese.capitalize()} andrai in {luogo.capitalize()}. "
    print(testo_finale)
