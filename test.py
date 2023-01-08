if __name__ == "__main__":
    n = 4
    for k in range(n):
        for x in range(n):
            if k < n//2 and x < n//2:
                print("-", end="")
            elif k >= n//2 and x >= n//2:
                print("+", end="")
            else:
                print("0", end="")
        
        print()