ari = 0 # 0
ane = 0 # 1

i,j,n = map(int, input().split())

jogos = []

for p in range(n):
    for pp in range(i):
        lista=list(map(str, input().split()))
        ari+=lista.count('0')
        ane+=lista.count('1')
    if ane == ari:
        jogos.append('Empate')
    elif ane > ari:
        jogos.append('Ane venceu')
    else:
        jogos.append('Ari venceu')
    ane, ari = 0, 0

for r in jogos:
    print(r)
