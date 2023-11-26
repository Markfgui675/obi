impares = []
pares = []
for i in range(10):
    x = int(input())
    if abs(x)%2==0:
        pares.append(x)
    else:
        impares.append(x)

for p in pares:
    print(p, end=' ')
print()
for i in impares:
    print(i, end=' ')
