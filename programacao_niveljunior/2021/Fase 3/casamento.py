lista1 = ''
lista2 = ''

a = [int(y) for y in input()]
b = [int(x) for x in input()]

#preenche as diferenças com o número zero se houver
dif = abs(len(a)-len(b))
if dif != 0:
  if len(a) < len(b):
    for d in range(abs(dif)):
      a.insert(d, 0)
  else:
    for d in range(abs(dif)):
      b.insert(d, 0)
  
#verificação
for k in range(len(a)):
  if a[k] > b[k]:
    lista1+=str(a[k])
  elif b[k] > a[k]:
    lista2+=str(b[k])
  else:
    lista1+=str(a[k])
    lista2+=str(b[k])

if lista1 == '':
  lista1 = -1

if lista2 == '':
  lista2 = -1

res = [int(lista1), int(lista2)]
res = sorted(res)

for r in res:
  print(r, end=' ')
