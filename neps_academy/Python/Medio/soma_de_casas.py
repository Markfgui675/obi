n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

k = int(input())
res = []

for num in nums:
    complemento = k - num
    if complemento in nums and complemento != num:
        res.append(complemento)
        res.append(num)
        break

for r in sorted(res):
    print(r, end=' ')