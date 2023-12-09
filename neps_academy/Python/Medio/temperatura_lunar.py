res = []

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    temperaturas = []
    for t in range(n):
        temperaturas.append(int(input()))
    medias = []
    i = m
    c = 0
    while i < len(temperaturas)+1:
        medias.append(int(sum(temperaturas[c:i])/m))
        i+=1
        c+=1
    
    res.append([min(medias), max(medias)])


for idx, r in enumerate(res, start=1):
    print(f'Teste {idx}')
    print(*r, end=' ')
    print()
    print()
