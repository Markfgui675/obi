n = int(input())
dias = 0
qtd_acessos = 0
objetivo = 1000000
acessos = []
for d in range(n):
    acessos.append(int(input()))

for v in range(len(acessos)):
    dias+=1
    qtd_acessos+=acessos[v]
    if qtd_acessos>=objetivo:
        break

print(dias)