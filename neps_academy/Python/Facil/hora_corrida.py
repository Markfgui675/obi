from math import ceil

v, n = map(int, input().split())
res = []
for i in range(9):
    c = ((v*n)*((i+1)*10))/100
    res.append(ceil(c))

for r in res:
    print(r, end=' ')
