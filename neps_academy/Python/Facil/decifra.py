alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o ', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

permutacao = input()
criptografia = input()
frase = ''

for i in range(len(criptografia)):
    frase+=alfabeto[permutacao.index(criptografia[i])]

frase_final = ''
for f in frase:
    if f!=' ':
        frase_final+=f

print(frase_final)
