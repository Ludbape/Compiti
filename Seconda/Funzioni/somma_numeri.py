def somma_numeri(x, y, p):
    s = 0
    if p:
        for i in range(min(x, y), max(x, y)):
            if i % 2 == 0:
                s += i
    else:
        for i in range(min(x, y), max(x, y)):
            if i % 2 == 1:
                s += i
    return s


def main():
    print(somma_numeri(1, 1000, False))
    
    
if __name__ == "__main__":
    main()