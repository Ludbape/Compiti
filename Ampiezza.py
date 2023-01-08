def ampiezza(a: int, b: int):
    if a < b:
        a, b = b, a
    return len(range(b, a))


def main():
    A = int(input("A:"))
    B = int(input("B:"))
    print(ampiezza(A, B))
    
    
if __name__ == "__main__":
    main()