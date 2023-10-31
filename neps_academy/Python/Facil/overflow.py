limite = int(input())
p,c,q = map(str, input().split())
if c == '*':
    conta = int(p)*int(q)
    if conta > limite:
        print('OVERFLOW')
    else:
        print('OK')
if c == '+':
    conta = int(p)+int(q)
    if conta > limite:
        print('OVERFLOW')
    else:
        print('OK')