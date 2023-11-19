def bin2dec(s1: str):
    if not (s1.isnumeric()):
        print("Errore!!\n Il numero inserito non è in binario")
    s1 = s1[::-1]
    num = 0
    for i in range(len(s1) - 1, -1, -1):
        num = num + float(s1[i]) * 2**i
    return num


def main():
    bin = input("Inserisci un numero bianrio: ")
    print(bin2dec(bin))


if __name__ == "__main__":
    main()
