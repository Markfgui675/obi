n = int(input())
k = int(input())

cota_total = k+60
preco = 0

if cota_total >= n:
    preco = n*1500
elif cota_total < n:
    dif = n-cota_total
    preco = cota_total*1500
    preco+=dif*3000

print(preco)
