def input_diverso_multiplo(diverso_da: int, multiplo_di: int) -> int:
    tantativo_utente = int(input("Inserisci un numero:"))
    if not tantativo_utente != diverso_da or not tantativo_utente % multiplo_di == 0:
        print("Tentativo errato!!\nRitenta")
        return input_diverso_multiplo(diverso_da, multiplo_di)
    else:
        print("BRAVO!!!\nHAI VINTO!!!")
