v = int(input())
s = [1,5,10,25,50,100]
resto = v
moedas = 0
while resto > 0:
    if resto >= 100:
        resto-=100
        moedas+=1
    elif resto >= 50:
        resto-=50
        moedas+=1
    elif resto >= 25:
        resto-=25
        moedas+=1
    elif resto >= 10:
        resto-=10
        moedas+=1
    elif resto >= 5:
        resto-=5
        moedas+=1
    elif resto >= 1:
        resto-=1
        moedas+=1

print(moedas)
