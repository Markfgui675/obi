n = int(input())
mensagens = []
amigos = []
ultima = False
instante_atual = 0
for e in range(n):
    evento, amigo = map(str, input().split())
    ultima = False
    if evento == 'T':
        instante_atual+=int(amigo)-1
    elif int(amigo) not in amigos:
        amigos.append(int(amigo))
        mensagens.append([int(amigo), 0, [[instante_atual, evento]]])
        ultima = True
    else:
        for m in mensagens:
            if int(amigo) == m[0]: 
                if len(m[2])%2!=0:
                    tempo_ultimo_vento = m[2][-1][0]
                    tempo_acumulado = instante_atual-tempo_ultimo_vento
                    m[1]+=tempo_acumulado
                m[2].append([instante_atual, evento])
        instante_atual+=1
    if ultima:
        instante_atual+=1

for m in mensagens:
    eventos = len(m[2])
    if eventos%2!=0:
        m[1] = -1

for k in sorted(mensagens):
    print(k[0], k[1])
