tomadas = list(map(int, input().split()))

soma = 0
for t in tomadas:
    soma+=t-1

print(soma+1)
