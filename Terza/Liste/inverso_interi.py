def crea_lista():
    lista = []
    n_ele = input("Quanti numeri vuoi inserire? ")
    while not n_ele.isdigit():
        print("Errore!!\nInserisci un numero!")
        n_ele = input("Quanti numeri vuoi inserire? ")
    n_ele = int(n_ele)
    for i in range(n_ele):
        n = input("Inserisci un numero: ")
        while not n.isdigit():
            print("Errore!!\nInserisci un numero!")
            n = input("Inserisci un numero: ")
        n = int(n)
        lista.append(n)
    return lista


def reverse_1(lista: list):
    lista.reverse()
    return lista


def reverse_2(lista):
    return lista[::-1]


if __name__ == '__main__':
    l = crea_lista()
    print(reverse_1(l.copy()))
    print()
    print(reverse_2(l.copy()))
