nums = list(map(int, input().split()))
x = int(input())
indices = []
if x in nums:
    for i in range(len(nums)):
        if nums[i] == x:
            indices.append(i)
    print(len(indices))
    for r in indices:
        print(r, end=' ')
else:
    print("Mia x")
