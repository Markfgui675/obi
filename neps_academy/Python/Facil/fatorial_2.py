def fatorial(N):
	fatorial = 1
	for i in range(n, 0, -1):
		fatorial = fatorial*i
	return fatorial
    
n = int(input())
print(fatorial(n))
