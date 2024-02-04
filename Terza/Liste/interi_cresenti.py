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


def sort_1(lista):
    lista.sort()
    print(lista)
    lista.pop()
    lista.pop(0)
    return lista


def sort_2(lista):
    lista_finale = []
    for i in range(len(lista)):
        lista_finale.append(min(lista))
        lista.remove(min(lista))
    print(lista_finale)
    lista_finale.pop()
    lista_finale.pop(0)
    return lista_finale


if __name__ == '__main__':
    l = crea_lista()
    print(sort_1(l.copy()))
    print()
    print(sort_2(l.copy()))
