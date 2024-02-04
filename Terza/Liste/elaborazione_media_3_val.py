def chiedi_valori():
    lista = []
    n_ele = input("Quanti valoru vuoi inserire? ")
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

def elabora_media(lista):
    valori_finali = []
    for i in range(len(lista)):
        if i == 0:
            valori_finali.append((2*lista[i] + lista[i+1])/3)
        elif i == len(lista)-1:
            valori_finali.append((2*lista[i] + lista[i-1])/3)
        else:
            valori_finali.append((lista[i-1] + lista[i] + lista[i+1])/3)
    return valori_finali
if __name__ == "__main__":
    val = chiedi_valori()
    print(elabora_media(val))

