n = int(input())
ns = input().split(' ')
nums = [int(x) for x in ns]
for l in sorted(nums):
    print(l, end=' ')