info_ncs = str(input('')).split(' ')
info_c = str(input('')).split(' ')
s = int(info_ncs[2])

C = []
for l in range(len(info_c)):
    C.append(int(info_c[l]))

n_list = []
for n in range(int(info_ncs[0])):
    n_list.append(n+1)

estacao_atual = 1
vezes_na_estacao_s = 0

for k in range(len(C)):
    if k == 0:
        if estacao_atual == s:
            vezes_na_estacao_s+=1
    if C[k] == 1:
        if estacao_atual == n_list[-1]:
            estacao_atual=1
        else:
            estacao_atual+=1
        vezes_na_estacao_s += 1 if estacao_atual == s else 0
    if C[k] == -1:
        if estacao_atual == 1:
            estacao_atual=n_list[-1]
        else:
            estacao_atual-=1
        vezes_na_estacao_s += 1 if estacao_atual == s else 0

print(vezes_na_estacao_s)
