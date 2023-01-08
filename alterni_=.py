
def riga(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print("=", end="")
        else:
            print("+", end="")
    print()
    
    
def main():
    n = int(input("N:"))
    while not (0 <= n <= 10):
        print("N deve essere maggiore o uguale a 0 e minore o uguale a 10")
        n = int(input("N:"))
    
    for j in range(n):
        riga(n)


if __name__ == "__main__":
    main()