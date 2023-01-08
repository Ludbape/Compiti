def quadrato(n):
    for i in range(n):
        for i in range(n):
            print("#", end="")
        print()
        
        
def triangolo(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("#", end="")
        print()
        
        
def trapezio(n):
    if n % 2 == 1:
        print('ERRORE\nIL VALORE INSERITO NON È CORRETTO')
    else:
        triangolo(n//2)
        quadrato(n//2)
        
        
def main():
    n = int(input("Inserisci un numero: "))
    trapezio(n)
    
    
if __name__ == "__main__":
    main()
