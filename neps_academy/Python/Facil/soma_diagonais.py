matriz = [[], [], []]
for i in range(9):
    x = int(input())
    if i in range(0, 3):
        matriz[0].append(x)
    elif i in range(3, 6):
        matriz[1].append(x)
    else:
        matriz[2].append(x)

diagonal_principal = matriz[0][0]+matriz[1][1]+matriz[2][2]
diagonal_secundaria = matriz[0][2]+matriz[1][1]+matriz[2][0]

print(f'Diagonal principal: {diagonal_principal}')
print(f'Diagonal secundaria: {diagonal_secundaria}')
