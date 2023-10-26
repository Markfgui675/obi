from math import sqrt

a = int(input())
b = int(input())
c = a + b
p_i = []
tem_como = False
meio = int(c/2)
x_i = 0

sqr = str(sqrt(c)).split('.')

if a<=2 or (a<=2 or b<2):
    print('-1 -1')
elif a==b:
    print('-1 -1')
elif sqr[1] == '0':
    print(f'{sqr[0]} {sqr[0]}')
else:
    for x in range(meio, 0, -1):
        x_i+=1
        if x*x_i==c:
            p_i.append(x_i)
            p_i.append(x)
            tem_como = True
            break
        for y in range(x_i):
            if y*x==c:
                p_i.append(y)
                p_i.append(x)
                tem_como = True
                break
        if tem_como:
            break

    if tem_como:
        print(sorted(p_i)[0], sorted(p_i)[1])
    else:
        print('-1 -1')
