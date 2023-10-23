k = int(input())
l = int(input())

def distancia(x:int,y:int):
    p = x-y
    jogo = ''
    if p<0:
      p = (-1)*p
    if p == 1:
        return 'oitavas'
    elif p in range(2,4):
        return 'quartas'
    elif p >= 4:
        return 'semifinal'


if (k >= 9 and l < 9) or (l >= 9 and k < 9):
    print('final')
else:
    print(distancia(k,l))
