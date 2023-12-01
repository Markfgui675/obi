n = int(input())

jogo = []
for i in range(n):
    jogo.append(input())

comida = 0
comidas = []
k = 1
for j in jogo:
    if k%2==0:
        #começa do fim
        reverse_list = list(j)
        reverse_list.reverse()
        for jj in reverse_list:
            if jj == 'A':
                comidas.append(comida)
                comida = 0
            elif jj == 'o':
                comida+=1
    else:
        #começa do início
        for jj in j:
            if jj == 'A':
                comidas.append(comida)
                comida = 0
            elif jj == 'o':
                comida+=1

    k+=1
comidas.append(comida)
print(max(comidas))
