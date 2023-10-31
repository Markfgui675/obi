n = int(input())
gabarito = input()
resposta = input()
corretas = 0
for r in range(n):
    if gabarito[r]==resposta[r]:
        corretas+=1

print(corretas)
