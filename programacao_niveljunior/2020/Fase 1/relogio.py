r = int(input('')) # repouso
f = int(input('')) # atual
c = int(input('')) # oxigenação

if f>r*3 or c < 95:
    print('diminuir')
elif f<r*2 and c>97:
    print('aumentar')
else:
    print('manter')
