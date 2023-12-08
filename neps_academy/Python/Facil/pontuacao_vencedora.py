m3 = int(input())
m2 = int(input())
m1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

pontos_m = (3*m3)+(2*m2)+m1
pontos_b = (3*b3)+(2*b2)+b1

if pontos_m == pontos_b:
    print('T')
elif pontos_m > pontos_b:
    print('A')
else:
    print('B')
