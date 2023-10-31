tempos = []
for t in range(3):
    r = int(input())
    tempos.append([r, t+1])
for j in sorted(tempos):
    print(j[1])
