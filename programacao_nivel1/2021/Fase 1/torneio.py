vitorias = 0
for p in range(6):
    r = input()
    vitorias = vitorias + 1 if r == 'V' else vitorias + 0

if vitorias == 0:
    print(-1)
elif vitorias <= 2:
    print(3)
elif vitorias <= 4:
    print(2)
elif vitorias <= 6:
    print(1)
