a = int(input("Inserisci A:"))
b = int(input("Inserisci B:"))

while a == b or a < 0 or b < 0:
    print("A e B devono esseri diversi e positivi")
    a = int(input("Inserisci A:"))
    b = int(input("Inserisci B:"))

if a < b:
    a, b = b, a

p = 1

for i in range(b, a):
    if i % 2 != 0:
        p *= i
print(p)
