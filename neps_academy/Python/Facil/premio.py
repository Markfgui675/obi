p = int(input())
d = int(input())
b = int(input())

pontos = p+(d*2)+(b*3)

if pontos >= 150:
    print('B')
elif pontos >= 120:
    print('D')
elif pontos >= 100:
    print('P')
else:
    print('N')
