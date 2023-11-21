n, m = map(int, input().split())
premio_intervalo = list(map(int, input().split()))
premio = list(map(int, input().split()))
ogros = list(map(int, input().split()))
res = []

def busca_binaria(arr, x): #O(log n)
    esquerda, direita = 0, len(arr) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if arr[meio] == x:
            return meio + 1
        elif arr[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return esquerda

for gg in ogros: #O(n)
    indice = busca_binaria(premio_intervalo, gg)

    if indice == 0:
        res.append(premio[0])
    elif indice == len(premio_intervalo):
        res.append(premio[-1])
    else:
        res.append(premio[indice])

for r in res:
    print(r, end=' ')

# Complexidade: O(n*O(log n))
# O(n log n)
