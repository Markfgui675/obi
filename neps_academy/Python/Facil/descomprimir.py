l = int(input())

codigo = []
for i in range(l):
	codigo.append(list(map(str, input().split())))

for c in codigo:
	for cc in range(int(c[0])):
		print(c[1], end='')
	print()
	