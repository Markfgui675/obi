n = int(input())
bonecas = list(map(int, input().split()))
bonecas_sort = sorted(bonecas)
dif = 0
res = []
for b in range(len(bonecas)):
    if bonecas[b] != bonecas_sort[b]:
        dif+=1
        res.append(bonecas[b])

print(dif)
for r in sorted(res):
    print(r, end=' ')
