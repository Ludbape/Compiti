if __name__ == '__main__':
    lato = int(input("Inserisci il lato del quadrato: "))
    while lato <= 1:
        print("Errore!!\nIl numero dev'essere maggiore di 1")
        lato = int(input("Inserisci il lato del quadrato: "))
    for riga in range(lato):
        for colonna in range(lato):
            print("*", end=" ")
        print()
