coluna1 = 0
coluna2 = 0
coluna3 = 0

c = 0
for i in range(9):
	c+=1
	x = int(input())
	if c == 1:
		coluna1+=x
	elif c == 2:
		coluna2+=x
	else:
		coluna3+=x
	if c == 3:
		c = 0


print(f'Coluna 0: {coluna1}')
print(f'Coluna 1: {coluna2}')
print(f'Coluna 2: {coluna3}')