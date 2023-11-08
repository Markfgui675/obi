x = int(input())
divisores = 0
for i in range(x):
    if i > 0:
        if x%i==0:
            divisores+=1
    if divisores > 2:
        break
if divisores > 2:
    print('N')
else:
    print('S')
