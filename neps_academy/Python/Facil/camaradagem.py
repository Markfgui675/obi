w, n, p = map(int, input().split())
socos = list(map(int, input().split()))
validos = 0

for s in socos:
    if s in range(w, n+1):
        validos+=1

print(validos)
