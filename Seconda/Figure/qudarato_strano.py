def riga(n, s):
    for i in range(n):
        print(s, end="")
        
        
def quadrato(lato):
    for r in range(lato):
        if r % 2 == 0:
            riga(lato, "=")
        else:
            riga(lato, "+")
        print()
        
        
def main():
    L = int(input("L:"))
    while not (0 < L < 10) and L % 2 == 1:
        print("L dev'essere compreso tra 0 e 10 (inclusi) e pari")
        L = int(input("L:"))
        
    quadrato(L)
    
    
if __name__ == "__main__":
    main()
