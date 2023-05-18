import warnings

import numpy as np

warnings.filterwarnings("ignore")


def quante_parole() -> str:
    scleta_file = int(input("Con qaante parole vuoi giocare? 1,000 o 660,000: "))
    while scleta_file not in [1000, 660000]:
        print("Scelta non valida!!")
        scleta_file = int(input("Con qaante parole vuoi giocare? 1,000 o 660,000: "))
    if scleta_file == 1000:
        path = r"1000_parole.txt"
    else:
        path = r"660000_parole.txt"
    return path


def difficoltà():
    difficile, intermedio, facile = (
        "Difficile: massimo 5 tentativi",
        "Intermedio: massimo 8 tentativi",
        "Facile: massimo 10 tentativi",
    )
    print("Scegli la difficoltà: ")
    print(difficile, intermedio, facile, sep="\n")
    scelta = input("Scegli la difficoltà: ")
    print("-----------------------------------")
    while scelta not in ["facile", "intermedio", "difficile"]:
        print("Scelta non valida!!")
        print(difficile, intermedio, facile, sep="\n")
        scelta = input("Scegli la difficoltà: ")
    return scelta


def lunghezza_parole(lunghezza_massima):
    testo = f"Scegli la lunghezza della parola? Minimo 5 massimo {lunghezza_massima} :"
    lunghezza_parola = int(input(testo))
    while lunghezza_parola < 5 or lunghezza_parola > lunghezza_massima:
        print("Scelta non valida!!")
        lunghezza_parola = int(input(testo))
    return lunghezza_parola


def leggi_file(percorso_file: str) -> np.array(str):
    with open(percorso_file, encoding="UTF-8") as file:
        testo = file.readlines()
        return np.array([parola.strip() for parola in testo])


def scegli_parola(testo: np.array(str), lunghezza_scelta: int):
    func_mask = np.vectorize(lambda x: len(x) == lunghezza_scelta)
    parole_corrette = testo[func_mask(testo)]
    return np.random.choice(parole_corrette, size=1)


def nascondi(parola: str) -> str:
    vocali = "aeiouàèìòù"
    st = ""
    for carattere in parola:
        if carattere in vocali:
            st = st + "+"
        else:
            st = st + "-"
    return st


def aggiorna(inserimento: np.array(str), enigma: str) -> str:
    sr = ""
    for lettera in enigma:
        if lettera in inserimento:
            sr += lettera
        else:
            sr += nascondi(lettera)
    return sr


def fai_tentativi(scelta: str, parola: str):
    if scelta == "facile":
        n_tentativi = 10
        inserimenti_utente = np.array((parola[0], parola[-1]))
    elif scelta == "intermedio":
        n_tentativi = 8
        inserimenti_utente = np.array((parola[0]))
    else:
        n_tentativi = 5
        inserimenti_utente = np.array([])

    while n_tentativi > 0:
        print(f"{n_tentativi} tentativi rimasti!")
        if scelta == "facile":
            print("Lettera già inserita: ", end="")
            for i in inserimenti_utente:
                if i != inserimenti_utente[-1]:
                    print(i, end=" | ")
                else:
                    print(i)
        parola_nascosta = aggiorna(inserimenti_utente, parola)
        print(parola_nascosta)
        utente = input("Fai un tentativo: ")
        inserimenti_utente = np.append(inserimenti_utente, utente)
        parola_aggiornata = aggiorna(inserimenti_utente, parola)
        if utente in parola_nascosta and scelta in ["facile", "intermedio"]:
            print("Lettera già inserita!")
        elif utente == parola or parola_aggiornata == parola:
            fine(True, parola)
            return
        elif utente not in parola:
            n_tentativi -= 1
            print("No! Ritenta")
        print("-----------------------------------")
    else:
        fine(False, parola)


def fine(vittoria: bool, enigma: str):
    if vittoria:
        print("Hai vinto!!")
        print(f"La parola era: {enigma}")
    else:
        print("IMPICCATO!!  :(")
        print(f"La parola era: {enigma}")


def main():
    func_mask = np.vectorize(lambda x: len(x))
    print("BENVENUTO NEL GIOCO DELL'IMPICCATO!")
    print("-----------------------------------")
    percorso_file = quante_parole()
    file = leggi_file(percorso_file)
    max_len = np.max(func_mask(file))
    scelta = difficoltà()
    len_parola = lunghezza_parole(max_len)
    parola = scegli_parola(file, len_parola)
    fai_tentativi(scelta, parola[0])


if __name__ == "__main__":
    main()
