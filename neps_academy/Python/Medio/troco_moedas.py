c = int(input())

cem = 0
cinquenta = 0
vinte_cinco = 0
dez = 0
cinco = 0
um = 0

resto = c
while resto > 0:
    if resto >= 100:
        cem+=1
        resto-=100
    elif resto >= 50:
        cinquenta+=1
        resto-=50
    elif resto >= 25:
        vinte_cinco+=1
        resto-=25
    elif resto >= 10:
        dez+=1
        resto-=10
    elif resto >= 5:
        cinco+=1
        resto-=5
    elif resto >= 1:
        um+=1
        resto-=1

print(cem+cinquenta+vinte_cinco+dez+cinco+um)
print(cem)
print(cinquenta)
print(vinte_cinco)
print(dez)
print(cinco)
print(um)
