n = int(input())
comandos = input()

#direcoes = [0, 1, 2, 3]
d = 0

for c in comandos:
	if c == 'D':
		if d == 3:
			d = 0
		else:
			d+=1
	elif c == 'E':
		if d == 0:
			d = 3
		else:
			d-=1

if d == 0:
	print('N')
elif d == 1:
	print('L')
elif d == 2:
	print('S')
else:
	print('O')

