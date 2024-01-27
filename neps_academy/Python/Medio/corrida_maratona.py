n = int(input())
tempos = list(map(int, input().split()))
ordem = tempos[:]
ordem = sorted(ordem)
ordem_final = []
for i in range(n):
    ordem_final.append(ordem.index(tempos[i])+1)
for r in ordem_final:
    print(r)
