a = int(input())
b = int(input())

m = str((a*b)/2).split('.')
if m[1]!='0':
    n = f'{m[0]}.{m[1]}'
    print(n)
else:
    print(m[0])
