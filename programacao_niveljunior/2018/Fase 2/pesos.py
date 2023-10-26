n = int(input())
c = input().split(' ')
caixas = [int(x) for x in c]
pode = 0
for i in range(len(caixas)):
    if i == 0:
        if caixas[i] <= 8:
            pode+=1
    else:
        if caixas[i]-caixas[i-1] <= 8:
            pode+=1

print('S' if pode == len(caixas) else 'N')
        