times = []
jogadores = []

n, t = map(int, input().split())

for tt in range(t):
    times.append([])

for i in range(n):
    j = input().split(' ')
    jogadores.append([int(j[1]), j[0]])

c = 0
for tt in sorted(jogadores, reverse=True):
    if c > len(times)-1:
        c = 0
    times[c].append(tt[1])
    c+=1

for t in range(len(times)):
    print(f'Time {t+1}')
    for k in sorted(times[t]):
        print(k)
    print()
