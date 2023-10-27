from math import sqrt

n = int(input())
ns = input().split(' ')
nums = [float(x) for x in ns]
raizes = []
for i in nums:
    raizes.append(sqrt(i))
for r in raizes:
    print(f'{r:.4f}')
