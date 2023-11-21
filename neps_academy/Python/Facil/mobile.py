a = int(input())
b = int(input())
c = int(input())
d = int(input())

certos = 0
if a == (b + c + d):
    certos+=1
if d == (b + c):
    certos+=1
if b == c:
    certos+=1

if certos == 3:
    print('S')
else:
    print('N')
