h = int(input("H:"))
b = int(input("B:"))
while b <= 0 or h <= 0:
    print("H e B devono essere strettamente positivi")
    h = int(input("H:"))
    b = int(input("B:"))

for r in range(h):
    for c in range(1, b + 1):
        print(c, end=" ")
    print()
