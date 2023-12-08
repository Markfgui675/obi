n, x, y, r = map(int, input().split())

tangente_minima_x = x-r-1
tangente_maxima_x = x+r+1
tangente_minima_y = y-r-1
tangente_maxima_y = y+r+1

tiros_certos = 0

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if ((x1==tangente_minima_x or x1==tangente_maxima_x) or (y1==tangente_minima_y or y1==tangente_maxima_x)) or (x1==x and y1==y):
        tiros_certos+=1
    if ((x2==tangente_minima_x or x2==tangente_maxima_x) or (y2==tangente_minima_y or y2==tangente_maxima_x)) or (x2==x and y2==y):
        tiros_certos+=1

print(tiros_certos)
