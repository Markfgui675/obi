letras = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','x','z']

c = str(input(''))

letras_c_semordem = []
for x in range(len(c)):
    if x == 0:
        if c[x] in letras:
            letras_c_semordem.append(c[x])
    else:
        if c[x] in letras and c[x] not in letras_c_semordem:
            letras_c_semordem.append(c[x])

if sorted(letras_c_semordem) == letras:
    print('S')
else:
    print('N')
