x, l, r = map(int, input().split())

menor = 0
difs = []

for i in range(l, r+1):
    if i == l:
        menor = i
        difs.append(abs(i-x))
    else:
        y = abs(x-i)
        if y < difs[-1]:
            menor = i
            difs.append(y)

print(menor)
