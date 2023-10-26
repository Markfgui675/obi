from itertools import combinations

jogadores = []
for j in range(4):
    jogadores.append(int(input()))

print(list(combinations(jogadores, 2))) 
combinations = []
for c in range(len(jogadores)):
    j1 = jogadores[c]
    for j2 in range(len(jogadores)):
        if jogadores.index(j1) != jogadores.index(jogadores[j2]):
            j1j2 = sorted([j1, jogadores[j2]])
            if j1j2 not in combinations:
                combinations.append(j1j2) 
