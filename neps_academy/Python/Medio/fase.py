n = int(input())
k = int(input())

pontuacoes = []

for i in range(n):
    pontuacoes.append(int(input()))

pontuacoes = sorted(pontuacoes, reverse=True)

jogadores_classificados = pontuacoes[:k]

pront = False
pos_v = len(jogadores_classificados)

while True:

    if pontuacoes[pos_v] < jogadores_classificados[-1]:
        pront = True
    else:
        jogadores_classificados.append(pontuacoes[pos_v])
        pos_v+=1

    if pront or pos_v+1>n:
        break

print(len(jogadores_classificados))
