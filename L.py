def cancelletti(n: int, v: bool):
    if v:
        for i in range(n):
            print("#")
    else:
        for i in range(n):
            print("#", end="")
            

def stampa_L(n: int):
    cancelletti(n-1, True)
    cancelletti(n, False)


def main():
    numero = int(input("N:"))
    stampa_L(numero)
    

if __name__ == "__main__":
    main()