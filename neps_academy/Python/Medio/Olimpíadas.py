# outro = 3 pontos
# prata = 2 pontos
# bronze = 1 ponto
n, m = map(int, input().split())
classificacao = []
classificados = []
classificacao_final = []

for modalidades in range(m):
    o,p,b = map(int, input().split())
    if o not in classificados:
        classificacao.append([0, o])
        classificados.append(o)
    if p not in classificados:
        classificacao.append([0, p])
        classificados.append(p)
    if b not in classificados:
        classificacao.append([0, b])
        classificados.append(b)
    for po in classificacao:
        if o == po[1]:
            po[0]+=6
    for pp in classificacao:
        if p == pp[1]:
            pp[0]+=3
    for pb in classificacao:
        if b == pb[1]:
            pb[0]+=1

for r in sorted(classificacao, reverse=True):
    print(r[1], end=' ')
