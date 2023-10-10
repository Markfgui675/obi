palavra1 = str(input(''))
palavra2 = str(input(''))
existe = False
for i in range(len(palavra1), 0, -1):
    for j in range(len(palavra2), 0, -1):
        if palavra1[i-1] == palavra2[j-1]:
            print(f'{i} {j}')
            existe = True
            break
    if existe:
        break
if not existe:
    print(f'{-1} {-1}')