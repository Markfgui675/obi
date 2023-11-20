n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

k = int(input())
res = []

meio = len(nums)//2
faltante = k-nums[meio]
if faltante in nums:
    res.append(nums[meio])
    res.append(faltante)
    for r in sorted(res):
        print(r, end=' ')
else:
    print('tá aqui não, man')

