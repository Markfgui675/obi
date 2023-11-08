nums = []
for n in range(10):
    nums.append(int(input()))

for p in range(len(nums)):
    if p == 10:
        print(nums[-(p-1)])
    else:
        print(nums[-(p+1)])
