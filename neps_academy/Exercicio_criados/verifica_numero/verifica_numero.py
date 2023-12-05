n = input()
sistema = [
    'unidade',
    'dezena',
    'centena',
    'unidade de milhar',
    'dezena de milhar',
    'centena de milhar',
    'milhao'
]

res = []
pos_invertida = len(n)-1
for nn in range(0, len(n)):
    res.append([n[nn], sistema[pos_invertida]])
    pos_invertida-=1

res.reverse()

for r in res:
    print(r[0], r[1])
