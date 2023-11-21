n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

k = int(input())
res = []
certo = False
for i in range(n):
    for j in range(n):
        if nums[i] != nums[j] and nums[i] + nums[j] == k:
            res.append(nums[i])
            res.append(nums[j])
            certo = True
            break
    if certo:
        break

for r in sorted(res):
    print(r, end=' ')

