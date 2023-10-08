n = int(input(''))
tamanhos = str(input('')).split(' ')
p = int(input(''))
m = int(input(''))

n_p = 0
n_m = 0
for i in range(len(tamanhos)):
    if int(tamanhos[i]) == 1:
        n_p+=1
    else:
        n_m+=1

if (n_p == p) and (n_m == m):
    print('S')
else:
    print('N')
