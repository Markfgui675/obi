res = []
t = int(input())
for tr in range(t):
    m, d = map(int, input().split())
    chaves = []
    diretores = []
    for dd in range(d):
        chaves_diretor = input().split(' ')
        chaves_diretor.pop(0)
        diretor = f'{str(tr)}{str(dd)}'
        dif = 0
        for c in chaves_diretor:
            if c not in chaves:
                chaves.append(c)
                dif+=1
        if dif > 0:
            diretores.append(diretor)

    if len(chaves) >= m:
        res.append(len(diretores))
    else:
        res.append('Desastre!')

for r in res:
    print(r)
