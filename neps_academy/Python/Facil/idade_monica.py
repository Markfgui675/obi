idades = []
m = int(input())
m1 = int(input())
m2 = int(input())

idades.append(m1)
idades.append(m2)
c = m - (m1+m2)
idades.append(c)
print(sorted(idades)[-1])
