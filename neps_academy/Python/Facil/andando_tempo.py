creditos = list(map(int, input().split()))
tem_como = False
def primeira_tentativa():
    global tem_como
    c = creditos[:]
    maximo = max(creditos)
    c.remove(maximo)
    if sum(c) == maximo:
        tem_como = True

primeira_tentativa()

if not tem_como:
    maximo = max(creditos)
    p_m = 0
    for i in creditos:
        if i == maximo:
            p_m+=1
        if p_m >= 2:
            tem_como = True
            break

print('S' if tem_como else 'N')
