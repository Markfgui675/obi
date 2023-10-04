letras = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','x','z']

c = str(input(''))

letras_c_semordem = []
for x in range(len(c)):
    if x == 0:
        letras_c_semordem.append(c[x])
    else:
        if (c[x] != ' ') and (c[x] != ',') and (c[x] != ':'):
            if c[x] not in letras_c_semordem:
                letras_c_semordem.append(c[x])

if letras_c_semordem == letras:
    print('S')
else:
    print('N')
