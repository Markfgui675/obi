n = int(input())
quadrado = []
for i in range(n):
    l = list(map(int, input().split()))
    quadrado.append(l)

somas = []
magico = True

# verifica a soma das linhas
for i in range(n):
    s = sum(quadrado[i])
    if i == 0:
        somas.append(s)
    else:
        if s not in somas:
            magico = False
            break
        else:
            somas.append(s)

# verifica a soma das colunas
if magico:
    for i in range(n):
        s = 0
        for j in range(n):
            s += quadrado[j][i]
        if s not in somas:
            magico = False
            break
        else:
            somas.append(s)
    
# verifica a soma das diagonais
if magico:
    s = 0
    for i in range(n):
        s += quadrado[i][i]
    if s not in somas:
        magico = False
    else:
        somas.append(s)
    if magico:
        s = 0
        j = n-1
        for i in range(n):
            s += quadrado[i][j]
            j-=1
        if s not in somas:
            magico = False
        else:
            somas.append(s)

if magico:
    print(somas[0])
else:
    print(-1)
