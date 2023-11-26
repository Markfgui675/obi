s = input()
vogais = ['a','e', 'i', 'o', 'u']
v = []
nv = []
for ss in s:
    if ss not in vogais:
        nv.append(ss)
    else:
        v.append(ss)

print('Vogais:', end=' ')
for vv in v:
    print(vv, end='')
print()
print('Consoantes:', end=' ')
for nvv in nv:
    print(nvv, end='')
