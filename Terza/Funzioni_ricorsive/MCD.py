def mcd(num_1, num_2, div):
    if div == 1 or (num_1 % div == 0 and num_2 % div == 0):
        return div
    else:
        return mcd(num_1, num_2, div - 1)


if __name__ == '__main__':
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero:"))
    print(f"Il massimo comune divisore tra i due numeri è {mcd(a, b, min(a, b))}")
