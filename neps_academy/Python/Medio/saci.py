n,m = map(int, input().split())
matriz = []
coordenada2 = []
coordenada3 = []
for i in range(n):
    lista = list(map(int, input().split()))
    if 2 in lista:
        coordenada2 = [len(matriz), lista.index(2)]
        matriz.append(lista)
    else:
        matriz.append(lista)
    if 3 in lista:
        coordenada3 = [len(matriz)-1, lista.index(3)]

def contar(x, y):
    for l in range(coordenada3[0]):
        for m in matriz[x:]:
            ...

if coordenada2[0] == 0 and coordenada2[1] == 0:
    #verifica apenas do lado direito e abaixo'
    if matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
    elif matriz[coordenada2[0]][coordenada2[1]+1] == 1:
        contar(coordenada2[0], coordenada2[1]+1)
elif coordenada2[0] == 0 and coordenada2[1] == m-1:
    #verifica do lado esquerdo e abaixo')
    if matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
    elif matriz[coordenada2[0]][coordenada2[1]-1] == 1:
        contar(coordenada2[0], coordenada2[1]-1)
elif coordenada2[0] == n-1 and coordenada2[1] == 0:
    #verifica acima e do lado direito')
    if matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
    elif matriz[coordenada2[0]][coordenada2[1]+1] == 1:
        contar(coordenada2[0], coordenada2[1]+1)
elif coordenada2[0] == n-1 and coordenada2[1] == m-1:
    #verifica acima e do lado esquerdo')
    if matriz[coordenada2[0]-1][coordenada2[1]] == 1:
        contar(coordenada2[0]-1, coordenada2[1])
    elif matriz[coordenada2[0]][coordenada2[1]-1] == 1:
        contar(coordenada2[0], coordenada2[1]-1)
elif coordenada2[0] == 0 and coordenada2[1] > 0:
    #verifica dos dois lados e abaixo')
    if matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
    elif matriz[coordenada2[0]-1][coordenada2[1]] == 1:
        contar(coordenada2[0]-1, coordenada2[1])
    elif matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
elif coordenada2[0] > 0 and coordenada2[1] == 0:
    #verifica acima e abaixo e do lado direito')
    if matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
    elif matriz[coordenada2[0]][coordenada2[1]-1] == 1:
        contar(coordenada2[0], coordenada2[1]-1)
    elif matriz[coordenada2[0]][coordenada2[1]+1] == 1:
        contar(coordenada2[0], coordenada2[1]+1)
    elif matriz[coordenada2[0]-1][coordenada2[1]] == 1:
        contar(coordenada2[0]-1, coordenada2[1])
elif coordenada2[0] > 0 and coordenada2[1] == m-1:
    #verifica acima e abaixo e do lado esquerdo')
    if matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
    elif matriz[coordenada2[0]][coordenada2[1]-1] == 1:
        contar(coordenada2[0], coordenada2[1]-1)
    elif matriz[coordenada2[0]-1][coordenada2[1]] == 1:
        contar(coordenada2[0]-1, coordenada2[1])
elif coordenada2[0] == n-1 and coordenada2[1] > 0:
    #verifica acima e dos dois lados')
    if matriz[coordenada2[0]][coordenada2[1]-1] == 1:
        contar(coordenada2[0], coordenada2[1]-1)
    elif matriz[coordenada2[0]][coordenada2[1]+1] == 1:
        contar(coordenada2[0], coordenada2[1]+1)
    elif matriz[coordenada2[0]-1][coordenada2[1]] == 1:
        contar(coordenada2[0]-1, coordenada2[1])
else:
    #verifica todos os lados')
    if matriz[coordenada2[0]+1][coordenada2[1]] == 1:
        contar(coordenada2[0]+1, coordenada2[1])
    elif matriz[coordenada2[0]][coordenada2[1]-1] == 1:
        contar(coordenada2[0], coordenada2[1]-1)
    elif matriz[coordenada2[0]][coordenada2[1]+1] == 1:
        contar(coordenada2[0], coordenada2[1]+1)
    elif matriz[coordenada2[0]-1][coordenada2[1]] == 1:
        contar(coordenada2[0]-1, coordenada2[1])
