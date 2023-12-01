bolas = list(map(int, input().split()))

#verifica bolas que se repetem
balls = []
B = []
for b in bolas:
    if b not in B:
        B.append(b)
        balls.append([1, b])
    else:
        for bb in balls:
            if bb[1] == b:
                bb[0]+=1
                break

if len(bolas)%2==0:
    c = max(balls, key=lambda x: x[0])[0] <= len(bolas)//2
else:
    c = max(balls, key=lambda x: x[0])[0] < len(bolas)//2 or max(balls, key=lambda x: x[0])[0] <= len(bolas)//2+1

if c:
    print('S')
else:
    print('N')
