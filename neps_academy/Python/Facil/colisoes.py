x0, y0, x1, y1 = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

colisao = (x2 in range(x0, y1+1)) or (x3 in range(x0, y1+1)) or (x0 in range(x2, y3+1)) or (x1 in range(x2, y3+1))

if colisao:
    print(1)
else:
    print(0)
