qtd_minas = []
minas = []

n = int(input())
for m in range(n):
    minas.append(int(input()))

for l in range(len(minas)):
    q_mina = 0
    if l == 0:
        if minas[l] == 1:
            q_mina+=1
        if l+1 <= len(minas)-1:
            if minas[l+1] == 1:
                q_mina+=1
    else:
        if minas[l] == 1:
            q_mina+=1
        if l+1 <= len(minas)-1:
            if minas[l+1] == 1:
                q_mina+=1
        if minas[l-1] == 1:
            q_mina+=1
    qtd_minas.append(q_mina)
for q in qtd_minas:
    print(q)
