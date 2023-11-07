o = input()
n1, n2 = map(float, input().split())
if o == 'M':
    print(f'{(n1*n2):.2f}')
elif o == 'D':
    print(f'{(n1/n2):.2f}')