
a, b = map(int, input().split())

calculos = [a+b, a-b]

for c in sorted(calculos, reverse=True):
	print(c)
