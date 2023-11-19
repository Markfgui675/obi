n, m = map(int, input().split())
pinos = list(map(int, input().split()))
certo = False
movimentos = 0
i = 0
certos = 0
while not certo:
    if i+1 <= len(pinos):
        if pinos[i] != m:
            dif = m-pinos[i]
            pinos[i]+=dif
            pinos[i+1]+=dif
            movimentos+=abs(dif)
        i+=1
    for j in pinos:
        if j != m:
            certos = 0
            break
        certos +=1
    certo = True if certos == len(pinos) else False
print(movimentos)
