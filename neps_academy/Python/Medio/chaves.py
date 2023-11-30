n = int(input())
qtd = 0
erro = False
for l in range(n):
    s = input()
    for ss in s:
        if ss == '{':
            qtd+=1
        if ss == '}':
            if qtd < 1:
                erro = True
            qtd-=1
if erro or qtd>0:
    print('N')
else:
    print('S')
