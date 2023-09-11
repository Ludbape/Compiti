def input_compresi(a, b):
    minore = min(a, b)
    maggiore = max(a, b)
    tentativo_utente = int(input("Fai un tentativo:"))
    if not minore < tentativo_utente < maggiore:
        print("Hai sbaglito\nRitenta!")
        return input_compresi(a, b)
    else:
        print("BRAVO!!!\nHAI VINTO!!!")


input_compresi(10, 7)
