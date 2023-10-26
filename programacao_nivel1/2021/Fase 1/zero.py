nums = []
n = int(input())
for i in range(n):
    r = int(input())
    if r != 0:
        nums.append(r)
    else:
        nums.pop()

print(sum(nums))
