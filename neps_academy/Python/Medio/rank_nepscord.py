rank = []
us = []

n, k = map(int, input().split())
for i in range(n):
    u, m = map(str, input().split())
    if u not in us:
        us.append(u)
    else:
        ...

for n in range(3):
    if n < len(rank):
        print(f'#{n+1}', rank[n])
    else:
        print(f'#{n+1}')
