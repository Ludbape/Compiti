def conta_cifre(string: str):
    n_cifre = 0
    for i in string:
        if i.isnumeric():
            n_cifre += 1
    return n_cifre


def main():
    st = input('Inserisci una stringa: ')
    print(conta_cifre(st))


if __name__ == '__main__':
    main()