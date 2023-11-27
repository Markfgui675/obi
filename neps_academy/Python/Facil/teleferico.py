c = int(input())
a = int(input())

if a < c:
    print(1)
else:
    qtd_inicial = c-1
    viagens = 1
    while qtd_inicial < a:
        dif = a - qtd_inicial
        if dif > c-1:
            qtd_inicial+=c-1
            viagens+=1
        else:
            qtd_inicial+=dif
            viagens+=1
    print(viagens)
