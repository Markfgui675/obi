n = int(input())

nums = [0]
for i in range(n+1):
    if i < 3:
        if i == 2:
            nums.append(2)
        else:
            nums.append(1)
    else:
        nums.append(nums[i]+nums[i-1])

for r in range(n):
    print(nums[r], end=' ')
