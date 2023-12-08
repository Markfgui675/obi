p = int(input())
c = int(input())

pontos = (p*50)-(c*10)
pontos += 500 if p > c else 0

print(pontos)
