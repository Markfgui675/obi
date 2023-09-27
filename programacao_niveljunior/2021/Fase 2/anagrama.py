def anagrama(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return 'S'
    else:
        for x in range(len(s1)):
            if s1[x] == '.' or s1[x] == ',':
                s1[x] = ' '
        for y in range(len(s2)):
            if s2[y] == '.' or s2[y] == ',':
                s2[y] = ' '

        pos = 0
        iguais = True

        while pos < len(s1) and iguais:
            if s1[pos] == s2[pos]:
                pos+=1
            else:
                iguais = False
        
        if iguais:
            return 'S'
        else:
            return 'N'

n = int(input(''))
s1 = str(input(''))
s2 = str(input(''))
resultado = anagrama(s1,s2)
print(resultado)
