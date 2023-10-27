n = int(input())
vs = input().split(' ')
valores = [int(x) for x in vs]
consecutivos = []
existe = False
for v in range(len(valores)):
    if v == 0:
        valor_anterior = valores[v]
        consecutivos.append([1, valores[v]])
    else:
        if valor_anterior == valores[v]:
            for va in consecutivos:
                if va[1]==valores[v]:
                    va[0]+=1
        else:
            valor_anterior = valores[v]
            #verifica se já existe
            for e in consecutivos:
                if e[1] == valores[v]:
                    existe = True
                    e[0]=1
            if not existe:
                consecutivos.append([1, valores[v]])

print(sorted(consecutivos, reverse=True)[0][0])
