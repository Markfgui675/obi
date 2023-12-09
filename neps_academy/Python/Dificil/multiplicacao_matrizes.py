n = int(input())
matriz_a = []
matriz_b = []

p, q, r, s, x, y = map(int, input().split())

def multiplicar_matrizes(matriz1, matriz2):
    linhas_matriz1 = len(matriz1)
    colunas_matriz1 = len(matriz1[0])
    linhas_matriz2 = len(matriz2)
    colunas_matriz2 = len(matriz2[0])

    # Verifica se as matrizes podem ser multiplicadas
    if colunas_matriz1 != linhas_matriz2:
        raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")

    # Inicializa a matriz resultante com zeros
    resultado = [[0 for _ in range(colunas_matriz2)] for _ in range(linhas_matriz1)]

    # Realiza a multiplicação das matrizes
    for i in range(linhas_matriz1):
        for j in range(colunas_matriz2):
            for k in range(colunas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado


for i in range(1, n+1):
    nums_a = []
    nums_b = []
    for j in range(1, n+1):
        nums_a.append(((p*i)+(q*j)%x))
        nums_b.append(((r*i)+(s*j)%y))
    matriz_a.append(nums_a[:])
    matriz_b.append(nums_b[:])
    nums_a.clear()
    nums_b.clear()


result = multiplicar_matrizes(matriz1=matriz_a, matriz2=matriz_b)
print(result[i-1][j-1])