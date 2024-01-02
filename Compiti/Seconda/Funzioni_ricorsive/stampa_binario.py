def binario(n):
    if n == 1:
        print(1, end=" ")
    else:
        if n % 2 == 0:
            binario(n//2)
            print(0, end=" ")
        else:
            binario(n//2)
            print(1, end=" ")
