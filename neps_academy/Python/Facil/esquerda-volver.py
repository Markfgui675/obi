n = int(input())
comandos = input()

direcoes = ['N', 'L', 'S', 'O']
d = 0

for c in comandos:
    if c == 'D' and d == 3:
        d = 0
    elif c == 'D':
        d+=1
    elif c == 'E' and d == 0:
        d = 3
    else:
        d-=1

print(direcoes[d])
