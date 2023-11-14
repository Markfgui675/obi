s = input()
vogais = ['a', 'e', 'i', 'o', 'u']
calabreso = []
certo = True
i = 0
f = len(s)-1
while i < f:
    if s[i] in vogais and s[f] in vogais:
        if s[i] != s[f]:
            certo = False
            break
        i+=1
        f-=1
    else:
        if s[i] not in vogais:
            i+=1
        if s[f] not in vogais:
            f-=1

print('S' if certo else 'N')
