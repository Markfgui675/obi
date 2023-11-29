n = int(input())
nums = set(int(input()) for _ in range(n))
k = int(input())
res = []
for num in nums:
    complemento = k - num
    if complemento in nums and complemento != num:
        res.extend(sorted([num, complemento]))
        break

for r in res:
    print(r, end=' ')
