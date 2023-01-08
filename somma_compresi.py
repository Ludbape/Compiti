def somma_compresi(a, b):
    s = 0
    if a < b:
        a, b = b, a
    for i in range(b, a + 1):
        s += i
    return s


def main():
    A = int(input("A:"))
    B = int(input("B:"))
    while A == B:
        print("A deve'essere diverso da B")
        A = int(input("A:"))
        B = int(input("B:"))
    print(somma_compresi(A, B))


if __name__ == "__main__":
    main()
