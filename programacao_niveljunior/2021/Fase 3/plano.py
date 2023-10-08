n = int(input(''))
m = int(input(''))
v_i = []
for v in range(m):
    v_i.append(int(input('')))

vagas_ocupadas = []
for c in range(m):
    if v_i[c] not in vagas_ocupadas:
        vagas_ocupadas.append(v_i[c])

print(len(vagas_ocupadas))
