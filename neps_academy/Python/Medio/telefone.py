telefone = list(input())

numero_2 = ['A', 'B', 'C']
numero_3 = ['D', 'E', 'F']
numero_4 = ['G', 'H', 'I']
numero_5 = ['J', 'K', 'L']
numero_6 = ['M', 'N', 'O']
numero_7 = ['P', 'Q', 'R', 'S']
numero_8 = ['T', 'U', 'V']
numero_9 = ['W', 'X', 'Y', 'Z']

for t in range(len(telefone)):
    if telefone[t] in numero_2:
        telefone[t] = 2
    if telefone[t] in numero_3:
        telefone[t] = 3
    if telefone[t] in numero_4:
        telefone[t] = 4
    if telefone[t] in numero_5:
        telefone[t] = 5
    if telefone[t] in numero_6:
        telefone[t] = 6
    if telefone[t] in numero_7:
        telefone[t] = 7
    if telefone[t] in numero_8:
        telefone[t] = 8
    if telefone[t] in numero_9:
        telefone[t] = 9

for tel in telefone:
    print(tel, end='')
