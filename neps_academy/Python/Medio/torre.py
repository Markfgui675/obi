tabuleiro = []
m = int(input())
for i in range(m):
    j = list(map(int, input().split()))
    tabuleiro.append(j)

soma_linhas = []
soma_colunas = []
for l in tabuleiro:
    soma_linhas.append(sum(l))

for c in range(len(tabuleiro)):
    soma = 0
    for cc in range(len(tabuleiro)):
        soma+=tabuleiro[cc][c]
    soma_colunas.append(soma)

resp = []
for l in range(len(tabuleiro)):
    for c in range(len(tabuleiro)):
        resp.append(soma_linhas[l]+soma_colunas[c]-2*tabuleiro[l][c])

print(max(resp))
