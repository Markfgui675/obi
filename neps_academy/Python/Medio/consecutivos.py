def calcular_pontos(N, valores):
    max_pontos = 1
    pontos_atual = 1

    for i in range(1, N):
        if valores[i] == valores[i - 1]:
            pontos_atual += 1
        else:
            max_pontos = max(max_pontos, pontos_atual)
            pontos_atual = 1

    return max(max_pontos, pontos_atual)

# Leitura da entrada
N = int(input())
valores = list(map(int, input().split()))

# Chamada da função e impressão do resultado
pontos = calcular_pontos(N, valores)
print(pontos)
