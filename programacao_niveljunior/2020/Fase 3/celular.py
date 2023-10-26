n = int(input())
coordenadas = []
for l in range(n):
    coordenadas.append(input().split(' '))
cobertura = int(input())

minima_conexao = n-1

def calculoDistancia(*args):
    print(*args)

x = []
y = []

for z in range(len(coordenadas)):
    if z%2==0 and z!=0:
        calculoDistancia(x, y)
    else:
        x.append(int(coordenadas[z][0]))
        y.append(int(coordenadas[z][1]))
