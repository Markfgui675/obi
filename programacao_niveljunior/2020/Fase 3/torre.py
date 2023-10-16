d = int(input())

dados = []
lados_opostos = []

for d in range(d):
    u = input().split(' ')
    for k in range(len(u)):
        lista = [int(x) for x in u]
    lados_opostos = [[lista[0], lista[5]], 
         [lista[1], lista[3]],
         [lista[2], lista[4]]]
    dados.append(lados_opostos[:])
    lados_opostos.clear()

for t in range(len(dados)):
    print(dados[t])
