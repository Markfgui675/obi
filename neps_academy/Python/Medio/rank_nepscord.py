rank = []
#[ xp, nome, último minuto ]

us = []

n, k = map(int, input().split())
for i in range(n):
    u, m = map(str, input().split())
    if u not in us:
        us.append(u)
        rank.append([u, 25, int(m)])
    else:
        for r in rank:
            if r[0] == u:
                if int(m) >= r[2]+k:
                    r[1]+=25
                r[2] = int(m)
                break

for ra in rank:
    ra.pop()
max_rank = max(rank, key=lambda x: x[1])[-1]
rank = sorted(rank, key=lambda x: x[0])
rank_final = []
for ra in rank:
    if ra[1] == max_rank:
        rank_final.append(ra)
    if len(rank_final) == 3:
        break

if len(rank_final) < 3:
    for ra in rank:
        if ra[1] < max_rank:
            rank_final.append(ra)
        if len(rank_final) == 3:
            break


print('--Rank do Nepscord--')
for n in range(3):
    if n < len(rank_final):
        print(f'#{n+1}. {rank_final[n][0]} - {'Nivel 2'if rank_final[n][1] >= 100 else 'Nivel 1'}')
    else:
        print(f'#{n+1}')
