quadrado = [[],[],[]]
for q in range(9):
    x = int(input())
    if q in range(0,3):
        quadrado[0].append(x)
    elif q in range(3,6):
        quadrado[1].append(x)
    else:
        quadrado[2].append(x)

certo = True

#verifica linhas
primeira_soma = sum(quadrado[0])

for i in quadrado:
    if sum(i)!=primeira_soma:
        certo = False
        break

#verifica colunas
if certo:
    for i in range(len(quadrado)):
        soma = quadrado[0][i]+quadrado[1][i]+quadrado[2][i]
        if soma != primeira_soma:
            certo = False
            break

#verifica diagonal principal
if certo:
    soma=quadrado[0][0]+quadrado[1][1]+quadrado[2][2]
    if soma != primeira_soma:
        certo = False

if certo:
    soma=quadrado[0][2]+quadrado[1][1]+quadrado[2][0]
    if soma != primeira_soma:
        certo = False


if certo:
    print('SIM')
else:
    print('NAO')
