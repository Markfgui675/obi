res = []

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

while True:
    try:
        n = int(input())
        grid_inicial = list(map(int, input().split()))
        grid_final = list(map(int, input().split()))
        passos_inicial = ordena(grid_inicial)
        passos_final = ordena(grid_final)
        res.append(abs(passos_final-passos_inicial))
    except EOFError:
        break

for r in res:
    print(r)
