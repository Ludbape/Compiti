def maggiore(a, b):
    if a > b:
        return a
    else:
        return b
    
    
def minore(a, b):
    if a > b:
        return b
    else:
        return a
    
    
def stampa_maggiore(a, b):
    print(maggiore(a, b))
    
    
def stampa_minore(a, b):
    print(minore(a, b))
    
    
def somma_pari(a, b):
    s = 0
    for i in range(minore(a, b), maggiore(a, b) + 1):
        if i % 2 == 0:
            s = s + i
            
            
    return s
def conta_multipli(a, b, x):
    if a == 0:
        c = -1
    else:
        c = 0
    for i in range(minore(a, b), maggiore(a, b) + 1):
        if i % x == 0:
            c = c + 1
    return c
                
    
def somma_step(a,b, step):
    s = 0
    for i in range(minore(a, b), maggiore(a, b), step):
        s = s + i
    return s    
        
        
def main():
    a = int(input('A: '))
    b = int(input('B: '))
    #x = int(input('X: '))
    step = int(input('STEP: '))
    print(somma_step(a, b, step))
    
    
if __name__ == '__main__':
    main()