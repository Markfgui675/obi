resultados = []
for r in range(6):
    x = str(input(''))
    resultados.append(x)

vitorias = 0
for y in range(len(resultados)):
    if resultados[y] == 'V':
        vitorias+=1

if vitorias >= 5 and vitorias <= 6:
    print(1)
elif vitorias >= 3 and vitorias <= 4:
    print(2)
elif vitorias >= 1 and vitorias <= 2:
    print(3)
else:
    print(-1)
