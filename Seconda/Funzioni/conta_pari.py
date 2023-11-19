def conta_pari(a: int, b: int):
    c = 0
    if a < b:
        a, b = b, a
    for i in range(b, a + 1):
        if i % 2 == 0:
            c += 1
    return c


def main():
    A = int(input("A:"))
    B = int(input("B:"))
    while A == B or A <= 0 or B <= 0:
        print("A e B devo essere diversi e strettamente positivi")
        A = int(input("A:"))
        B = int(input("B:"))
    print(conta_pari(A, B))


if __name__ == "__main__":
    main()
