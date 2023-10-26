n = int(input())
m = int(input())
figurinhas = []
for x in range(m):
    f = int(input())
    if f not in figurinhas:
        figurinhas.append(f)

print(n - len(figurinhas))
