n = int(input(''))
nums_string = []

for t in range(n):
    nums_string.append(str(input('')))

soma = 0
base = 0
potencia = 0
x = 0
for k in range(len(nums_string)):
    potencia = int(nums_string[k][-1])
    base = int(nums_string[k][:-1])
    x = base**potencia
    soma += x

print(soma)
