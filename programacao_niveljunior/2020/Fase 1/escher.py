n = int(input(''))
ns = str(input('')).split(' ')
nums = [int(x) for x in ns]

somas = int(len(nums)/2)
primeira_soma = nums[0]+nums[-1]
soma_atual = 0
v = 0

if n%2!=0:
    elemento_meio = nums[somas]
    if elemento_meio == primeira_soma:
        for r in range(somas):
            ultimo = nums[-(r+1)]
            atual = nums[r]
            soma_atual = atual+ultimo
            if soma_atual == primeira_soma:
                v+=1
        
else:
    for r in range(somas):
        ultimo = nums[-(r+1)]
        atual = nums[r]
        soma_atual = atual+ultimo
        if soma_atual == primeira_soma:
            v+=1

if v == somas:
    print('S')
else:
    print('N')
