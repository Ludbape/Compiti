def riga_n(n, s):
    for i in range(n):
        print(s, end=" ")


def rettangolo(b, h):
    for riga in range(h):
        riga_n(b, riga)
        print()


def main():
    B = int(input("B:"))
    H = int(input("H:"))
    while B < 0 or H < 0:
        print("B e H devono essere positivi")
        B = int(input("B:"))
        H = int(input("H:"))
    rettangolo(B, H)


if __name__ == "__main__":
    main()
