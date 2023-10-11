a = int(input(''))
b = int(input(''))
c = a + b
p_i = []
tem_como = False
meio = int(c/2)
x_i = 0

for x in range(meio, 0, -1):
    x_i+=1
    if x*x_i==c:
        p_i.append(x_i)
        p_i.append(x)
        tem_como = True
        break

if tem_como:
    for p in sorted(p_i):
        print(p, end=' ')
else:
    print('-1 -1')
