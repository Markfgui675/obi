tacos = set()
c = int(input())
consultas = list(map(int, input().split()))
tacos_produzidos = 0
for t in consultas:
    if t in tacos:
        tacos.remove(t)
    else:
        tacos_produzidos+=2
        tacos.add(t)
print(tacos_produzidos)
