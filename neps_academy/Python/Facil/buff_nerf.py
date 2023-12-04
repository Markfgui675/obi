n,d,m,p = map(int, input().split())

f1 = n*d
f2 = m*p

if f1 < f2:
    print('BUFF')
else:
    print('NERF')
