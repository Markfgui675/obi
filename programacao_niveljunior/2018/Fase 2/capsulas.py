caixa = []
#caixa = [[nº de moedas, ciclo]]

n, f = map(int, input().split())
ciclos = input().split(' ')
ciclos = [int(x) for x in ciclos]
for t in range(n):
    caixa.append([0,ciclos[t]])

acumulado = 0
dias = 0
while acumulado <= f:
    dias+=1
    for d in caixa:
        if dias%d[1]==0:
            acumulado+=1

print(dias)
