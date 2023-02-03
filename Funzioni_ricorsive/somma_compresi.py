def somma_compresi(a, b):
    minore = min(a, b)
    maggiore = max(a, b)
    if minore == maggiore:
        return maggiore
    else:
        return minore + somma_compresi(minore + 1, maggiore)
    

def main():
    print(somma_compresi(10, 13))
    
    
if __name__ == "__main__":
    main()