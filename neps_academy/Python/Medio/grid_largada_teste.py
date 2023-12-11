n = int(input())
grid_inicial = list(map(int, input().split()))
grid_final = list(map(int, input().split()))

def ordena(lista: list[int]) -> int:
    passos = 0
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                ordenado = False
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                passos+=1
    return passos

passos_inicial = ordena(grid_inicial)
passos_final = ordena(grid_final)

print(abs(passos_inicial-passos_final))
