a = int(input(''))
s = int(input(''))
d = int(input(''))

distancia_percorrida = 0
dias = 0

while distancia_percorrida<=a:
    dias+=1
    distancia_percorrida+=s
    if distancia_percorrida>=a:
        break
    else:
        distancia_percorrida-=d

print(dias)
