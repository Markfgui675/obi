n = int(input())
ouro = True
top_jogadores = 0

for i in range(n):
    x = int(input())
    y = int(input())
    ludimilo = (x*5)-(y*3)
    if ludimilo <= 40:
        ouro = False
    else:
        top_jogadores+=1

if ouro:
    print(f'{top_jogadores}+')
else:
    print(f'{top_jogadores}')
