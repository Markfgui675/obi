palavra = input().lower()
repetidas = []
qtd_repetidas = []
for l in palavra:
    if l not in repetidas and l != ' ':
        repetidas.append(l)
        qtd_repetidas.append([1, l])
    else:
        for ll in qtd_repetidas:
            if l == ll[1]:
                ll[0]+=1
                break

print(f'A letra que mais apareceu foi {sorted(qtd_repetidas, reverse=True)[0][1]}, {sorted(qtd_repetidas, reverse=True)[0][0]}x')