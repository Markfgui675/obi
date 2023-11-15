int_a = str(input(''))
int_b = str(input(''))

r_a = []
r_b = []
result_a = ''
result_b = ''
list_a = [int(x) for x in int_a]
list_b = [int(y) for y in int_b]

a_menor_b = True if len(list_a) < len(list_b) else False
b_menor_a = True if len(list_b) < len(list_a) else False

if a_menor_b:
  dif = len(list_b) - len(list_a)
  for d in range(dif):
    list_a.insert(0, 0)

  for i in range(len(list_a)):
    if list_a[i] < list_b[i]:
      r_b.append(list_b[i])
    if list_a[i] > list_b[i]:
      r_a.append(list_a[i])
    if list_a[i] == list_b[i]:
      r_a.append(list_a[i])
      r_b.append(list_b[i])
elif b_menor_a:
  dif = len(list_b) - len(list_a)
  for d in range(dif):
    list_a.insert(0, 0)

  for i in range(len(list_a)):
    if list_a[i] < list_b[i]:
      r_b.append(list_b[i])
    if list_a[i] > list_b[i]:
      r_a.append(list_a[i])
    if list_a[i] == list_b[i]:
      r_a.append(list_a[i])
      r_b.append(list_b[i])
else:
  for i in range(len(list_a)):
    if list_a[i] < list_b[i]:
      r_b.append(list_b[i])
    if list_a[i] > list_b[i]:
      r_a.append(list_a[i])
    if list_a[i] == list_b[i]:
      r_a.append(list_a[i])
      r_b.append(list_b[i])

#verificação de zeros===========

so_tem_zero_A = False
for za in range(len(r_a)):
  if r_a[za] ==  0:
    so_tem_zero_A = True
  else:
    so_tem_zero_A = False
    break

so_tem_zero_B = False
for zb in range(len(r_b)):
  if r_b[zb] == 0:
    so_tem_zero_B = True
  else:
    so_tem_zero_B = False
    break

#=============================

if so_tem_zero_A:
  result_a = '0'
else:
  if len(r_a) == 0:
    result_a = '-1'
  else:
    for ra in range(len(r_a)):
      if ra == 0:
        result_a = str(r_a[ra])
      else:
        result_a += str(r_a[ra])

if so_tem_zero_B:
  result_b = '0'
else:
  if len(r_b) == 0:
    result_b = '-1'
  else:
    for rb in range(len(r_b)):
      if rb == 0:
        result_b = str(r_b[rb])
      else:
        result_b += str(r_b[rb])

print(f'{result_b} {result_a}')
