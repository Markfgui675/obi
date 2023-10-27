def fibonacci(x:int):
    nums = []
    for y in range(x+1):
        if y < 3:
            if y == 2:
                nums.append(2)
            else:
                nums.append(1)
        else:
            nums.append(nums[y-1]+nums[y-2])
    return nums[-1]

n = int(input())
r = fibonacci(n)
print(r)