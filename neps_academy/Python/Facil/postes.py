n = int(input())
arr = list(map(int, input().split()))

substituido = 0
consertado = 0

for i in arr:
    if i < 50:
        substituido+=1
    elif i >= 50 and i < 85:
        consertado+=1

print(substituido, consertado)
