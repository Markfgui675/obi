m = int(input())
h = m / 60
if h > 0:
    hh = str(h).split('.')
    horas = int(hh[0])
    if hh[1] != 0:
        minutos = m-(horas*60)
    else:
        minutos = 0

print(horas)
print(minutos)