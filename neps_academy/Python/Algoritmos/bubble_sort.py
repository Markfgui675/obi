nums = list(map(int, input().split()))

ordenado = False

while not ordenado:
    ordenado = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            ordenado = False
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp

print(nums)
