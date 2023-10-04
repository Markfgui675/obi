def menorDif(niveis):
    min_dif = 0
    t1 = 0
    t2 = 0
    lista = niveis
    for y in range(len(niveis)):
        if y == len(niveis)-1:
            return min_dif
        else:
            t1 = lista[0]+lista[y+1]
            lista = lista.pop()

niveis = []
for n in range(4):
    niveis.append(int(input('')))

resultado = menorDif(niveis)
print(resultado)

# todo: terminar a implementação da lógica
