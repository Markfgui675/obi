def busca(lista, nome_pesquisado):
    tamanho_da_lista = len(lista)
    inicio = 0
    fim=tamanho_da_lista-1

    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista[meio] == nome_pesquisado:
            return meio
        elif lista[meio] < nome_pesquisado:
            inicio=meio+1
        elif lista[meio] > nome_pesquisado:
            fim = meio-1

    return -1

lista = ['Marcos', 'Jorge', 'Isabelly', 'Kaio', 'Lucas', 'Ana', 'Fatima', 'Maria', 'Claudio', 'Igor', 'Zuleida']
lista2 = [2,2,4,7,11,21,23,30,41]
resultado = busca(sorted(lista2), 30)
print(resultado)
