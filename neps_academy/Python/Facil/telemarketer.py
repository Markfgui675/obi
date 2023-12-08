nums = []
for i in range(4):
    nums.append(int(input()))

if nums[0] in range(8, 10) and nums[-1] in range(8, 10) and nums[1] == nums[2]:
    print('ignore')
else:
    print('answer')
