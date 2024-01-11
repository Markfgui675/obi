n = int(input())
divisores = []
for i in range(1, n+1):
    if n%i==0:
        divisores.append(i)

print(f'{len(divisores)} divisor(es): ', end='')
for p in divisores:
    print(p, end=' ')
print()
print(f'Soma de divisores = {sum(divisores)}')
print('Primo' if len(divisores) == 2 else 'Nao primo')
