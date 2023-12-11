n, m = map(int, input().split())
baus = list(map(int, input().split()))
chaves = list(map(int, input().split()))
baus_d = [[x, 0] for x in baus]
abriveis = 0
for mm in chaves:
    for bb in baus_d:
        if mm == bb[0]:
            if bb[1] == 0:
                bb[1] = 1
                abriveis+=1

print(abriveis)
