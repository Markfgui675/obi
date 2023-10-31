x = int(input())
divisores = []
for n in range(x):
    if x%(n+1)==0:
        divisores.append(n+1)
for d in divisores:
    print(d, end=' ')