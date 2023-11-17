n = int(input())
horarios = []
for i in range(n): # O(n)
    horarios.append(list(map(int, input().split())))

atendimentos = 0
for i in range(n): # O(n)
    if i == 0:
        atendimentos+=1
        termino=horarios[i][1]
    else:
        if horarios[i][0] >= termino:
            termino=horarios[i][1]
            atendimentos+=1

print(atendimentos)

# O(n) + O(n)
# O(2n)
# O(n)
