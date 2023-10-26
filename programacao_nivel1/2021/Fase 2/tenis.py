jogadores = []

for k in range(4):
    n = int(input())
    jogadores.append((k, n))

combinations = []
for c in range(len(jogadores)):
    j1 = jogadores[c]
    for j2 in range(len(jogadores)):
        if jogadores.index(j1) != jogadores.index(jogadores[j2]):
            j1j2 = sorted([j1, jogadores[j2]])
            if j1j2 not in combinations:
                combinations.append(j1j2) 

def dois_times(time1: list[tuple], time2: list[tuple]) -> bool:
    for j1 in time1:
        for j2 in time2:
            if j1 == j2:
                return False
    return True

dif = 0
forca = 0
for j in range(len(combinations)):
    dupla1 = [combinations[j][0], combinations[j][1]]
    for jj in range(len(combinations)):
        dupla2 = [combinations[jj][0], combinations[jj][1]]
        if dupla1 != dupla2:
            if dois_times(dupla1, dupla2):
                if (dupla1[0][1]+dupla1[1][1])>(dupla2[0][1]+dupla2[1][1]):
                    dif = (dupla1[0][1]+dupla1[1][1])-(dupla2[0][1]+dupla2[1][1])
                elif (dupla1[0][1]+dupla1[1][1])<(dupla2[0][1]+dupla2[1][1]):
                    dif = (dupla2[0][1]+dupla2[1][1])-(dupla1[0][1]+dupla1[1][1])
                else:
                    dif = (dupla1[0][1]+dupla1[1][1])-(dupla2[0][1]+dupla2[1][1])

        if j == 0:
            forca = dif
        else:
            if dif < forca:
                forca = dif

print(forca)    