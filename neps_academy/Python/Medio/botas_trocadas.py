#lista = [[41, ['e'], ['d']], [40, ['e'], ['d']]]

n = int(input())
pares = 0
lista = []
numeros = []

for i in range(n):
    numero, pe = map(str, input().split())
    if numero not in numeros:
        numeros.append(numero)
        if pe == 'D':
            lista.append([numero, [], [pe]])
        else:
            lista.append([numero, [pe], []])
    else:
        fim = len(lista)-1
        inicio = 0
        lo = sorted(lista)
        while inicio <= fim:
            meio = (inicio+fim)//2
            if lo[meio][0] == numero:
                if pe == 'D':
                    lo[meio][2].append(pe)
                else:
                    lo[meio][1].append(pe)
                if len(lo[meio][1]) > 0 and len(lo[meio][2]) > 0 and (len(lo[meio][1])+len(lo[meio][2]))%2==0 and (len(lo[meio][1])+len(lo[meio][2])) > 0:
                    pares+=1
                break
            elif lo[meio][0] > numero:
                fim = meio -1
            else:
                inicio = meio + 1
print(pares)
