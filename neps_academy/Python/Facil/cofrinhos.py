res = []

def conta(status: bool, j: int, z: int) -> int:
    r = 0
    if not status:
        if j > z:
            dif = j - z
            r = dif
        elif j < z:
            dif = z - j
            r = -dif
    else:
        if j > z:
            dif = j - z
            r = -dif
        elif j < z:
            dif = z - j
            r = dif
    return r    



while True:
    n = int(input())
    if n == 0:
        break
    ultima_dif = 0
    lista = []
    invertido = False
    for i in range(n):
        j, z = map(int, input().split())
        if j!=z and len(lista) == 0 and j > z:
            invertido = True
        if j!=z:
            result = conta(invertido, j, z)
            lista.append(ultima_dif+result)
            ultima_dif=lista[-1]
        else:
            lista.append(lista[-1])
    res.append(lista[:])
    lista.clear()

for r in range(len(res)):
    print(f'Teste {r+1}')
    for rr in res[r]:
        print(rr)
    print()
        
