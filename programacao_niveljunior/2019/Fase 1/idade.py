idades = []

m = int(input())
idades.append(int(input()))
idades.append(int(input()))

f = m-(sum(idades))

if f > max(idades):
    print(f)
else:
    print(max(idades))