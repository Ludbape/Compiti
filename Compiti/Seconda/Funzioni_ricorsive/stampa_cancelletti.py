def canc(n, v):
    if v:
        if n == 0:
            return
        else:
            print("#")
            canc(n - 1, True)
    else:
        if n == 0:
            return
        else:
            print("#", end=" ")
            canc(n - 1, False)
