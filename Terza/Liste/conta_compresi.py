def conta_compresi(sequenza: list[int], val1: int, val2: int):
    minore = min(val1, val2)
    maggiore = max(val1, val2)
    c = 0
    for val in sequenza:
        if minore <= val <= maggiore:
            c += 1
    return c


def chiedi_valori():
    lista = []
    n_ele = input("Quanti valori vuoi inserire? ")
    while not n_ele.isdigit():
        print("Errore!!\nInserisci un numero!")
        n_ele = input("Quanti numeri vuoi inserire? ")
    n_ele = int(n_ele)
    for i in range(n_ele):
        n = input("Inserisci un valore: ")
        while not n.isdigit():
            print("Errore!!\nInserisci un numero!")
            n = input("Inserisci un numero: ")
        n = float(n)
        if round(n) == n:
            n = int(n)
        lista.append(n)
    return lista


if __name__ == '__main__':
    lista = chiedi_valori()
    estremo1 = input("Inserisci un estremo tra cui devono essere contenuti i numeri: ")
    while not estremo1.isnumeric():
        print("Errore!!\nInserisci un valore numerico intero")
        estremo1 = input("Inserisci un estremo tra cui devono essere contenuti i numeri: ")
    estremo1 = int(estremo1)

    estremo2 = input("Inserisci l'altro estremo tra cui devono essere contenuti i numeri: ")
    while not estremo2.isnumeric():
        print("Errore!!\nInserisci un valore numerico intero")
        estremo2 = input("Inserisci l'altro estremo tra cui devono essere contenuti i numeri: ")
    estremo2 = int(estremo2)

    print(f"{conta_compresi(lista, estremo1, estremo2)} numeri sono contenuti entro gli estremi inseriti")
