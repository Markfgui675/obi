res = []

def hanoi(x:int, i:int):
    res.append([f'Teste {i}', (2**x)-1])
        
i = 0     
while True:
    i += 1
    n = int(input())
    if n == 0:
        break
    else:
        hanoi(n, i)

for r in res:
    for rr in r:
        print(rr)
    print()
