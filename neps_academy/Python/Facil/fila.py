n = int(input())
fila_inicial = list(map(int, input().split()))
m = int(input())
sairam = list(map(int, input().split()))
for j in sairam:
    for i in fila_inicial:
        if j == i:
            fila_inicial.remove(j)
            break
for r in fila_inicial:
    print(r, end=' ')