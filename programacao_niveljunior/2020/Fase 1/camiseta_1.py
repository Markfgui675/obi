n = int(input())
camisetas = list(map(int, input().split()))
p = int(input())
m = int(input())
qtd_p = []
qtd_m = []
for k in camisetas:
    if k == 1:
        qtd_p.append(1)
    else:
        qtd_m.append(1)

if len(qtd_p) == p and len(qtd_m) == m:
    print('S')
else:
    print('N')
