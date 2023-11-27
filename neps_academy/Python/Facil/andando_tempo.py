creditos = list(map(int, input().split()))
a = creditos[0]
b = creditos[1]
c = creditos[2]
if a + b == c or b + c == a or a + c == b or a == b or a == c or b == c:
    print('S')
else:
    print('N')
