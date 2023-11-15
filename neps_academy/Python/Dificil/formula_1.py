res = []

while True:
    g, p = map(int, input().split())

    if g == 0 and p == 0:
        break

    grandes_premios = []
    pontuacao_total = []
    pilotos = []
    for grande_premio in range(g):
        k = list(map(int, input().split()))
        grandes_premios.append(k)
        for kk in k:
            if kk not in pilotos:
                pilotos.append(kk)
                pontuacao_total.append([0, kk])
    
    s = int(input())

    pontuacoes = []
    for ss in range(s):
        pp = list(map(int, input().split()))
        pontuacoes.append(pp[1:])
    
    # lógica
    for d in pontuacoes:
        pontos = 0
        for l in range(len(d)):
            pontos=d[l]
            for gg in range(g):
                piloto = grandes_premios[gg][l]
                encontrei = False
                for k in pontuacao_total:
                    if k[1] == piloto:
                        k[0]+=pontos
                        encontrei = True
                    if encontrei:
                        break


    campeoes = []
    camp = max(pontuacao_total)[0]
    for h in pontuacao_total:
        if h[0] == camp:
            campeoes.append(h[1])
    print(campeoes)
    res.append(campeoes)

print(res)