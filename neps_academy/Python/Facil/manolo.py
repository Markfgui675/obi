n, c = map(int, input().split())
preco_total = 0

for i in range(n):
    if c > 1:
        preco_total+=c
        c-=1
    else:
        preco_total+=1

print(preco_total)

