n, t = map(int, input().split())
c = input().split(' ')
b = input().split(' ')
cima = [int(C) for C in c]
baixo = [int(B) for B in b]
operacoes = []

for p in range(t):
    i, j = map(int, input().split())
    operacoes.append([i,j])

for operacao in operacoes:
    I = operacao[0]-1
    J = operacao[1]
    intervalo_cima = cima[I:J]
    intervalo_baixo = baixo[I:J]
    baixo[I:J] = intervalo_cima
    cima[I:J] = intervalo_baixo

for a in cima:
    print(a, end=' ')
