caixas = []

for c in range(3):
    caixas.append(int(input('')))

# a, b e c

a = caixas[0]
b = caixas[1]
c = caixas[-1]

if (a+b) < c:
    print(1)
else:
    if a==b==c:
        print(3)
    elif a <= b:
        print(2)
