notas = list(map(int, input().split()))
notas = sorted(notas, reverse=True)
print(sum(notas[:2]))
