def secoes(ns):
    qtd_secoes = 0
    borda = 0
    for q in range(len(ns)):
        if q == 0:
            borda = ns[q]
        else:
            if ns[q] < borda: 
                qtd_secoes += 1
    return qtd_secoes
            

n = int(input(''))
ns = []
for r in range(n):
    x = int(input(''))
    ns.append(x)

result = secoes(ns)
print(result)
