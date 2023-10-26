from itertools import product, combinations

n,i,f = map(int, input().split())
lista = input().split(' ')
lista = [int(x) for x in lista]
permsList = []
genComb = product(lista, repeat=2)
for subset in genComb:
    soma_valida = False
    if sum(list(subset)) >= i and sum(list(subset)) <= f:
        soma_valida = True
        if len(permsList) == 0:
            permsList.append(list(subset))
    reverso = list(subset)
    reverso.reverse()
    dif = 0
    for y in permsList:
        if list(subset) != y:
            dif+=1
        if reverso != y:
            dif+=1
        if list(subset)[0] != list(subset)[1]:
            dif+=1
    if dif==3*len(permsList) and soma_valida:
        permsList.append(list(subset))

print(len(permsList))
