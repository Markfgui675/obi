seq = list(map(int, input().split()))
correto = False
anterior = 0
ultra_anterior = 0
for s in range(len(seq)):
    if s == 0:
        anterior = seq[s]
    else:
        if seq[s] != anterior and seq[s] == ultra_anterior:
            correto = True
        ultra_anterior = anterior
        anterior = seq[s]
print('V' if correto else 'F')