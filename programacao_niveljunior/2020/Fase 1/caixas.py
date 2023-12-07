caixas = []

for i in range(3):
    caixas.append(int(input()))

caixas = sorted(caixas)
c_caixas = caixas[:]
v = 3

maior_caixa = max(c_caixas)
c_caixas.remove(maior_caixa)
if sum(c_caixas) < maior_caixa:
    print(1)
else:
    for c in range(len(caixas)-1):
        if caixas[c] < caixas[c+1]:
            v-=1
    
    print(v)