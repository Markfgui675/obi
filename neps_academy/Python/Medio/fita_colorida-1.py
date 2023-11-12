n = int(input())
nums = list(map(int, input().split()))
res = []
for n in range(len(nums)):
    tom = []
    if nums[n] == 0:
        res.append(0)
    else:
        zero_encontrado_direita = False
        zero_encontrado_esquerda = False
        dif = 0
        # verifica direita
        for nd in nums[n:]:
            if nd == 0:
                zero_encontrado_direita = True
                break
            dif+=1
        tom.append(dif)
        dif = 0
        #verifica esquerda
        for ne in range(len(nums[:n]), -1, -1):
            if nums[ne] == 0:
                zero_encontrado_esquerda = True
                break
            dif+=1
        if (ne > 0 and dif > 0) or zero_encontrado_esquerda or zero_encontrado_direita:
            tom.append(dif)

        #verifica qual é menor e adiciona de acordo com o tom na lista 'res'
        if zero_encontrado_esquerda and zero_encontrado_direita:
            if tom[0] > 9 or tom[1] > 9:
                res.append(9)
            else:
                res.append(min(tom))
        elif zero_encontrado_esquerda and not zero_encontrado_direita:
            if tom[1] > 9:
                res.append(9)
            else:
                res.append(tom[1])
        elif zero_encontrado_direita and not zero_encontrado_esquerda:
            if tom[0] > 9:
                res.append(9)
            else:
                res.append(tom[0])
        tom.clear()

for r in res:
    print(r, end=' ')
