res = []

def busca(arr: list[int], x: int):
    fim = len(arr)-1
    inicio = 0
    while inicio <= fim:
        meio = (fim+inicio)//2
        if arr[meio][1] == x:
            arr[meio][0]+=1
            break
        elif arr[meio][1] > x:
            fim = meio - 1
        else:
            inicio = meio + 1


while True:
    a, v = map(int, input().split())
    if a == 0 and v == 0:
        break
    voos = []

    for aa in range(a):
        voos.append([0, (aa+1)])

    for aa in range(v):
        ino, voltano = map(int, input().split())
        busca(voos, ino)
        busca(voos, voltano)
    
    maximo = max(voos)[0]
    l = []
    for r in sorted(voos, reverse=True):
        if r[0] < maximo:
            break
        else:
            l.append(r[1])
    res.append(l)



for r in range(len(res)):
    print(f'Teste {r+1}')
    for rr in sorted(res[r]):
        print(rr, end=' ')
    print()
