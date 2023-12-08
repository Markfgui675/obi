n = int(input())
k = int(input())

cota = k
soma = 0

if n <= 60:
    cota+=n
    soma = cota*1500
else:
    cota+=60
    restante = n-cota
    soma = (cota*1500)+(restante*3000)
print(soma)
