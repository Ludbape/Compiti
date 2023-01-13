def stampariga(a):
    for i in range(abs(a)):
        print("#", end=" ")


def main():
    z = int(input("Inserisci un numero:"))
    stampariga(abs(z))


if __name__ == "__main__":
    main()
